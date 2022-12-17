import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
import streamlit.components.v1 as stc
from PIL import Image

html_temp= """ 
            <div style="background-color: blue; padding: 10px; border-radius: 10px">
            <h1 style="color: white; text-align: centre;"> Used Car Price Prediction Web App </h1>
            </div>
            """

def main():
    #st.title("Main App")
    stc.html(html_temp)
    
    menu=["Home", "Price Prediction Model", "Explore"]
    choice=st.sidebar.selectbox("Navigation", menu)

    if choice=="Home":
        img=Image.open("C:\\Users\\SHAIKH MARIYA\\Pictures\\car image.jpg")
        st.image(img)
        st.write("""### About the App""")
        st.write("This application is a part of the Data Science project. This Web Application includes  a machine learning model that will easily predict the resale valuation of the Car and the customer can access this model from the Web Application directly and get benefit from the prediction. The customer will just have to provide some features of the Car on the Website and my model will provide the Best Price Prediction.")
        st.write("Through the upper left button you can choose the 'Navigation' in the sidebar, and from there you can choose any options:")
        #st.header("Home")
        st.write("##### 1. Price Predicition Model: ")
        st.write("Manually enter the car's features to get the price prediction")
                       
        st.write("##### 2.Explore: ")
        st.write("Explore selling prices of collected data with the help of Visualization")
    
    elif choice=="Price Prediction Model":
        show_predict_page()
    
    elif choice=="Explore":
        show_explore_page()

main()