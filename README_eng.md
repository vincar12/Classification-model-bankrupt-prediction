# Bankruptcy Prediction Classification Model

### 1. Project Overview
The goal of this project is to create a classification model that can predict whether a business will go bankrupt based on the provided financial data. The model aims to reduce losses for banks by minimizing loans to businesses predicted to go bankrupt.  
Deployment: [Huggingface](https://huggingface.co/spaces/vincar12/bankrupt_predict)

---

### 2. Project Structure
```bash
├── deployment/                     # Contains deployment files
├── P1M2_Vincar.ipynb               # Jupyter notebook for analysis and model creation
├── P1M2_Vincar_Inference.ipynb     # Jupyter notebook for model inference
├── data.csv                        # Original dataset
├── data_inf.csv                    # Inference dataset
├── data_inf_target.csv             # Inference dataset with target
├── model.pkl                       # Stored model
├── README.md                       # Project README file
├── README_eng.md                   # Project README file in English
```

---

### 3. Workflow
1. **Data Loading & Cleaning**:
  - Load the original data from CSV and clean column names.
2. **Exploratory Data Analysis (EDA)**:
  - Explore the dataset to better understand the data.
3. **Feature Engineering**: Modify the data so it can be processed by the model.
  - **Cardinality**: Check the cardinality or uniqueness of the dataset, as low cardinality usually indicates categorical rather than numerical data.
  - **Split Data**: Divide the data into inference, target, training, and test sets.
  - **Handling Outliers**: Handle outliers by calculating skewness and using Z-Score or Tukey's Rule; apply capping with a winsorizer.
  - **Feature Selection**: Select features for the model using correlation analysis. For nominal data, use Chi-Square correlation analysis, and for numerical data, use Spearman analysis.
  - **Balancing, Scaling, Dimension Reduction**: Balance the data to avoid bias towards the majority class. Scaling ensures the data is on the same scale, and PCA (Principal Component Analysis) is used for dimensionality reduction to avoid overfitting.
4. **Model Definition**:
  - Four models were used to find the best one for predicting bankruptcy: SVM, K-Nearest Neighbors, Decision Tree, Random Forest.
5. **Hyperparameter Tuning**:
  - Tuning hyperparameters to improve the model's performance by identifying the best parameters.
6. **Model Evaluation**:
  - Evaluate the model to assess its error rate and success in predicting the target variable after training.
  - Focus on Recall since the goal is to minimize the chances of predicting a business as non-bankrupt when it is actually bankrupt.
7. **Model Saving**:
  - Save the model using pickle for later use in inference.
8. **Conclusion & Recommendations**:
  - Provide conclusions from the project and business recommendations based on the model.
9. **Inference**:
  - Inference is performed in a separate notebook to reduce the risk of data leakage.

---

### 4. Results and Conclusion
Several key insights can be drawn:
1. Based on the financial dataset of Taiwanese businesses, we conclude that bankruptcy is influenced by financial factors.
2. Bankruptcy prediction can be achieved by analyzing data using machine learning models.
3. After training the model, tuning, and boosting to find the best performing model, the SVM model was found to be the best after tuning.
4. The model selection is based on recall, as banks want to minimize the risk of giving loans to businesses that may go bankrupt.
5. Although the recall value of the model is good (89%), the precision is poor (17%). This means that while the model is good at filtering out businesses likely to go bankrupt, it often predicts bankruptcy for businesses that are actually not bankrupt.
6. The instability in the results may be due to unbalanced data, as only 3% of businesses in the dataset were bankrupt, causing the model to struggle with learning the data optimally.
7. Future improvements in model performance can be achieved by adding more bankrupt business data so the model can learn better. Focusing on metrics like assets, liabilities, and cash could further strengthen bankruptcy predictions.
The business recommendation is to use the model for an initial filter, where the model flags businesses showing consistent financial signs of bankruptcy. These flagged businesses should then be manually reviewed in greater detail to reduce the likelihood of loans being issued to businesses that may go bankrupt.

---

### 5. References
Dataset: [Taiwanese Bankruptcy Prediction](https://archive.ics.uci.edu/dataset/572/taiwanese+bankruptcy+prediction)

Tools: Python, Pandas, NumPy, Seaborn, Matplotlib, Scikit-Learn, IMB-Learn, Streamlit.
