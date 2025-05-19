import pandas as pd
import matplotlib.pyplot as plt

data={
  'product':['A','B','C'],
  'sales':[100,200,100],
  'region':['north', 'north','north']
}

df=pd.DataFrame(data)
north_df=df[df['region']=='north']

sales_per_product= north_df.groupby('product')['sales'].sum().reset_index()

plt.figure(figsize=(8,5))
plt.bar(sales_per_product['product'], sales_per_product['sales'], color='skyblue')
plt.title('total sales of the product')
plt.xlabel('product')
plt.ylabel('total sales')
plt.grid(axis='y', linestyle='--', alpha=(0.7))
plt.tight_layout()
plt.show()
