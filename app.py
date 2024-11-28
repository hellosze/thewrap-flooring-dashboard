import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development


dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"

# read csv from a URL
# @st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Real-Time / Live Data Science Dashboard")
job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))

df = df[df["job"] == job_filter]


# create three columns
kpi1, kpi2, kpi3 = st.columns(3)

# fill in those three columns with respective metrics or KPIs
kpi1.metric(
    label="Age ⏳",
    value=round(avg_age),
    delta=round(avg_age) - 10,
)

kpi2.metric(
    label="Married Count 💍",
    value=int(count_married),
    delta=-10 + count_married,
)

kpi3.metric(
    label="A/C Balance ＄",
    value=f"$ {round(balance,2)} ",
    delta=-round(balance / count_married) * 100,
)
