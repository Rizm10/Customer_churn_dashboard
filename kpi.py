import streamlit as st
from style import BACKGROUND, TEXT_COLOR_PRIMARY, TEXT_COLOR_SECONDARY, PRIMARY_COLOR, FONT_FAMILY, SECONDARY_COLOR, NEGATIVE_COLOR
from chart_styles import get_base_layout

def average_tenure_kpi(df):
    return df['tenure'].mean()

def churn_rate_kpi(df):
    churn_col = df['Churn']
    if churn_col.dtype == 'object':
        churn_col = churn_col.str.lower().map({'yes': 1, 'no': 0})
    return churn_col.mean() * 100

def total_customers_kpi(df):
    return df.shape[0]

def average_monthly_charges_kpi(df):
    return df['MonthlyCharges'].mean()

def customer_retention_kpi(df):
    churn_col = df['Churn']
    if churn_col.dtype == 'object':
        churn_col = churn_col.str.lower().map({'yes': 1, 'no': 0})
    retained_customers = (churn_col == 0).sum()
    total_customers = len(churn_col)
    return (retained_customers / total_customers) * 100 if total_customers else 0