import streamlit as st
from pages import home, results
import os

PAGES = {
    "Home": home,
    "Results": results
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    # Check if BASE_URL is set
    if not os.environ.get("BASE_URL"):
        st.warning("BASE_URL environment variable is not set. Using default URL.")

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
