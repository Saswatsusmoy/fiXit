import streamlit as st
from pages import home, results

PAGES = {
    "Home": home,
    "Results": results
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    # Check if BASE_URL is set
    if not st.secrets.get("BASE_URL"):
        st.error("BASE_URL is not set. Please set it in your Streamlit secrets.")
        st.stop()

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
