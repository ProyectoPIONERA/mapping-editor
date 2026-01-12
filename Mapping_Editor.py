import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import base64


# Config---------------------------------------------------
if "dark_mode_flag" not in st.session_state or not st.session_state["dark_mode_flag"]:
    st.set_page_config(page_title="Mapping Editor", layout="wide")
    color = "#511D66"
else:
    st.set_page_config(page_title="Mapping Editor", layout="wide")
    color = "#d8c3f0"

# Automatic detection of dark mode-------------------------
if "dark_mode_flag" not in st.session_state or st.session_state["dark_mode_flag"] is None:
    st.session_state["dark_mode_flag"] = streamlit_js_eval(js_expressions="window.matchMedia('(prefers-color-scheme: dark)').matches",
        key="dark_mode")



st.markdown(f"""
<h1>Welcome to <span style='color:{color};'>Mapping Editor</span></h1>
""", unsafe_allow_html=True)
st.write("Use sidebar to work with existing or new mapping.")
