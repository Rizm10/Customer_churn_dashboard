from data_preprocessing import preprocessing_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

def train_and_select_best_model(file_path="Streamlit dashboard/Telco ML dashboard/Telco-Customer-Churn.csv"):
    X, y, encoders, scaler, churn_col = preprocessing_data(file_path)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    models = {
        "logreg": LogisticRegression(),
        "rfc": RandomForestClassifier(),
        "xgb": XGBClassifier(use_label_encoder=False, eval_metric='logloss')
        }

    f1_scores = {}
    trained_models = {}

    for name, model in models.items():
        model.fit(X_train,y_train)
        preds = model.predict(X_test)
        f1_scores[name] = f1_score(y_test,preds)
        trained_models[name] = model
    
    best_model_name = max(f1_scores, key = f1_scores.get)
    print("Best model based on F1:", best_model_name)

    return trained_models[best_model_name], best_model_name, X_train, y_train


def retrain_best_model(data,labels , model_name = "xgb"):
    if model_name == "logreg":
        model = LogisticRegression()
    elif model_name == "rfc":
        model = RandomForestClassifier()
    else:
        model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

    model.fit(data, labels)
    return model
  