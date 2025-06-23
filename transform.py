import sqlite3
import pandas as pd

def read_sqlite(db_name: str, table_name: str) -> pd.DataFrame:
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df
def analyze_data(df: pd.DataFrame) -> None:
    print("\n=== Data Analysis ===")

    print("\nValores únicos - Quantidade:")
    print(df["quantidade"].unique())

    print("\nValores únicos - Preço Unitário:")
    print(df["preco_unitario"].unique())

    print("\nValores únicos - Valor Total:")
    print(df["valor_total"].unique())

    print("\nVerificando possíveis duplicatas:")

    duplicates = df.groupby([
        "data",
        "genero",
        "idade",
        "categoria_produto",
        "quantidade",
        "preco_unitario",
        "valor_total"
    ]).size().reset_index(name='count')

    duplicates = duplicates[duplicates["count"] > 1]

    print(duplicates)


if __name__ == "__main__":
    db_name = "databases/stage.db"
    table_name = "vendas"

    df = read_sqlite(db_name, table_name)
   # print(df.head())
    
    analyze_data(df)
