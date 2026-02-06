# This script takes 5 sensor values from the user and uses a trained Decision Tree model to print the prediction.
import numpy as np
import joblib

model = joblib.load("decision_tree_model.joblib")

print("\nEnter sensor values:")

p_pdg = float(input("P-PDG: "))
t_tpt = float(input("T-TPT: "))
p_tpt = float(input("P-TPT: "))
t_jus_ckp = float(input("T-JUS-CKP: "))
p_mon_ckp = float(input("P-MON-CKP: "))

# Arrange input in correct shape
user_input = np.array([[p_pdg, t_tpt, p_tpt, t_jus_ckp, p_mon_ckp]])

# Predict
prediction = model.predict(user_input)

print(f"\nPredicted Class: {prediction[0]}")
