import plotly.express as px
from style import (
    BACKGROUND, TEXT_COLOR_PRIMARY, TEXT_COLOR_SECONDARY,
    PRIMARY_COLOR, FONT_FAMILY, SECONDARY_COLOR
)

def get_base_layout():
    return {
        "paper_bgcolor": BACKGROUND,
        "plot_bgcolor": BACKGROUND,
        "font": {
            "color": TEXT_COLOR_PRIMARY,
            "family": FONT_FAMILY,
            "size": 14,
        },
        "title": {
            "font": {
                "family": FONT_FAMILY,
                "color": TEXT_COLOR_PRIMARY,
                "size": 18
            }
        },
        "margin": {"l": 60, "r": 40, "t": 40, "b": 40},
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
        }
    }

def normalize_churn_column(df):
    churn_col = next((col for col in df.columns if col.lower() == "churn"), None)
    if churn_col is None:
        raise ValueError("Churn column not found.")
    df[churn_col] = df[churn_col].astype(str).str.strip().str.lower().replace({"0": "no", "1": "yes"})
    df[churn_col] = df[churn_col].str.capitalize()
    return df, churn_col

def churn_distribution_chart(df):
    df, churn_col = normalize_churn_column(df)
    fig = px.pie(
        df, names=churn_col, color=churn_col,
        title="Churn Distribution",
        labels={churn_col: "Churn Status"},
        color_discrete_sequence=[PRIMARY_COLOR, SECONDARY_COLOR],
        category_orders={churn_col: ["No", "Yes"]},
    )
    fig.update_layout(**get_base_layout(), height=400)
    fig.update_traces(textinfo='percent+label', pull=[0.1, 0.1])
    return fig

def churn_bycontract_chart(df):
    df, churn_col = normalize_churn_column(df)
    fig = px.bar(
        df, x="Contract", color=churn_col,
        title="Churn by Contract Type",
        labels={"Contract": "Contract Type", churn_col: "Churn Status"},
        color_discrete_sequence=[PRIMARY_COLOR, SECONDARY_COLOR],
        category_orders={churn_col: ["No", "Yes"]},
        barmode="group"
    )
    fig.update_layout(**get_base_layout(), height=400)
    fig.update_traces(texttemplate='%{y}', textposition='outside')
    fig.update_xaxes(title_text="Contract Type")
    fig.update_yaxes(title_text="Churn Count")
    return fig

def monthly_charges_chart(df):
    df, churn_col = normalize_churn_column(df)
    fig = px.box(
        df, x=churn_col, y="MonthlyCharges", color=churn_col,
        title="Monthly Charges by Churn Status",
        labels={churn_col: "Churn Status", "MonthlyCharges": "Monthly Charges"},
        color_discrete_sequence=[PRIMARY_COLOR, SECONDARY_COLOR],
        category_orders={churn_col: ["No", "Yes"]}
    )
    fig.update_layout(**get_base_layout(), height=400)
    fig.update_traces(boxmean='sd')
    fig.update_xaxes(title_text="Churn Status")
    fig.update_yaxes(title_text="Monthly Charges")
    return fig

def tenure_distribution_chart(df):
    df, churn_col = normalize_churn_column(df)
    grouped_df = df.groupby(['tenure', churn_col]).size().reset_index(name='Count')
    fig = px.line(
        grouped_df, x="tenure", y="Count", color=churn_col,
        title="Churn by Tenure",
        labels={"tenure": "Tenure (Months)", "Count": "Churn Count", churn_col: "Churn Status"},
        color_discrete_sequence=[PRIMARY_COLOR, SECONDARY_COLOR],
        category_orders={churn_col: ["No", "Yes"]},
    )
    fig.update_layout(**get_base_layout(), height=400)
    fig.update_traces(mode='lines+markers', line=dict(width=2))
    fig.update_xaxes(title_text="Tenure (Months)")
    fig.update_yaxes(title_text="Churn Count")
    return fig

def internet_service_churn_chart(df):
    df, churn_col = normalize_churn_column(df)
    grouped_df = df.groupby(['InternetService', churn_col]).size().reset_index(name='Count')
    fig = px.bar(
        grouped_df,
        x="InternetService", y="Count", color=churn_col,
        title="Churn by Internet Service Type",
        labels={"InternetService": "Internet Service", "Count": "Churn Count", churn_col: "Churn Status"},
        color_discrete_sequence=[PRIMARY_COLOR, SECONDARY_COLOR],
        category_orders={churn_col: ["No", "Yes"]},
        barmode="group"
    )
    fig.update_layout(**get_base_layout(), height=400)
    fig.update_traces(texttemplate='%{y}', textposition='outside')
    fig.update_xaxes(title_text="Internet Service Type")
    fig.update_yaxes(title_text="Churn Count")
    return fig