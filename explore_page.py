import streamlit as st
import pandas as pd
import seaborn as sns



def show_explore_page():
    submenu=st.sidebar.selectbox("Submenu", ["Descriptive","Plots"])

    cars=pd.read_csv("cardekho_updated.csv")
    cars_cleaned=pd.read_csv("clean_train.csv")

    cars['Company']=cars['full_name'].str.split(' ', expand=True)[0]

    for i in range(cars.shape[0]):
        try:
            price = float(cars['selling_price'][i].split(' ')[0])
            digit = cars['selling_price'][i].split(' ')[1]
            if digit == 'Lakh*':
                price = price * 100000
                cars['selling_price'][i] = price
            elif digit == 'Cr*':
                price = price * 10000000
                cars['selling_price'][i] = price
        except:
            price = cars['selling_price'][i][:-1]
            price = price.replace(',', '')
            cars['selling_price'][i] = float(price)
    
    if submenu=="Descriptive":
        st.subheader("Exploratory Data Analysis")
        st.dataframe(cars)

        with st.expander("Data Types"):
            st.dataframe(cars.dtypes)
        
        with st.expander("Summary"):
            st.dataframe(cars.describe())

    elif submenu=="Plots":
        st.subheader("Visualization Plots")
        st.write("#### Top 10 Company in the Dataset")
        with st.expander("Plot based on Top 10 company in the Dataset"):
            new1=cars.Company.value_counts().head(10)
            st.bar_chart(new1)
        
        st.write("#### Least 15 Company in the Dataset")
        with st.expander("Plot based on Least 15 company in the Dataset"):
            new2=cars.Company.value_counts().tail(15)
            st.bar_chart(new2)

        st.write("#### Top 10 years with Highest Sales")
        with st.expander("Plot based on Top 10 years with Highest Sales"):
            new3=cars.year.value_counts().head(10)
            st.bar_chart(new3)

        st.write("#### Top 10 Car company with Highest selling price")
        with st.expander("Plot based on Top 10 Company with Highest Selling Price"):
            new4=cars.groupby('Company')['selling_price'].mean().sort_values(ascending=False).head(10)/1000000
            st.bar_chart(new4)

        
        
    
