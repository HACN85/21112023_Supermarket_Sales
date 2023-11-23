import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page configuration to wide layout
st.set_page_config(layout="wide")

# Read the CSV file into a DataFrame
df = pd.read_csv("supermarket_sales - Sheet1.csv")

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date']).dt.date
df = df.sort_values("Date")

# Extract the year and create a new column 'Year'
df['Year'] = pd.to_datetime(df['Date']).dt.year

# Extract the month and create a new column 'Month' in 'YYYY-MM' format
df['Month'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m')

# Prepend 'All' option to the unique months
unique_months = ['All'] + df['Month'].unique().tolist()

# Create a sidebar selectbox to choose a month with 'All' option
selected_month = st.sidebar.selectbox("Month", unique_months)

# Add new sidebar options for City, Gender, and Product Line
selected_city = st.sidebar.multiselect("City", df['City'].unique())
selected_gender = st.sidebar.multiselect("Gender", df['Gender'].unique())
selected_product_line = st.sidebar.multiselect("Product Line", df['Product line'].unique())

# Filter the DataFrame based on the selected options
df_filtered = df
if selected_month != 'All':
    df_filtered = df_filtered[df_filtered["Month"] == selected_month]
if selected_city:
    df_filtered = df_filtered[df_filtered["City"].isin(selected_city)]
if selected_gender:
    df_filtered = df_filtered[df_filtered["Gender"].isin(selected_gender)]
if selected_product_line:
    df_filtered = df_filtered[df_filtered["Product line"].isin(selected_product_line)]

# Display a title above the charts
st.title("Supermarket Sales Data")

# Create tabs for "Sales" and "Habits"
tabs = ["Sales", "Habits"]
selected_tab = st.radio("Go to", tabs)

if selected_tab == "Sales":
    # Display visualizations using columns
    col1, col2 = st.columns(2)
    col3, col4, col5 = st.columns(3)

    # Visualization 1: Billing per Day
    fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Billing per Day")
    col1.plotly_chart(fig_date, use_container_width=True)

    # Visualization 2: Billing per Product
    fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Billing per Product", orientation="h")
    col2.plotly_chart(fig_prod, use_container_width=True)

    # Visualization 3: Billing by City
    city_total_sales = df_filtered.groupby("City")[["Total"]].sum().reset_index()
    fig_city = px.bar(city_total_sales, x="City", y="Total", title="Billing by City")
    col3.plotly_chart(fig_city, use_container_width=True)

    # Visualization 4: Billing by type of Payment
    fig_type = px.pie(df_filtered, values="Total", names="Payment", title="Billing by type of Payment")
    col4.plotly_chart(fig_type, use_container_width=True)

    # Visualization 5: Evaluation by City
    city_total_ratings = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
    fig_rating = px.bar(city_total_ratings, x="Rating", y="City", title="Evaluation by City")
    col5.plotly_chart(fig_rating, use_container_width=True)

    st.write("---")

    # Display a title above the table
    st.title("Table")

    # Display the DataFrame table at the bottom
    st.write(df_filtered)

elif selected_tab == "Habits":
    # Visualization for Habits Analysis
    st.write("## Habits Analysis")
    # Add your code for habits analysis here, such as the gender consumption comparison chart
    # Example:
    habits_data = df_filtered.groupby('Gender')['Total'].sum().reset_index()
    habits_chart = px.bar(habits_data, x='Gender', y='Total', title='Consumption Comparison by Gender')
    st.plotly_chart(habits_chart)

    st.write("---")
    st.title("Table for Habits Analysis")
    st.write(df_filtered)  # Display the filtered data in a table for habits analysis
