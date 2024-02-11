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
   ('Athletic Club', 'Shakhtar Donetsk', '0-0'),
    ('FC Porto', 'BATE Borisov', '6-0'),
    ('Maribor', 'Sporting CP', '1-1'),
    ('Chelsea', 'Schalke', '1-1'),
    ('Ajax', 'Paris', '1-1'),
    ('Barcelona', 'APOEL', '1-0'),
    ('Bayern', 'Man City', '1-0'),
    ('Roma', 'CSKA Moskva', '5-1'),
    ('Galatasaray', 'Anderlecht', '1-1'),
    ('Benfica', 'Zenit', '0-2'),
    ('Monaco', 'Leverkusen', '1-0'),
    ('Dortmund', 'Arsenal', '2-0'),
    ('Real Madrid', 'Basel', '5-1'),
    ('Liverpool', 'Ludogorets', '2-1'),
    ('Olympiacos', 'Atlético de Madrid', '3-2'),
    ('Juventus', 'Malmö', '2-0'),
    ('Anderlecht', 'Dortmund', '0-3'),
    ('Arsenal', 'Galatasaray', '4-1'),
    ('Leverkusen', 'Benfica', '3-1'),
    ('Ludogorets', 'Real Madrid', '1-2'),
    ('Basel', 'Liverpool', '1-0'),
    ('Atlético de Madrid', 'Juventus', '1-0'),
    ('Malmö', 'Olympiacos', '2-0'),
    ('Zenit', 'Monaco', '0-0'),
    ('Shakhtar Donetsk', 'FC Porto', '2-2'),
    ('BATE Borisov', 'Athletic Club', '2-1'),
    ('Schalke', 'Maribor', '1-1'),
    ('Sporting CP', 'Chelsea', '0-1'),
    ('APOEL', 'Ajax', '1-1'),
    ('Paris', 'Barcelona', '3-2'),
    ('CSKA Moskva', 'Bayern', '0-1'),
    ('Man City', 'Roma', '1-1'),
    ('Galatasaray', 'Dortmund', '0-4'),
    ('Anderlecht', 'Arsenal', '1-2'),
    ('Monaco', 'Benfica', '0-0'),
    ('Leverkusen', 'Zenit', '2-0'),
    ('Liverpool', 'Real Madrid', '0-3'),
    ('Ludogorets', 'Basel', '1-0'),
    ('Olympiacos', 'Juventus', '1-0'),
    ('Atlético de Madrid', 'Malmö', '5-0'),
    ('BATE Borisov', 'Shakhtar Donetsk', '0-7'),
    ('FC Porto', 'Athletic Club', '2-1'),
    ('Chelsea', 'Maribor', '6-0'),
    ('Schalke', 'Sporting CP', '4-3'),
    ('Barcelona', 'Ajax', '3-1'),
    ('APOEL', 'Paris', '0-1'),
    ('CSKA Moskva', 'Man City', '2-2'),
    ('Roma', 'Bayern', '1-7'),
     ('Athletic Club', 'FC Porto', '0-2'),
    ('Shakhtar Donetsk', 'BATE Borisov', '5-0'),
    ('Sporting CP', 'Schalke', '4-2'),
    ('Ajax', 'Barcelona', '0-2'),
    ('Maribor', 'Chelsea', '1-1'),
    ('Paris', 'APOEL', '1-0'),
    ('Bayern', 'Roma', '2-0'),
    ('Man City', 'CSKA Moskva', '1-2'),
    ('Arsenal', 'Anderlecht', '3-3'),
    ('Dortmund', 'Galatasaray', '4-1'),
    ('Basel', 'Ludogorets', '4-0'),
    ('Benfica', 'Monaco', '1-0'),
    ('Real Madrid', 'Liverpool', '1-0'),
    ('Juventus', 'Olympiacos', '3-2'),
    ('Zenit', 'Leverkusen', '1-2'),
    ('Malmö', 'Atlético de Madrid', '0-2'),
     ('Arsenal', 'Dortmund', '2-0'),
    ('Anderlecht', 'Galatasaray', '2-0'),
    ('Leverkusen', 'Monaco', '0-1'),
    ('Basel', 'Real Madrid', '0-1'),
    ('Ludogorets', 'Liverpool', '2-2'),
    ('Atlético de Madrid', 'Olympiacos', '4-0'),
    ('Malmö', 'Juventus', '0-2'),
    ('Zenit', 'Benfica', '1-0'),
    ('Sporting CP', 'Maribor', '3-1'),
    ('Schalke', 'Chelsea', '0-5'),
    ('APOEL', 'Barcelona', '0-4'),
    ('Manchester City', 'Bayern Munich', '3-2'),
    ('CSKA Moskva', 'Roma', '1-1'),
    ('Shakhtar Donetsk', 'Athletic Club', '0-1'),
    ('BATE Borisov', 'FC Porto', '0-3'),
    ('Paris', 'Ajax', '3-1'),
    ('Athletic Club', 'BATE Borisov', '2-0'),
    ('FC Porto', 'Shakhtar Donetsk', '1-1'),
    ('Chelsea', 'Sporting CP', '3-1'),
    ('Maribor', 'Schalke', '0-1'),
    ('Ajax', 'APOEL', '4-0'),
    ('Barcelona', 'Paris', '3-1'),
    ('Bayern', 'CSKA Moskva', '3-0'),
    ('Roma', 'Man City', '0-2'),
    ('Galatasaray', 'Arsenal', '1-4'),
    ('Dortmund', 'Anderlecht', '1-1'),
    ('Benfica', 'Leverkusen', '0-0'),
    ('Monaco', 'Zenit', '2-0'),
    ('Real Madrid', 'Ludogorets', '4-0'),
    ('Liverpool', 'Basel', '1-1'),
    ('Olympiacos', 'Malmö', '4-2'),
    ('Juventus', 'Atlético de Madrid', '0-0')



]
# Insertar datos en la tabla de la fase de grupos
def insert_group_stage_matches(cursor, matches):
    cursor.executemany('''
        INSERT INTO fase_de_grupos (equipo_local, equipo_visitante, resultado_final)
        VALUES (?, ?, ?)
    ''', matches)

# Insert data into 'octavos' table
octavos_matches = [
    (1, 'Bayern', 'Shakhtar Donetsk', '0-0', '7-0'), 
    (2, 'Chelsea', 'Paris', '1-1', '2-2'), 
    (3, 'Real Madrid', 'Schalke', '2-0', '3-4'), 
    (4, 'FC Porto', 'Basel', '1-1', '4-0'), 
    (5, 'Leverkusen', 'Atlético de Madrid', '1-0', '0-1'), 
    (6, 'Arsenal', 'Monaco', '1-3', '2-0'), 
    (7, 'Man City', 'Barcelona', '1-2', '0-1'), 
    (8, 'Juventus', 'Dortmund', '2-1', '3-0')
]

# Insert data into 'cuartos' table
cuartos_matches = [
    (1, 'Real Madrid', 'Atlético de Madrid', '0-0', '1-0'), 
    (2, 'FC Porto', 'Bayern', '3-1', '1-6'), 
    (3, 'Paris', 'Barcelona', '1-3', '0-2'), 
    (4, 'Juventus', 'Monaco', '1-0', '0-0')
]


# Insert data into 'semis' table
semis_matches = [
    (1, 'Barcelona', 'Bayern', '3-0', '2-3'),
    (2, 'Juventus', 'Real Madrid', '2-1', '1-1')
]


# Insert data into 'final' table
final_match = [
    (1, 'Juventus', 'Barcelona', '1-3')
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
