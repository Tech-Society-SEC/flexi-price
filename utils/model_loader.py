import joblib

# =========================
# LOAD MODELS
# =========================
linear_model = joblib.load(
    "models/linear_regression_model.pkl"
)

rf_model = joblib.load(
    "models/random_forest_model.pkl"
)

xgb_model = joblib.load(
    "models/xgboost_model.pkl"
)