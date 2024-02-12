import sqlite3
import pandas as pd

def export_db_tables_to_csv(database_path):
    # Nombres de las tablas a exportar
    table_names = ['fase_de_grupos', 'octavos', 'cuartos', 'semis', 'final']
    # DataFrame global para acumular los datos de todas las tablas
    df_global = pd.DataFrame()
    
    # Conectar a la base de datos
    conn = sqlite3.connect(database_path)
    
    # Iterar sobre cada nombre de tabla
    for table_name in table_names:
        # Leer los datos de la tabla actual
        df = pd.read_sql_query(f"SELECT *, '{table_name}' as fase FROM {table_name}", conn)
        # Concatenar el DataFrame de la tabla actual con el DataFrame global
        df_global = pd.concat([df_global, df], ignore_index=True)
    
    # Cerrar la conexión a la base de datos
    conn.close()
    
    # Exportar el DataFrame global a un único archivo CSV
    csv_file_name = "16-17.csv"
    df_global.to_csv(csv_file_name, index=False)
    print(f"Todas las tablas han sido exportadas a {csv_file_name}")

# Para ejecutar la función, asegúrate de que el nombre de la base de datos sea correcto
export_db_tables_to_csv('16-17/SQL/champions(16-17).db')
