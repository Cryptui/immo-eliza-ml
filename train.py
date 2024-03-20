import h2o
from h2o.automl import H2OAutoML
import os

def train_model(train_file, model_path):
    # Initialize H2O
    h2o.init()

    # Load the training data
    train_data = h2o.import_file(train_file)

    # Split the data into training and validation sets
    train, temp = train_data.split_frame(ratios=[0.8], seed=42)  # Split off 80% for training
    valid, test = temp.split_frame(ratios=[0.5], seed=42)  # Split the remaining 20% into validation and test

    # Save the test set as a CSV for later use in evaluation
    h2o.export_file(frame=test, path='data/test_data.csv', force=True)

    # Specify target and predictor variables
    target = 'price'
    predictors = train.columns
    predictors.remove(target)

    # Train AutoML model
    aml = H2OAutoML(max_models=20, seed=42, max_runtime_secs=600)
    aml.train(x=predictors, y=target, training_frame=train, validation_frame=valid)

    # Save the best model
    best_model_path = h2o.save_model(model=aml.leader, path=model_path, force=True)
    print(f"Best model saved to: {best_model_path}")

    # Save the path of the best model to a file
    with open('model_path.txt', 'w') as f:
        f.write(best_model_path)

if __name__ == "__main__":
    train_file = 'data/data_20240313_modified.csv'
    model_path = 'models/automl_model'
    if not os.path.exists(model_path):
        os.makedirs(model_path)
    train_model(train_file, model_path)
