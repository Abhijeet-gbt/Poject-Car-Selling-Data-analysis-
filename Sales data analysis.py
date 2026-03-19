#using import function importing libaries required for this project 
import matplotlib.pyplot as plt          
import pandas as pd     

df = pd.read_csv("car_details_raw_data.csv")
print(df)

#Understanding Data to perform operations on Data
print(df.head(10))
print(df.info())
print(df.describe())
print(df.columns)

#Sorting values by there selling price
max_value = df["selling_price"].sort_values(ascending=False)
print(max_value)

#Checking the data contains the null or duplicate value 
print(df.isnull())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.drop_duplicates())       #droping duplicates values 

print(df.head(10))

#The cars are selled in year 2007
print(df.loc[df["year"].isin([2007])].reset_index())

#Every seller type average of selling price 
print(df.groupby("seller_type")["selling_price"].mean())

#Cars that are selled in 2005 and selling price is between 150000 to 200000
da = df.loc[
    df["year"].isin([2005])
    & df["selling_price"].between(150000,200000)]
print(da)

#Most selled car types Manual or Automatic
result = df["transmission"].value_counts()
print(result)

#Contribution of seller types for selling Cars 
seller = df["seller_type"].value_counts()
print(seller)

#Top Cars Brand and their average selling price 
df["brand"] = df["name"].str.split().str[0]
brand_avg = df.groupby("brand")["selling_price"].mean().sort_values(ascending=False).head(5)

#Counting Cars with their fuel type and which type of car selled most 
counts = df["fuel"].value_counts()
print(counts)


fig, ax = plt.subplots(2,2, figsize=(10,8))

# 1 Transmission bar chart
ax[0,0].bar(result.index, result.values)
ax[0,0].set_title("Manual Cars vs Automatic Cars")
ax[0,0].set_xlabel("Car Type")
ax[0,0].set_ylabel("Count")
ax[0,0].grid(axis="y")

# 2 Seller type pie chart
ax[0,1].pie(
    seller.values,
    labels=seller.index,
    autopct="%1.1f%%",
    colors=["skyblue","red","green"],
    startangle=90
)
ax[0,1].set_title("Seller Contribution")

# 3 Brand average selling price
ax[1,0].bar(
    brand_avg.index,
    brand_avg.values,
    color=["skyblue","red","green","orange","yellow"]
)
ax[1,0].set_title("Top 5 Brands Average Selling Price")
ax[1,0].set_xlabel("Car Brand")
ax[1,0].set_ylabel("Average Price")
ax[1,0].grid(axis="y")

# 4 Cars With fuel Type Comparison 
ax[1,1].bar(counts.index,counts.values,
            color = ["red","green","skyblue","orange","black"])
ax[1,1].set_title("Domination of Cars by Fuel type")
ax[1,1].set_xlabel("Fuel Types")
ax[1,1].set_ylabel("Domination of Cars")
ax[1,1].grid(axis = "y")

plt.tight_layout()
plt.savefig("Car_Sell_DataAnalysis.png", dpi=600, bbox_inches="tight")
plt.show()