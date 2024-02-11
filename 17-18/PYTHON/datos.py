import sqlite3

# Conectarse a la base de datos nueva con el nombre especificado
conn = sqlite3.connect('14-15/SQL/champions(14-15).db')
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
   
    ("Club Brugge", "Dortmund", "0-1"),
    ("Monaco", "Atlético", "1-2"),
    ("Barcelona", "PSV Eindhoven", "4-0"),
    ("Inter", "Tottenham", "2-1"),
    ("Liverpool", "Paris", "3-2"),
    ("Crvena zvezda", "Napoli", "0-0"),
    ("Galatasaray", "Lokomotiv Moskva", "3-0"),
    ("Schalke", "Porto", "1-1"),
    ("Ajax", "AEK Athens", "3-0"),
    ("Benfica", "Bayern München", "0-2"),
    ("Shakhtar", "Hoffenheim", "2-2"),
    ("Manchester City", "Lyon", "1-2"),
    ("Real Madrid", "Roma", "3-0"),
    ("Viktoria Plzeň", "CSKA Moskva", "2-2"),
    ("Young Boys", "Manchester United", "0-3"),
    ("Valencia", "Juventus", "0-2"),
    ("Bayern München", "Ajax", "1-1"),
    ("AEK Athens", "Benfica", "2-3"),
    ("Hoffenheim", "Manchester City", "1-2"),
    ("Lyon", "Shakhtar Donetsk", "2-2"),
    ("CSKA Moskva", "Real Madrid", "1-0"),
    ("Roma", "Viktoria Plzeň", "5-0"),
    ("Juventus", "Young Boys", "3-0"),
    ("Manchester United", "Valencia", "0-0"),
    ("Atlético Madrid", "Club Brugge", "3-1"),
    ("Dortmund", "Monaco", "3-0"),
    ("Tottenham", "Barcelona", "2-4"),
    ("PSV Eindhoven", "Inter", "1-2"),
    ("Paris Saint-Germain", "Crvena zvezda", "6-1"),
    ("Napoli", "Liverpool", "1-0"),
    ("Lokomotiv Moskva", "Schalke 04", "0-1"),
    ("Porto", "Galatasaray", "1-0"),
    ("AEK Athens", "Bayern München", "0-2"),
    ("Young Boys", "Valencia", "1-1"),
    ("Ajax", "Benfica", "1-0"),
    ("Shakhtar Donetsk", "Manchester City", "0-3"),
    ("Real Madrid", "Viktoria Plzeň", "2-1"),
    ("Roma", "CSKA Moskva", "3-0"),
    ("Manchester United", "Juventus", "0-1"),
    ("Hoffenheim", "Lyon", "3-3"),
    ("Club Brugge", "Monaco", "1-1"),
    ("PSV Eindhoven", "Tottenham", "2-2"),
    ("Barcelona", "Inter", "2-0"),
    ("Borussia Dortmund", "Atlético Madrid", "4-0"),
    ("Liverpool", "Crvena zvezda", "4-0"),
    ("Galatasaray", "Schalke 04", "0-0"),
    ("Lokomotiv Moskva", "Porto", "1-3"),
    ("Paris Saint-Germain", "Napoli", "2-2"),
    ("Bayern München", "AEK Athens", "2-0"),
    ("Valencia", "Young Boys", "3-1"),
    ("Benfica", "Ajax", "1-1"),
    ("Manchester City", "Shakhtar Donetsk", "6-0"),
    ("Viktoria Plzeň", "Real Madrid", "0-5"),
    ("CSKA Moskva", "Roma", "1-2"),
    ("Juventus", "Manchester United", "1-2"),
    ("Lyon", "Hoffenheim", "2-2"),
    ("Monaco", "Club Brugge", "0-4"),
    ("Tottenham", "PSV Eindhoven", "2-1"),
    ("Inter", "Barcelona", "1-1"),
    ("Atlético Madrid", "Borussia Dortmund", "2-0"),
    ("Crvena zvezda", "Liverpool", "2-0"),
    ("Schalke 04", "Galatasaray", "2-0"),
    ("Porto", "Lokomotiv Moskva", "4-1"),
    ("Napoli", "Paris Saint-Germain", "1-1"),
    ("AEK Athens", "Ajax", "0-2"),
    ("CSKA Moskva", "Viktoria Plzeň", "1-2"),
    ("Roma", "Real Madrid", "0-2"),
    ("Manchester United", "Young Boys", "1-0"),
    ("Juventus", "Valencia", "1-0"),
    ("Lyon", "Manchester City", "2-2"),
    ("Bayern München", "Benfica", "5-1"),
    ("Hoffenheim", "Shakhtar Donetsk", "2-3"),
    ("Ajax", "AEK Athens", "2-0"),
    ("Shakhtar Donetsk", "Hoffenheim", "3-2"),
    ("Lokomotiv Moskva", "Galatasaray", "2-0"),
    ("Atlético Madrid", "Monaco", "2-0"),
    ("Borussia Dortmund", "Club Brugge", "0-0"),
    ("PSV Eindhoven", "Barcelona", "1-2"),
    ("Tottenham", "Inter", "1-0"),
    ("Paris Saint-Germain", "Liverpool", "2-1"),
    ("Napoli", "Crvena zvezda", "3-1"),
    ("Porto", "Schalke 04", "3-1"),
     ("Viktoria Plzeň", "Roma", "2-1"),
    ("Real Madrid", "CSKA Moskva", "0-3"),
    ("Young Boys", "Juventus", "2-1"),
    ("Valencia", "Manchester United", "2-1"),
    ("Ajax", "Bayern München", "3-3"),
    ("Benfica", "AEK Athens", "1-0"),
    ("Manchester City", "Hoffenheim", "2-1"),
    ("Shakhtar Donetsk", "Lyon", "1-1"),
    ("Viktoria Plzeň", "Roma", "2-1"),
    ("Real Madrid", "CSKA Moskva", "0-3"),
    ("Club Brugge", "Atlético Madrid", "0-0"),
    ("Monaco", "Borussia Dortmund", "0-2"),
    ("Barcelona", "Tottenham", "1-1"),
    ("Red Star Belgrade", "Paris Saint-Germain", "1-4"),
    ("Liverpool", "Napoli", "1-0"),
    ("Galatasaray", "Porto", "2-3"),
    ("Schalke 04", "Lokomotiv Moskva", "1-0"),
    ("Inter", "PSV Eindhoven", "1-1")


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
db_file_path = '14-15/SQL/champions(14-15).db'
print(db_file_path)
