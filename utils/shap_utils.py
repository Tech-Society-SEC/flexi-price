import shap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import streamlit as st

matplotlib.rcParams.update({
    'figure.facecolor': '#08090d',
    'axes.facecolor': '#13151f',
    'axes.edgecolor': '#2a2d3e',
    'axes.labelcolor': '#f0f2ff',
    'text.color': '#f0f2ff',
    'xtick.color': '#8b8fa8',
    'ytick.color': '#8b8fa8',
    'grid.color': '#1a1d2e',
    'font.family': 'sans-serif',
    'font.size': 11,
})

FEATURE_LABELS = {
    "TotalDemand": "Total Demand",
    "AveragePrice": "Avg Price",
    "StockLevel": "Stock Level",
    "CompetitorPrice": "Competitor Price",
    "Month": "Month",
    "WeekOfYear": "Week of Year",
    "DayOfWeek": "Day of Week",
    "PriceGapRatio": "Price Gap Ratio",
}


@st.cache_data
def compute_shap(_model, _input_df):
    explainer = shap.TreeExplainer(_model)
    shap_values = explainer.shap_values(_input_df)
    expected_value = float(explainer.expected_value)
    return shap_values, expected_value


def plot_shap_waterfall(shap_values, expected_value, input_df, predicted_price):
    sv = shap_values[0]
    features = input_df.columns.tolist()
    values = input_df.iloc[0].tolist()

    # Sort by absolute SHAP value
    pairs = sorted(zip(sv, features, values), key=lambda x: abs(x[0]), reverse=True)
    sv_sorted = [p[0] for p in pairs]
    feat_sorted = [FEATURE_LABELS.get(p[1], p[1]) for p in pairs]
    val_sorted = [p[2] for p in pairs]

    fig, ax = plt.subplots(figsize=(9, 5))
    fig.patch.set_facecolor('#08090d')
    ax.set_facecolor('#0f1117')

    colors = ['#00e5a0' if v >= 0 else '#ff4d8d' for v in sv_sorted]
    bars = ax.barh(feat_sorted, sv_sorted, color=colors, alpha=0.85, height=0.6,
                   edgecolor='none')

    for bar, val, sv_val in zip(bars, val_sorted, sv_sorted):
        label = f"  {val:.1f}" if isinstance(val, float) else f"  {val}"
        x_pos = bar.get_width() + (0.5 if sv_val >= 0 else -0.5)
        ax.text(x_pos, bar.get_y() + bar.get_height() / 2,
                label, va='center', ha='left' if sv_val >= 0 else 'right',
                color='#8b8fa8', fontsize=9)

    ax.axvline(0, color='#2a2d3e', linewidth=1.5)
    ax.set_xlabel("SHAP Value (impact on predicted price)", color='#8b8fa8', fontsize=10)
    ax.set_title(f"Feature Contribution — Predicted: ₹{predicted_price:.2f}", 
                 color='#f0f2ff', fontsize=13, fontweight='bold', pad=15)
    ax.tick_params(colors='#8b8fa8')
    ax.spines[:].set_visible(False)
    plt.tight_layout()
    return fig


def plot_feature_importance(model):
    importances = model.feature_importances_
    features = ["TotalDemand", "AveragePrice", "StockLevel", "CompetitorPrice",
                "Month", "WeekOfYear", "DayOfWeek", "PriceGapRatio"]
    labels = [FEATURE_LABELS.get(f, f) for f in features]

    pairs = sorted(zip(importances, labels), reverse=True)
    imp_sorted = [p[0] for p in pairs]
    lbl_sorted = [p[1] for p in pairs]

    fig, ax = plt.subplots(figsize=(9, 4.5))
    fig.patch.set_facecolor('#08090d')
    ax.set_facecolor('#0f1117')

    gradient_colors = ['#6c63ff', '#7b73ff', '#8a84ff', '#9996ff',
                       '#00d4ff', '#00c0e8', '#00acd0', '#0098b8']
    bars = ax.barh(lbl_sorted, imp_sorted, color=gradient_colors[:len(lbl_sorted)],
                   alpha=0.9, height=0.6, edgecolor='none')

    for bar, val in zip(bars, imp_sorted):
        ax.text(bar.get_width() + 0.005, bar.get_y() + bar.get_height() / 2,
                f"{val:.3f}", va='center', color='#8b8fa8', fontsize=9)

    ax.set_xlabel("Feature Importance Score", color='#8b8fa8', fontsize=10)
    ax.set_title("Global Feature Importance (XGBoost)", 
                 color='#f0f2ff', fontsize=13, fontweight='bold', pad=15)
    ax.tick_params(colors='#8b8fa8')
    ax.spines[:].set_visible(False)
    ax.set_xlim(0, max(imp_sorted) * 1.18)
    plt.tight_layout()
    return fig
