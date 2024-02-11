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
    ('Gent', 'Lyon', '1-1'),
    ('Valencia', 'Zenit', '2-3'),
    ('Dynamo Kyiv', 'FC Porto', '2-2'),
    ('Olympiacos', 'Bayern', '0-3'),
    ('Chelsea', 'Maccabi Tel Aviv', '4-0'),
    ('Dinamo Zagreb', 'Arsenal', '2-1'),
    ('Roma', 'Barcelona', '1-1'),
    ('Leverkusen', 'BATE Borisov', '4-1'),
    ('Sevilla', 'Mönchengladbach', '3-0'),
    ('Man City', 'Juventus', '1-2'),
    ('PSV', 'Man United', '2-1'),
    ('Wolfsburg', 'CSKA Moskva', '1-0'),
    ('Paris', 'Malmö', '2-0'),
    ('Real Madrid', 'Shakhtar Donetsk', '4-0'),
    ('Galatasaray', 'Atlético de Madrid', '0-2'),
    ('Benfica', 'Astana', '2-0'),
    ('Juventus', 'Sevilla', '2-0'),
    ('Mönchengladbach', 'Man City', '1-2'),
    ('CSKA Moskva', 'PSV', '3-2'),
    ('Man United', 'Wolfsburg', '2-1'),
    ('Shakhtar Donetsk', 'Paris', '0-3'),
    ('Malmö', 'Real Madrid', '0-2'),
    ('Astana', 'Galatasaray', '2-2'),
    ('Atlético de Madrid', 'Benfica', '1-2'),
    ('Lyon', 'Valencia', '0-1'),
    ('Zenit', 'Gent', '2-1'),
    ('FC Porto', 'Chelsea', '2-1'),
    ('Maccabi Tel Aviv', 'Dynamo Kyiv', '0-2'),
    ('Arsenal', 'Olympiacos', '2-3'),
    ('Bayern', 'Dinamo Zagreb', '5-0'),
    ('Barcelona', 'Leverkusen', '2-1'),
    ('BATE Borisov', 'Roma', '3-2'),
    ('Man City', 'Sevilla', '2-1'),
    ('Juventus', 'Mönchengladbach', '0-0'),
    ('Atlético de Madrid', 'Astana', '4-0'),
    ('Galatasaray', 'Benfica', '2-1'),
    ('Wolfsburg', 'PSV', '2-0'),
    ('CSKA Moskva', 'Man United', '1-1'),
    ('Paris', 'Real Madrid', '0-0'),
    ('Malmö', 'Shakhtar Donetsk', '1-0'),
    ('Zenit', 'Lyon', '3-1'),
    ('Valencia', 'Gent', '2-1'),
    ('Dynamo Kyiv', 'Chelsea', '0-0'),
    ('FC Porto', 'Maccabi Tel Aviv', '2-0'),
    ('Dinamo Zagreb', 'Olympiacos', '0-1'),
    ('Arsenal', 'Bayern', '2-0'),
    ('BATE Borisov', 'Barcelona', '0-2'),
    ('Leverkusen', 'Roma', '4-4'),
    ('Gent', 'Valencia', '1-0'),
    ('Lyon', 'Zenit', '0-2'),
    ('Maccabi Tel Aviv', 'FC Porto', '1-3'),
    ('Olympiacos', 'Dinamo Zagreb', '2-1'),
    ('Chelsea', 'Dynamo Kyiv', '2-1'),
    ('Bayern', 'Arsenal', '5-1'),
    ('Roma', 'Leverkusen', '3-2'),
    ('Barcelona', 'BATE Borisov', '3-0'),
    ('Mönchengladbach', 'Juventus', '1-1'),
    ('Sevilla', 'Man City', '1-3'),
    ('Benfica', 'Galatasaray', '2-1'),
    ('PSV', 'Wolfsburg', '2-0'),
    ('Man United', 'CSKA Moskva', '1-0'),
    ('Astana', 'Atlético de Madrid', '0-0'),
    ('Real Madrid', 'Paris', '1-0'),
    ('Shakhtar Donetsk', 'Malmö', '4-0'),
    ('Mönchengladbach', 'Sevilla', '4-2'),
    ('Juventus', 'Man City', '1-0'),
    ('Man United', 'PSV', '0-0'),
    ('CSKA Moskva', 'Wolfsburg', '0-2'),
    ('Maccabi Tel Aviv', 'Chelsea', '0-4'),
    ('Shakhtar Donetsk', 'Real Madrid', '3-4'),
    ('Malmö', 'Paris', '0-5'),
    ('Atlético de Madrid', 'Galatasaray', '2-0'),
    ('Astana', 'Benfica', '2-2'),
    ('Lyon', 'Gent', '1-2'),
    ('FC Porto', 'Dynamo Kyiv', '0-2'),
    ('Bayern', 'Olympiacos', '4-0'),
    ('Arsenal', 'Dinamo Zagreb', '3-0'),
    ('Barcelona', 'Roma', '6-1'),
    ('BATE Borisov', 'Leverkusen', '1-1'),
    ('Zenit', 'Valencia', '2-0'),
    ('Gent', 'Zenit', '2-1'),
    ('Valencia', 'Lyon', '0-2'),
    ('Dynamo Kyiv', 'Maccabi Tel Aviv', '1-0'),
    ('Chelsea', 'FC Porto', '2-0'),
    ('Olympiacos', 'Arsenal', '0-3'),
    ('Dinamo Zagreb', 'Bayern', '0-2'),
    ('Roma', 'BATE Borisov', '0-0'),
    ('Leverkusen', 'Barcelona', '1-1'),
    ('Man City', 'Mönchengladbach', '4-2'),
    ('Sevilla', 'Juventus', '1-0'),
    ('Benfica', 'Atlético de Madrid', '1-2'),
    ('Galatasaray', 'Astana', '1-1'),
    ('PSV', 'CSKA Moskva', '2-1'),
    ('Wolfsburg', 'Man United', '3-2'),
    ('Paris', 'Shakhtar Donetsk', '2-0'),
    ('Real Madrid', 'Malmö', '8-0')


]
# Insertar datos en la tabla de la fase de grupos
def insert_group_stage_matches(cursor, matches):
    cursor.executemany('''
        INSERT INTO fase_de_grupos (equipo_local, equipo_visitante, resultado_final)
        VALUES (?, ?, ?)
    ''', matches)

# Insert data into 'octavos' table
octavos_matches = [
    (1, 'Barcelona', 'Arsenal', '2-0', '3-1'), 
    (2, 'Bayern', 'Juventus', '2-2', '4-2'), 
    (3, 'Man City', 'Dynamo Kyiv', '3-1', '0-0'), 
    (4, 'Atlético de Madrid', 'PSV', '0-0', '0-0'), 
    (5, 'Chelsea', 'Paris', '1-2', '1-2'),
    (6, 'Zenit', 'Benfica', '0-1', '1-2'), 
    (7, 'Wolfsburg', 'Gent', '3-2', '1-0'), 
    (8, 'Real Madrid', 'Roma', '2-0', '2-0')
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
