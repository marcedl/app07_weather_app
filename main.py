import streamlit as st 
import plotly.express as px
from backend import get_data

st.title("Weather Forecst for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help= "Select the number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
temperatures = [30, 31, 29]
temperatures = [days * i for i in temperatures]

d, t  = get_data(place, days, type)

figure = px.line(x= d, y= t, labels= {"x":"Dates", "y":"Temperatures"})  
st.plotly_chart(figure)