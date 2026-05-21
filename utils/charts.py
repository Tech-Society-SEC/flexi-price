import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

COLORS = {
    "primary": "#6c63ff",
    "secondary": "#00d4ff",
    "green": "#00e5a0",
    "orange": "#ff7c4d",
    "pink": "#ff4d8d",
    "bg": "#08090d",
    "card": "#13151f",
    "elevated": "#1a1d2e",
    "text": "#f0f2ff",
    "muted": "#8b8fa8",
    "border": "rgba(108,99,255,0.2)",
}

LAYOUT_BASE = dict(
    paper_bgcolor=COLORS["card"],
    plot_bgcolor=COLORS["card"],
    font=dict(family="DM Sans, sans-serif", color=COLORS["muted"], size=12),
    margin=dict(l=20, r=20, t=50, b=20),
    xaxis=dict(gridcolor=COLORS["elevated"], showline=False, zeroline=False, tickfont=dict(color=COLORS["muted"])),
    yaxis=dict(gridcolor=COLORS["elevated"], showline=False, zeroline=False, tickfont=dict(color=COLORS["muted"])),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=COLORS["muted"])),
)


def demand_vs_price_chart():
    demand = np.linspace(100, 10000, 100)
    price_base = 150 + (demand / 10000) * 120
    price_upper = price_base * 1.12
    price_lower = price_base * 0.88

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=demand, y=price_upper, fill=None, mode='lines',
        line=dict(color='rgba(108,99,255,0.1)', width=0), showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=demand, y=price_lower, fill='tonexty', mode='lines',
        line=dict(color='rgba(108,99,255,0.1)', width=0),
        fillcolor='rgba(108,99,255,0.12)', name='Confidence Band'
    ))
    fig.add_trace(go.Scatter(
        x=demand, y=price_base, mode='lines',
        line=dict(color=COLORS["primary"], width=3),
        name='Predicted Price'
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text="Demand vs Predicted Price", font=dict(color=COLORS["text"], size=15, family="Syne, sans-serif")),
        xaxis_title="Total Demand",
        yaxis_title="Recommended Price (₹)",
        height=320,
    )
    return fig


def seasonal_pricing_chart():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    prices = [182, 175, 178, 190, 195, 205, 210, 215, 200, 225, 250, 270]
    competitor = [185, 180, 182, 188, 192, 200, 205, 210, 198, 220, 245, 265]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=prices, mode='lines+markers',
        line=dict(color=COLORS["primary"], width=3),
        marker=dict(size=8, color=COLORS["primary"], line=dict(width=2, color=COLORS["card"])),
        name='Our Price'
    ))
    fig.add_trace(go.Scatter(
        x=months, y=competitor, mode='lines+markers',
        line=dict(color=COLORS["orange"], width=2, dash='dot'),
        marker=dict(size=7, color=COLORS["orange"]),
        name='Competitor Price'
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text="Seasonal Pricing Trends", font=dict(color=COLORS["text"], size=15, family="Syne, sans-serif")),
        xaxis_title="Month",
        yaxis_title="Price (₹)",
        height=320,
    )
    return fig


def weekly_predictions_chart():
    weeks = list(range(1, 53))
    base = 180
    predictions = [base + 15 * np.sin(w * 0.3) + np.random.normal(0, 5) for w in weeks]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=weeks, y=predictions,
        marker=dict(
            color=predictions,
            colorscale=[[0, COLORS["primary"]], [0.5, COLORS["secondary"]], [1, COLORS["green"]]],
            showscale=False,
            line=dict(width=0),
        ),
        name='Predicted Price'
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text="Weekly Price Predictions (52 Weeks)", font=dict(color=COLORS["text"], size=15, family="Syne, sans-serif")),
        xaxis_title="Week of Year",
        yaxis_title="Price (₹)",
        height=300,
        bargap=0.15,
    )
    return fig


def stock_impact_chart():
    stock = np.linspace(0, 1000, 50)
    price = 250 - (stock / 1000) * 80 + np.random.normal(0, 3, 50)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=stock, y=price, mode='markers',
        marker=dict(
            size=8, color=stock,
            colorscale=[[0, COLORS["pink"]], [1, COLORS["green"]]],
            showscale=True,
            colorbar=dict(title="Stock", tickfont=dict(color=COLORS["muted"]), len=0.7),
            opacity=0.8,
        ),
        name='Price vs Stock'
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text="Stock Level → Price Impact", font=dict(color=COLORS["text"], size=15, family="Syne, sans-serif")),
        xaxis_title="Stock Level",
        yaxis_title="Recommended Price (₹)",
        height=320,
    )
    return fig


def competitor_analysis_chart():
    categories = ['Electronics', 'Fashion', 'Home', 'Sports', 'Beauty', 'Books']
    our_prices = [320, 150, 200, 180, 90, 45]
    comp_prices = [335, 145, 210, 175, 95, 48]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Our Price', x=categories, y=our_prices,
        marker_color=COLORS["primary"], marker_line_width=0,
    ))
    fig.add_trace(go.Bar(
        name='Competitor Avg', x=categories, y=comp_prices,
        marker_color=COLORS["secondary"], marker_line_width=0, opacity=0.75,
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text="Category-wise Competitor Analysis", font=dict(color=COLORS["text"], size=15, family="Syne, sans-serif")),
        barmode='group',
        bargap=0.25,
        bargroupgap=0.08,
        height=340,
    )
    return fig


def demand_distribution_chart():
    np.random.seed(42)
    demand_data = np.concatenate([
        np.random.normal(2000, 600, 300),
        np.random.normal(6000, 800, 200),
    ])
    demand_data = demand_data[(demand_data > 0) & (demand_data < 10000)]

    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=demand_data, nbinsx=40,
        marker=dict(
            color=COLORS["primary"],
            opacity=0.85,
            line=dict(width=0),
        ),
        name='Demand Distribution'
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text="Demand Distribution", font=dict(color=COLORS["text"], size=15, family="Syne, sans-serif")),
        xaxis_title="Total Demand",
        yaxis_title="Frequency",
        height=300,
    )
    return fig


def pricing_heatmap_chart():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    categories = ['Electronics', 'Fashion', 'Home', 'Sports', 'Beauty']

    np.random.seed(7)
    z = np.random.uniform(100, 400, (len(categories), len(months)))
    z[0][10:] += 80   # Electronics peak Nov-Dec
    z[1][3:6] += 50   # Fashion peak Apr-Jun

    fig = go.Figure(data=go.Heatmap(
        z=z, x=months, y=categories,
        colorscale=[[0, '#13151f'], [0.4, '#6c63ff'], [0.7, '#00d4ff'], [1, '#00e5a0']],
        showscale=True,
        colorbar=dict(title="Price (₹)", tickfont=dict(color=COLORS["muted"]), len=0.8),
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text="Pricing Heatmap — Category × Month", font=dict(color=COLORS["text"], size=15, family="Syne, sans-serif")),
        height=320,
    )
    return fig


def confidence_gauge(predicted_price, ci_lower, ci_upper):
    ci_width = (ci_upper - ci_lower) / predicted_price * 100
    confidence = max(60, min(98, 100 - ci_width * 2))

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence,
        number=dict(suffix="%", font=dict(size=36, color=COLORS["text"], family="Syne, sans-serif")),
        title=dict(text="Prediction Confidence", font=dict(color=COLORS["muted"], size=13)),
        gauge=dict(
            axis=dict(range=[0, 100], tickfont=dict(color=COLORS["muted"])),
            bar=dict(color=COLORS["primary"]),
            bgcolor=COLORS["elevated"],
            borderwidth=0,
            steps=[
                dict(range=[0, 60], color=COLORS["elevated"]),
                dict(range=[60, 80], color=COLORS["elevated"]),
                dict(range=[80, 100], color=COLORS["elevated"]),
            ],
            threshold=dict(
                line=dict(color=COLORS["green"], width=3),
                thickness=0.85,
                value=90
            )
        )
    ))
    fig.update_layout(
        paper_bgcolor=COLORS["card"],
        font=dict(color=COLORS["text"]),
        height=250,
        margin=dict(l=20, r=20, t=40, b=20),
    )
    return fig, confidence
