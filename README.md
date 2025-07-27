Telco Customer Churn Prediction Dashboard
A professional, interactive Streamlit dashboard that leverages machine learning to analyze and predict customer churn in telecommunications data. This modular application provides comprehensive data visualization, model comparison, and actionable insights for business stakeholders.
🎯 Project Overview
This portfolio project demonstrates end-to-end machine learning implementation in a production-ready dashboard format. The application processes telecommunications customer data to identify churn patterns, compare multiple ML models, and deliver insights through an intuitive web interface designed for both technical and business audiences.
✨ Key Features
Interactive Dashboard Components
	•	Dynamic KPI Cards: Real-time metrics including Churn Rate, Average Customer Tenure, Monthly Charges, and Total Revenue
	•	Responsive UI: Clean, professional Streamlit interface optimized for desktop and mobile viewing
	•	Live Model Predictions: Real-time churn probability scoring for individual customers
Advanced Data Visualizations
	•	Churn Analysis: Interactive pie charts and bar plots showing churn distribution across customer segments
	•	Tenure Distribution: Histogram analysis revealing customer lifecycle patterns
	•	Revenue Analysis: Scatter plots and box plots correlating charges with churn behavior
	•	Model Performance Metrics: Confusion matrices, ROC curves, and AUC scores for model evaluation
Machine Learning Pipeline
	•	Multi-Model Comparison: Logistic Regression, Random Forest, and XGBoost implementations
	•	Automated Hyperparameter Tuning: GridSearchCV optimization for enhanced model performance
	•	Model Persistence: Trained models saved for consistent predictions across sessions
	•	Feature Engineering: Automated preprocessing and feature selection pipeline
	•	SHAP Integration: Explainable AI features for model interpretability (in development)
Production-Ready Architecture
	•	Modular Design: Separation of concerns across multiple Python modules
	•	Scalable Deployment: Compatible with cloud platforms via ngrok integration
	•	Error Handling: Robust exception management and user feedback systems
🛠️ Technology Stack
Core Framework
	•	Python 3.8+: Primary development language
	•	Streamlit: Web application framework for rapid dashboard development
Machine Learning & Data Science
	•	scikit-learn: Model training, evaluation, and preprocessing
	•	XGBoost: Gradient boosting implementation for enhanced prediction accuracy
	•	pandas: Data manipulation and analysis
	•	NumPy: Numerical computing and array operations
Visualization & UI
	•	Matplotlib: Statistical plotting and visualization
	•	Plotly: Interactive charts and dashboard components
	•	Seaborn: Enhanced statistical visualizations
Optional Extensions
	•	SHAP: Model explainability and feature importance analysis
	•	Google Colab: Cloud-based development and deployment environment



 📁 Project Structure


 Module Responsibilities
	•	app.py: Orchestrates the Streamlit interface, handles user interactions, and coordinates between modules
	•	data_processing.py: Implements ETL pipeline, handles missing values, encodes categorical variables, and performs feature scaling
	•	model_training.py: Manages model training workflows, hyperparameter optimization, and performance evaluation
	•	best_model.py: Provides production-ready prediction interface and model loading utilities
	•	style.py: Centralizes CSS styling and maintains consistent UI/UX across the application


 🚀 Getting Started

 Streamlit link :

 local installation:
Prerequisites
	•	Python 3.8 or higher
	•	pip package manager
	•	Internet connection for initial setup
Installation & Setup
	1.	Clone the repository
 git clone https://github.com/Rizm10/telco-churn-dashboard.git
cd telco-churn-dashboard

 	2.	Install dependencies
  pip install -r requirements.txt

  3.	Launch the application
   streamlit run app.py

 Access the dashboard
	•	Local development: http://localhost:8501

