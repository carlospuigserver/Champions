import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('/mnt/data/champions_league_2021_2022.db')
cursor = conn.cursor()

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
db_file_path = '/mnt/data/champions_league_2021_2022.db'
db_file_path
