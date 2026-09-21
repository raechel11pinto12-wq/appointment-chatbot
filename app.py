import pandas as pd
import plotly.express as px
import streamlit as st

# Set page layout to wide
st.set_page_config(page_title="Predictive Maintenance Dashboard", layout="wide")

st.title("🛠️ Industrial Predictive Maintenance Dashboard")

# 1. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("ai4i2020.csv")
    # Feature engineering for failures
    df["Temp_Diff"] = df["Process temperature [K]"] - df["Air temperature [K]"]
    df["Power_Factor"] = df["Rotational speed [rpm]"] * df["Torque [Nm]"]
    df["Overstrain_Factor"] = df["Torque [Nm]"] * df["Tool wear [min]"]
    return df


try:
    df = load_data()

    # 2. Sidebar Filters
    st.sidebar.header("Filter Telemetry")
    product_type = st.sidebar.multiselect(
        "Product Type",
        options=df["Type"].unique(),
        default=df["Type"].unique(),
    )
    failure_filter = st.sidebar.selectbox(
        "Filter by Failure State", ["All", "Only Failures", "Only Normal"]
    )

    # Filter logic
    filtered_df = df[df["Type"].isin(product_type)]
    if failure_filter == "Only Failures":
        filtered_df = filtered_df[filtered_df["Machine failure"] == 1]
    elif failure_filter == "Only Normal":
        filtered_df = filtered_df[filtered_df["Machine failure"] == 0]

    # 3. Top KPI Summary Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Monitored", f"{len(filtered_df):,}")
    col2.metric(
        "Total Failures", f"{filtered_df['Machine failure'].sum():,}"
    )
    col3.metric(
        "Failure Rate",
        f"{(filtered_df['Machine failure'].mean() * 100):.2f}%",
    )
    col4.metric(
        "Avg Tool Wear",
        f"{filtered_df['Tool wear [min]'].mean():.1f} min",
    )

    st.markdown("---")

    # 4. Main Telemetry Scatter Plot
    st.subheader("Speed vs. Torque Distribution (Color-Coded by Failure)")
    fig_scatter = px.scatter(
        filtered_df,
        x="Rotational speed [rpm]",
        y="Torque [Nm]",
        color="Machine failure",
        size="Tool wear [min]",
        color_continuous_scale=["#2b5c8f", "#e63946"],
        hover_data=["UDI", "Product ID", "Type"],
        title="Higher Torque / Extreme Speed Bounds Trigger Failures",
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # 5. Bottom Section: Temperatures & Breakdown Modes
    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("Temperature Difference Thresholds")
        fig_temp = px.line(
            filtered_df,
            x="UDI",
            y=["Air temperature [K]", "Process temperature [K]"],
            labels={"value": "Temperature (K)", "UDI": "Machine Run (UDI)"},
            title="Air vs. Process Temperature Tracking",
        )
        st.plotly_chart(fig_temp, use_container_width=True)

    with right_col:
        st.subheader("Specific Failure Breakdown")
        failure_counts = (
            filtered_df[["TWF", "HDF", "PWF", "OSF", "RNF"]]
            .sum()
            .reset_index()
        )
        failure_counts.columns = ["Failure Mode", "Count"]

        fig_bar = px.bar(
            failure_counts,
            x="Failure Mode",
            y="Count",
            color="Failure Mode",
            title="Frequency of Each Failure Trigger",
        )
        st.plotly_chart(fig_bar, use_container_width=True)

except Exception as e:
    st.error(
        f"Please place your dataset CSV file in this folder and make sure it is named 'ai4i2020.csv'. Error details: {e}"
    )