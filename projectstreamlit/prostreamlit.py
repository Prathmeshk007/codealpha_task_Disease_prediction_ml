import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded = pickle.load(open(r"C:\Users\91945\Downloads\projectstreamlit\train_model.sav", "rb"))

def diabetis(input_data):
    arr = np.asarray(input_data, dtype=float)   # convert to float
    a = arr.reshape(1, -1)
    prediction = loaded.predict(a)
    
    if prediction[0] == 0:
        return "The Person is not Diabetic"
    else:
        return "The Person is Diabetic"

def main():
    st.title("Welcome to Streamlit \nDiabetes Prediction Web App")
    
    # Collect inputs
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    diagnosis = ""
    
    if st.button('Diabetes Test Result'):
        # Convert inputs to numeric before passing
        input_data = [
            float(Pregnancies), float(Glucose), float(BloodPressure),
            float(SkinThickness), float(Insulin), float(BMI),
            float(DiabetesPedigreeFunction), float(Age)
        ]
        diagnosis = diabetis(input_data)
        
    st.success(diagnosis)

if __name__ == '__main__':
    main()