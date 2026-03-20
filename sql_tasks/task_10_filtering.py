import sqlite3

def get_pending_customers():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Select customer email and order_date where status is 'Pending'.
    query = """
    select c.email, o.order_date from Customers c join Orders o on c.customer_id = o.customer_id
    where o.status = 'Pending';
    """
    
    cursor.execute(query)
    return cursor.fetchall()