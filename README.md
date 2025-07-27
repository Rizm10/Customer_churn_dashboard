📊 Telco Customer Churn Prediction Dashboard

A clean, modular Streamlit dashboard built to analyze and predict customer churn using machine learning. This project transforms raw telco customer data into real-time insights with interactive visuals and live model retraining — built for both technical users and business decision-makers.

🔗 Live Demo: https://telco-ml-churn.streamlit.app
📂 GitHub Repo: https://github.com/Rizm10/Customer_churn_dashboard


⸻

🎯 Overview

Originally built as a hands-on portfolio project, this dashboard takes a real Telco dataset and walks through the full machine learning pipeline:
	•	Cleaned and processed the data
	•	Built multiple ML models (LogReg, Random Forest, XGBoost)
	•	Compared performance
	•	Deployed best model to a live dashboard
	•	Modularized everything for clarity and reusability

Use this as a blueprint for real-world ML dashboard deployments or business churn analysis.

⸻

✨ Key Features

✅ Dashboard Highlights
	•	Live KPIs: Churn rate, tenure, monthly charges, retention
	•	Dynamic Visuals: Compare churn trends, contract types, revenue impact
	•	Model Retraining: Push-button retraining with latest data
	•	Responsive Layout: Professional UI styled with clean CSS logic

📊 Visual Charts
	•	Churn distribution (pie)
	•	Contract type vs churn (bar)
	•	Monthly charges by churn status (box)
	•	Internet service impact on churn (grouped bar)

⚙️ Machine Learning Pipeline
	•	Logistic Regression, Random Forest, XGBoost
	•	Train/test split with stratified sampling
	•	F1-score based model selection
	•	Full preprocessing pipeline: encoding + scaling
	•	Model retraining built-in (real-time)

🛠️ Tech Stack
Area Tools
Core Python, Streamlit
ML   scikit-learn, XGBoost
Data pandas, NumPy
Viz  Plotly, Matplotlib
Structure Modular Python scripts

├── app.py                # Streamlit front-end logic
├── data_processing.py   # Cleans and encodes data
├── model_training.py    # Handles model training and retraining
├── best_model.py        # Utilities to get predictions
├── style.py             # Central theme/style config
├── chart_styles.py      # Chart layout + visuals
├── kpi.py               # KPI calculation functions


Getting Started

Option 1: Try It Online

Streamlit App → https://telco-ml-churn.streamlit.app


Option 2: Run Locally

Pre-requisites:
	•	Python 3.8+
	•	pip

Setup:

git clone https://github.com/your-username/telco-churn-dashboard.git
cd telco-churn-dashboard
pip install -r requirements.txt
streamlit run app.py



