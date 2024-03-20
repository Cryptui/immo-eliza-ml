# Model Card for Immo Eliza Price Prediction Model

## Model Details
- **Model type**: LinearRegression and Gradient Boosting Machine (GBM) with AutoML 
- **Model version**: 1.0
- **Date**: March 20, 2024
- **Developers**: Me

## Intended Use
- **Primary use**: Predicting real estate prices in Belgium
- **Users**: Immo Eliza analytics team and agents

## Training Data
- **Source**: Immoweb.be
- **Date Range**: March 13, 2024, to March 20, 2024
- **Preprocessing**: one-hot encoding for categorical variables, standardization of numeric features, LinearRegression and Gradient Boosting Machine (GBM) with AutoML 

## Evaluation Data
- **Split**: 80% training / 20% testing
- **Metrics**:
  - Mean Squared Error (MSE): 2952608966.817194
  - Root Mean Squared Error (RMSE): 54337.914634417044
  - Mean Absolute Error (MAE): 37062€
  - R-squared (R2): 0.821


## Performance
- The model achieved an R-squared value of 0.821 on the test dataset, indicating a good fit to the data. The MAE and RMSE values suggest that, on average, the model's predictions deviate by €37,062 and €54,338, respectively, from the actual prices.

## Ethical Considerations
- **Potential biases**: The model may be biased if the training data is not representative of the entire real estate market in Belgium. For example, if certain types of properties are overrepresented in the data, the model may be more accurate for those types of properties but less accurate for others.
- **Limitations and risks**: The model's predictions are based on historical data and may not accurately capture sudden changes or anomalies in the real estate market. Users should exercise caution when relying solely on the model's predictions for pricing decisions.

## Caveats and Recommendations
- While the model demonstrates strong performance, it is essential to consider its limitations. For example, it may not capture the full complexity of factors influencing real estate prices, such as economic trends, neighborhood changes, or property-specific characteristics not included in the dataset.
- To improve the model, additional features could be incorporated, such as proximity to public transportation, school ratings, or crime rates. Continuous monitoring of the model's performance and periodic retraining with updated data are recommended to ensure its accuracy and relevance over time.

## Model Management
- **Versioning**: Different versions of the model are tracked using version control systems like Git.
- **Monitoring and maintenance**: The model's performance is monitored regularly using metrics such as R-squared, MAE, and RMSE. Any significant deviations from expected performance triggers a review and potential retraining of the model.
- **Update policy**: The model should be retrained periodically (e.g., every six months or annually) to incorporate new data and ensure its predictions remain accurate and up-to-date. Additionally, updates may be required in response to changes in the real estate market or business requirements.
