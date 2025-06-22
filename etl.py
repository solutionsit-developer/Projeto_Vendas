import extract

if __name__ == "__main__":
    # Define o caminho do arquivo CSV
    file_path = "data/vendas.csv"

    # Extrai os dados do arquivo CSV
    data = extract.extract_data(file_path)

    # Realiza a exploração dos dados
    extract.data_exploration(data)

    # Cria o database SQLite
    db_name = "databases/stage.db"
    extract.create_database(db_name)

    # Cria a tabela
    table_name = "vendas"
    extract.create_table(db_name, table_name)

    # Insere os dados
    extract.insert_data(data, db_name, table_name)
