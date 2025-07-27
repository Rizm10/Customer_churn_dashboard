import streamlit as st
from style import BACKGROUND, TEXT_COLOR_PRIMARY, TEXT_COLOR_SECONDARY, PRIMARY_COLOR, FONT_FAMILY, SECONDARY_COLOR, NEGATIVE_COLOR
from chart_styles import get_base_layout

def churn_rate_kpi(df):
    churned = df[df['Churn'] == "Yes"].shape[0]
    total = df.shape[0]
    churn_rate = (churned / total) * 100 if total > 0 else 0
    return f"Churn Rate: {churn_rate:.2f}%"

def customer_retention_kpi(df):
    retained = df[df['Churn'] == "No"].shape[0]
    total = df.shape[0]
    retention_rate = (retained / total) * 100 if total > 0 else 0
    return f"Retention Rate: {retention_rate:.2f}%"

def total_customers_kpi(df):
    return f"Total Customers: {df.shape[0]}"

def average_tenure_kpi(df):
    avg_tenure = df['tenure'].mean()
    return f"Avg Tenure: {avg_tenure:.2f} months"

def average_monthly_charges_kpi(df):
    avg_charge = df['MonthlyCharges'].mean()
    return f"Avg Monthly Charges: ${avg_charge:.2f}"


