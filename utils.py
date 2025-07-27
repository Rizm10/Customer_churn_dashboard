# utils/shap_utils.py

import shap
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


@st.cache_data(show_spinner=False) # Cache SHAP values to avoid recomputation reserved for premium 
def get_shap_values(model, X):
    """
    Generate SHAP values using a model and input data.

    Returns:
        shap_values: SHAP values object
    """
    try:
        explainer = shap.Explainer(model, X)
        shap_values = explainer(X)
        return shap_values
    except Exception as e:
        st.warning(f"⚠️ SHAP could not be computed: {e}")
        return None


@st.cache_data(show_spinner=False)
def get_shap_bar_chart(shap_values, X, top_n=10):
    """
    Create a horizontal bar chart from SHAP values using Plotly.

    Parameters:
        shap_values: SHAP values object
        X: Original feature DataFrame
        top_n: Number of top features to display

    Returns:
        Plotly figure
    """
    if shap_values is None:
        st.error("SHAP values not available.")
        return None

    mean_abs_shap = np.abs(shap_values.values).mean(axis=0)
    shap_df = pd.DataFrame({
        "Feature": X.columns,
        "MeanAbsSHAP": mean_abs_shap
    }).sort_values("MeanAbsSHAP", ascending=True).tail(top_n)

    fig = px.bar(
        shap_df,
        x="MeanAbsSHAP",
        y="Feature",
        orientation="h",
        title="🔍 Top Feature Drivers (Mean SHAP Values)",
        labels={"MeanAbsSHAP": "Mean |SHAP| Value", "Feature": "Feature"},
        height=450
    )
    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        margin=dict(l=60, r=40, t=40, b=40)
    )
    return fig

def apply_filter(data, region=None, contract_type=None, tenure_range=None , gender=None):
    df= data.copy()
    if region and region != "All":
        df = df[df['Region'] == region]
    if contract_type and contract_type != "All":
        df = df[df['Contract'] == contract_type]
    if tenure_range:
        df = df[(df['tenure'] >= tenure_range[0]) & (df['tenure'] <= tenure_range[1])]
    
    if gender and gender != "All":
        df = df[df['gender'] == gender]
    
    return df
