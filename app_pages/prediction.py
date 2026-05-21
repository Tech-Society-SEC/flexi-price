# app_pages/prediction.py

import streamlit as st
import streamlit.components.v1 as components

from utils.prediction_utils import predict_price


def show_prediction():

    # =========================
    # PAGE HEADER
    # =========================
    st.markdown(
        """
<div class='main-title'>
    Dynamic Pricing Intelligence
</div>

<div class='subtitle'>
    Machine-learning powered pricing recommendations
    for adaptive e-commerce optimization.
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
Generate intelligent pricing recommendations using
ensemble machine learning models.
"""
    )

    st.markdown("---")

    # =========================
    # INPUT COLUMNS
    # =========================
    col1, col2 = st.columns(2)

    # =========================
    # LEFT COLUMN
    # =========================
    with col1:

        total_demand = st.number_input(
            "Total Demand",
            min_value=0.0,
            value=100.0
        )

        average_price = st.number_input(
            "Average Price",
            min_value=0.0,
            value=200.0
        )

        stock_level = st.number_input(
            "Stock Level",
            min_value=0.0,
            value=50.0
        )

        competitor_price = st.number_input(
            "Competitor Price",
            min_value=0.0,
            value=220.0
        )

    # =========================
    # RIGHT COLUMN
    # =========================
    with col2:

        month = st.selectbox(
            "Month",
            list(range(1, 13))
        )

        week_of_year = st.slider(
            "Week Of Year",
            1,
            52,
            10
        )

        day_of_week = st.selectbox(
            "Day Of Week",
            [0, 1, 2, 3, 4, 5, 6]
        )

    st.markdown("")

    # =========================
    # PREDICTION BUTTON
    # =========================
    if st.button(
        "Generate AI Recommendation",
        use_container_width=True
    ):

        # =========================
        # MODEL PREDICTION
        # =========================
        result = predict_price(
            total_demand,
            average_price,
            stock_level,
            competitor_price,
            month,
            week_of_year,
            day_of_week
        )

        st.markdown("---")

        # =========================
        # FINAL PRICE CARD
        # =========================
        result_html = f"""
<div style="
    background: linear-gradient(
        135deg,
        rgba(124,58,237,0.18),
        rgba(37,99,235,0.18)
    );
    padding: 35px;
    border-radius: 24px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
">

    <div style="
        font-size:15px;
        color:#94a3b8;
        margin-bottom:10px;
    ">
        Recommended Selling Price
    </div>

    <div style="
        font-size:56px;
        font-weight:700;
        color:white;
    ">
        ${result['final_prediction']:.2f}
    </div>

</div>
"""

        components.html(result_html, height=180)

        st.markdown("")

        # =========================
        # BUSINESS INSIGHTS
        # =========================
        metric1, metric2, metric3 = st.columns(3)

        # =========================
        # CONFIDENCE INTERVAL
        # =========================
        with metric1:

            metric1_html = f"""
<div style="
    background: rgba(255,255,255,0.04);
    padding:20px;
    border-radius:18px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.06);
">

    <div style="
        font-size:15px;
        color:#94a3b8;
        margin-bottom:10px;
    ">
        Confidence Interval
    </div>

    <div style="
        font-size:28px;
        font-weight:600;
        color:white;
    ">
        {result['confidence_interval']}
    </div>

</div>
"""

            components.html(metric1_html, height=140)

        # =========================
        # ELASTICITY SCORE
        # =========================
        with metric2:

            metric2_html = f"""
<div style="
    background: rgba(255,255,255,0.04);
    padding:20px;
    border-radius:18px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.06);
">

    <div style="
        font-size:15px;
        color:#94a3b8;
        margin-bottom:10px;
    ">
        Elasticity Score
    </div>

    <div style="
        font-size:28px;
        font-weight:600;
        color:white;
    ">
        {result['elasticity_score']}
    </div>

</div>
"""

            components.html(metric2_html, height=140)

        # =========================
        # MARKET STATUS
        # =========================
        with metric3:

            metric3_html = f"""
<div style="
    background: rgba(255,255,255,0.04);
    padding:20px;
    border-radius:18px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.06);
">

    <div style="
        font-size:15px;
        color:#94a3b8;
        margin-bottom:10px;
    ">
        Market Status
    </div>

    <div style="
        font-size:28px;
        font-weight:700;
        color:#38bdf8;
    ">
        {"High" if total_demand > 300 else "Stable"}
    </div>

</div>
"""

            components.html(metric3_html, height=140)

        st.markdown("---")

        # =========================
        # MARKET TREND
        # =========================
        st.success(result['market_trend'])

        # =========================
        # FOOTER NOTE
        # =========================
        st.markdown(
            """
<div style='
    margin-top:20px;
    color:#94a3b8;
    font-size:15px;
    text-align:center;
'>

This recommendation is generated using an ensemble
machine learning system combining Linear Regression,
Random Forest, and XGBoost.

</div>
""",
            unsafe_allow_html=True
        )