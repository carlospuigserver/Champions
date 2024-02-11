import sqlite3

# Conectarse a la base de datos nueva con el nombre especificado
conn = sqlite3.connect('22-23/SQL/champions(22-23).db')
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
    ("RB Leipzig", "Shakhtar Donetsk", "1-4"),
    ("Benfica", "Maccabi Haifa", "2-0"),
    ("PSG", "Juventus", "2-1"),
    ("Sevilla", "Manchester City", "0-4"),
    ("Celtic", "Real Madrid", "0-3"),
    ("Red Bull Salzburg", "Milan", "1-1"),
    ("Borussia Dortmund", "Kobenhavn", "3-0"),
    ("Dinamo Zagreb", "Chelsea", "1-0"),
    ("Eintracht Frankfurt", "Sporting de Portugal", "0-3"),
    ("Napoli", "Liverpool", "4-1"),
    ("Atlético de Madrid", "Porto", "2-1"),
    ("Brugge", "Bayer Leverkusen", "1-0"),
    ("Barcelona", "Viktoria Plzeň", "5-1"),
    ("Inter", "Bayern München", "0-2"),
    ("Tottenham", "Olympique de Marseille", "2-0"),
    ("Ajax", "Rangers", "4-0"),
    ("Porto", "Brugge", "0-4"),
    ("Olympique de Marseille", "Eintracht Frankfurt", "0-1"),
    ("Bayern München", "Barcelona", "2-0"),
    ("Bayer Leverkusen", "Atlético de Madrid", "2-0"),
    ("Viktoria Plzeň", "Inter", "0-2"),
    ("Sporting de Portugal", "Tottenham", "2-0"),
    ("Liverpool", "Ajax", "2-1"),
    ("Manchester City", "Borussia Dortmund", "2-1"),
    ("Maccabi Haifa", "PSG", "1-3"),
    ("Juventus", "Benfica", "1-2"),
    ("Kobenhavn", "Sevilla", "0-0"),
    ("Real Madrid", "RB Leipzig", "2-0"),
    ("Chelsea", "Red Bull Salzburg", "1-1"),
    ("Rangers", "Napoli", "0-3"),
    ("Shakhtar Donetsk", "Celtic", "1-1"),
    ("Milan", "Dinamo Zagreb", "3-1"),
    ("Eintracht Frankfurt", "Tottenham", "0-0"),
    ("Inter", "Barcelona", "1-0"),
    ("Brugge", "Atlético de Madrid", "2-0"),
    ("Porto", "Bayer Leverkusen", "2-0"),
    ("Ajax", "Napoli", "1-6"),
    ("Liverpool", "Rangers", "2-0"),
    ("Olympique de Marseille", "Sporting de Portugal", "4-1"),
    ("Bayern München", "Viktoria Plzeň", "5-0"),
    ("RB Leipzig", "Celtic", "3-1"),
    ("Chelsea", "Milan", "3-0"),
    ("Manchester City", "Kobenhavn", "5-0"),
    ("Sevilla", "Borussia Dortmund", "1-4"),
    ("Juventus", "Maccabi Haifa", "3-1"),
    ("Benfica", "PSG", "1-1"),
    ("Real Madrid", "Shakhtar Donetsk", "2-1"),
     ("Red Bull Salzburg", "Dinamo Zagreb", "1-0"),
    ("Kobenhavn", "Manchester City", "0-0"),
    ("Maccabi Haifa", "Juventus", "2-0"),
    ("Milan", "Chelsea", "0-2"),
    ("Shakhtar Donetsk", "Real Madrid", "1-1"),
    ("Celtic", "RB Leipzig", "0-2"),
    ("Borussia Dortmund", "Sevilla", "1-1"),
    ("PSG", "Benfica", "1-1"),
    ("Dinamo Zagreb", "Red Bull Salzburg", "1-1"),
    ("Viktoria Plzeň", "Bayern München", "2-4"),
    ("Atlético de Madrid", "Brugge", "0-0"),
    ("Sporting de Portugal", "Olympique de Marseille", "0-2"),
    ("Tottenham", "Eintracht Frankfurt", "3-2"),
    ("Barcelona", "Inter", "3-3"),
    ("Napoli", "Ajax", "4-2"),
    ("Bayer Leverkusen", "Porto", "0-3"),
    ("Rangers", "Liverpool", "1-7"),
    ("Red Bull Salzburg", "Chelsea", "1-2"),
    ("Sevilla", "Kobenhavn", "3-0"),
    ("Dinamo Zagreb", "Milan", "0-4"),
    ("Celtic", "Shakhtar Donetsk", "1-1"),
    ("RB Leipzig", "Real Madrid", "3-2"),
    ("Borussia Dortmund", "Manchester City", "0-0"),
    ("PSG", "Maccabi Haifa", "7-2"),
    ("Benfica", "Juventus", "4-3"),
    ("Eintracht Frankfurt", "Olympique de Marseille", "2-1"),
    ("Ajax", "Liverpool", "0-3"),
    ("Tottenham", "Sporting de Portugal", "1-1"),
    ("Barcelona", "Bayern München", "0-3"),
    ("Atlético de Madrid", "Bayer Leverkusen", "2-2"),
    ("Napoli", "Rangers", "3-0"),
    ("Inter", "Viktoria Plzeň", "4-0"),
    ("Brugge", "Porto", "0-4"),
    ("Bayer Leverkusen", "Brugge", "0-0"),
    ("Olympique de Marseille", "Tottenham", "1-2"),
    ("Sporting de Portugal", "Eintracht Frankfurt", "1-2"),
    ("Bayern München", "Inter", "2-0"),
    ("Rangers", "Ajax", "1-3"),
    ("Liverpool", "Napoli", "2-0"),
    ("Viktoria Plzeň", "Barcelona", "2-4"),
    ("Porto", "Atlético de Madrid", "2-1"),
    ("Chelsea", "Dinamo Zagreb", "2-1"),
    ("Maccabi Haifa", "Benfica", "1-6"),
    ("Juventus", "PSG", "1-2"),
    ("Kobenhavn", "Borussia Dortmund", "1-1"),
    ("Manchester City", "Sevilla", "3-1"),
    ("Milan", "Red Bull Salzburg", "4-0"),
    ("Real Madrid", "Celtic", "5-1"),
    ("Shakhtar Donetsk", "RB Leipzig", "0-4")

]
# Insertar datos en la tabla de la fase de grupos
def insert_group_stage_matches(cursor, matches):
    cursor.executemany('''
        INSERT INTO fase_de_grupos (equipo_local, equipo_visitante, resultado_final)
        VALUES (?, ?, ?)
    ''', matches)

# Insert data into 'octavos' table
octavos_matches = [
    (1,"Real Madrid", "Liverpool", "5-2", "1-0"),  
    (2,"Borussia Dortmund", "Chelsea", "1-0", "0-2"), 
    (3,"RB Leipzig", "Manchester City", "1-1", "0-7"),  
    (4,"PSG", "Bayern München", "0-1", "0-2"), 
    (5,"Milan", "Tottenham", "1-0", "0-0"),  
    (6,"Eintracht Frankfurt", "Napoli", "0-2", "0-3"),  
    (7,"Brugge", "Benfica", "0-2", "1-5"), 
    (8,"Inter", "Porto", "1-0", "0-0")  
]

# Insert data into 'cuartos' table
cuartos_matches = [
    (1,"Real Madrid", "Chelsea", "2-0", "2-0"),
    (2,"Manchester City", "Bayern München", "3-0", "1-1"),
    (3,"Milan", "Napoli", "1-0", "1-1"),
    (4,"Benfica", "Inter", "0-2", "3-3")
]


# Insert data into 'semis' table
semis_matches = [
    (1,"Real Madrid", "Manchester City", "1-1", "0-4"),
    (2,"Milan", "Inter", "0-2", "0-1")
]

# Insert data into 'final' table
final_match = [
    (1,"Manchester City", "Inter", "1-0")
        
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
db_file_path = '22-23/SQL/champions(22-23).db'
print(db_file_path)
