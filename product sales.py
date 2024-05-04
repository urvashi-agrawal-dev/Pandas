import pandas as pd
data={
    'ID':[1,2,3,4],
    'Product':['Apple','Banana','Orange','Mango'],
    'Quantity':[100,150,120,80],
    'Price_per_Unit':[2.5,1.8,3.0,2.7]
}
df=pd.DataFrame(data)
df['revenue']=df['Quantity']*df['Price_per_Unit']
print("total revenue generated",df[['Product','revenue']])
highest_total_revenue=df.loc[df['revenue'].idxmax()]
print("Highest total revenue of product",highest_total_revenue)
average_price=df['Price_per_Unit'].mean()
print("Average priceper unit across all products",average_price)
total_quantity=df['Quantity'].sum()
print("Total quantity of all products",total_quantity)
products=df['Product'].nunique()
print("differnet types of product",products)