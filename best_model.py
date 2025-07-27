from model_training import train_and_select_best_model
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import joblib

# Step 1: Get best model + data
model, best_model_name, X_train, y_train = train_and_select_best_model()

# Step 2: Set param grid + base model
if best_model_name == "logreg":
    base_model = LogisticRegression()
    param_grid = {
        'C': [0.001, 0.01, 0.1, 1, 10, 100],
        'penalty': ['l1', 'l2'],
        'solver': ['liblinear']
    }

elif best_model_name == "rfc":
    base_model = RandomForestClassifier()
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

elif best_model_name == "xgb":
    base_model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [3, 4, 5],
        'learning_rate': [0.01, 0.1, 0.2]
    }

# Step 3: Run grid search
grid = GridSearchCV(base_model, param_grid, cv=5, n_jobs=-1)
grid.fit(X_train, y_train)

# Step 4: Save best model
joblib.dump(grid.best_estimator_, "best_model.pkl")

# Step 5: Output
print(f"✅ {best_model_name.upper()} saved as best_model.pkl")
print("Best Params:", grid.best_params_)
print("Best CV Score:", grid.best_score_)