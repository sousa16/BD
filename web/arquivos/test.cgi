#!/usr/bin/python3
from wsgiref.handlers import CGIHandler

from flask import Flask
from flask import render_template, request

## PostgreSQL database adapter
import psycopg2
import psycopg2.extras

## SGBD configs
DB_HOST="db.tecnico.ulisboa.pt"
DB_USER="db"
DB_DATABASE=DB_USER
DB_PASSWORD="db"
DB_CONNECTION_STRING = "host=%s dbname=%s user=%s password=%s" %(DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD)

app = Flask(__name__)

# List All

@app.route('/customers')
def list_clients():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        query = "SELECT * FROM customer;"
        cursor.execute(query)
        return render_template("customers.html", cursor = cursor)
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        dbConn.close()

@app.route('/products')
def list_products():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        query = "SELECT * FROM product;"
        cursor.execute(query)
        return render_template("products.html", cursor = cursor)
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        dbConn.close()

@app.route('/products')
def list_suppliers():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        query = "SELECT * FROM supplier;"
        cursor.execute(query)
        return render_template("products.html", cursor = cursor)
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        dbConn.close()
        
# Clientes

@app.route('/registar_cliente', methods=["POST"])
def registar_cliente():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        name = request.form["name"]
        email = request.form["email"]
        query = "INSERT INTO customer (name, email) VALUES (%s, %s)"
        data = (name, email)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()
        
@app.route('/remove_customer')
def remove_customer():
    try:
        return render_template("remove_customer.html", params=request.args)
    except Exception as e:
        return str(e)

@app.route('/update_customer', methods=["POST"])
def update_customer():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        email = request.form["email"]
        query = (
        "BEGIN; "
            "DELETE FROM customer WHERE email = %s; "
        "COMMIT;")
        data = (email)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()

# Produtos

@app.route('/registar_produto', methods=["POST"])
def registar_produto():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        name = request.form["name"]
        sku = request.form["sku"]
        price = request.form["price"]
        query = "INSERT INTO product (name, sku, price) VALUES (%s, %s, %s)"
        data = (name, sku, price)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()
        
@app.route('/remove_product')
def remove_product():
    try:
        return render_template("remove_product.html", params=request.args)
    except Exception as e:
        return str(e)

@app.route('/update_product', methods=["POST"])
def update_product():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        sku = request.form["sku"]
        query = (
        "BEGIN; "
            "DELETE FROM product WHERE sku = %s; "
        "COMMIT;")
        data = (sku)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()

# Fornecedores

@app.route('/registar_fornecedor', methods=["POST"])
def registar_fornecedor():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        tin = request.form["tin"]
        sku = request.form["sku"]
        query = "INSERT INTO supplier (tin, sku) VALUES (%s, %s)"
        data = (tin, sku)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()
        
@app.route('/remove_supplier')
def remove_supplier():
    try:
        return render_template("remove_supplier.html", params=request.args)
    except Exception as e:
        return str(e)

@app.route('/update_supplier', methods=["POST"])
def update_supplier():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        tin = request.form["tin"]
        query = (
        "BEGIN; "
            "DELETE FROM supplier WHERE tin = %s; "
        "COMMIT;")
        data = (tin)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()

# Entregas

@app.route('/realizar_encomenda', methods=["POST"])
def realizar_encomenda():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cust_no = request.form["cust_no"]
        sku = request.form["sku"]
        amount = request.form["amount"]
        query = "INSERT INTO orders (cust_no, sku, amount) VALUES (%s, %s, %s)"
        data = (cust_no, sku, amount)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()
        
@app.route('/pagar_encomenda', methods=["POST"])
def pagar_encomenda():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cust_no = request.form["cust_no"]
        order_no = request.form["order_no"]
        query = """
        INSERT INTO pay (cust_no, order_no) VALUES (%s, %s);
        DELETE FROM orders (order_no) VALUES (%s);
        """
        data = (cust_no, order_no)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()

CGIHandler().run(app)

