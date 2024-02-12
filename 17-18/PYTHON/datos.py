import sqlite3

# Conectarse a la base de datos nueva con el nombre especificado
conn = sqlite3.connect('17-18/SQL/champions(17-18).db')
cursor = conn.cursor()

# Crear la tabla de la fase de grupos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS fase_de_grupos (
        id_partido INTEGER PRIMARY KEY AUTOINCREMENT,
        equipo_local TEXT,
        equipo_visitante TEXT,
        resultado_final TEXT
    )
''')

# Crear las tablas de octavos, cuartos, semis y final
cursor.execute('''
    CREATE TABLE IF NOT EXISTS octavos (
        id_partido INTEGER PRIMARY KEY,
        equipo_local TEXT,
        equipo_visitante TEXT,
        resultado_ida TEXT,
        resultado_vuelta TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cuartos (
        id_partido INTEGER PRIMARY KEY,
        equipo_local TEXT,
        equipo_visitante TEXT,
        resultado_ida TEXT,
        resultado_vuelta TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS semis (
        id_partido INTEGER PRIMARY KEY,
        equipo_local TEXT,
        equipo_visitante TEXT,
        resultado_ida TEXT,
        resultado_vuelta TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS final (
        id_partido INTEGER PRIMARY KEY,
        equipo_local TEXT,
        equipo_visitante TEXT,
        resultado_final TEXT
    )
''')


# Lista de partidos y resultados de la fase de grupos para insertar en la base de datos
group_stage_matches = [
    ("Benfica", "CSKA Moskva", "1-2"),
    ("Manchester United", "Basel", "3-0"),
    ("Bayern München", "Anderlecht", "3-0"),
    ("Celtic", "Paris Saint-Germain", "0-5"),
    ("Chelsea", "Qarabağ", "6-0"),
    ("Roma", "Atlético Madrid", "0-0"),
    ("Barcelona", "Juventus", "3-0"),
    ("Olympiacos", "Sporting CP", "2-3"),
    ("Liverpool", "Sevilla", "2-2"),
    ("Maribor", "Spartak Moskva", "1-1"),
    ("RB Leipzig", "Monaco", "1-1"),
    ("Porto", "Beşiktaş", "1-3"),
    ("Real Madrid", "APOEL", "3-0"),
    ("Tottenham", "Borussia Dortmund", "3-1"),
    ("Shakhtar Donetsk", "Napoli", "2-1"),
    ("Feyenoord", "Manchester City", "0-4"),
    ("Qarabağ", "Roma", "1-2"),
    ("Basel", "Benfica", "5-0"),
    ("CSKA Moskva", "Manchester United", "1-4"),
    ("Anderlecht", "Celtic", "0-3"),
    ("Paris Saint-Germain", "Bayern München", "3-0"),
    ("Sporting CP", "Barcelona", "0-1"),
    ("Atlético Madrid", "Chelsea", "1-2"),
    ("Juventus", "Olympiacos", "2-0"),
    ("Sevilla", "Maribor", "3-0"),
    ("Spartak Moskva", "Liverpool", "1-1"),
    ("Manchester City", "Shakhtar Donetsk", "2-0"),
    ("Napoli", "Feyenoord", "3-1"),
    ("Monaco", "Porto", "0-3"),
    ("Beşiktaş", "RB Leipzig", "2-0"),
    ("Borussia Dortmund", "Real Madrid", "1-3"),
    ("APOEL", "Tottenham", "0-3"),
    ("Qarabağ", "Atlético Madrid", "0-0"),
    ("Chelsea", "Roma", "3-3"),
    ("Barcelona", "Olympiacos", "3-1"),
    ("Juventus", "Sporting CP", "2-1"),
    ("Benfica", "Manchester United", "0-1"),
    ("CSKA Moskva", "Basel", "0-2"),
    ("Bayern München", "Celtic", "3-0"),
    ("Anderlecht", "Paris Saint-Germain", "0-4"),
    ("Feyenoord", "Shakhtar Donetsk", "1-2"),
    ("Manchester City", "Napoli", "2-1"),
    ("RB Leipzig", "Porto", "3-2"),
    ("Monaco", "Beşiktaş", "1-2"),
    ("Real Madrid", "Tottenham", "1-1"),
    ("APOEL", "Borussia Dortmund", "1-1"),
    ("Maribor", "Liverpool", "0-7"),
    ("Spartak Moskva", "Sevilla", "5-1"),
    ("Atlético Madrid", "Qarabağ", "1-1"),
    ("Roma", "Chelsea", "3-0"),
    ("Olympiacos", "Barcelona", "0-0"),
    ("Sporting CP", "Juventus", "1-1"),
    ("Manchester United", "Benfica", "2-0"),
    ("Basel", "CSKA Moskva", "1-2"),
    ("Celtic", "Bayern München", "1-2"),
    ("Paris Saint-Germain", "Anderlecht", "5-0"),
    ("Shakhtar Donetsk", "Feyenoord", "3-1"),
    ("Napoli", "Manchester City", "2-4"),
    ("Porto", "RB Leipzig", "3-1"),
    ("Beşiktaş", "Monaco", "1-1"),
    ("Tottenham", "Real Madrid", "3-1"),
    ("Borussia Dortmund", "APOEL", "1-1"),
    ("Liverpool", "Maribor", "3-0"),
    ("Sevilla", "Spartak Moskva", "2-1"),
    ("Qarabağ", "Chelsea", "0-4"),
    ("CSKA Moskva", "Benfica", "2-0"),
    ("Basel", "Manchester United", "1-0"),
    ("Anderlecht", "Bayern München", "1-2"),
    ("Paris Saint-Germain", "Celtic", "7-1"),
    ("Atlético Madrid", "Roma", "2-0"),
    ("Juventus", "Barcelona", "0-0"),
    ("Sporting CP", "Olympiacos", "3-1"),
    ("Spartak Moskva", "Maribor", "1-1"),
    ("Sevilla", "Liverpool", "3-3"),
    ("Manchester City", "Feyenoord", "1-0"),
    ("Napoli", "Shakhtar Donetsk", "3-0"),
    ("Monaco", "RB Leipzig", "1-4"),
    ("Dortmund", "Tottenham", "1-2"),
    ("APOEL", "Real Madrid", "0-6"),
    ("Beşiktaş", "Porto", "1-1"),("Chelsea", "Atlético Madrid", "1-1"),
    ("Roma", "Qarabağ", "1-0"),
    ("Barcelona", "Sporting CP", "2-0"),
    ("Olympiacos", "Juventus", "0-2"),
    ("Manchester United", "CSKA Moskva", "2-1"),
    ("Benfica", "Basel", "0-2"),
    ("Bayern München", "Paris Saint-Germain", "3-1"),
    ("Celtic", "Anderlecht", "0-1"),
    ("Liverpool", "Spartak Moskva", "7-0"),
    ("Maribor", "Sevilla", "1-1"),
    ("Feyenoord", "Napoli", "2-1"),
    ("Shakhtar Donetsk", "Manchester City", "2-1"),
    ("RB Leipzig", "Beşiktaş", "1-2"),
    ("Porto", "Monaco", "5-2"),
    ("Tottenham", "APOEL", "3-0"),
    ("Real Madrid", "Borussia Dortmund", "3-2")

]


# Insertar datos en la tabla de la fase de grupos
def insert_group_stage_matches(cursor, matches):
    cursor.executemany('''
        INSERT INTO fase_de_grupos (equipo_local, equipo_visitante, resultado_final)
        VALUES (?, ?, ?)
    ''', matches)

# Insert data into 'octavos' table
octavos_matches = [
    (1, "Juventus", "Tottenham", "2-2", "2-1"),
    (2, "Basel", "Manchester City", "0-4", "2-1"),
    (3, "Porto", "Liverpool", "0-5", "0-0"),
    (4, "Real Madrid", "Paris Saint-Germain", "3-1", "2-1"),
    (5, "Chelsea", "Barcelona", "1-1", "0-3"),
    (6, "Bayern Munich", "Besiktas", "5-0", "3-1"),
    (7, "Sevilla", "Manchester United", "0-0", "2-1"),
    (8, "Shakhtar Donetsk", "Roma", "2-1", "0-1")
]



# Insert data into 'cuartos' table
cuartos_matches = [
    (1, "Barcelona", "Roma", "4-1", "0-3"),
    (2, "Sevilla", "Bayern Munich", "1-2", "0-0"),
    (3, "Juventus", "Real Madrid", "0-3", "3-1"),
    (4, "Liverpool", "Manchester City", "3-0", "2-1")
]



# Insert data into 'semis' table
semis_matches = [
    (1, "Liverpool", "Roma", "5-2", "2-4"),
    (2, "Bayern Munich", "Real Madrid", "1-2", "2-2")
]




# Insert data into 'final' table
final_match = [
    (1, "Real Madrid", "Liverpool", "3-1")
]


# Insertar los datos en las tablas correspondientes
insert_group_stage_matches(cursor, group_stage_matches)
cursor.executemany('INSERT INTO octavos VALUES (?,?,?,?,?)', octavos_matches)
cursor.executemany('INSERT INTO cuartos VALUES (?,?,?,?,?)', cuartos_matches)
cursor.executemany('INSERT INTO semis VALUES (?,?,?,?,?)', semis_matches)
cursor.executemany('INSERT INTO final VALUES (?,?,?,?)', final_match)

conn.commit()
conn.close()

# Ruta al archivo de la base de datos
db_file_path = '17-18/SQL/champions(17-18).db'
print(db_file_path)
