# 🏡 Immo Eliza Real Estate Price Prediction Model Card

## Model Details
- **Model name**: `Immo-Eliza-Price-Prediction`
- **Model version**: 1.0
- **Model type**: LinearRegression and Gradient Boosting Machine (GBM) with AutoML 
- **Model framework**: H2O, scikit-learn
- **Date**: March 20, 2024
- **Developers**: Cryptui

## Model Objective
- **Purpose**: The purpose of this model is to predict real estate prices in Belgium based on various property characteristics. It was created as part of a request from the real estate company Immo Eliza.
- **Intended use**: The model is intended to provide price estimates to support real estate agents and potential buyers in the valuation of properties.
- **Intended audience**: Real estate agents, property sellers, buyers, and data scientists in the real estate industry.

## Intended Use
- **Primary use**: Predicting real estate prices in Belgium
- **Users**: Immo Eliza analytics team and agents
- **Target Audience**: The model is designed to predict prices for customers interested in properties within a specific price range and size criteria, focusing on features such as 'price', 'surface_land_sqm', 'total_area_sqm', and 'nbr_bedrooms'.

## Data
- **Source**: The dataset used for training this model comes from roughly 76,000 properties across Belgium from Immoweb.be
- **Date Range**: March 1, 2024, to March 20, 2024
- **Preprocessing**: one-hot encoding for categorical variables, standardization of numeric features, LinearRegression and Gradient Boosting Machine (GBM) with AutoML 
- **Features**: The dataset includes features like property type, size, location, and several binary (`fl_`) and size (`_sqm`) indicators.

## Training
- **Preprocessing steps**: NaN values were handled using imputation, categorical data were converted using one-hot encoding
- **Algorithm(s)**: Linear regression was used as the base model. Additional GBM model from AutoML that combines multiple decision trees to generate the final predictions was also used. 
- **Splitting**: The data was split into training and testing sets, with an 80/20 split.

## Evaluation Metrics Presentation 
- **Split**: 80% training / 20% testing

The model's performance was evaluated using the following metrics:

| Metric                 | Value             |
|------------------------|-------------------|
| Mean Squared Error (MSE) | 2952608966 |
| Root Mean Squared Error (RMSE) | 54338 |
| Mean Absolute Error (MAE) | €37062 |
| R-squared (R2)         | 0.821             |

These metrics provide insights into the model's accuracy, precision, and overall performance. For instance, the R-squared value of 0.821 indicates that approximately 82.1% of the variability in real estate prices is explained by the model. The MAE and RMSE values suggest the average deviation between predicted and actual prices, with MAE representing the average absolute error and RMSE indicating the standard deviation of these errors.

## Performance
- The model achieved an R-squared value of 0.821 on the test dataset, indicating a good fit to the data. The MAE and RMSE values suggest that, on average, the model's predictions deviate by €37,062 and €54,338, respectively, from the actual prices.

## Ethical Considerations
- **Potential biases**: The model may be biased if the training data is not representative of the entire real estate market in Belgium. For example, if certain types of properties are overrepresented in the data, the model may be more accurate for those types of properties but less accurate for others.
- **Limitations and risks**: The model's predictions are based on historical data and may not accurately capture sudden changes or anomalies in the real estate market. Users should exercise caution when relying solely on the model's predictions for pricing decisions.

## Warning and Recommendations
- **Warning**: While the model demonstrates strong performance, it is essential to consider its limitations. For example, it may not capture the full complexity of factors influencing real estate prices, such as economic trends, neighborhood changes, or property-specific characteristics not included in the dataset.
- **Improvements**: To improve the model, additional features could be incorporated, such as proximity to public transportation, school ratings, or crime rates. Continuous monitoring of the model's performance and periodic retraining with updated data are recommended to ensure its accuracy and relevance over time.
- **Use cases**: The model performs best when used on properties similar to those found in the training data.
- **Misuse potential**: The model should not be used as the sole decision-making tool for real estate pricing. Human judgment and market knowledge are essential complements to the model's predictions.
- **Inflation and Market Dynamics**: The model's predictions are based on historical data that may not capture future market conditions. Stakeholders should be aware that factors such as inflation, which affects property values and the overall economy, can influence the accuracy of predictions. 

## Maintenance
- **Update frequency**: Due to the impact of external factors such as inflation, which currently stands at 3.60%, and other market dynamics, it is recommended that the model be re-evaluated and retrained every 6 months to ensure its accuracy remains high.
- **Monitoring**: Model performance should be monitored on a monthly basis to detect any significant deviations in prediction accuracy that could be attributed to rapid changes in the market.
- **Recalibration**: If substantial shifts in the economy or the real estate market occur (such as a notable increase or decrease in the inflation rate), an immediate model recalibration should be considered rather than waiting for the next scheduled update.

## Model Management
- **Versioning**: Different versions of the model are tracked using version control systems like Git.
- **Monitoring and maintenance**: The model's performance is monitored regularly using metrics such as R-squared, MAE, and RMSE. Any significant deviations from expected performance triggers a review and potential retraining of the model.
- **Update policy**: The model should be retrained periodically (e.g., every six months or annually) to incorporate new data and ensure its predictions remain accurate and up-to-date. Additionally, updates may be required in response to changes in the real estate market or business requirements.
