import sqlite3

# Conectarse a la base de datos nueva con el nombre especificado
conn = sqlite3.connect('16-17/SQL/champions(16-17).db')
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
    
('Juventus', 'Sevilla', '0-0'),
    ('Lyon', 'Dinamo Zagreb', '3-0'),
    ('Club Brugge', 'Leicester', '0-3'),
    ('FC Porto', 'Copenhagen', '1-1'),
    ('Legia', 'Dortmund', '0-6'),
    ('Real Madrid', 'Sporting CP', '2-1'),
    ('Tottenham', 'Monaco', '1-2'),
    ('Leverkusen', 'CSKA Moskva', '2-2'),
    ('Man City', 'Mönchengladbach', '4-0'),
    ('Bayern', 'Rostov', '5-0'),
    ('Barcelona', 'Celtic', '7-0'),
    ('PSV', 'Atlético de Madrid', '0-1'),
    ('Benfica', 'Beşiktaş', '1-1'),
    ('Dynamo Kyiv', 'Napoli', '1-2'),
    ('Paris', 'Arsenal', '1-1'),
    ('Basel', 'Ludogorets', '1-1'),
     ('Rostov', 'PSV', '2-2'),
    ('Atlético de Madrid', 'Bayern', '1-0'),
    ('Mönchengladbach', 'Barcelona', '1-2'),
    ('Celtic', 'Man City', '3-3'),
    ('Napoli', 'Benfica', '4-2'),
    ('Besiktas', 'Dynamo Kyiv', '1-1'),
    ('Arsenal', 'Basel', '2-0'),
    ('Ludogorets', 'Paris', '1-3'),
    ('Sevilla', 'Lyon', '1-0'),
    ('Dinamo Zagreb', 'Juventus', '0-4'),
    ('Sporting CP', 'Legia', '2-0'),
    ('Dortmund', 'Real Madrid', '2-2'),
    ('Monaco', 'Leverkusen', '1-1'),
    ('CSKA Moskva', 'Tottenham', '0-1'),
    ('Leicester', 'FC Porto', '1-0'),
    ('Copenhagen', 'Club Brugge', '4-0'),
     ('Bayern', 'PSV', '4-1'),
    ('Rostov', 'Atlético de Madrid', '0-1'),
    ('Celtic', 'Mönchengladbach', '0-2'),
    ('Barcelona', 'Man City', '4-0'),
    ('Dynamo Kyiv', 'Benfica', '0-2'),
    ('Napoli', 'Besiktas', '2-3'),
    ('Paris', 'Basel', '3-0'),
    ('Arsenal', 'Ludogorets', '6-0'),
    ('Dinamo Zagreb', 'Sevilla', '0-1'),
    ('Lyon', 'Juventus', '0-1'),
    ('Club Brugge', 'FC Porto', '1-2'),
    ('Leicester', 'Copenhagen', '1-0'),
    ('Real Madrid', 'Legia', '5-1'),
    ('Sporting CP', 'Dortmund', '1-2'),
    ('CSKA Moskva', 'Monaco', '1-1'),
    ('Leverkusen', 'Tottenham', '0-0'),
    ('Juventus', 'Lyon', '1-1'),
    ('Sevilla', 'Dinamo Zagreb', '4-0'),
    ('Copenhagen', 'Leicester', '0-0'),
    ('FC Porto', 'Club Brugge', '1-0'),
    ('Legia', 'Real Madrid', '3-3'),
    ('Dortmund', 'Sporting CP', '1-0'),
    ('Tottenham', 'Leverkusen', '0-1'),
    ('Monaco', 'CSKA Moskva', '3-0'),
    ('Atlético de Madrid', 'Rostov', '2-1'),
    ('PSV', 'Bayern', '1-2'),
    ('Man City', 'Barcelona', '3-1'),
    ('Mönchengladbach', 'Celtic', '1-1'),
    ('Benfica', 'Dynamo Kyiv', '1-0'),
    ('Besiktas', 'Napoli', '1-1'),
    ('Basel', 'Paris', '1-2'),
    ('Ludogorets', 'Arsenal', '2-3'),
    ('Atlético de Madrid', 'PSV', '2-0'),
    ('Napoli', 'Dynamo Kyiv', '0-0'),
    ('Besiktas', 'Benfica', '3-3'),
    ('Dinamo Zagreb', 'Lyon', '0-1'),
    ('Mönchengladbach', 'Man City', '1-1'),
    ('Celtic', 'Barcelona', '0-2'),
    ('Arsenal', 'Paris', '2-2'),
    ('Ludogorets', 'Basel', '0-0'),
    ('Rostov', 'Bayern', '3-2'),
    ('Sevilla', 'Juventus', '1-3'),
    ('Copenhagen', 'FC Porto', '0-0'),
    ('Leicester', 'Club Brugge', '2-1'),
    ('Dortmund', 'Legia', '8-4'),
    ('Sporting CP', 'Real Madrid', '1-2'),
    ('CSKA Moskva', 'Leverkusen', '1-1'),
    ('Monaco', 'Tottenham', '2-1'),
    ('Juventus', 'Dinamo Zagreb', '2-0'),
    ('Lyon', 'Sevilla', '0-0'),
    ('Club Brugge', 'Copenhagen', '0-2'),
    ('FC Porto', 'Leicester', '5-0'),
    ('Tottenham', 'CSKA Moskva', '3-1'),
    ('Leverkusen', 'Monaco', '3-0'),
    ('Bayern', 'Atlético de Madrid', '1-0'),
    ('Man City', 'Celtic', '1-1'),
    ('Benfica', 'Napoli', '1-2'),
    ('Dynamo Kyiv', 'Besiktas', '6-0'),
    ('Paris', 'Ludogorets', '2-2'),
    ('PSV', 'Rostov', '0-0'),
    ('Legia', 'Sporting CP', '1-0'),
    ('Real Madrid', 'Dortmund', '2-2'),
    ('Arsenal', 'Basel', '4-1'),
    ('Barcelona', 'Mönchengladbach', '4-0')
    


]
# Insertar datos en la tabla de la fase de grupos
def insert_group_stage_matches(cursor, matches):
    cursor.executemany('''
        INSERT INTO fase_de_grupos (equipo_local, equipo_visitante, resultado_final)
        VALUES (?, ?, ?)
    ''', matches)

# Insert data into 'octavos' table
octavos_matches = [
    (1, 'Atlético de Madrid', 'Leverkusen', '4-2', '0-0'),
    (2, 'Mónaco', 'Man City', '3-5', '3-1'),
    (3, 'Leicester', 'Sevilla', '1-2', '2-0'),
    (4, 'Juventus', 'FC Porto', '2-0', '1-0'),
    (5, 'Dortmund', 'Benfica', '0-1', '4-0'),
    (6, 'Barcelona', 'Paris', '0-4', '6-1'),
    (7, 'Real Madrid', 'Napoli', '3-1', '3-1'),
    (8, 'Bayern', 'Arsenal', '5-1', '5-1')
]

# Insert data into 'cuartos' table
cuartos_matches = [
   (1, 'Monaco', 'Dortmund', '3-2', '3-1'),
    (2, 'Juventus', 'Barcelona', '3-0', '0-0'),
    (3, 'Real Madrid', 'Bayern', '2-1', '4-2'),
    (4, 'Atlético de Madrid', 'Leicester', '1-0', '1-1')
]


# Insert data into 'semis' table
semis_matches = [
    (1, 'Real Madrid', 'Atlético de Madrid', '3-0', '1-2'),
    (2, 'Juventus', 'Monaco', '2-0', '2-1')
]


# Insert data into 'final' table
final_match = [
    (1, 'Juventus', 'Real Madrid', '1-4')
    
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
db_file_path = '16-17/SQL/champions(16-17).db'
print(db_file_path)
