import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import pickle
import os

X = np.array([[1, 2, 3, 1], [2, 3, 2, 0], [3, 2, 4, 1], [4, 1, 3, 0]])
y = np.array([0, 1, 0, 1])  # 0: Safe, 1: Risk

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = SVC()
model.fit(X_scaled, y)

os.makedirs("accident_model", exist_ok=True)
pickle.dump(model, open('accident_model/accident_model.pkl', 'wb'))
pickle.dump(scaler, open('accident_model/scaler.pkl', 'wb'))