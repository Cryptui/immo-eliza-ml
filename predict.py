import pandas as pd
import h2o
from clean import fill_missing_values, remove_outliers

def initialize_h2o():
    """
    Initialize the H2O server.
    """
    h2o.init()

def load_model(model_path):
    """
    Load a saved H2O model from a specified path.

    Parameters:
    - model_path: Path to the saved model.

    Returns:
    - The loaded H2O model.
    """
    return h2o.load_model(model_path)

def preprocess_data_for_prediction(input_path):
    """
    Preprocess new data for prediction. This includes loading the data,
    filling missing values, and optionally removing outliers.

    Parameters:
    - input_path: Path to the new data to preprocess.

    Returns:
    - A DataFrame of the preprocessed data.
    """
    # Load the new data into a DataFrame
    new_data = pd.read_csv(input_path)

    # Fill missing values and replace specific indicators
    new_data = fill_missing_values(new_data)

    # Note: If you decide to remove outliers in the prediction data, uncomment the following line
    # new_data, _ = remove_outliers(new_data, features_to_check=['surface_land_sqm', 'total_area_sqm', 'nbr_bedrooms'])

    return new_data

def predict_prices(model, preprocessed_data, output_path):
    """
    Predict prices for the preprocessed data using a specified model and save the predictions.

    Parameters:
    - model: The H2O model to use for predictions.
    - preprocessed_data: DataFrame of the preprocessed data for prediction.
    - output_path: Path to save the predictions.
    """
    try:
        # Convert the DataFrame to an H2OFrame
        preprocessed_hf = h2o.H2OFrame(preprocessed_data)
        
        # Make predictions
        predictions = model.predict(preprocessed_hf)
        
        # Add predictions to the original data
        preprocessed_data['predicted_price'] = predictions.as_data_frame().values.flatten()
        
        # Output the predictions to a CSV file
        preprocessed_data.to_csv(output_path, index=False)
        print("Predictions have been saved to:", output_path)

    except Exception as e:
        print("An error occurred while making predictions:", e)

if __name__ == "__main__":
    # Initialize H2O
    initialize_h2o()

    # Load the saved model
    model_path = 'models/automl_model/GBM_4_AutoML_4_20240320_141321'
    model = load_model(model_path)

    # Path to new data
    data_to_predict_path = 'data/data_20240313_cleaned_to_predict.csv'

    # Preprocess the new data for prediction
    preprocessed_data = preprocess_data_for_prediction(data_to_predict_path)

    # Predict the prices and save the predictions
    output_predictions_path = 'data/predicted_prices.csv'
    predict_prices(model, preprocessed_data, output_predictions_path)
