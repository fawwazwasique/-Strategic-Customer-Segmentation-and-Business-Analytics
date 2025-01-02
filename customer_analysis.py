import pandas as pd
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_icon="Icon.png",layout='wide', initial_sidebar_state="auto" ,  page_title='Customer Segmentation')
df = pd.read_csv('final_customer_data.csv')
customer_data1 = pd.read_excel('eu_storedata.xlsx')


def load_business_analysis():
    st.title("Business Analysis")
    # Total Sales
    Total_Sales = round(customer_data1['Sales'].sum(), 2)
    # Avg sale per order
    Avg_Sale_Per_Order = round(customer_data1['Sales'].mean(), 2)
    # Total profit from business
    Total_Profit = round(customer_data1['Profit'].sum(), 2)
    # Avg order time for shipping
    customer_data1['Order Date'] = pd.to_datetime(customer_data1['Order Date'])
    customer_data1['Ship Date'] = pd.to_datetime(customer_data1['Ship Date'])
    customer_data1["Ship Time"] = abs((customer_data1['Order Date'] - customer_data1['Ship Date']).dt.days)
    Avg_ship_time = round(customer_data1['Ship Time'].mean())
    st.header("Business Metrics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Sales", Total_Sales)
    with col2:
        st.metric("Avg Sale Per Order", Avg_Sale_Per_Order)
    with col3:
        st.metric("Total Profit", Total_Profit)
    with col4:
        st.metric("Avg Order Ship Time", Avg_ship_time)

    col6, col7 = st.columns(2)

    with col6:
        st.header("Profit In Each Segment")
        # Profit per segment
        profit_per_segment = customer_data1.groupby("Segment")['Profit'].sum().reset_index()
        fig4 = px.bar(profit_per_segment, x="Segment", y="Profit")
        st.plotly_chart(fig4, use_container_width=True)

    with col7:
        st.header("Customer Count In Each Segment")
        # Cutomer in each segment
        Customer_per_segment = customer_data1.groupby("Segment")['Customer ID'].nunique().reset_index()
        Customer_per_segment.rename(columns={'Customer ID': "Unique customer"}, inplace=True)
        fig5 = px.bar(Customer_per_segment, x="Segment", y="Unique customer")
        st.plotly_chart(fig5, use_container_width=True)


    col9, col10 = st.columns(2)
    with col9:
        # Sales By category
        cat = customer_data1.groupby("Category")['Sales'].sum().reset_index()
        fig9 = px.bar(cat, y='Sales', x='Category', text_auto='.2s',
                      title="Sales by Category")
        st.plotly_chart(fig9, use_container_width=True)
    with col10:
        # Sales By sub category
        sub = customer_data1.groupby("Sub-Category")['Sales'].sum().reset_index()
        fig8 = px.bar(sub, y='Sales', x='Sub-Category', text_auto='.2s',
                      title="Sales by Sub-Category")
        st.plotly_chart(fig8, use_container_width=True)
    st.header("Top 10 Customer By Spending")
    # Top 10 Customers according to sales
    cus_10 = customer_data1.groupby("Customer Name")['Sales'].sum().nlargest(10).sample(10).reset_index()
    fig6 = px.bar(cus_10, x= "Customer Name", y = "Sales", color="Sales")
    st.plotly_chart(fig6, use_container_width=True)
    st.header("Sales By Country")
    # Sales by country
    sales_by_country = customer_data1.groupby('Country')['Sales'].sum().reset_index()
    # Create a choropleth map
    fig7 = px.choropleth(sales_by_country,
                        locations='Country',
                        locationmode='country names',
                        color='Sales',
                        color_continuous_scale='Viridis',
                        title='Sales by Country'
                        )
    fig7.update_layout(height=1000, width=1000)
    st.plotly_chart(fig7, use_container_width=True)







def laod_customer_segmentation(customer):
    st.title("Customer Segmentation")
    customer_data = df[df["Customer Name"] == customer]
    total_spent = customer_data["total_spent"].max() if not customer_data.empty else 0
    n_transaction = customer_data["n_transaction"].max() if not customer_data.empty else 0
    first_date = customer_data["first_date"].max() if not customer_data.empty else 0
    last_date = customer_data["last_date"].max() if not customer_data.empty else 0
    if first_date != 0:
        first_date = datetime.strptime(str(first_date), "%Y-%m-%d").strftime("%d %B, %Y")
    if last_date != 0:
        last_date = datetime.strptime(str(last_date), "%Y-%m-%d").strftime("%d %B, %Y")

    day_since_last_visit = customer_data["day_since_last_visit"].max() if not customer_data.empty else 0
    median_days = customer_data["median_days"].max() if not customer_data.empty else 0
    rfm_score = customer_data["rfm_score"].max() if not customer_data.empty else 0
    rfm_segment = customer_data["rfm_segment"].max() if not customer_data.empty else 0

    st.subheader("Customer Metrics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Spent", total_spent)
    with col2:
        st.metric("Number Of Transaction", n_transaction)
    with col3:
        st.metric("First Date", first_date)
    with col4:
        st.metric("Last Date", last_date)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Last Visit At Store", day_since_last_visit, "Days")
    with col2:
        st.metric("Median Days Between Transaction", median_days, "Days")
    with col3:
        st.metric("RFM Score", rfm_score, "Score")
    with col4:
        st.metric("Customer Segment", rfm_segment, "Segment")

    col1, col2 = st.columns(2)

    with col1:
        fig2 = px.bar(customer_data, x='Category', y='sale_per_category')
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        fig3 = px.bar(customer_data, x='Sub-Category', y='sale_per_subcategory')
        st.plotly_chart(fig3, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        plt.figure(figsize=(8, 8))
        plt.pie(customer_data['sale_per_category'].unique(), labels=customer_data['Category'].unique(),
                autopct='%0.1f%%')
        plt.title('Sales Distribution per Category')
        pie_chart = plt.gcf()
        st.pyplot(pie_chart)
    with col2:
        plt.figure(figsize=(8, 8))
        plt.pie(customer_data['sale_per_subcategory'].unique(), labels=customer_data['Sub-Category'].unique(),
                autopct="%0.1f%%")
        plt.title("Sales Distribution per Sub-Category")
        pie_chart_sc = plt.gcf()
        st.pyplot(pie_chart_sc)

    # Sales Trend
    customer_data1['Order Date'] = pd.to_datetime(customer_data1['Order Date'])
    daily_sales = customer_data1.resample('D', on='Order Date')['Sales'].sum().reset_index()
    # Streamlit app code
    st.title('Sales Trend Analysis')
    # Line chart for daily sales trend
    st.subheader('Daily Sales Trend')
    st.line_chart(daily_sales.set_index('Order Date'))

    # Bar chart for monthly sales trend
    monthly_sales = customer_data1.resample('M', on='Order Date')['Sales'].sum().reset_index()
    st.subheader('Monthly Sales Trend')
    st.bar_chart(monthly_sales.set_index('Order Date'))

    st.title('Customers Counts in Every RFM Segment')
    data = df['rfm_segment'].value_counts().reset_index()
    data.columns = ['RFM Segment', 'Count']
    fig = px.bar(data, x="RFM Segment", y="Count")
    st.plotly_chart(fig, use_container_width=True)

    # Grouping and processing the data to show top 10 Champion Customers
    c = df.groupby("Customer Name")['rfm_segment'].unique().reset_index()
    c['rfm_segment'] = c['rfm_segment'].apply(lambda x: ', '.join(map(str, x)))
    c = c[c['rfm_segment'] == 'Champions'].head(10)

    # Grouping and processing the data to show top 10 Champion Customers
    a = df.groupby("Customer Name")['rfm_segment'].unique().reset_index()
    a['rfm_segment'] = a['rfm_segment'].apply(lambda x: ', '.join(map(str, x)))
    a = a[a['rfm_segment'] == 'At Risk'].head(10)

    # Grouping and processing the data to show top 10 Champion Customers
    s = df.groupby("Customer Name")['rfm_segment'].unique().reset_index()
    s['rfm_segment'] = s['rfm_segment'].apply(lambda x: ', '.join(map(str, x)))
    s = s[s['rfm_segment'] == 'Potential Loyalist'].head(10)
    st.title("Top 10 Customers that has high in top 3 Segment")
    c1, c2, c3 = st.columns(3)
    with c1:
        # Champion Customers
        st.subheader("Top 10 Champion Customers")
        st.dataframe(c.style.highlight_max(axis=1))
    with c2:
        # At Risk
        st.subheader("Top 10 At Risk Customers")
        st.dataframe(a.style.highlight_max(axis=1))
    with c3:
        # Potential Loyalist
        st.subheader("Top 10 Potential Loyalist Customers")
        st.dataframe(s.style.highlight_max(axis=1))


st.sidebar.title("Customer Segmentation")

# Define the "option" variable
option = st.sidebar.selectbox('Select One', ["Business Analysis", "Customer Segmentation"])

if option == "Business Analysis":
        load_business_analysis()

else:
    customer = st.sidebar.selectbox('Select Customer', (df["Customer Name"].unique()), index=None,
                                    placeholder="Select Customer", )
    laod_customer_segmentation(customer)
