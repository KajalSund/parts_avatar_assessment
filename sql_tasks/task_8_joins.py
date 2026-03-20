import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = """
    select c.name, sum(oi.price * oi. quantity) as spend from Customers c join Orders o on c.customer_id
= o.customer_id join Order_Items oi on o.order_id = oi.order_id group by c.name """
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results