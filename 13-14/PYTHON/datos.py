import sqlite3

# Conectarse a la base de datos nueva con el nombre especificado
conn = sqlite3.connect('13-14/SQL/champions(13-14).db')
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
    ('Barcelona', 'Ajax', '4-0'),
    ('Milan', 'Celtic', '2-0'),
    ('Austria Wien', 'FC Porto', '0-1'),
    ('Atlético de Madrid', 'Zenit', '3-1'),
    ('Chelsea', 'Basel', '1-2'),
    ('Schalke', 'FCSB', '3-0'),
    ('Bayern', 'CSKA Moskva', '3-0'),
    ('Olympiacos', 'Paris', '1-4'),
    ('Napoli', 'Dortmund', '2-1'),
    ('Marseille', 'Arsenal', '1-2'),
    ('Viktoria Plzeň', 'Man City', '0-3'),
    ('Benfica', 'Anderlecht', '2-0'),
    ('Copenhagen', 'Juventus', '1-1'),
    ('Galatasaray', 'Real Madrid', '1-6'),
    ('Man United', 'Leverkusen', '4-2'),
    ('Real Sociedad', 'Shakhtar Donetsk', '0-2'),
    ('Man City', 'Bayern', '1-3'),
    ('Anderlecht', 'Olympiacos', '0-3'),
    ('Real Madrid', 'Copenhagen', '4-0'),
    ('Juventus', 'Galatasaray', '2-2'),
    ('Shakhtar Donetsk', 'Man United', '1-1'),
    ('CSKA Moskva', 'Viktoria Plzeň', '3-2'),
    ('Ajax', 'Milan', '1-1'),
    ('FC Porto', 'Atlético de Madrid', '1-2'),
    ('Dortmund', 'Marseille', '3-0'),
    ('FCSB', 'Chelsea', '0-4'),
    ('Zenit', 'Austria Wien', '0-0'),
    ('Paris', 'Benfica', '3-0'),
    ('Leverkusen', 'Real Sociedad', '2-1'),
    ('Celtic', 'Barcelona', '0-1'),
    ('Arsenal', 'Napoli', '2-0'),
    ('Basel', 'Schalke', '0-1'),
    ('Bayern', 'Viktoria Plzeň', '5-0'),
    ('Galatasaray', 'Copenhagen', '3-1'),
    ('Benfica', 'Olympiacos', '1-1'),
    ('Anderlecht', 'Paris', '0-5'),
    ('Leverkusen', 'Shakhtar Donetsk', '4-0'),
    ('Real Madrid', 'Juventus', '2-1'),
    ('Man United', 'Real Sociedad', '1-0'),
    ('CSKA Moskva', 'Man City', '1-2'),
    ('Celtic', 'Ajax', '2-1'),
    ('Austria Wien', 'Atlético de Madrid', '0-3'),
    ('Milan', 'Barcelona', '1-1'),
    ('FC Porto', 'Zenit', '0-1'),
    ('Marseille', 'Napoli', '1-2'),
    ('Arsenal', 'Dortmund', '1-2'),
    ('FCSB', 'Basel', '1-1'),
    ('Schalke', 'Chelsea', '0-3'),
    ('Barcelona', 'Milan', '3-1'),
    ('Ajax', 'Celtic', '1-0'),
    ('Atlético de Madrid', 'Austria Wien', '4-0'),
    ('Napoli', 'Marseille', '3-2'),
    ('Dortmund', 'Arsenal', '0-1'),
    ('Chelsea', 'Schalke', '3-0'),
    ('Basel', 'FCSB', '1-1'),
    ('Zenit', 'FC Porto', '1-1'),
    ('Viktoria Plzeň', 'Bayern', '0-1'),
    ('Man City', 'CSKA Moskva', '5-2'),
    ('Olympiacos', 'Benfica', '1-0'),
    ('Paris', 'Anderlecht', '1-1'),
    ('Copenhagen', 'Galatasaray', '1-0'),
    ('Juventus', 'Real Madrid', '2-2'),
    ('Shakhtar Donetsk', 'Leverkusen', '0-0'),
    ('Real Sociedad', 'Man United', '0-0'),
    ('Man City', 'Viktoria Plzeň', '4-2'),
    ('Paris', 'Olympiacos', '2-1'),
    ('Juventus', 'Copenhagen', '3-1'),
    ('Real Madrid', 'Galatasaray', '4-1'),
    ('Leverkusen', 'Man United', '0-5'),
    ('CSKA Moskva', 'Bayern', '1-3'),
    ('Celtic', 'Milan', '0-3'),
    ('FC Porto', 'Austria Wien', '1-1'),
    ('Arsenal', 'Marseille', '2-0'),
    ('Basel', 'Chelsea', '1-0'),
    ('Zenit', 'Atlético de Madrid', '1-1'),
    ('Anderlecht', 'Benfica', '2-3'),
    ('Shakhtar Donetsk', 'Real Sociedad', '4-0'),
    ('Ajax', 'Barcelona', '2-1'),
    ('Dortmund', 'Napoli', '3-1'),
    ('FCSB', 'Schalke', '0-0'),
    ('Barcelona', 'Celtic', '6-1'),
    ('Milan', 'Ajax', '0-0'),
    ('Austria Wien', 'Zenit', '4-1'),
    ('Atlético de Madrid', 'FC Porto', '2-0'),
    ('Chelsea', 'FCSB', '1-0'),
    ('Schalke', 'Basel', '2-0'),
    ('Viktoria Plzeň', 'CSKA Moskva', '2-1'),
    ('Bayern', 'Man City', '2-3'),
    ('Napoli', 'Arsenal', '2-0'),
    ('Marseille', 'Dortmund', '1-2'),
    ('Galatasaray', 'Juventus', '1-0'),
    ('Benfica', 'Paris', '2-1'),
    ('Olympiacos', 'Anderlecht', '3-1'),
    ('Man United', 'Shakhtar Donetsk', '1-0'),
    ('Copenhagen', 'Real Madrid', '0-2'),
    ('Real Sociedad', 'Leverkusen', '0-1')
    

]
# Insertar datos en la tabla de la fase de grupos
def insert_group_stage_matches(cursor, matches):
    cursor.executemany('''
        INSERT INTO fase_de_grupos (equipo_local, equipo_visitante, resultado_final)
        VALUES (?, ?, ?)
    ''', matches)

# Insert data into 'octavos' table
octavos_matches = [
    (1, 'Milan', 'Atlético de Madrid', '0-1', '1-4'),
    (2, 'Arsenal', 'Bayern', '0-2', '1-1'),
    (3, 'Man City', 'Barcelona', '0-2', '1-2'),
    (4, 'Schalke', 'Real Madrid', '1-6', '1-3'),
    (5, 'Galatasaray', 'Chelsea', '1-1', '0-2'),
    (6, 'Zenit', 'Dortmund', '2-4', '1-2'),
    (7, 'Olympiacos', 'Man United', '2-0', '0-3'),
    (8, 'Leverkusen', 'Paris', '0-4', '1-2')
]

# Insert data into 'cuartos' table
cuartos_matches = [
    (1, 'Atlético de Madrid', 'Barcelona', '1-1', '1-0'), 
    (2, 'Chelsea', 'Paris', '1-3', '2-0'), 
    (3, 'Bayern', 'Man United', '1-1', '3-1'), 
    (4, 'Real Madrid', 'Dortmund', '3-0', '0-2')
]


# Insert data into 'semis' table
semis_matches = [
    (1, 'Bayern', 'Real Madrid', '0-1', '0-4'),
    (2, 'Atlético de Madrid', 'Chelsea', '0-0', '3-1')

]

# Insert data into 'final' table
final_match = [
    (1, 'Real Madrid', 'Atlético de Madrid', '4-1')
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
db_file_path = '13-14/SQL/champions(13-14).db'
print(db_file_path)
