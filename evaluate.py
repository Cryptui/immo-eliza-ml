import h2o
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def evaluate_model(test_data_path, target):
    try:
        # Initialize H2O
        h2o.init()

        # Load the specific model
        model_path = 'models/automl_model/GBM_4_AutoML_2_20240321_133555'
        loaded_model = h2o.load_model(model_path)

        # Load the test data
        test_data = h2o.import_file(test_data_path)

        # Make predictions
        predictions = loaded_model.predict(test_data)

        # Convert predictions to pandas DataFrame
        predictions_df = predictions.as_data_frame()

        # Load actual target values from test data
        actuals = test_data[target].as_data_frame().values.flatten()

        # Calculate evaluation metrics
        mse = mean_squared_error(actuals, predictions_df['predict'])
        rmse = mean_squared_error(actuals, predictions_df['predict'], squared=False)
        mae = mean_absolute_error(actuals, predictions_df['predict'])
        r2 = r2_score(actuals, predictions_df['predict'])

        # Print the metrics
        print(f'Mean Squared Error (MSE): {mse}')
        print(f'Root Mean Squared Error (RMSE): {rmse}')
        print(f'Mean Absolute Error (MAE): {mae}')
        print(f'R-squared (R2): {r2}')

    except Exception as e:
        print("An error occurred while evaluating the model:", e)

if __name__ == "__main__":
    test_data_path = 'data/test_data.csv'
    target = 'price'
    evaluate_model(test_data_path, target)
