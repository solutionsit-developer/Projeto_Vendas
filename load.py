import pandas as pd
import sqlite3

def create_database(db_name: str)-> None:

    conn = sqlite3.connect(db_name)
    conn.close()
    print("Database {db_name} created")

def create_table(db_name: str, table_name: str)-> None:

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name}(
            data TEXT,
            genero TEXT,
            idade INTEGER,
            categoria_produto TEXT,
            quantidade INTEGER,
            preco_unitario REAL,
            valor_total REAL,
            UNIQUE(data, genero, idade, 
            categoria_produto, quantidade, preco_unitario, valor_total))
                   

                   """)
    conn.commit()
    conn.close()  
    print(f"Table {table_name} created in {db_name}")  

    if __name__== "__main__":
     db_name = "databases/datawarehouse.db"
     table_name = "vendas"

     create_database(db_name)
     create_table(db_name, table_name)