import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import warnings

# Optional: Hide the warning
warnings.filterwarnings("ignore", category=UserWarning)

#1. Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",  
    database="sales_db"
)

# 2. Write SQL query to get total quantity and revenue per product
query = """
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
"""

# 3. Load the result into a pandas DataFrame
df = pd.read_sql(query, conn)

# 4. Print the summary
print("Sales Summary:")
print(df)

# 5. Plot bar chart of revenue by product
df.plot(kind='bar', x='product', y='revenue', color='skyblue')
plt.title('Revenue by Product')
plt.ylabel('Revenue')
plt.xlabel('Product')
plt.tight_layout()
plt.savefig('sales_chart.png')  
plt.show()

# 6. Close the connection
conn.close()
