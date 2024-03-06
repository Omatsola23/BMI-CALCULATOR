import streamlit as st
st.title("BMI CALCULATOR")
weight=st.number_input('Enter your weight in kg')
status=st.radio('Select your heigHt format:', ('cms','meters', 'feet'))
if(status=='cms'):
    height=st.number_input('Centimeters')
    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Enter some values for height")
elif(status=='meters'):
    height = st.number_input('Meters')
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some values for height")
else:
    height = st.number_input('Feets')
    try:
        bmi = weight / (((height/3.28)) ** 2)
    except:
        st.text("Enter some values for height")
if(st.button('CALCULATE BMI')):
    st.text("Your BMI is {}.".format(bmi))
    if(bmi<16):
        st.error("You are extremely Underweight")
    elif(bmi>=16 and bmi<18.5):
        st.warning("You are underweight")
    elif(bmi>=18.5 and bmi<25):
        st.success("Healthy")
    elif(bmi>=25 and bmi<30):
        st.warning("OverweigHt")
    elif(bmi>=30):
        st.error("Extremely Overweight")
