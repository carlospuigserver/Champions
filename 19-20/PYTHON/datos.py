import sqlite3

# Conectarse a la base de datos nueva con el nombre especificado
conn = sqlite3.connect('19-20/SQL/champions(19-20).db')
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
    ('Inter de Milán', 'Slavia Praga', '1-1'),
    ('Lyon', 'Zenit', '1-1'),
    ('Nápoles', 'Liverpool', '2-0'),
    ('Borussia Dortmund', 'Barcelona', '0-0'),
    ('Chelsea', 'Valencia', '0-1'),
    ('Salzburgo', 'Genk', '6-2'),
    ('Napoli', 'Liverpool', '2-0'),
    ('Ajax', 'Lille', '3-0'),
    ('Benfica', 'RB Leipzig', '1-2'),
    ('Olympiacos', 'Tottenham', '2-2'),
    ('Club Brugge', 'Galatasaray', '0-0'),
    ('PSG', 'Real Madrid', '3-0'),
    ('Shakhtar Donetsk', 'Manchester City', '0-3'),
    ('Atalanta', 'Dinamo Zagreb', '0-4'),
    ('Bayern Munich', 'Estrella Roja', '3-0'),
    ('Leverkusen', 'Lokomotiv Moscú', '1-2'),
     ('Real Madrid', 'Club Brugge', '2-2'),
    ('Atalanta', 'Shakhtar Donetsk', '1-2'),
    ('Manchester City', 'Dinamo Zagreb', '2-0'),
    ('Juventus', 'Bayer Leverkusen', '3-0'),
    ('Lokomotiv Moscú', 'Atlético Madrid', '0-2'),
    ('Tottenham', 'Bayern Múnich', '2-7'),
    ('Galatasaray', 'PSG', '0-1'),
    ('Estrella Roja', 'Olympiacos', '3-1'),
    ('Genk', 'Napoli', '0-0'),
    ('Liverpool', 'Salzburg', '4-3'),
    ('Barcelona', 'Inter Milan', '2-1'),
    ('Slavia Praga', 'Borussia Dortmund', '0-2'),
    ('Zenit', 'Benfica', '3-1'),
    ('Lille', 'Chelsea', '1-2'),
    ('Valencia', 'Ajax', '0-3'),
    ('RB Leipzig', 'Lyon', '0-2'),
    ('Shakhtar Donetsk', 'Dinamo Zagreb', '2-2'),
    ('Atlético Madrid', 'Bayer Leverkusen', '1-0'),
    ('Club Brugge', 'PSG', '0-5'),
    ('Galatasaray', 'Real Madrid', '0-1'),
    ('Tottenham', 'Crvena Zvezda', '5-0'),
    ('Manchester City', 'Atalanta', '5-1'),
    ('Olympiacos', 'Bayern Múnich', '2-3'),
    ('Juventus', 'Lokomotiv Moscú', '2-1'),
    ('Salzburg', 'Napoli', '2-3'),
    ('Genk', 'Liverpool', '1-4'),
    ('Slavia Praga', 'Barcelona', '1-2'),
    ('Inter Milan', 'Borussia Dortmund', '2-0'),
    ('Benfica', 'Lyon', '2-1'),
    ('Lille', 'Valencia', '1-1'),
    ('Ajax', 'Chelsea', '0-1'),
    ('RB Leipzig', 'Zenit', '2-1'),
    ('Dinamo Zagreb', 'Shakhtar Donetsk', '3-3'),
    ('Bayer Leverkusen', 'Atlético Madrid', '2-1'),
    ('PSG', 'Club Brugge', '1-0'),
    ('Real Madrid', 'Galatasaray', '6-0'),
    ('Crvena Zvezda', 'Tottenham', '0-4'),
    ('Atalanta', 'Manchester City', '1-1'),
    ('Bayern Múnich', 'Olympiacos', '2-0'),
    ('Lokomotiv Moscú', 'Juventus', '1-2'),
    ('Napoli', 'Salzburg', '1-1'),
    ('Liverpool', 'Genk', '2-1'),
    ('Barcelona', 'Slavia Praga', '0-0'),
    ('Borussia Dortmund', 'Inter Milan', '3-2'),
    ('Lyon', 'Benfica', '3-1'),
    ('Valencia', 'Lille', '4-1'),
    ('Chelsea', 'Ajax', '4-4'),
    ('Zenit', 'RB Leipzig', '0-2'),
    ('Galatasaray', 'Club Brugge', '1-1'),
    ('Lokomotiv Moscú', 'Bayer Leverkusen', '0-2'),
    ('Real Madrid', 'PSG', '2-2'),
    ('Tottenham', 'Olympiacos', '4-2'),
    ('Manchester City', 'Shakhtar Donetsk', '1-1'),
    ('Juventus', 'Atlético Madrid', '1-0'),
    ('Estrella Roja', 'Bayern Múnich', '0-6'),
    ('Atalanta', 'Dinamo Zagreb', '2-0'),
    ('Valencia', 'Chelsea', '2-2'),
    ('Zenit', 'Lyon', '2-0'),
    ('Liverpool', 'Napoli', '1-1'),
    ('Genk', 'Salzburg', '1-4'),
    ('Barcelona', 'Borussia Dortmund', '3-1'),
    ('Slavia Praga', 'Inter Milan', '1-3'),
    ('RB Leipzig', 'Benfica', '2-2'),
    ('Lille', 'Ajax', '0-2'),
    ('Bayern Múnich', 'Tottenham', '3-1'),
    ('Olympiacos', 'Estrella Roja', '1-0'),
    ('PSG', 'Galatasaray', '5-0'),
    ('Club Brugge', 'Real Madrid', '1-3'),
    ('Atlético Madrid', 'Lokomotiv Moscú', '2-0'),
    ('Bayer Leverkusen', 'Juventus', '0-2'),
    ('Shakhtar Donetsk', 'Atalanta', '0-3'),
    ('Dinamo Zagreb', 'Manchester City', '1-4'),
    ('Ajax', 'Valencia', '0-1'),
    ('Chelsea', 'Lille', '2-1'),
    ('Benfica', 'Zenit', '3-0'),
    ('Lyon', 'RB Leipzig', '2-2'),
    ('Borussia Dortmund', 'Slavia Praga', '2-1'),
    ('Inter Milan', 'Barcelona', '1-2'),
    ('Napoli', 'Genk', '4-0'),
    ('Salzburg', 'Liverpool', '0-2')

]

# Insertar datos en la tabla de la fase de grupos
def insert_group_stage_matches(cursor, matches):
    cursor.executemany('''
        INSERT INTO fase_de_grupos (equipo_local, equipo_visitante, resultado_final)
        VALUES (?, ?, ?)
    ''', matches)

# Insert data into 'octavos' table
octavos_matches = [
    (1, 'Borussia Dortmund', 'PSG', '2-1', '0-2'),
    (2, 'Real Madrid', 'Manchester City', '1-2', '1-2'),
    (3, 'Atalanta', 'Valencia', '4-1', '4-3'),
    (4, 'Atlético Madrid', 'Liverpool', '1-0', '3-2'),
    (5, 'Chelsea', 'Bayern Múnich', '0-3', '1-4'),
    (6, 'Lyon', 'Juventus', '1-0', '1-2'),
    (7, 'Tottenham', 'RB Leipzig', '0-1', '0-3'),
    (8, 'Napoli', 'Barcelona', '1-1', '1-3')
]


# Insert data into 'cuartos' table
cuartos_matches = [
    (1, 'Atalanta', 'PSG', '1-2', None),
    (2, 'RB Leipzig', 'Atlético Madrid', '2-1', None),
    (3, 'Barcelona', 'Bayern Múnich', '2-8', None),
    (4, 'Manchester City', 'Lyon', '1-3', None)
]


# Insert data into 'semis' table
semis_matches = [
    (1, 'RB Leipzig', 'PSG', '0-3', None),
    (2, 'Lyon', 'Bayern Múnich', '0-3', None)
]




# Insert data into 'final' table
final_match = [
    (1, 'PSG', 'Bayern Múnich', '0-1')
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
db_file_path = '19-20/SQL/champions(19-20).db'
print(db_file_path)
