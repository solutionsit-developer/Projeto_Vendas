import extract
import transform

if __name__ == "__main__":
    file_path = "data/vendas.csv"
    corrected_file_path = extract.corrects_thousand_separator(file_path)

    data = extract.extract_data(corrected_file_path)
    extract.data_exploration(data)

    db_name = "databases/stage.db"
    extract.create_database(db_name)

    table_name = "vendas"
    extract.create_table(db_name, table_name)

    extract.insert_data(data, db_name, table_name)


    
