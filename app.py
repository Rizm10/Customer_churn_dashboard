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

    # File path input
    file_path = st.sidebar.text_input("Enter the path to the dataset:", "Telco-Customer-Churn.csv")

    # Load Data
    if st.sidebar.button("Load Data"):
        try:
            df = pd.read_csv(file_path)
            model, best_model_name, X_train, y_train = train_and_select_best_model(file_path)
            st.session_state["df"] = df
            st.session_state["model"] = model
            st.session_state["best_model_name"] = best_model_name
            st.success(f"Data loaded and best model trained: {best_model_name}")
        except Exception as e:
            st.error(f"Error loading data: {e}")

    # KPIs
    st.sidebar.markdown("### Key Performance Indicators (KPIs)")

    if "df" in st.session_state:
        df = st.session_state["df"]

        if st.sidebar.button("Show KPIs"):
            try:
                col1, col2, col3 = st.columns(3)
                col1.metric("Churn Rate", f"{churn_rate_kpi(df):.2f}%")
                col2.metric("Avg Tenure", f"{average_tenure_kpi(df):.2f} months")
                col3.metric("Avg Monthly Charges", f"${average_monthly_charges_kpi(df):.2f}")

                col4, col5 = st.columns(2)
                col4.metric("Total Customers", total_customers_kpi(df))
                col5.metric("Retention Rate", f"{customer_retention_kpi(df):.2f}%")
            except Exception as e:
                st.error(f"Error displaying KPIs: {e}")
    else:
        st.sidebar.warning("⚠️ Load the data first to view KPIs.")

    # Charts
    st.sidebar.markdown("### Charts")
    selected_charts = st.sidebar.multiselect(
        "Select charts to display:",
        [
            "Churn Distribution",
            "Churn by Contract Type",
            "Monthly Charges by Churn Status",
            "Internet Service vs Churn"
        ],
        default=["Churn Distribution", "Churn by Contract Type"]
    )

    chart_map = {
        "Churn Distribution": churn_distribution_chart,
        "Churn by Contract Type": churn_bycontract_chart,
        "Monthly Charges by Churn Status": monthly_charges_chart,
        "Internet Service vs Churn": internet_service_churn_chart
    }

    if "df" in st.session_state:
        df = st.session_state["df"]
        try:
            for i in range(0, len(selected_charts), 2):
                cols = st.columns(2)
                for j, chart_name in enumerate(selected_charts[i:i+2]):
                    chart_func = chart_map.get(chart_name)
                    if chart_func:
                        fig = chart_func(df)
                        cols[j].plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error rendering selected charts: {e}")
    else:
        st.sidebar.warning("⚠️ Load the data first to display charts.")

    # Retrain Model
    st.sidebar.markdown("### Model Retraining")
    if st.sidebar.button("Retrain Best Model"):
        if "df" in st.session_state:
            try:
                retrain_best_model(file_path)
                st.success("Best model retrained successfully.")
            except Exception as e:
                st.error(f"Error retraining model: {e}")
        else:
            st.warning("⚠️ Load the model before retraining.")

if __name__ == "__main__":
    main()
