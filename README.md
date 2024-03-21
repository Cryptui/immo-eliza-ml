# 🏡 Immo Eliza Real Estate Price Prediction Model Card

This repository contains the Immo Eliza Price Prediction Model, designed to predict real estate prices in Belgium. It integrates various machine learning algorithms, including GBM from H2O's AutoML.

## 📑 Table of Contents
- [Getting Started](#getting-started)
- [Model Details](#model-details)
- [Project Context](#project-context)
- [Data Preprocessing](#data-preprocessing)
- [Training Data](#training-data)
- [Model Architecture](#model-architecture)
- [Training Procedure](#training-procedure)
- [Evaluation](#evaluation)
- [Limitations](#limitations)
- [Maintenance](#maintenance)
- [Usage](#usage)
- [Maintainers](#maintainers)

## Getting Started 🚀

To begin using the Immo Eliza Price Prediction Model, follow these steps:

**Clone the Repository**: 
   git clone https://github.com/Cryptui/immo-eliza-ml
   Install Dependencies: Navigate to the project directory and install the required dependencies using pip:
   pip install -r requirements.txt

## Model Details 📝

- **Developer**: Cryptui
- **Model Date**: March 20, 2024
- **Model Version**: 1.0

## Data Preprocessing 🧼

Before training, the dataset underwent several preprocessing steps:

- **Handling Missing Values**: Missing numerical data was filled with -1, and categorical missing values were replaced with the string 'missing_info'.
- **Outlier Removal**: Outliers were detected and removed using the Interquartile Range (IQR) method for key features.

## Detailed Cleaning Steps:

- **Modified Data Path**: `data/data_20240313_modified.csv`
- Outliers were removed from the following features, with the resulting new ranges:
  - **Price**: 5800 outliers removed; new range: €76,000 - €774,500.
  - **Surface Land (sqm)**: 6940 outliers removed; new range: 0 - 876 sqm (assuming '-1' was a placeholder for missing data).
  - **Total Area (sqm)**: 2282 outliers removed; new range: 0 - 270 sqm.
  - **Number of Bedrooms**: 3608 outliers removed; new range: 1 - 4 bedrooms.

The preprocessing steps are essential to prepare the dataset for machine learning and to ensure the model receives quality input for its predictions.

## Project Context 🌐

The Immo Eliza model was developed to estimate the market value of real estate properties in Belgium. Given the dynamic nature of the housing market and factors such as the inflation rate, which is currently at 3.60%, the model requires regular updates to maintain accuracy.

## Training Data 🔢

- **Dataset Composition**: Approximately 75,000 properties, equally distributed between houses and apartments, each with a unique identifier.
- **Feature Encoding**: Categorical data were converted into numeric features via one-hot encoding.

## Model Architecture 📐

- **Type**: The model architecture encompasses several machine learning algorithms, with a primary focus on Linear Regression and H2O's AutoML for model selection, which includes a Gradient Boosting Machine (GBM).
- **Regularization Techniques**: Applied to Linear Regression to prevent overfitting and improve model performance.
- **Libraries**: The model was developed using scikit-learn for initial approaches, h2o for AutoML optimization, and pandas for data manipulation.

## Training Procedure 📈

- **Environment**: The models were trained in an isolated Python 3.12 environment, ensuring reproducibility.
- **Hyperparameter Tuning**: Techniques such as Grid Search and Random Search were utilized, with cross-validation to prevent overfitting.

## Evaluation 📊

- **Metrics**: The model's performance was evaluated using RMSE, MAE, and R-squared.
  - Mean Squared Error (MSE): 2952608966
  - Root Mean Squared Error (RMSE): 54338
  - Mean Absolute Error (MAE): 37063
  - R-squared (R2): 0.82128
- **Cross-validation**: Conducted to ensure the model's generalizability across different subsets of data.

## Limitations 🚫

The model's predictions are based on the current market state and are subject to change as economic conditions evolve, particularly in response to fluctuating inflation rates.

## Maintenance 🛠️

- **Recalculation Period**: It is recommended that the model be recalculated semi-annually, taking into account the latest market data and economic indicators such as inflation rates.
- **Monitoring Strategy**: A monthly review of prediction accuracy is advised to detect any need for early recalibration.

## Usage 👨‍💻

For detailed instructions on training the model or making predictions with the provided scripts (`train.py` and `predict.py`), refer to the `USAGE.md`.

## Maintainers 👷‍♂️

Questions or updates contact [Cryptui](https://github.com/Cryptui).
