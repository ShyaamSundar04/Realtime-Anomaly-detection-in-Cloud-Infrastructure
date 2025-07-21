import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'isolation_forest_model.pkl')

class AnomalyDetector:
    def __init__(self):
        if os.path.exists(MODEL_PATH):
            self.model = joblib.load(MODEL_PATH)
        else:
            self.model = IsolationForest(contamination=0.01, random_state=42)
            self.model.fit(np.zeros((1, 6)))  # Dummy fit to initialize

    def train(self, X):
        """
        Train the Isolation Forest model on the given data X.
        X: numpy array of shape (n_samples, n_features)
        """
        self.model.fit(X)
        joblib.dump(self.model, MODEL_PATH)

    def predict(self, X):
        """
        Predict anomalies in the given data X.
        Returns: array of -1 for anomalies and 1 for normal points.
        """
        return self.model.predict(X)
