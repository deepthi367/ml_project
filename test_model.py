<<<<<<< HEAD
import pickle

model = pickle.load(open('model.pkl', 'rb'))

print(model.feature_names_in_)
=======
import pickle

model = pickle.load(open('model.pkl', 'rb'))

print(model.feature_names_in_)
>>>>>>> d96b7b6116abab498a76d60e8d72c3173703b6b7
print(len(model.feature_names_in_))