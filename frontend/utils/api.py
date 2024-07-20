import os
import requests
import streamlit as st

# Use environment variable or default value
BASE_URL = os.environ.get("BASE_URL", "https://fixit-zvso.onrender.com")

def upload_file(file):
    try:
        response = requests.post(f"{BASE_URL}/upload", files={"file": file})
        response.raise_for_status()
        data = response.json()
        return data.get("file_id")
    except requests.RequestException as e:
        st.error(f"Error uploading file: {str(e)}")
        return None

def analyze_sentiment(input_data):
    try:
        if isinstance(input_data, str):
            response = requests.post(f"{BASE_URL}/analyze", json={"text": input_data})
        else:
            response = requests.post(f"{BASE_URL}/analyze", json={"file_id": input_data})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error analyzing sentiment: {str(e)}")
        return None

def get_all_results():
    try:
        response = requests.get(f"{BASE_URL}/results")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error fetching results: {str(e)}")
        return None
