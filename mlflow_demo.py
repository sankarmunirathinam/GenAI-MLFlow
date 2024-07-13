import mlflow
from mlflow.models import infer_signature
import mlflow.sklearn

import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define the model hyperparameters
params = {
    "solver": "lbfgs",
    "max_iter": 1000,
    "multi_class": "auto",
    "random_state": 8888,
}

# Train the model
lr = LogisticRegression(**params)
lr.fit(X_train, y_train)

# Predict on the test set
y_pred = lr.predict(X_test)
y_proba = lr.predict_proba(X_test)  # For ROC-AUC

# Calculate original metrics
original_accuracy = accuracy_score(y_test, y_pred)
original_precision = precision_score(y_test, y_pred, average='weighted')
original_recall = recall_score(y_test, y_pred, average='weighted')
original_f1 = f1_score(y_test, y_pred, average='weighted')
roc_auc = roc_auc_score(y_test, y_proba, multi_class='ovr')

# Modify the metrics slightly for demo purposes
accuracy = original_accuracy * 0.9  # Reduce accuracy by 10%
precision = original_precision * 0.85  # Reduce precision by 15%
recall = original_recall * 0.8  # Reduce recall by 20%
f1 = original_f1 * 0.75  # Reduce f1_score by 25%

# Set our tracking server URI for logging
mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")

# Create a new MLflow Experiment
mlflow.set_experiment("HCL-MLFlow Demo")

# Start an MLflow run
with mlflow.start_run() as run:
    run_id = run.info.run_id
    
    # Log the hyperparameters
    mlflow.log_params(params)

    # Log the modified metrics
    mlflow.log_metrics({
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "roc_auc": roc_auc
    })

    # Log the model
    signature = infer_signature(X_train, lr.predict(X_train))
    input_example = X_train[:5]
    
    mlflow.sklearn.log_model(
        sk_model=lr,
        artifact_path="model",
        signature=signature,
        input_example=input_example
    )
    
    # Log artifacts
    with open("iris_model_summary.txt", "w") as f:
        f.write("Logistic Regression model for Iris dataset\n")
        f.write(f"Original Accuracy: {original_accuracy}\n")
        f.write(f"Original Precision: {original_precision}\n")
        f.write(f"Original Recall: {original_recall}\n")
        f.write(f"Original F1 Score: {original_f1}\n")
        f.write(f"Modified Accuracy: {accuracy}\n")
        f.write(f"Modified Precision: {precision}\n")
        f.write(f"Modified Recall: {recall}\n")
        f.write(f"Modified F1 Score: {f1}\n")
        f.write(f"ROC AUC: {roc_auc}\n")
    
    mlflow.log_artifact("iris_model_summary.txt")

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "Basic LR model for iris data")

# Loading the model for predictions
loaded_model = mlflow.pyfunc.load_model(f"runs:/{run_id}/model")

predictions = loaded_model.predict(X_test)

#Displaying the results
iris_feature_names = datasets.load_iris().feature_names

result = pd.DataFrame(X_test, columns=iris_feature_names)
result["actual_class"] = y_test
result["predicted_class"] = predictions

print(result[:4])
