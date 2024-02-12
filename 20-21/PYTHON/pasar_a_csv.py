import sqlite3
import pandas as pd

def export_db_tables_to_csv(database_path):
    table_names = ['fase_de_grupos', 'octavos', 'cuartos', 'semis', 'final']
    
    conn = sqlite3.connect(database_path)
    
    for table_name in table_names:
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        csv_file_name = f"{table_name}.csv"
        df.to_csv(csv_file_name, index=False)
        print(f"Tabla {table_name} exportada a {csv_file_name}")
    
    conn.close()

# Para ejecutar la función, descomenta la siguiente línea y asegúrate de que el nombre de la base de datos sea correcto.
export_db_tables_to_csv('20-21/SQL/champions(20-21).db')
