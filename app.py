import streamlit as st
import pandas as pd

from style import (
    BACKGROUND, TEXT_COLOR_PRIMARY, TEXT_COLOR_SECONDARY,
    PRIMARY_COLOR, FONT_FAMILY, SECONDARY_COLOR, NEGATIVE_COLOR
)
from chart_styles import (
    churn_distribution_chart, churn_bycontract_chart,
    monthly_charges_chart, tenure_distribution_chart,
    internet_service_churn_chart
)
from model_training import train_and_select_best_model, retrain_best_model
from kpi import (
    churn_rate_kpi, customer_retention_kpi, total_customers_kpi,
    average_tenure_kpi, average_monthly_charges_kpi
)

def main():
    st.set_page_config(
        page_title="Telco ML Customer Churn Dashboard",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Telco Customer Churn Dashboard")
    st.markdown("This dashboard provides insights into customer churn using machine learning models.")
    st.sidebar.title("Navigation")

    # Load data and preprocess
    file_path = st.sidebar.text_input("Enter the path to the dataset:", "Telco-Customer-Churn.csv")
    df = None  # Define upfront for re-use

    if st.sidebar.button("Load Data"):
        try:
            model, best_model_name, X_train, y_train = train_and_select_best_model(file_path)
            st.success(f"Data loaded and best model trained: {best_model_name}")
        except Exception as e:
            st.error(f"Error loading data: {e}")

    # KPIs
    # KPIs
    st.sidebar.markdown("### Key Performance Indicators (KPIs)")

    if st.sidebar.button("Show KPIs"):
        try:
            df = pd.read_csv(file_path)

            col1, col2, col3 = st.columns(3)
            col1.metric("Churn Rate", f"{churn_rate_kpi(df):.2f}%")
            col2.metric("Avg Tenure", f"{average_tenure_kpi(df):.2f} months")
            col3.metric("Avg Monthly Charges", f"${average_monthly_charges_kpi(df):.2f}")

            col4, col5 = st.columns(2)
            col4.metric("Total Customers", f"{total_customers_kpi(df)}")
            col5.metric("Retention Rate", f"{customer_retention_kpi(df):.2f}%")

        except Exception as e:
            st.error(f"Error displaying KPIs: {e}")

    # Charts
    st.sidebar.markdown("### Charts")
    chart_choice = st.sidebar.selectbox(
        "Select a chart to display:",
        [
            "Churn Distribution",
            "Churn by Contract Type",
            "Monthly Charges by Churn Status",
            "Tenure Distribution",
            "Internet Service vs Churn"
        ]
    )

    try:
        df = pd.read_csv(file_path)
        fig = None

        if chart_choice == "Churn Distribution":
            fig = churn_distribution_chart(df)
        elif chart_choice == "Churn by Contract Type":
            fig = churn_bycontract_chart(df)
        elif chart_choice == "Monthly Charges by Churn Status":
            fig = monthly_charges_chart(df)
        elif chart_choice == "Tenure Distribution":
            fig = tenure_distribution_chart(df)
        elif chart_choice == "Internet Service vs Churn":
            fig = internet_service_churn_chart(df)

        if fig:
            st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Error displaying chart: {e}")

    # Model retraining
    st.sidebar.markdown("### Model Retraining")
    if st.sidebar.button("Retrain Best Model"):
        try:
            retrain_best_model(file_path)
            st.success("Best model retrained successfully.")
        except Exception as e:
            st.error(f"Error retraining model: {e}")

if __name__ == "__main__":
    main()