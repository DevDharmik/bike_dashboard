import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Bike Rental Dashboard", layout="wide")

st.title("🚴‍♂️ Washington D.C. Bike Rental Dashboard")
st.write("Interactive dashboard summarizing key trends in the dataset.")

import pandas as pd
import os

file_path = os.path.join("data", "train.csv")

df = pd.read_csv("D:\bike_dashboard\data\train.csv")

# --- Sidebar Filters ---
st.sidebar.header("Filters")

year = st.sidebar.selectbox("Select Year", df['yr'].unique())
month = st.sidebar.slider("Select Month (1-12)", 1, 12)
weather = st.sidebar.multiselect(
    "Weather Condition",
    df['weathersit'].unique(),
    default=df['weathersit'].unique()
)

filtered_df = df[
    (df['yr'] == year) &
    (df['mnth'] == month) &
    (df['weathersit'].isin(weather))
]

st.write(f"### Showing data for Year {year}, Month {month}")

# --- Plot 1 ---
st.subheader("1. Hourly Bike Rental Trend")
fig1 = px.line(filtered_df, x="hr", y="cnt", title="Hourly Rentals")
st.plotly_chart(fig1, use_container_width=True)

# --- Plot 2 ---
st.subheader("2. Temperature Impact on Rentals")
fig2 = px.scatter(filtered_df, x="temp", y="cnt", color="hr",
                  title="Temperature vs Rental Count")
st.plotly_chart(fig2, use_container_width=True)

# --- Plot 3 ---
st.subheader("3. Rentals by Weather Condition")
fig3 = px.box(filtered_df, x="weathersit", y="cnt",
              title="Weather Condition vs Rentals")
st.plotly_chart(fig3, use_container_width=True)

# --- Plot 4 ---
st.subheader("4. Monthly Average Rentals")
monthly_avg = df.groupby("mnth")["cnt"].mean().reset_index()
fig4 = px.bar(monthly_avg, x="mnth", y="cnt", title="Average Rentals per Month")
st.plotly_chart(fig4, use_container_width=True)

# --- Plot 5 ---
st.subheader("5. Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(df[['temp','hum','windspeed','cnt']].corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

st.success("Dashboard Loaded Successfully 🎉")
