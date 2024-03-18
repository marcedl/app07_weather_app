import streamlit as st 
from plotly import express as px
from backend import get_data

#Title, text input, slider, selectbox and subheader 
st.title("Weather Forecst for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help= "Select the number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    #get temperature/sky data
    try:
        filtered_data  = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            #temperature plot
            figure = px.line(x= dates, y= temperatures, labels= {"x":"Dates", "y":"Temperatures"})  
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear":"images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width= 115)
    except KeyError:
        st.write("The place does not exists")