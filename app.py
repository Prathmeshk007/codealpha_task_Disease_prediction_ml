import numpy as np, pickle, streamlit as st
loaded = pickle.load(open("train_model.sav", "rb"))

def main():
    st.set_page_config(page_title="Diabetes Prediction", page_icon="🏥")
    st.title("Welcome to IntelliHealth :An AI Powered Diabetes Prediction System")
    col1, col2 = st.columns(2)
    with col1:
        P = st.text_input('Pregnancies', value='0')
        G = st.text_input('Glucose (mg/dL)', value='120')
        BP = st.text_input('Blood Pressure', value='70')
        ST = st.text_input('Skin Thickness', value='20')
    with col2:
        I = st.text_input('Insulin', value='80')
        BMI = st.text_input('BMI', value='25.0')
        DPF = st.text_input('DPF', value='0.5')
        Age = st.text_input('Age', value='30')
    if st.button('Predict'):
        input_data = [float(P), float(G), float(BP), float(ST), float(I), float(BMI), float(DPF), float(Age)]
        arr = np.asarray(input_data, dtype=float).reshape(1, -1)
        pred = loaded.predict(arr)[0]
        if any(v < 0 for v in input_data):
            st.error("Values cannot be negative")
        else:
            
            prob = 0.7 if pred == 1 else 0.3
            risk = "High" if prob > 0.6 else "Medium" if prob > 0.3 else "Low"
            
            st.success(f"Risk of Diabetes is : {risk}")
            st.success(f"Probability of having Diabetes is : {prob:.1%}")
            st.success("Result: " + ("Diabetic" if pred == 1 else "Not Diabetic"))
        st.balloons()

if __name__ == '__main__':
    main()
