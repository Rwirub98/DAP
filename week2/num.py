import numpy as np

data = np.array([
  [100,23,24,33],
  [200,24,55,77],
  [90,67,89,45]
])

total_sales_per_product= np.sum(data, axis=1)
highest_sales=np.max(data)

print("total data", data)
print("total sales per product",total_sales_per_product)
print("highest sales", highest_sales)
