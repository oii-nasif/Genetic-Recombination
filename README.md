# Genetic Recombinational Hotspot using Machine Learning
## iR-Spot: Predicting sequence based recombination hotspot using CONV-1D
---


Recombination is the process where two DNA molecules exchange nucleotide sequences with each other. The existence of recombination hotspots offers a way to learn what other processes are associated with recombination. The objective of our work is to find a better predicting model for recombination hotspot. iRSpot starts with DNA sequences for given hotspot and coldspot dataset. We use three feature extraction technique to find important features. Recursive feature elemination and XGboost both are used for feature selection. Model gives 77% accuracy after applying 1D neural network.



#### PERFORMANCE COMPARISON WITH STATE - OF - THE - ART PREDICTORS

|      Methods     | Sn(%) | Sp(%) |   MCC  | Acc(%) |
|:----------------:|:-----:|:-----:|:------:|:------:|
| iRSpot-TNCPseAAC | 76.56 | 70.99 | 0.4737 |  73.52 |
| iRSpot-PseDNC    | 71.75 | 85.84 | 0.5830 |  79.30 |
| IDQD             | 79.52 | 81.82 | 0.6160 |  80.77 |
| iRSpot-ADPM      | 77.19 | 90.73 | 0.6905 |  84.57 |
| iRSpot-SF        | 84.57 | 75.76 | 0.6941 |  84.58 |
| iRSpot-EF        | 94.35 | 95.80 | 0.9037 |  95.14 |
| iRSpot-CNN-1D    | 60.04 | 89.97 | 0.5345 |  76.41 |


### References
**[1]** Al Maruf, Md Abdullah and Shatabda, Swakkhar, “iRSpot-SF: Prediction of recombination hotspots by incorporating sequence based features into Chou’s Pseudo components,” in Genomics, vol. 111, no. 4, pages: 966–972, Elsevier, 2019.

**[2]** Yang, Hui and Qiu, Wang-Ren and Liu, Guoqing and Guo, Feng-Biao and Chen, Wei and Chou, Kuo-Chen and Lin, Hao, “iRSpot-Pse6NC: Identifying recombination spots in Saccharomyces cerevisiae by incorporating hexamer composition into general PseKNC“ in International journal of biological sciences, vol. 14, no. 8, page: 883, Ivyspring International Publisher, 2018

**[3]** Jiang, Peng and Wu, Haonan and Wei, Jiawei and Sang, Fei and Sun, Xiao and Lu, Zuhong“‘RF-DYMHC: detecting the yeast meiotic recombination hotspots and coldspots by random forest model using gapped dinucleotide composition features“‘ in Nucleic acids research, Oxford University Press, 2007

**[4]** Chen, Wei and Feng, Peng-Mian and Lin, Hao and Chou, Kuo-Chen“‘iRSpot-PseDNC: identify recombination spots with pseudo dinucleotide composition“‘ in Nucleic acids research, vol. 41, Oxford University Press, 2013

**[5]** Qiu, Wang-Ren and Xiao, Xuan and Chou, Kuo-Chen “‘iRSpot-TNCPseAAC: identify recombination spots with trinucleotide composition and pseudo amino acid components“‘ in International journal of molecular sciences, vol. 15, no 2 Multidisciplinary Digital Publishing Institute, 2014

**[6]** Liu, Bin and Wang, Shanyi and Long, Ren and Chou, Kuo-Chen“‘iRSpot-EL: identify recombination spots with an ensemble learning approach“‘ in Bioinformatics, vol. 33, no. 1, page. 35-41, Oxford University Press, 2017

**[7]** Zhang, Lichao and Kong, Liang “‘iRSpot-ADPM: Identify recombination spots by incorporating the associated dinucleotide product model into Chou’s pseudo components “‘ in Journal of theoretical biology, vol.441, page. 1-8, Elsevier, 2018

**[8]** Zhang, Lichao and Kong, Liang “‘iRSpot-PDI: Identification of recombination spots by incorporating dinucleotide property diversity information into Chou’s pseudo components“‘ in Genomics,vol. 111, no. 3, Elsevier, 2019

**[9]** Jani, Md Rafsan and Mozlish, Md Toha Khan and Ahmed, Sajid and Tahniat, Niger Sultana and Farid, Dewan Md and Shatabda, Swakkhar “‘iRecSpot-EF: Effective sequence based features for recombination hotspot prediction“‘ in Computers in biology and medicine, vol. 103, page. 17-23, Elsevier, 2018

---
*This project is supervised by **Md Rakibul Haque** Sir (faculty member, Department of CSE, United International University)* 