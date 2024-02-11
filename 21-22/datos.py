import sqlite3

# Conectarse a la base de datos nueva con el nombre especificado
conn = sqlite3.connect('21-22/champions(21-22).db')
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
    ('Inter', 'Real Madrid', '0-1'),
    ('Borussia Dortmund', 'Sporting de Portugal', '1-0'),
    ('Milan', 'Atlético de Madrid', '1-2'),
    ('Porto', 'Liverpool', '1-5'),
    ('RB Leipzig', 'Brugge', '1-2'),
    ('PSG', 'Manchester City', '2-0'),
    ('Shakhtar Donetsk', 'Inter', '0-0'),
    ('Real Madrid', 'Sheriff Tiraspol', '1-2'),
    ('Juventus', 'Chelsea', '1-0'),
    ('Red Bull Salzburg', 'Lille', '2-1'),
    ('Atalanta', 'Young Boys', '1-0'),
    ('Wolfsburg', 'Sevilla', '1-1'),
    ('Manchester United', 'Villarreal', '2-1'),
    ('Benfica', 'Barcelona', '3-0'),
    ('Bayern München', 'Dynamo Kyiv', '5-0'),
    ('Zenit', 'Malmö', '4-0'),
    ('Atlético de Madrid', 'Liverpool', '2-3'),
    ('Inter', 'Sheriff Tiraspol', '3-1'),
    ('Shakhtar Donetsk', 'Real Madrid', '0-5'),
    ('Brugge', 'Manchester City', '1-5'),
    ('Beşiktaş', 'Sporting de Portugal', '1-4'),
    ('PSG', 'RB Leipzig', '3-2'),
    ('Porto', 'Milan', '1-0'),
    ('Ajax', 'Borussia Dortmund', '4-0'),
    ('Manchester United', 'Atalanta', '3-2'),
    ('Zenit', 'Juventus', '0-1'),
    ('Chelsea', 'Malmö', '4-0'),
    ('Lille', 'Sevilla', '0-0'),
    ('Young Boys', 'Villarreal', '1-4'),
    ('Benfica', 'Bayern München', '0-4'),
    ('Red Bull Salzburg', 'Wolfsburg', '3-1'),
    ('Barcelona', 'Dynamo Kyiv', '1-0'),
    ('Juventus', 'Zenit', '4-2'),
    ('Dynamo Kyiv', 'Barcelona', '0-1'),
    ('Atalanta', 'Manchester United', '2-2'),
    ('Villarreal', 'Young Boys', '2-0'),
    ('Bayern München', 'Benfica', '5-2'),
    ('Sevilla', 'Lille', '1-2'),
    ('Malmö', 'Chelsea', '0-1'),
    ('Wolfsburg', 'Red Bull Salzburg', '2-1'),
    ('Borussia Dortmund', 'Ajax', '1-3'),
    ('Sporting de Portugal', 'Beşiktaş', '4-0'),
    ('Liverpool', 'Atlético de Madrid', '2-0'),
    ('RB Leipzig', 'PSG', '2-2'),
    ('Manchester City', 'Brugge', '4-1'),
    ('Real Madrid', 'Shakhtar Donetsk', '2-1'),
    ('Milan', 'Porto', '1-1'),
    ('Sheriff Tiraspol', 'Inter', '1-3'),
    ('Lille', 'Red Bull Salzburg', '1-0'),
    ('Sevilla', 'Wolfsburg', '2-0'),
    ('Malmö', 'Zenit', '1-1'),
    ('Villarreal', 'Manchester United', '0-2'),
    ('Barcelona', 'Benfica', '0-0'),
    ('Chelsea', 'Juventus', '4-0'),
    ('Young Boys', 'Atalanta', '3-3'),
    ('Dynamo Kyiv', 'Bayern München', '1-2'),
    ('Inter', 'Shakhtar Donetsk', '2-0'),
    ('Sporting de Portugal', 'Borussia Dortmund', '3-1'),
    ('Beşiktaş', 'Ajax', '1-2'),
    ('Sheriff Tiraspol', 'Real Madrid', '0-3'),
    ('Brugge', 'RB Leipzig', '0-5'),
    ('Manchester City', 'PSG', '2-1'),
    ('Liverpool', 'Porto', '2-0'),
    ('Atlético de Madrid', 'Milan', '0-1'),
    ('Porto', 'Atlético de Madrid', '1-3'),
    ('RB Leipzig', 'Manchester City', '2-1'),
    ('Milan', 'Liverpool', '1-2'),
    ('PSG', 'Brugge', '4-1'),
    ('Borussia Dortmund', 'Beşiktaş', '5-0'),
    ('Shakhtar Donetsk', 'Sheriff Tiraspol', '1-1'),
    ('Real Madrid', 'Inter', '2-0'),
    ('Ajax', 'Sporting de Portugal', '4-2'),
    ('Manchester United', 'Young Boys', '1-1'),
    ('Red Bull Salzburg', 'Sevilla', '1-0'),
    ('Wolfsburg', 'Lille', '1-3'),
    ('Juventus', 'Malmö', '1-0'),
    ('Zenit', 'Chelsea', '3-3'),
    ('Benfica', 'Dynamo Kyiv', '2-0'),
    ('Bayern München', 'Barcelona', '3-0'),
    ('Atalanta', 'Villarreal', '2-3')

]
# Insertar datos en la tabla de la fase de grupos
def insert_group_stage_matches(cursor, matches):
    cursor.executemany('''
        INSERT INTO fase_de_grupos (equipo_local, equipo_visitante, resultado_final)
        VALUES (?, ?, ?)
    ''', matches)

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

# Insert data into 'cuartos' table
cuartos_matches = [
    (1, 'Benfica', 'Liverpool', '1-3', '3-3'),
    (2, 'Villarreal', 'Bayern München', '1-0', '1-1'),
    (3, 'Manchester City', 'Atlético Madrid', '1-0', '0-0'),
    (4, 'Chelsea', 'Real Madrid', '1-3', '2-3')
]


# Insert data into 'semis' table
semis_matches = [
    (1, 'Villarreal', 'Liverpool', '2-3', '0-2'),
    (2, 'Manchester City', 'Real Madrid', '4-3', '1-3')
]

# Insert data into 'final' table
final_match = [
    (1, 'Liverpool', 'Real Madrid', '0-1')
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
db_file_path = '21-22/champions(21-22).db'
print(db_file_path)
