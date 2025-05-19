import streamlit as st
import pandas as pd
import altair as alt
import time
import os
from datetime import datetime

st.set_page_config(page_title="Intrusion Detection Dashboard", layout="wide")
st.title("🚨 Real-Time Intrusion Detection & Analysis")

def load_data():
    if os.path.exists("predictions.csv"):
        df = pd.read_csv("predictions.csv")
        df["timestamp"] = pd.to_datetime("now")
        df["hour"] = df["timestamp"].dt.hour
        df["minute"] = df["timestamp"].dt.strftime("%H:%M")
        df["prediction_label"] = df["prediction"].map({0: "Benign", 1: "Attack"})
        df["proto"] = df["proto"].map({0: "TCP", 1: "UDP", 2: "ICMP"}).fillna("Other")
        df["service"] = df["service"].map({0: "HTTP", 1: "FTP", 2: "SSH"}).fillna("Other")
        return df
    return pd.DataFrame()

# Sidebar filtering options
st.sidebar.title("🔍 Filters")
hour_range = st.sidebar.slider("Filter by Hour", 0, 23, (0, 23))
proto_filter = st.sidebar.multiselect("Protocol Filter", ["TCP", "UDP", "ICMP"], default=["TCP", "UDP", "ICMP"])

placeholder = st.empty()

while True:
    df = load_data()
    if df.empty:
        st.warning("Waiting for predictions.csv...")
        time.sleep(5)
        continue

    # Apply user filters
    filtered = df[df["proto"].isin(proto_filter)]
    filtered = filtered[filtered["hour"].between(hour_range[0], hour_range[1])]

    with placeholder.container():
        st.markdown("### 📊 Prediction Counts and Trends")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Prediction Totals")
            st.bar_chart(filtered["prediction_label"].value_counts())

        with col2:
            trend = filtered.groupby(["minute", "prediction_label"]).size().reset_index(name="count")
            chart = alt.Chart(trend).mark_line().encode(
                x="minute:T", y="count:Q", color="prediction_label:N"
            ).properties(height=300)
            st.altair_chart(chart, use_container_width=True)

        st.divider()

        st.markdown("### 📡 Attack Proportion by Protocol")
        proto_stats = (
            filtered.groupby(["proto", "prediction_label"])
            .size()
            .reset_index(name="count")
            .pivot(index="proto", columns="prediction_label", values="count")
            .fillna(0)
        )
        proto_stats["Total"] = proto_stats.sum(axis=1)
        proto_stats["Attack %"] = (proto_stats.get("Attack", 0) / proto_stats["Total"]) * 100
        st.bar_chart(proto_stats["Attack %"])

        st.divider()

        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Top Protocols (Attack Volume)")
            proto_attack = filtered[filtered["prediction_label"] == "Attack"]["proto"].value_counts()
            st.bar_chart(proto_attack)

        with col4:
            st.subheader("Top Services (Attack Volume)")
            service_attack = filtered[filtered["prediction_label"] == "Attack"]["service"].value_counts()
            st.bar_chart(service_attack)

        st.divider()

        st.subheader("📦 Feature Distributions (Boxplots)")
        boxplot_features = ["rate", "sbytes", "dbytes", "sload", "dload", "tcprtt"]
        for feat in boxplot_features:
            box = alt.Chart(filtered).mark_boxplot().encode(
                x=alt.X("prediction_label:N", title="Prediction"),
                y=alt.Y(feat, title=feat)
            ).properties(title=f"{feat} by Prediction", height=300)
            st.altair_chart(box, use_container_width=True)

        st.divider()
        st.subheader("🧠 Sample Prediction Snapshots")
        sample = filtered.tail(5)
        for i, row in sample.iterrows():
            st.markdown(f"**Sample #{i} → `{row['prediction_label']}`**")
            st.dataframe(row.to_frame().transpose(), use_container_width=True)

    time.sleep(5)
