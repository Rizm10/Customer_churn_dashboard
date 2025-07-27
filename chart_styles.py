from style import BACKGROUND, TEXT_COLOR_PRIMARY, TEXT_COLOR_SECONDARY, PRIMARY_COLOR, FONT_FAMILY , SECONDARY_COLOR ,NEGATIVE_COLOR

import streamlit as st
import plotly.express as px


def get_base_layout():
    return {
        "paper_bgcolor": BACKGROUND,
        "plot_bgcolor": BACKGROUND,
        "font": {
            "color": TEXT_COLOR_PRIMARY,
            "family": FONT_FAMILY,
            "size": 14,},
        
       "title":{
            "font": {
                "family": FONT_FAMILY,
                "color": TEXT_COLOR_PRIMARY,
                "size": 18 

        } },
        "margin": {
            "l": 60,
            "r": 40,
            "t": 40,
            "b": 40
        
        },
       "xaxis": {
            "gridcolor": TEXT_COLOR_SECONDARY,
            "zerolinecolor": TEXT_COLOR_SECONDARY,
            "showline": True,
            "linecolor": TEXT_COLOR_PRIMARY
        },
        "yaxis": {
            "gridcolor": TEXT_COLOR_SECONDARY,
            "zerolinecolor": TEXT_COLOR_SECONDARY,
            "showline": True,
            "linecolor": TEXT_COLOR_PRIMARY
        },
        "legend": {
            "font": {
                "family": FONT_FAMILY,
                "color": TEXT_COLOR_PRIMARY,
                "size": 12
            },
            "bgcolor": BACKGROUND,
            "bordercolor": TEXT_COLOR_SECONDARY,
            "borderwidth": 1

    }}


def churn_distribution_chart(df):
    fig = px.pie(
        df,
        names="Churn",
        color="Churn",
        title=" Churn Distribution",
        labels={"Churn": "Churn Status"},
        color_discrete_sequence=[PRIMARY_COLOR, SECONDARY_COLOR],
        category_orders={"Churn": ["No", "Yes"]},
    )
    fig.update_layout(**get_base_layout(), height=400)
    fig.update_traces(textinfo='percent+label', pull=[0.1, 0.1])
    return fig

def churn_bycontract_chart(df):
    fig = px.bar(
        df,
        x= "Contract",
        y = "Churn",
        color="Churn",
        title = "Churn by Contract Type",
        labels={"Contract": "Contract Type", "Churn": "Churn Count"},
        color_discrete_sequence=[PRIMARY_COLOR, SECONDARY_COLOR],
        category_orders = {"Churn": ["No", "Yes"]},
        barmode="group")
    fig.update_layout(**get_base_layout(), height=400)
    fig.update_traces(texttemplate='%{y}', textposition='outside')
    fig.update_xaxes(title_text="Contract Type")
    fig.update_yaxes(title_text="Churn Count")
    return fig

    
def monthly_charges_chart(df):
    fig = px.box(
        df,
        x="Churn",
        y= "MonthlyCharges",
        color="Churn",
        title = "Monthly charges by Churn Status",
        labels={"Churn": "Churn Status", "MonthlyCharges": "Monthly Charges"},
        color_discrete_sequence=[PRIMARY_COLOR, SECONDARY_COLOR],
        category_orders={"Churn": ["No", "Yes"]},

        )
    fig.update_layout(**get_base_layout(), height=400)
    fig.update_traces(boxmean='sd')
    fig.update_xaxes(title_text="Churn Status")
    fig.update_yaxes(title_text="Monthly Charges")
    return fig
    
def tenure_distribution_chart(df):
    grouped_df = df.groupby(['tenure', 'Churn']).size().reset_index(name='Count')
    fig = px.line(
        grouped_df,
        x="tenure",
        y="Count",
        color="Churn",
        title="Churn by Tenure",
        labels={"tenure": "Tenure (Months)", "Count": "Churn Count", "Churn": "Churn Status"},
        color_discrete_sequence=[PRIMARY_COLOR, SECONDARY_COLOR],
        category_orders={"Churn": ["No", "Yes"]},
    )
    fig.update_layout(**get_base_layout(), height=400)
    fig.update_traces(mode='lines+markers', line=dict(width=2))
    fig.update_xaxes(title_text="Tenure (Months)")
    fig.update_yaxes(title_text="Churn Count")
    return fig

def internet_service_churn_chart(df):
    grouped_df = df.groupby(['InternetService', 'Churn']).size().reset_index(name='Count')
    fig = px.bar(
        grouped_df,
        x="InternetService",
        y="Count",
        color="Churn",
        title="Churn by Internet Service Type",
        labels={"InternetService": "Internet Service Type", "Count": "Churn Count", "Churn": "Churn Status"},
        color_discrete_sequence=[PRIMARY_COLOR, SECONDARY_COLOR],
        category_orders={"Churn": ["No", "Yes"]},
        barmode="group"
    )
    fig.update_layout(**get_base_layout(), height=400)
    fig.update_traces(texttemplate='%{y}', textposition='outside')
    fig.update_xaxes(title_text="Internet Service Type")
    fig.update_yaxes(title_text="Churn Count")
    return fig