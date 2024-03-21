import h2o
from h2o.automl import H2OAutoML
import os
import logging

def load_data(train_file):
    """
    Load training data from a CSV file into an H2OFrame.

    Parameters:
    - train_file: Path to the CSV file containing training data.

    Returns:
    - H2OFrame containing the training data.
    """
    try:
        train_data = h2o.import_file(train_file)
        return train_data
    except Exception as e:
        logging.error(f"Error loading training data: {e}")
        exit(1)

def split_data(train_data):
    """
    Split the data into training, validation, and test sets.

    Parameters:
    - train_data: H2OFrame containing the training data.

    Returns:
    - Tuple of (training_frame, validation_frame, test_frame).
    """
    train, temp = train_data.split_frame(ratios=[0.8], seed=42)
    valid, test = temp.split_frame(ratios=[0.5], seed=42)
    return train, valid, test

def train_model(train, valid, model_path):
    """
    Train an AutoML model using H2O.

    Parameters:
    - train: H2OFrame containing the training data.
    - valid: H2OFrame containing the validation data.
    - model_path: Path to save the trained model.
    """
    target = 'price'
    predictors = train.columns
    predictors.remove(target)

    aml = H2OAutoML(max_models=20, seed=42, max_runtime_secs=600)
    aml.train(x=predictors, y=target, training_frame=train, validation_frame=valid)

    best_model_path = h2o.save_model(model=aml.leader, path=model_path, force=True)
    logging.info(f"Best model saved to: {best_model_path}")

def main():
    logging.basicConfig(level=logging.INFO)

    # Initialize H2O
    h2o.init()

    train_file = 'data/data_20240313_modified.csv'
    model_path = 'models/automl_model'

    if not os.path.exists(model_path):
        os.makedirs(model_path)

    train_data = load_data(train_file)
    train, valid, _ = split_data(train_data)
    train_model(train, valid, model_path)

if __name__ == "__main__":
    main()
