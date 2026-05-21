import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np


def show_dashboard():

    st.title("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Predictions", "1,250")
    col2.metric("Average Price", "$245")
    col3.metric("Demand Trend", "+18%")
    col4.metric("Competitor Impact", "High")

    st.markdown("---")

    df = pd.DataFrame({
        "Demand": np.random.randint(50, 500, 20),
        "Price": np.random.randint(100, 1000, 20)
    })

    fig = px.scatter(
        df,
        x="Demand",
        y="Price",
        title="Demand vs Price"
    )

    st.plotly_chart(fig, use_container_width=True)