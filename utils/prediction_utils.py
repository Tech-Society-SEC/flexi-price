import pandas as pd

from utils.model_loader import (
    linear_model,
    rf_model,
    xgb_model
)


feature_columns = [
    'TotalDemand',
    'AveragePrice',
    'StockLevel',
    'CompetitorPrice',
    'Month',
    'WeekOfYear',
    'DayOfWeek',
    'PriceGapRatio'
]


def predict_price(
    total_demand,
    average_price,
    stock_level,
    competitor_price,
    month,
    week_of_year,
    day_of_week
):

    # =========================
    # DERIVED FEATURE
    # =========================
    price_gap_ratio = (
        (competitor_price - average_price)
        / average_price
    )

    # =========================
    # CREATE INPUT DATAFRAME
    # =========================
    sample_data = pd.DataFrame({
        'TotalDemand': [total_demand],
        'AveragePrice': [average_price],
        'StockLevel': [stock_level],
        'CompetitorPrice': [competitor_price],
        'Month': [month],
        'WeekOfYear': [week_of_year],
        'DayOfWeek': [day_of_week],
        'PriceGapRatio': [price_gap_ratio]
    })

    sample_data = sample_data.astype(float)

    # =========================
    # MODEL PREDICTIONS
    # =========================
    linear_pred = linear_model.predict(sample_data)[0]

    rf_pred = rf_model.predict(sample_data)[0]

    xgb_pred = xgb_model.predict(sample_data)[0]

    # =========================
    # ENSEMBLE FINAL PREDICTION
    # =========================
    final_prediction = (
        linear_pred * 0.4 +
        rf_pred * 0.3 +
        xgb_pred * 0.3
    )

    final_prediction = round(final_prediction, 2)

    # =========================
    # CONFIDENCE INTERVAL
    # =========================
    lower_bound = round(final_prediction - 10, 2)

    upper_bound = round(final_prediction + 10, 2)

    # =========================
    # ELASTICITY SCORE
    # =========================
    elasticity_score = round(price_gap_ratio, 2)

    # =========================
    # MARKET TREND
    # =========================
    if total_demand > 300:

        market_trend = "🔥 High Demand Market"

    else:

        market_trend = "📈 Stable Market"

    # =========================
    # RETURN FINAL OUTPUT ONLY
    # =========================
    return {

        "final_prediction": final_prediction,

        "confidence_interval":
        f"${lower_bound} - ${upper_bound}",

        "elasticity_score":
        elasticity_score,

        "market_trend":
        market_trend
    }