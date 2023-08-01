import pandas as pd
import streamlit as st 
import plotly.express as px

st.set_page_config(page_title="Tickets Dashboard 📊 ", layout="wide" )

df = pd.read_csv('customer_support_tickets.csv')
print(df)


st.title("📊 Tickets Dashboard")
st.markdown("##")

st.sidebar.header("Please Filter Here:")
# ticket_ID = st.sidebar.multiselect(
#     "select the ticket id:",
#     options = df["Ticket ID"].unique(),
#     default = df["Ticket ID"].unique()
# )
customer_Gender = st.sidebar.multiselect(
    "select the Customer Gender:",
    options = df["Customer Gender"].unique(),
    default = df["Customer Gender"].unique()
)
ticket_Priority = st.sidebar.multiselect(
    "select the Ticket Priority:",
    options = df["Ticket Priority"].unique(),
    default = df["Ticket Priority"].unique()
)

df_selection = pd.read_csv("customer_support_tickets.csv")

st.dataframe(df_selection)

total_tickets = int(df_selection["Ticket ID"].sum())
Customer_Satisfaction_Rating = round(df_selection["Customer Satisfaction Rating"].mean(), 1)
star_rating = ":star" * int(round(Customer_Satisfaction_Rating, 0))

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Total Number of Tickets:")
    st.subheader(f"{total_tickets:}")
with right_column:
    st.subheader("Average Customer Rating:")
    st.subheader(f"{Customer_Satisfaction_Rating}{star_rating}")
    
st.markdown("---")

Ticket_Type_Count = df_selection["Ticket Type"].value_counts().reset_index()
Ticket_Type_Count.columns = ["Ticket Type", "Count"]

fig_product_sales = px.bar(
    Ticket_Type_Count, 
    x="Ticket Type",
    y="Count",
    orientation="v",
    title="<b>Ticket Type Occurrence</b>",
    template="plotly_white",
)

st.plotly_chart(fig_product_sales)