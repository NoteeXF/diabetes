# -*- coding: utf-8 -*-
"""hasbi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TL8vNC2AG9tN6LWbCoO-V4WyK4cytgxB

## deploy
"""

import numpy as np
import streamlit as st
from sklearn.preprocessing import StandardScaler
from streamlit_option_menu import option_menu

from joblib import load

Diabetes_trained_model = load('rf_model.sav')

import joblib
Diabetes_trained_model = joblib.load('rf_model.sav')



from sklearn.preprocessing import StandardScaler
import numpy as np



# Function for prediction
def diabetes_prediction(input_data):
    # Convert the input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Standardize the input data
    scaler = StandardScaler()
    std_data = scaler.fit_transform(input_data_reshaped)

    # Make prediction
    prediction = Diabetes_trained_model.predict(std_data)

    # Return the prediction result
    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'


def main():
    # Giving Title
    st.title('Diabetes Prediction Web App')

    # Getting input data from the user
    # Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Level')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age of the Person')

    # Code for prediction
    diagnosis = ''

    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
       diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)


if __name__ == '__main__':
    main()