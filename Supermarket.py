import streamlit as st
import pandas as pd
import plotly.express as px



# Function for the Sales page
def sales_page(df):
    # Display a title for the Sales page
    st.title("Sales")

    # Display a subheader for the Sales page
    st.subheader("_Supermarket - Consumer purchasing habits_")
    st.write("---")
    # Display visualizations using columns
    col1, col2 = st.columns(2)
    col3, col4, col5 = st.columns(3)

    # Visualization 1: Billing per Day
    fig_date = px.bar(df, x="Date", y="Total", color="City", title="Billing per Day")
    col1.plotly_chart(fig_date, use_container_width=True)

    # Visualization 2: Billing per Product
    fig_prod = px.bar(df, x="Date", y="Product line", color="City", title="Billing per Product", orientation="h")
    col2.plotly_chart(fig_prod, use_container_width=True)

    # Visualization 3: Billing by City
    city_total_sales = df.groupby("City")[["Total"]].sum().reset_index()
    fig_city = px.bar(city_total_sales, x="City", y="Total", title="Billing by City")
    col3.plotly_chart(fig_city, use_container_width=True)

    st.write("---")

    # Visualization 4: Billing by type of Payment
    fig_type = px.pie(df, values="Total", names="Payment", title="Billing by type of Payment")
    col4.plotly_chart(fig_type, use_container_width=True)

    # Visualization 5: Evaluation by City
    city_total_ratings = df.groupby("City")[["Rating"]].mean().reset_index()
    fig_rating = px.bar(city_total_ratings, x="Rating", y="City", title="Evaluation by City")
    col5.plotly_chart(fig_rating, use_container_width=True)

    # Display a subtitle above the table
    st.subheader("Table")

    # Display the DataFrame table at the bottom
    st.write(df)
    st.write("---")

    # Adding a footer for data source
    st.markdown("_Source: Supermarket dataset from Kaggle's repository_")

# Function for the Habits page
def habits_page(df):
    # Display a title for the Habits page
    st.title("Habits")


    # Filter dataframe for men and women separately
    df_male = df[df['Gender'] == 'Male']
    df_female = df[df['Gender'] == 'Female']

    # Visualization 1: Purchase behavior by city for Men and Women
    fig_city_gender = px.histogram(df, x='City', color='Gender', title='Purchase behavior by City for Men and Women')
    st.plotly_chart(fig_city_gender, use_container_width=True)

    # Visualization 2: Purchase behavior by product line for Men and Women
    fig_product_gender = px.histogram(df, x='Product line', color='Gender',
                                      title='Purchase behavior by Product for Men and Women')
    st.plotly_chart(fig_product_gender, use_container_width=True)
    st.write("---")
    st.markdown("_Source: Supermarket dataset from Kaggle's repository_")



# Main function to handle navigation between pages
def main():
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

    # Sidebar menu options
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Sales", "Habits"))
    st.write("---")

    # Sidebar menu for selecting month, city, and gender
    st.sidebar.title("Filters")
    selected_month = st.sidebar.selectbox("Month", unique_months)
    selected_city = st.sidebar.selectbox("City", ["All"] + df["City"].unique().tolist())
    selected_gender = st.sidebar.selectbox("Gender", ["All", "Male", "Female"])

    # Filter the DataFrame based on the selected options
    df_filtered = df.copy()
    if selected_month != 'All':
        df_filtered = df_filtered[df_filtered["Month"] == selected_month]
    if selected_city != 'All':
        df_filtered = df_filtered[df_filtered["City"] == selected_city]
    if selected_gender != 'All':
        df_filtered = df_filtered[df_filtered["Gender"] == selected_gender]

    # Display the selected page
    if page == "Sales":
        sales_page(df_filtered)
    elif page == "Habits":
        habits_page(df_filtered)


if __name__ == "__main__":
    main()
