# %% [markdown]
# ## Data Wrangling

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime


# %%
df = pd.read_excel("eu_storedata.xlsx")
df.head().set_index("Row ID")

# %%
df.shape

# %%
df.columns

# %% [markdown]
# #### Summary Of Data:
# This dataset, consisting of `10,000` rows and `20` columns, offers a comprehensive view of orders placed, their shipping details, customer information, geographical distribution, and specifics about the products sold and their financial implications. Analyzing this data could provide insights into customer behavior, popular products, geographical sales trends, and the store's overall performance in the European market.

# %% [markdown]
# #### Column descriptions:
# - `Row ID`: An identifier for each row in the dataset, likely used for referencing or indexing purposes.
# - `Order ID`: A unique identifier assigned to each order placed by customers.
# 
# - `Order Date`: The date when the order was placed by the customer.
# 
# - `Ship Date`: The date when the order was shipped to the customer.
# 
# - `Ship Mode`: Indicates the method or mode used for shipping the order (e.g., standard shipping, Second Class, First Class and Same Day shipping).
# 
# - `Customer ID`: A unique identifier for each customer.
# 
# - `Customer Name`: Name of the customer who placed the order.
# 
# - `Segment`: Classification or segmentation of customers (e.g., consumer, corporate) based on certain criteria or characteristics.
# 
# - `City`: The city where the customer placing the order is located.
# 
# - `State`: The state or region where the customer is situated.
# 
# - `Country`: The country where the customer is located.
# 
# - `Region`: A broader geographical area or region where the store operates or where customers are based.
# 
# - `Product ID`: A unique identifier for each product being sold.
# 
# - `Category`: The broad category to which the product belongs (e.g., electronics, furniture).
# 
# - `Sub-Category`: A more specific category that further classifies the product (e.g., phones, chairs).
# 
# - `Product Name`: The name or description of the specific product being sold.
# 
# - `Sales`: The monetary value or revenue generated from the sale of the product in that order.
# 
# - `Quantity`: The number of units of the product sold in that particular order.
# 
# - `Discount`: Any discount or reduction applied to the product's original price for that order.
# 
# - `Profit`: The amount of profit or loss incurred from the sale of the product in that order, considering costs and revenue.

# %%
df.head(2)

# %%
df.sample(10)

# %%
df.info()

# %%
df.isnull().sum()

# %%
df.duplicated().sum()

# %%
df.describe()

# %% [markdown]
# **Conclusion:**
# 
# In This Data:
# - No Duplicate Value
# - No Null Value
# - Date coloumn in correct format

# %% [markdown]
# ## **EDA:**

# %% [markdown]
# #### Coloumn Type:
# 
# **Numerical**
# 
#    -  Sales, Quantity, Discount, Profit
# 
# **Catagorical**
# 
# -  Ship Mode, Customer Name, Segment, City, State, Country, Region,Category, Sub-Category, Product Name
# 
# **Date Columns**
# 
# -  Order Date, Ship Date
# 
# **Mixed**
# -   Product ID, Customer ID, Order ID
# 

# %%
df.head()

# %% [markdown]
# ### Univariate Analysis

# %% [markdown]
# **Conclusion**
# - Sales is positively skewd
# - There are outlier
# - No missing Values

# %%
df["Sales"].describe()

# %%
df['Sales'].plot(kind='hist', bins = 20)

# %%
df['Sales'].plot(kind='kde')

# %%
df['Sales'].skew()

# %%
df['Sales'].plot(kind = "box")

# %%
df[df['Sales'] < 1050]['Sales'].plot(kind = "box")

# %% [markdown]
# **Conclusion**
# - Positively Skewed
# - There are some outliers

# %%
# Quantity
df['Quantity'].describe()

# %%
df[df['Quantity']==14]

# %%
df['Quantity'].plot(kind = 'kde')

# %%
df['Quantity'].plot(kind = 'box')

# %%
df['Quantity'].plot(kind = 'hist')

# %%
df['Quantity'].skew()

# %% [markdown]
# **Conclusion**
# -  Positively Skewd
# - There are some outliers
# - No Duplicate values
# - No missing values

# %%
# Discount
df["Discount"].describe ()

# %%
df["Discount"].plot(kind="box")

# %%
df["Discount"].plot(kind="kde")

# %%
df["Discount"].plot(kind="hist")

# %%
df["Discount"].skew()

# %% [markdown]
# **Conclusion**
# - There are some highly positive and negative outliers
# - Profit is normally(Almost) distributed

# %%
#Profit
df['Profit'].describe ()

# %%
df[df["Profit"] == -3059.82]

# %%
df["Profit"].plot(kind = "hist")

# %%
df["Profit"].plot(kind = "box")

# %%
df["Profit"].plot(kind = "kde")

# %%
df["Profit"].skew()

# %% [markdown]
# **Conclusion**
# - "Standard Class" appears to be the most commonly used shipping mode
# - "Standard Class" Mostly customer favor

# %%
df['Ship Mode'].value_counts()

# %%
df['Ship Mode'].value_counts().plot(kind='bar')

# %%
df['Ship Mode'].value_counts().plot(kind='pie', autopct = "%0.1f%%")

# %%
df['Segment'].value_counts()

# %% [markdown]
# **Conclusion**
# -  Consumer Dominance: The store's primary customer base is comprised of individual consumers, representing the largest segment.
# 
# - Corporate and Home Office: While smaller in number compared to consumers, both the corporate and home office segments are significant, indicating the presence of business or office-related custome

# %%
df['Segment'].value_counts().plot(kind = "pie", autopct = "%0.1f%%")

# %%
df['Segment'].value_counts().plot(kind = "bar")

# %%
# City
df['City'].value_counts().sort_values(ascending=False).head(10)

# %%
df['City'].value_counts().sort_values(ascending=False).head(10).plot(kind="bar" )

# %%
df['City'].value_counts().sort_values(ascending=False).head(5).plot(kind="pie", autopct = "%0.1f%%" )

# %%
df['Country'].value_counts()

# %%
df['Country'].value_counts().plot(kind="bar")

# %%
df['Country'].value_counts().plot(kind="pie", autopct = "%0.1f%%")

# %%
df["State"].value_counts()

# %%
df["State"].value_counts().head(10).plot(kind = "bar")

# %%
df["Category"].value_counts()

# %%
df["Category"].value_counts().plot(kind = "pie", autopct = "%0.1f%%")

# %%
df["Sub-Category"].value_counts()

# %%
df["Sub-Category"].value_counts().plot(kind = "bar")

# %%
df["Region"].value_counts()

# %%
df["Region"].value_counts().plot(kind = "bar")

# %% [markdown]
# ## Bivariate Analysis

# %%
sns.barplot(pd.crosstab(df["Sales"],df["Quantity"]))


# %%
pd.crosstab(df["Segment"],df["Ship Mode"])

# %%
pd.crosstab(df["Segment"],df["Region"])

# %%
# Which category how much sales
main_category = df.groupby("Category")['Sales'].sum().reset_index()
main_category["Sales"] =round(main_category["Sales"],2)
main_category

# %%
# Which sub category category how much sales
sub_category = df.groupby("Sub-Category")['Sales'].sum().reset_index()
sub_category

# %%
# Profit by category
profit_per_category = df.groupby("Category")['Profit'].sum().reset_index()
profit_per_category["Profit"] = round(profit_per_category["Profit"],2)
profit_per_category

# %% [markdown]
# -----
# -----

# %% [markdown]
# **`EU_Store Data Case Study:`**
# 

# %% [markdown]
# ## **Customer Segmentation:**
# -  `Customer segmentation is the process of dividing a customer base into distinct groups or segments that share similar characteristics, behaviors, or needs. By categorizing customers into different segments, businesses can better understand their diverse customer base and tailor their marketing strategies, products, and services to meet the specific needs of each group.`

# %%
df.head(5)

# %%
# total spent per customer
total_spent = df.groupby(["Customer Name","Customer ID"])['Sales'].sum().reset_index()

# %%
transaction_summary =df.groupby(["Customer Name","Customer ID"]).agg(
    n_transaction = ("Order ID",pd.Series.nunique), # Number of total transactions
    first_date = ("Order Date","min"),              # Date of first order
    last_date = ("Order Date","max"),               # Date of last order
).reset_index()

# %%
# Merging the data
df1 = pd.merge(total_spent, transaction_summary, on = ["Customer Name","Customer ID"], how = 'left')

# %%
# Rename the column name
df1 = df1.rename(columns={'Sales': 'total_spent'})

# %%
df1.info()

# %%
from datetime import datetime
reference_date = datetime.strptime("2019-01-31", "%Y-%m-%d")

# %%
# Day since last vist by customer
df1["day_since_last_visit"] = (reference_date - df1['last_date']).dt.days
df1.head(2)

# %%
# Sorting the data by date before calculating differences
temp_df = df.sort_values(['Customer ID', 'Customer Name', 'Order Date'])

# Calculating the last visit date per order per customer
temp_df = temp_df.groupby(["Customer ID", "Customer Name", "Order ID"])["Order Date"].max().reset_index()

# Calculating days between consecutive visits per customer
temp_df['last_visit_n'] = temp_df.groupby(["Customer ID", "Customer Name"])["Order Date"].diff().dt.days

# Taking absolute values of the differences
temp_df['last_visit_n'] = temp_df['last_visit_n'].abs()

# Calculating median days between transactions per customer
median_days = temp_df.groupby(["Customer ID", "Customer Name"])["last_visit_n"].median().reset_index()


# %%
# Rename the columns
median_days = median_days.rename(columns={'last_visit_n': 'median_days'})

# %%
# Merging Dataset

df2 = pd.merge(df1, median_days, on = ["Customer Name","Customer ID"], how = 'left')
df2.head(2)

# %%
# Quatity purchase per customer in each Category
df_cat_qun = df.groupby(["Customer ID", 'Customer Name', 'Category'])["Sales"].sum().reset_index()
df_cat_qun = df_cat_qun.rename(columns={"Sales":"sale_per_category"})
df_cat_qun.head(3)

# %%
# Quatity purchase per customer in each Sub-Category
df_scat_qun = df.groupby(["Customer ID", 'Customer Name', 'Sub-Category'])["Sales"].sum().reset_index()
df_scat_qun = df_scat_qun.rename(columns={"Sales":"sale_per_subcategory"})
df_scat_qun.head(6)

# %%
# Merging
temp_df1 = pd.merge(df_cat_qun,df_scat_qun,on = ["Customer ID","Customer Name"], how = 'left')
temp_df1

# %% [markdown]
# ## RFM
# - **RFM analysis is basically scoring our customers based on their Recency, Frequency and Monetary values.**
# -- `Recency:` How recently a customer made a purchase.
# -- `Frequency:` How often customers make a purchase.
# -- `Monetary Value:` How much money a customer spends on purchases.

# %% [markdown]
# `Recency` --> `day_since_last_visti`
# 
# `Frequency` --> `n_transaction`
# 
# `Monetary Value` --> `total_spent`

# %%
# Making Copy of Data
df_rfm = df2.copy()

# %%
# Making interval and doing labeling
df_rfm["recency"] = pd.qcut(df_rfm['day_since_last_visit'], q = 5, labels=[5,4,3,2,1])
df_rfm["frequency"] = pd.qcut(df_rfm['n_transaction'], q = 5 , labels=[1,2,3,4,5])
df_rfm["monetary"] = pd.qcut(df_rfm['total_spent'], q = 5 , labels=[1,2,3,4,5])
df_rfm.head(10)

# %%
df_rfm.info()

# %%
# Converting `recency`, `frequency` and `monetary` in integer from category
df_rfm['recency'] = df_rfm['recency'].astype(int)
df_rfm['frequency'] = df_rfm['frequency'].astype(int)
df_rfm['monetary'] = df_rfm['monetary'].astype(int)

# %%
# RFM Score
df_rfm['rfm_score'] = (df_rfm['recency'] * 100) + (df_rfm['frequency'] * 10) + df_rfm['monetary']

# %% [markdown]
# | Segments | Scores |
# | -------- | -------- |
# | Champions | 555, 554, 544, 545, 454, 455, 445 |
# | Loyal customers | 543, 444, 435, 355, 354, 345, 344, 335 |
# | Potential loyalist | 553, 551, 552, 541, 542, 533, 532, 531, 452, 451, 442, 441, 431, 453, 433, 432, 423, 353, 352, 351, 342, 341, 333, 323 |
# | Recent customers	 | 512, 511, 422, 421, 412, 411, 311 |
# | Promising | 525, 524, 523, 522, 521, 515, 514, 513, 425, 424, 413, 414, 415, 315, 314, 313 |
# | Customers needing attention | 535, 534, 443, 434, 343, 334, 325, 324 |
# | About to sleep	 | 331, 321, 312, 221, 213
#  |
# | At risk | 255, 254, 245, 244, 253, 252, 243, 242, 235, 234, 225, 224, 153, 152, 145, 143, 142, 135, 134, 133, 125, 124 |
# | Can’t lose them | 155, 154, 144, 214, 215, 115, 114, 113 |
# | Hibernating	 | 332, 322, 231, 241, 251, 233, 232, 223, 222, 132, 123, 122, 212, 211 |
# | Lost | 111, 112, 121, 131, 141, 151 |
# ------------------------------------------- | -----------------------------------------------------------------------------------------------------------------------------------------
# 
# 

# %%
# Define segments based on RFM score
conditions = [
    (df_rfm['rfm_score'].isin([555, 554, 544, 545, 454, 455, 445])),
    (df_rfm['rfm_score'].isin([543, 444, 435, 355, 354, 345, 344, 335])),
    (df_rfm['rfm_score'].isin([553, 551, 552, 541, 542, 533, 532, 531, 452, 451, 442, 441, 431, 453, 433, 432, 423, 353, 352, 351, 342, 341, 333, 323])),
    (df_rfm['rfm_score'].isin([512, 511, 422, 421, 412, 411, 311])),
    (df_rfm['rfm_score'].isin([525, 524, 523, 522, 521, 515, 514, 513, 425, 424, 413, 414, 415, 315, 314, 313])),
    (df_rfm['rfm_score'].isin([535, 534, 443, 434, 343, 334, 325, 324])),
    (df_rfm['rfm_score'].isin([331, 321, 312, 221, 213])),
    (df_rfm['rfm_score'].isin([255, 254, 245, 244, 253, 252, 243, 242, 235, 234, 225, 224, 153, 152, 145, 143, 142, 135, 134, 133, 125, 124])),
    (df_rfm['rfm_score'].isin([155, 154, 144, 214, 215, 115, 114, 113])),
    (df_rfm['rfm_score'].isin([332, 322, 231, 241, 251, 233, 232, 223, 222, 132, 123, 122, 212, 211])),
    (df_rfm['rfm_score'].isin([111, 112, 121, 131, 141, 151]))
]

# %% [markdown]
# ##Step by step RFM segmentation algorithm
# 
# 1. Calculate Recency (R), Frequency (F), and Monetary (M) values at the
# customer, source, brand, and country levels.
# 
# 2. Calculate approximate quantile cutoff values for R, F, and M using the approxQuantile() function. Quantiles divide the data into five equal parts.
# 
# 3. Calculate the RFM score based on quantile cutoff values. For example, customers who are frequent buyers, have recently bought from you, and usually are spending a lot of money would get a score of 555: Recency (R) = 5, Frequency (F) = 5, Monetary (M) = 5.
# 
# 4. Get RFM segment based on the RFM score (using RFM Matrix).

# %% [markdown]
# ## Understanding different segments  
# | Customer segment | Description         |
# | ---------------- | ---------------- |
# | Champions  | Recent purchase, frequent transactions, high spending  |
# | Loyal Customers  | Often spend good money buying your products. Responsive to promotions  |
# | Potential Loyalist  | Recent customers but spent a good amount and bought more than once  |
# | Recent Customers	  | Bought most recently, but not often  |
# | Promising	  | Recent shoppers but haven’t spent much  |
# | Customers Needing Attention  | Above-average recency, frequency and monetary values. They may not have bought very recently though  |
# | About to Sleep  | Below average recency, frequency, and monetary values. Will lose them if not reactivated|
# | At Risk  | They spent big money and purchased often. But the last purchase was a long time ago |
# | Can’t Lose Them  | Often made the biggest purchases but they haven’t returned for a long time  |
# | Hibernating | The last purchase was long ago. Low spenders with a low number of order |
# | Lost | Lowest recency, frequency, and monetary scores |
# 
# 

# %%
choices = [
    "Champions",
    "Loyal Customers",
    "Potential Loyalist",
    "Recent Customers",
    "Promising",
    "Customers Needing Attention",
    "About to Sleep",
    "At Risk",
    "Can’t Lose Them",
    "Hibernating",
    "Lost"
]


# %%
df_rfm['rfm_segment'] = np.select(conditions, choices, default="Other")


# %%
df_rfm.head()

# %%
# Merging
final_customer_data = pd.merge(temp_df1, df_rfm, on = ["Customer ID","Customer Name"], how = 'left')
final_customer_data.head(2)

# %%
# Downlaod data in csv files
final_customer_data.to_csv("final_customer_data.csv", index=False)

# %%
rfm = pd.read_csv("final_customer_data.csv")
rfm.head(2)

# %%
df.columns

# %%
df.groupby(['Customer ID','Customer Name'])['Segment'].unique()


# %%
r2=rfm.groupby("Customer Name")['rfm_segment'].unique().reset_index()

# %%
r2['rfm_segment'] = r2['rfm_segment'].apply(lambda x: ', '.join(map(str, x)))


# %%
r2 = r2[r2['rfm_segment'] == 'Champions'].head()

# %%
r2

# %%



