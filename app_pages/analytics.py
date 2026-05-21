import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def show_analytics():

    st.title("📈 Analytics")

    months = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    values = np.random.randint(100, 1000, 12)

    df = pd.DataFrame({
        "Month": months,
        "Price": values
    })

    fig = px.line(
        df,
        x="Month",
        y="Price",
        title="Seasonal Pricing Trend"
    )

    st.plotly_chart(fig, use_container_width=True)