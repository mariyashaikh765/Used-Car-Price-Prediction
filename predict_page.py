import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

with open("saved_rfr.pkl", "rb") as file:
    data2=pickle.load(file)


def predict_note_authentication(year, km, fuel, transmission, mileage, CC, bhp, Seats):
    prediction=data2.predict([[year, km, fuel, transmission, mileage, CC, bhp, Seats]])
    print(prediction)
    return prediction 
    
def show_predict_page():
    st.title("Price Prediction Model")

    fuel={
        0,
        1,
        2,
        3,
        4
    }

    Seats={
        2,
        4,
        5,
        6,
        7, 
        8,
        9,
        10
    }

    transmission={
        0,
        1
    }

    year=st.slider("Year", 1950, 2022, 1980)
    km=st.number_input("Kilometer Driven")
    fuel=st.selectbox("Fuel, Select 0:Petrol, 1:Diesel, 2:CNG, 3:LPG, 4: Electric", fuel)
    transmission=st.selectbox("Transmision, Select 0:Manual, 1:Automatic", transmission)
    mileage=st.number_input("Mileage")
    CC=st.number_input("Capacity of Engine(cc)")
    bhp=st.number_input("Engine Power(bhp)")
    Seats=st.selectbox("Seats", Seats)

    result=""
    ok=st.button("Calculate Price")
    if ok:

        result=predict_note_authentication(year, km, fuel, transmission, mileage, CC, bhp, Seats)
        st.success("".format(result))
        st.subheader(f"The Estimated Price is {result[0]:.2f}")
        
        

#show_predict_page()




  
