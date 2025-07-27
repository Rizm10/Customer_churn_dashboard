import streamlit as st
#Colour Palette
PRIMARY_COLOR = "#1A73E8"
SECONDARY_COLOR = "#4CAF50"
NEGATIVE_COLOR = "#E53935"
UTILITY = "#B0BEC5"

#Base Themes
BACKGROUND= "#F9FAFB"
TEXT_COLOR_PRIMARY = "#111111"
TEXT_COLOR_SECONDARY = "#333333"

#Font Family
FONT_FAMILY = '"Segoe UI", "Helvetica Neue", sans-serif'

def apply_custom_style():
    st.markdown(f"""
       <style>
             body {{
            background-color:{BACKGROUND};
            color: {TEXT_COLOR_PRIMARY};
            font-family: {FONT_FAMILY}; }}
            h1,h2,h3{{
            color: {TEXT_COLOR_PRIMARY};
            }}
            p, span {{
            color: {TEXT_COLOR_SECONDARY};
            }}
       </style>
                """, unsafe_allow_html=True)
    
def apply_button_style():
    st.markdown(f"""
        <style>
            div.stButton > button  {{
                background-color: {BACKGROUND};
                color: {TEXT_COLOR_PRIMARY};
                border: 2px solid {PRIMARY_COLOR};
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 16px;
            }}

            div.stButton > button:hover {{
                background-color: {PRIMARY_COLOR};
                color: {BACKGROUND};
            }}
            div.stButton > button:focus {{
                box-shadow: 0 0 0 2px {PRIMARY_COLOR};
            }}
        </style>
    """, unsafe_allow_html=True)
    

def apply_selectbox_style():
    st.markdown(f"""
        <style>
            div[data-baseweb="select"] > div {{
                background-color: {BACKGROUND};
                color: {TEXT_COLOR_PRIMARY};
                border: 2px solid {PRIMARY_COLOR};
                padding: 10px 20px;
                border-radius: 8px;
            }}

            div[data-baseweb="select"] > div:hover {{
                background-color: {PRIMARY_COLOR};
                color: {BACKGROUND};
            }}

            div[data-baseweb="select"] > div:focus {{
                box-shadow: 0 0 0 2px {PRIMARY_COLOR};
            }}
        </style>
    """, unsafe_allow_html=True)


def apply_metric_style():
    st.markdown(f"""
        <style>
            div[data-testid="metric-container"] {{
                background-color: {BACKGROUND};
                color: {TEXT_COLOR_PRIMARY};
                border: 1.5px solid {PRIMARY_COLOR};
                border-radius: 8px;
                padding: 16px;
                margin: 6px;
                text-align: center;
            }}

            div[data-testid="metric-container"] > label {{
                color: {TEXT_COLOR_SECONDARY};
                font-size: 16px;
            }}
        </style>
    """, unsafe_allow_html=True)