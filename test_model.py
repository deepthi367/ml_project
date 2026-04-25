import joblib

# load model
model = joblib.load("ada_model.joblib")

# sample input (10 features)
sample = [[20, 5, 30, 4, 1, 40, 0, 13, 22, 135]]

# predict
prediction = model.predict(sample)

print("Prediction:", prediction)