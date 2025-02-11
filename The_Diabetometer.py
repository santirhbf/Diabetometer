import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pickle

custom_css = """
<style>
    /* Main background (applies to the whole page) */
    body, .reportview-container {
        font-family: "Arial", sans-serif;
        text-align: center;
    
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #516494;
    }
   
    /* Bold sidebar title */
    [data-testid="stSidebar"] h1 {
        font-weight: bold;
        text-align: left;
    }
   
    /* Style the dog speech text (lighter green background) */
    .dog-text {
        text-align: center;
        font-size: 15px;
        color: #000000;
        background-color: #8796bf;  /* Lighter green than the page background */
        padding: 15px;
        border-radius: 10px;
        box-shadow: none;
    }
   
    /* Targeting Streamlit markdown elements directly */
    div.stMarkdown p {  
        padding: 15px;
        border-radius: 10px;
        box-shadow: none;
    
    /* Center the image */
    .center {
        display: flex;
        justify-content: center;
    }
    
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

st.sidebar.title("Welcome to The Diabetometer!")


st.sidebar.image("Doggy.jpg", width=200)
st.sidebar.markdown(
    "<p class='dog-text'>🐶 Woof! Hi, I am <b>Doctor Olivia McCutie</b>, and I am here to help you with your analysis."
    " How <b>The Diabetometer</b> works is, you need to fill in all the necessary data shown in your screen, and our "
    "<b>Super-Duper Intelligent friend Diabetometer</b> will predict if you have diabetes or not with incredible accuracy so that "
    "you don't have to do all those boring and expensive tests! Isn't it great? Woof Woof! 🐶</p>",
    unsafe_allow_html=True
)

st.title("Parameters for the prediction")

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; color:white;">Before we start, please tell us your name:</p>', unsafe_allow_html=True)
name=st.text_input("First Name:")
last_name=st.text_input("Last Name:")
name_button=st.button("SUBMIT")
if name_button==True:
    name=name
    last_name=last_name

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; color:white;"><br>Please insert your weight in kg:</p>', unsafe_allow_html=True)
weightkg=st.slider("",min_value=0.00,max_value=500.00,value=70.00,step=0.5)
weightlb=weightkg*2.205
st.markdown(f'<p style="font-size:16px; color:grey;">({weightlb:.2f} lb)</p>', unsafe_allow_html=True)

st.markdown(f'<p style="font-size:20px; font-weight:bold; text-align:left; color:white; ">Please insert your height in meters:</p>', unsafe_allow_html=True)
heightmt=st.slider("",min_value=0.00,max_value=2.50,value=1.65,step=0.01)
heightft=heightmt*3.281
st.markdown(f'<p style="font-size:16px; color:grey;">({heightft:.2f} feet)</p>', unsafe_allow_html=True)

BMI=weightkg/(heightmt**2)
st.markdown(f'<p style="font-size:20px; text-align:left; color:white;"><b>Your BMI ratio is --&rarr;</b> {BMI:.2f} kg/m<sup>2</sup></p>', unsafe_allow_html=True)

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; color:white;">Please insert the aproximate hours you sleep per night:</p>', unsafe_allow_html=True)
sleep=st.slider("",min_value=0.0,max_value=12.0,value=6.0,step=0.5)

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; color:white;">Please insert the number of pregnancies you have gone through:</p>', unsafe_allow_html=True)
pregnancies=st.slider("",min_value=0,max_value=20,value=6,step=1)

min_birth_date = datetime.date(1900, 1, 1)
max_birth_date = datetime.date.today()
st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; color:white;">Please insert your date of birth:</p>', unsafe_allow_html=True)
birth=st.date_input('',min_value=min_birth_date,max_value=max_birth_date)
today = datetime.date.today()
age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
st.markdown(f'<p style="font-size:16px; color:grey;">(Meaning you are {age} years old)</p>', unsafe_allow_html=True)

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; color:white;">Now please from the following boxes, check the ones which apply to you:</p>', unsafe_allow_html=True)
col1,col2,col3=st.columns(3)
with col1:
    history=st.checkbox("Family history of diabetes")
    hypertension=st.checkbox("Hypertension")
with col2:
    hyperlipidemia=st.checkbox("Hyperlipidemia")
    cardiovasc=st.checkbox("Cardiovascular disease")
with col3:
    polyov=st.checkbox("Polycystic Ovary Syndrome")
    smoker=st.checkbox("Smoker")

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; color:white;">Lastly, please select your ethnicity:</p>', unsafe_allow_html=True)
st.selectbox('',('Black','Asian','White','Hispanic','Other'))

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; color:white;"><br></p>', unsafe_allow_html=True) #JUST A SPACE BETWEEN TEXT AND BUTTON

button=st.button("GET TEST RESULTS")
if button==True:
    st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; color:white;">Thanks a lot {name} {last_name}! You did great! Here are your test results:</p>', unsafe_allow_html=True)