import sqlite3

# Conectarse a la base de datos nueva con el nombre especificado
conn = sqlite3.connect('23-24/SQL/champions(23-24).db')
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
    ("AC Milan", "Newcastle", "0-0"),
    ("Young Boys", "RB Leipzig", "1-3"),
    ("Feyenoord", "Celtic", "2-0"),
    ("Lazio", "Atletico Madrid", "1-1"),
    ("Paris Saint-Germain", "Borussia Dortmund", "2-0"),
    ("Manchester City", "Crvena zvezda", "3-1"),
    ("Barcelona", "Royal Antwerp", "5-0"),
    ("Shakhtar Donetsk", "Porto", "1-3"),
    ("Galatasaray", "Copenhagen", "2-2"),
    ("Real Madrid", "Union Berlin", "1-0"),
    ("Bayern Munich", "Manchester United", "4-3"),
    ("Arsenal", "PSV Eindhoven", "4-0"),
    ("Sevilla", "Lens", "1-1"),
    ("Braga", "Napoli", "1-2"),
    ("Real Sociedad", "Inter", "1-1"),
    ("Benfica", "Salzburg", "0-2"),
    ("Union Berlin", "Braga", "2-3"),
    ("Salzburg", "Real Sociedad", "0-2"),
    ("Manchester United", "Galatasaray", "2-3"),
    ("Copenhagen", "Bayern Munich", "1-2"),
    ("Lens", "Arsenal", "2-1"),
    ("PSV Eindhoven", "Sevilla", "2-2"),
    ("Napoli", "Real Madrid", "2-3"),
    ("Inter", "Benfica", "1-0"),
    ("Atletico Madrid", "Feyenoord", "3-2"),
    ("Royal Antwerp", "Shakhtar Donetsk", "2-3"),
    ("Celtic", "Lazio", "1-2"),
    ("Borussia Dortmund", "AC Milan", "0-0"),
    ("Newcastle", "Paris Saint-Germain", "4-1"),
    ("RB Leipzig", "Manchester City", "1-3"),
    ("Crvena zvezda", "Young Boys", "2-2"),
    ("Porto", "Barcelona", "0-1"),
    ("Galatasaray", "Bayern Munich", "1-3"),
    ("Inter", "Salzburg", "2-1"),
    ("Manchester United", "Copenhagen", "1-0"),
    ("Sevilla", "Arsenal", "1-2"),
    ("Lens", "PSV Eindhoven", "1-1"),
    ("Braga", "Real Madrid", "1-2"),
    ("Union Berlin", "Napoli", "0-1"),
    ("Benfica", "Real Sociedad", "0-1"),
    ("Feyenoord", "Lazio", "3-1"),
    ("Barcelona", "Shakhtar Donetsk", "2-1"),
    ("Celtic", "Atletico Madrid", "2-2"),
    ("Paris Saint-Germain", "AC Milan", "3-0"),
    ("Newcastle", "Borussia Dortmund", "0-1"),
    ("RB Leipzig", "Crvena zvezda", "3-1"),
    ("Young Boys", "Manchester City", "1-3"),
    ("Royal Antwerp", "Porto", "1-4"),
        ("Borussia Dortmund", "Newcastle", "2-0"),
    ("Shakhtar Donetsk", "Barcelona", "1-0"),
    ("Atletico Madrid", "Celtic", "6-0"),
    ("Lazio", "Feyenoord", "1-0"),
    ("AC Milan", "Paris Saint-Germain", "2-1"),
    ("Manchester City", "Young Boys", "3-0"),
    ("Crvena zvezda", "RB Leipzig", "1-2"),
    ("Porto", "Royal Antwerp", "2-0"),
    ("Napoli", "Union Berlin", "1-1"),
    ("Real Sociedad", "Benfica", "3-1"),
    ("Bayern Munich", "Galatasaray", "2-1"),
    ("Copenhagen", "Manchester United", "4-3"),
    ("Arsenal", "Sevilla", "2-0"),
    ("PSV Eindhoven", "Lens", "1-0"),
    ("Real Madrid", "Braga", "3-0"),
    ("Salzburg", "Inter", "0-1"),
     ("Lazio", "Celtic", "2-0"),
    ("Shakhtar Donetsk", "Royal Antwerp", "1-0"),
    ("Feyenoord", "Atletico Madrid", "1-3"),
    ("Paris Saint-Germain", "Newcastle", "1-1"),
    ("AC Milan", "Borussia Dortmund", "1-3"),
    ("Manchester City", "RB Leipzig", "3-2"),
    ("Young Boys", "Crvena zvezda", "2-0"),
    ("Barcelona", "Porto", "2-1"),
    ("Galatasaray", "Manchester United", "3-3"),
    ("Sevilla", "PSV Eindhoven", "2-3"),
    ("Bayern Munich", "Copenhagen", "0-0"),
    ("Arsenal", "Lens", "6-0"),
    ("Real Madrid", "Napoli", "4-2"),
    ("Braga", "Union Berlin", "1-1"),
    ("Benfica", "Inter", "3-3"),
    ("Real Sociedad", "Salzburg", "0-0"),
    ("Lens", "Sevilla", "2-1"),
    ("PSV Eindhoven", "Arsenal", "1-1"),
    ("Manchester United", "Bayern Munich", "0-1"),
    ("Copenhagen", "Galatasaray", "1-0"),
    ("Napoli", "Braga", "2-0"),
    ("Union Berlin", "Real Madrid", "2-3"),
    ("Inter", "Real Sociedad", "0-0"),
    ("Salzburg", "Benfica", "1-3"),
    ("RB Leipzig", "Young Boys", "2-1"),
    ("Crvena zvezda", "Manchester City", "2-3"),
    ("Atletico Madrid", "Lazio", "2-0"),
    ("Celtic", "Feyenoord", "2-1"),
    ("Borussia Dortmund", "Paris Saint-Germain", "1-1"),
    ("Newcastle", "AC Milan", "1-2"),
    ("Porto", "Shakhtar Donetsk", "5-3"),
    ("Royal Antwerp", "Barcelona", "3-2")


]
# Insertar datos en la tabla de la fase de grupos
def insert_group_stage_matches(cursor, matches):
    cursor.executemany('''
        INSERT INTO fase_de_grupos (equipo_local, equipo_visitante, resultado_final)
        VALUES (?, ?, ?)
    ''', matches)

# Insert data into 'octavos' table
octavos_matches = [
    
]

# Insert data into 'cuartos' table
cuartos_matches = [
   
]


# Insert data into 'semis' table
semis_matches = [
    
]

# Insert data into 'final' table
final_match = [
    
        
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
db_file_path = '23-24/SQL/champions(23-24).db'
print(db_file_path)
