# -*- coding: utf-8 -*-
"""CONV_1D_hotspot_77.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OtFUgWA0iXuxbZ-w6EPw4Jk9nUCx63GH
"""

import warnings; warnings.filterwarnings("ignore")

"""</br>

* **data processing (Merge all data)**
"""

import numpy as np

X_kmer = np.load('K-mer.npy')
X_revk = np.load('rev-k-mer.npy')
X_gapk = np.load('gapped_k_mer.npy')

print(X_kmer.shape)
print(X_revk.shape)
print(X_gapk.shape)

Y  = [1 for i in range(490)]
Y += [0 for i in range(591)]
Y = np.array(Y)
print(Y.shape)

X = np.concatenate((X_kmer,X_revk, X_gapk),axis=1)

X.shape

"""</br>

* **Shuffle**
"""

from sklearn.utils import shuffle
X, Y = shuffle(X, Y, random_state=0)

print(X.shape)
print(Y.shape)

X.shape

X = X.reshape(-1, 760, 1)
X.shape

X[0].shape

# Deep Neural Networks:
import tensorflow as tf; print('We\'re using TF-{}.'.format(tf.__version__))
from tensorflow.keras.layers import (Input, Dense, Dropout, Flatten, BatchNormalization,
                                     Conv1D, Conv2D, MaxPooling1D, MaxPooling2D,
                                     LSTM, GRU, Embedding, Bidirectional, Concatenate)
from tensorflow.keras.regularizers import (l1, l2, l1_l2)
from tensorflow.keras.optimizers import (RMSprop, Adam, SGD)
from tensorflow.keras.models import (Sequential, Model)


# Core:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interp
import matplotlib.patches as patches

# Performance:
from sklearn.metrics import (confusion_matrix, classification_report, matthews_corrcoef, precision_score, roc_curve, auc)
from sklearn.model_selection import (StratifiedKFold, KFold, train_test_split)

#Utilities:
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.utils import to_categorical as labelEncoding   
from tensorflow.keras.utils import plot_model                        
#end-import

Y = labelEncoding(Y, dtype=int)
Y

def lossPlot(results):
    plt.title(label='Loss: Training and Validation')
    plt.plot(results.history['loss'], label='Training Loss')
    plt.plot(results.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()


def accuracyPlot(results):
    plt.title(label='Accuracy: Training and Validation')
    plt.plot(results.history['accuracy'], label='Training Accuracy')
    plt.plot(results.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()


def rocPlot(TPR, meanFPR):
    plt.plot([0,1], [0,1],linestyle = '--',lw = 2,color = 'black')
    meanTPR = np.mean(TPR, axis=0)
    meanAUC = auc(meanFPR, meanTPR)
    plt.plot(meanFPR, meanTPR, color='blue',
            label=r'Mean ROC (AUC = %0.2f )' % (meanAUC),lw=2, alpha=1)

    plt.xlabel('False Positive Rate (FPR)')
    plt.ylabel('True Positive Rate (TPR)')
    plt.title('Receiver Operating Characteristic Curve (ROC Curve)')
    plt.legend(loc="lower right")
    plt.savefig('ROC-240.png')
    plt.show()

def Network():
    input1 = Input(shape=(760, 1))

 
    x = Conv1D(filters=16, kernel_size=4, padding='same', activation='relu', kernel_regularizer=l2(l=0.01))(input1)
    x = BatchNormalization()(x)
    x = Dropout(rate=0.80)(x)
    
    x = Flatten()(x)
        
    x = Dense(units=16, activation='relu', kernel_regularizer=l2(l=0.01))(x)
    x = Dropout(rate=0.80)(x)
    x = Dense(units=8, activation='relu', kernel_regularizer=l2(l=0.01))(x)
    o = Dense(units=2, activation='softmax')(x)

    return Model(inputs=[input1], outputs=[o])

model = Network()
model.summary()
plot_model(model, to_file='model-Nasif.png', show_shapes=True, show_layer_names=False, expand_nested=True)

X.shape

setEpochNumber     = 100     # Performed-well in epoch 100
setBatchSizeNumber = 8

fold = 5
cv = KFold(n_splits=fold, shuffle=True, random_state=101)

Accuracy = []
Sensitivity = []
Specificity = []
Precision = []
MCC = []

# ROC Curve:
fig = plt.figure(figsize=[12,12])

TPR = []
meanFPR = np.linspace(0, 1, 100)

i = 1
plotCount = 1


for train, test in cv.split(Y):

    # Compile Model:
    model = Network()
    model.compile(optimizer=Adam(learning_rate=0.0005),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])


    # Run Model:
    results = model.fit(x=X[train,:,:],
                        y=Y[train,:],
                        validation_data=(X[test,:,:], Y[test,:]),
                        batch_size=setBatchSizeNumber, epochs=setEpochNumber,
                        callbacks = [],
              )

    accuracy = model.evaluate(x=X[test,:,:], y=Y[test,:], batch_size=setBatchSizeNumber)
    Accuracy.append(accuracy[1])

    # Performance Metices:
    Yactual = Y[test,:].argmax(axis=1)
    Yp = model.predict(X[test,:,:])
    v = Yp
    Yp = Yp.argmax(axis=1)

    CM = confusion_matrix(y_pred=Yp, y_true=Yactual)
    TN, FP, FN, TP = CM.ravel()

    MCC.append(matthews_corrcoef(y_true=Yactual, y_pred=Yp))
    Sensitivity.append( TP / (TP + FN) )
    Specificity.append( TN / (TN + FP) )
    Precision.append(precision_score(y_true=Yactual, y_pred=Yp))
    
    # ROC Curve
    fpr, tpr, _ = roc_curve(Yactual, v[:,1])
    TPR.append(interp(meanFPR, fpr, tpr))
    rocauc = auc(fpr, tpr)
    plt.plot(fpr, tpr, lw=2, alpha=0.3, label='ROC fold %d (AUC = %0.2f)' % (i, rocauc))
    i= i+1
    
    # Performance Plot
    print('____________________________________________________')
    print('Fold\'s Accuracy-{}: {:.2f}'.format(plotCount, accuracy[1]*100.0))
    # lossPlot(results)
    # accuracyPlot(results)
    plotCount += 1
    print('____________________________________________________')



rocPlot(TPR, meanFPR)

print('Accuracy [Each Fold]: {}'.format(Accuracy))
print('Accuracy: {:.4f}'.format(np.sum(Accuracy)/fold))
print('Sensitivity: {0:.4f}'.format(np.sum(Sensitivity)/fold))
print('Specificity: {0:.4f}'.format(np.sum(Specificity)/fold))
print('MCC: {0:.4f}'.format(np.sum(MCC)/fold))
print('Precision: {0:.4f}'.format(np.sum(Precision)/fold))



