# DS Portfolio

This repository contains data science projects for the purpose of self-study and practice. These projects cover topics including data scraping, data wrangling, exploratory data analysis and machine learning tasks. Machine learning projects are done using python libraries such as scikit-learn and tensorflow. Please refer to the [_mathematical derivation notes_](https://github.com/anyangpeng/DS_notes/tree/main/ML_notes) for details on the algorithms.

## Contents

- Data scraping (Packages used: _BeautifulSoup_, _selenium_)

  [Project Linkedin](#project-linkedin),

- Data wrangling and exploratory data analysis (Packages used: _Pandas_, _Numpy_, _Matplotlib_, _Seaborn_)

  [Project IRCC](#project-ircc), [Project Titanic](#project-titanic), [Project insurance](#project-insurance)

- Machine Learning (Packages used: _scikit-learn_, _tensorflow_)
  - Supervised
    - Regression: [Project chemicals](#project-chemicals), [Project insurance](#project-insurance), [Project pH](#project-ph)
    - Classification: [Project Titanic](#project-titanic), [Project pH](#project-ph),
  - Unsupervised
    - Clustering: [Project color](#project-color)

## Projects

### [Project chemicals](https://github.com/anyangpeng/DS_Portfolio/tree/main/Project_chemicals)

This project demonstrates how to use tree-based models (**XGBoost**, **RandomForest**)to perform regression tasks. The dataset used in this project is scraped from _CRC Handbook of Chemistry and Physics_. The goal is to predict the boiling point of a given chemical knowing its structural information. Additional python packages used: _XGBoost_, _rdkit_, _shap_.

### [Project color](https://github.com/anyangpeng/DS_Portfolio/tree/main/Project_color)

This project demonstrates how to use **K-Means** algorithm to perform clustering tasks. The goal is to extract the palette of a given painting. Additional python packages used: _cv2_, _collections_.

### [Project IRCC](https://github.com/anyangpeng/DS_Portfolio/tree/main/Project_IRCC)

This project demonstrates how to clean Excel data with multi-level indexing. A data visualization template is included.

### [Project Titanic](https://github.com/anyangpeng/DS_Portfolio/blob/main/Project_Titanic/Titanic.ipynb)

This project demonstrates how to use **RandomForest** to perform classification tasks. The famous Titanic dataset from Kaggle is used. the goal is to predict whether a passenger will survive based on demographics. A detailed exploratory data analysis is included, and a simple hyper-parameter tuning example is shown.

### [Project pH](https://github.com/anyangpeng/DS_Portfolio/blob/main/Project_pH/pH.ipynb)

This project

### [Project insurance](https://github.com/anyangpeng/DS_Portfolio/blob/main/Project_insurance/insurance.ipynb)

This project demonstrates how to use **neural network** to perform regression tasks. The goal is to predict health insurance cost using demographic information. A detailed exploratory data analysis is included,and stratified sampling is examplified. Additional python packages used: _Scipy_.

### [Project Twitter]()

This project

### [Project Linkedin]()

This project

### [Project chatbot]()

This project
