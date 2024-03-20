# app/model.py

import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, predictions)}")

# Save the trained model
with open('trained_model/model.pkl', 'wb') as f:
    pickle.dump(model, f)
