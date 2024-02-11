import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('champions_league_2021_2022.db')
cursor = conn.cursor()


# Definiré primero la función para añadir la tabla de la fase de grupos
def create_group_stage_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fase_de_grupos (
            id_partido INTEGER PRIMARY KEY AUTOINCREMENT,
            equipo_local TEXT,
            equipo_visitante TEXT,
            resultado_final TEXT
        )
    ''')

# A continuación, definiré la función para insertar los partidos en la tabla de la fase de grupos
def insert_group_stage_matches(cursor, matches):
    cursor.executemany('''
        INSERT INTO fase_de_grupos (equipo_local, equipo_visitante, resultado_final)
        VALUES (?, ?, ?)
    ''', matches)

# Conectarse a la base de datos y crear la tabla de la fase de grupos
conn = sqlite3.connect('champions_league_2021_2022.db')
cursor = conn.cursor()
create_group_stage_table(cursor)

# Lista de partidos y resultados de la fase de grupos para insertar en la base de datos
group_stage_matches = [
    ('Barcelona', 'Bayern München', '0-3'),
    ('Dynamo Kyiv', 'Benfica', '0-0'),
    ('Chelsea', 'Zenit', '1-0'),
    ('Malmö', 'Juventus', '0-3'),
    ('Lille', 'Wolfsburg', '0-0'),
    ('Villarreal', 'Atalanta', '2-2'),
    ('Young Boys', 'Manchester United', '2-1'),
    ('Sevilla', 'Red Bull Salzburg', '1-1'),
    ('Sporting de Portugal', 'Ajax', '1-5'),
    ('Atlético de Madrid', 'Porto', '0-0'),
    ('Manchester City', 'RB Leipzig', '6-3'),
    ('Brugge', 'PSG', '1-1'),
    ('Sheriff Tiraspol', 'Shakhtar Donetsk', '2-0'),
    ('Beşiktaş', 'Borussia Dortmund', '1-2'),
    ('Liverpool', 'Milan', '3-2'),
    ('Inter', 'Real Madrid', '0-1')
]

# Insertar los partidos de la fase de grupos en la base de datos
insert_group_stage_matches(cursor, group_stage_matches)

# Guardar los cambios y cerrar la conexión a la base de datos


# Create tables for each stage of the Champions League
cursor.execute('''
    CREATE TABLE octavos (
        id_partido INTEGER PRIMARY KEY,
        equipo_local TEXT,
        equipo_visitante TEXT,
        resultado_ida TEXT,
        resultado_vuelta TEXT
    )
''')

cursor.execute('''
    CREATE TABLE cuartos (
        id_partido INTEGER PRIMARY KEY,
        equipo_local TEXT,
        equipo_visitante TEXT,
        resultado_ida TEXT,
        resultado_vuelta TEXT
    )
''')

cursor.execute('''
    CREATE TABLE semis (
        id_partido INTEGER PRIMARY KEY,
        equipo_local TEXT,
        equipo_visitante TEXT,
        resultado_ida TEXT,
        resultado_vuelta TEXT
    )
''')

cursor.execute('''
    CREATE TABLE final (
        id_partido INTEGER PRIMARY KEY,
        equipo_local TEXT,
        equipo_visitante TEXT,
        resultado_final TEXT
    )
''')

# Insert data into 'octavos' table
octavos_matches = [
    (1, 'Benfica', 'Ajax', '2-2', '1-0'),
    (2, 'Inter', 'Liverpool', '0-2', '1-0'),
    (3, 'Villarreal', 'Juventus', '1-1', '3-0'),
    (4, 'Red Bull Salzburg', 'Bayern München', '1-1', '1-7'),
    (5, 'Sporting CP', 'Manchester City', '0-5', '0-0'),
    (6, 'Atlético Madrid', 'Manchester United', '1-1', '0-1'),
    (7, 'Chelsea', 'Lille', '2-0', '2-1'),
    (8, 'PSG', 'Real Madrid', '1-0', '1-3')
]
cursor.executemany('INSERT INTO octavos VALUES (?,?,?,?,?)', octavos_matches)

# Insert data into 'cuartos' table
cuartos_matches = [
    (1, 'Benfica', 'Liverpool', '1-3', '3-3'),
    (2, 'Villarreal', 'Bayern München', '1-0', '1-1'),
    (3, 'Manchester City', 'Atlético Madrid', '1-0', '0-0'),
    (4, 'Chelsea', 'Real Madrid', '1-3', '2-3')
]
cursor.executemany('INSERT INTO cuartos VALUES (?,?,?,?,?)', cuartos_matches)

# Insert data into 'semis' table
semis_matches = [
    (1, 'Villarreal', 'Liverpool', '2-3', '0-2'),
    (2, 'Manchester City', 'Real Madrid', '4-3', '1-3')
]
cursor.executemany('INSERT INTO semis VALUES (?,?,?,?,?)', semis_matches)

# Insert data into 'final' table
final_match = [
    (1, 'Liverpool', 'Real Madrid', '0-1')
]
cursor.executemany('INSERT INTO final VALUES (?,?,?,?)', final_match)



# Provide the path to the database file
db_file_path = 'champions_league_2021_2022.db'
db_file_path
