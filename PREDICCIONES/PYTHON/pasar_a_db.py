import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine

# Crear conexión a la base de datos SQLite
engine = create_engine('sqlite:///PREDICCIONES/SQL/Predicciones.db')

def leer_y_estructurar_csv(archivo, fase):
    # Leer el archivo CSV
    df = pd.read_csv(archivo)
    
    # Asegurarse de que todas las columnas necesarias estén presentes
    columnas_necesarias = ['id_partido', 'equipo_local', 'equipo_visitante', 'resultado_final']
    for columna in columnas_necesarias:
        if columna not in df.columns:
            df[columna] = None  # Añadir columna faltante con valores None
    
    if fase == 'fase_de_grupos':
        # Mantener solo las columnas necesarias para la fase de grupos
        df = df[['id_partido', 'equipo_local', 'equipo_visitante', 'resultado_final']]
    elif fase == 'final':
        # Mantener solo las columnas necesarias para la final
        df = df[['id_partido', 'equipo_local', 'equipo_visitante', 'resultado_ida']]
    else:
        # Añadir las columnas 'resultado_ida' y 'resultado_vuelta' si no están presentes
        if 'resultado_ida' not in df.columns:
            df['resultado_ida'] = None
        if 'resultado_vuelta' not in df.columns:
            df['resultado_vuelta'] = None
    
    # Establecer la fase para todos los registros en el DataFrame
    df['fase'] = fase

    return df  # Asegurarse de retornar el DataFrame

def guardar_en_db(df, nombre_tabla):
    # Usar 'replace' para sobreescribir tablas existentes o 'append' para añadir datos a tablas existentes
    df.to_sql(nombre_tabla, engine, if_exists='replace', index=False)

archivo_paths = [
    'PREDICCIONES/CSV/final.csv',
    'PREDICCIONES/CSV/semis.csv',
    'PREDICCIONES/CSV/cuartos.csv',
    'PREDICCIONES/CSV/octavos.csv',
    'PREDICCIONES/CSV/fase_de_grupos.csv',
]

fases = [
    'final', 'semifinales', 'cuartos',
    'octavos', 'fase_de_grupos'
]

for archivo, fase in zip(archivo_paths, fases):
    df = leer_y_estructurar_csv(archivo, fase)
    guardar_en_db(df, fase.replace(' ', '_'))  # Reemplazar espacios con guiones bajos para el nombre de la tabla

print("Todas las tablas han sido creadas y pobladas en PREDICCIONES/Predicciones.db.")
