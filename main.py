import psycopg2
from psycopg2 import Error

conn = psycopg2.connect(
    database="n42",
    user="postgres",
    password="omad2006d",
    host="localhost",
    port="5432"
)


cur = conn.cursor()


def create_table():
    try:
        cur.execute("Create table if not exists product (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, price NUMERIC(10,2) NOT NULL);")
        conn.commit()
        print("Table created successfully")
    except Error as e:
        print(f"Error create table: {e}")


def insert_product(name, price):
    try:
        cur.execute("INSERT INTO product (name, price) VALUES (%s, %s)", (name, price))
        conn.commit()
        print("Product inserted successfully")
    except Error as e:
        print(f"Error insert product: {e}")


def select_all_product():
    try:
        cur.execute("SELECT * FROM product")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error selecting products: {e}")


def select_one_product(id):
    try:
       cur.execute("SELECT * FROM product WHERE id = %s", (id))
       row = cur.fetchone()
       if row:
           print(row)
       else:
           print("Product not found")
    except Error as e:
        print(f"Error insert product: {e}")


def update_product(id):
    try:
        cur.execute("UPDATE product SET name = %s, price = %s WHERE id = %s", (id))
        conn.commit()
        print("Product updated successfully")
    except Error as e:
        print(f"Error insert product: {e}")


def delete_product(id):
    try:
        cur.execute("DELETE FROM product WHERE id = %s", (id))
        conn.commit()
        print("Product deleted successfully")
    except Error as e:
        print(f"Error insert product: {e}")


create_table()


insert_product("Samsung S23", 750)
insert_product("Iphone 15", 1100)
select_all_product()
select_one_product(1)
update_product(1)
delete_product(2)
select_all_product()


cur.close()
conn.close()