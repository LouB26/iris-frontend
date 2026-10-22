import streamlit as st
import requests

st.title("My awesome MVP")
st.write("Iris predictor")
sepal_length = st.slider("Select a value for Sepal Length", min_value=0, max_value=4, value=1, step=1)
sepal_width = st.slider("Select a value for Sepal Width", min_value=0, max_value=4, value=1, step=1)
petal_length = st.slider("Select a value for Petal Length", min_value=0, max_value=4, value=1, step=1)
petal_width = st.slider("Select a value for Petal Width", min_value=0, max_value=4, value=1, step=1)


API_URL = "https://my-api-app-622755676208.europe-west1.run.app"

url = f"{API_URL}/predict"

params = {
    "X1": sepal_length,
    "X2": sepal_width,
    "X3": petal_length,
    "X4": petal_width 
}

response = requests.get(url, params=params).json()

st.write(f"This flower belongs to category {str(response['prediction'])}")