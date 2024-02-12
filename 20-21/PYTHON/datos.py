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
    ('Zenit', 'Club Brugge', '1-2'),
    ('Dinamo Kiev', 'Juventus', '0-2'),
    ('Chelsea', 'Sevilla', '0-0'),
    ('Rennes', 'Krasnodar', '1-1'),
    ('Lazio', 'Borussia Dortmund', '3-1'),
    ('Barcelona', 'Ferencváros', '5-1'),
    ('PSG', 'Manchester United', '1-2'),
    ('RB Leipzig', 'İstanbul Başakşehir', '2-0'),
    ('Real Madrid', 'Shakhtar Donetsk', '2-3'),
    ('Bayern Múnich', 'Atlético Madrid', '4-0'),
    ('Inter Milan', 'Borussia Mönchengladbach', '2-2'),
    ('Manchester City', 'Porto', '3-1'),
    ('Olympiacos', 'Marsella', '1-0'),
    ('Ajax', 'Liverpool', '0-1'),
    ('Midtjylland', 'Atalanta', '0-4'),
    ('Salzburg', 'Lokomotiv Moscú', '2-2'),
    ('Lokomotiv Moscú', 'Bayern Múnich', '1-2'),
    ('Shakhtar Donetsk', 'Inter Milan', '0-0'),
    ('Atlético Madrid', 'Salzburg', '3-2'),
    ('Borussia Mönchengladbach', 'Real Madrid', '2-2'),
    ('Porto', 'Olympiacos', '2-0'),
    ('Marsella', 'Manchester City', '0-3'),
    ('Liverpool', 'Midtjylland', '2-0'),
    ('Atalanta', 'Ajax', '2-2'),
    ('Krasnodar', 'Chelsea', '0-4'),
    ('İstanbul Başakşehir', 'PSG', '0-2'),
    ('Sevilla', 'Rennes', '1-0'),
    ('Borussia Dortmund', 'Zenit', '2-0'),
    ('Club Brugge', 'Lazio', '1-1'),
    ('Juventus', 'Barcelona', '0-2'),
    ('Ferencváros', 'Dinamo Kiev', '2-2'),
    ('Manchester United', 'RB Leipzig', '5-0'),
     ('Shakhtar Donetsk', 'Borussia Mönchengladbach', '0-6'),
    ('Lokomotiv Moscú', 'Atlético Madrid', '1-1'),
    ('Salzburg', 'Bayern Múnich', '2-6'),
    ('Real Madrid', 'Inter Milan', '3-2'),
    ('Manchester City', 'Olympiacos', '3-0'),
    ('Porto', 'Marsella', '3-0'),
    ('Midtjylland', 'Ajax', '1-2'),
    ('Atalanta', 'Liverpool', '0-5'),
    ('Zenit', 'Lazio', '1-1'),
    ('İstanbul Başakşehir', 'Manchester United', '2-1'),
    ('Barcelona', 'Dinamo Kiev', '2-1'),
    ('Ferencváros', 'Juventus', '1-4'),
    ('Club Brugge', 'Borussia Dortmund', '0-3'),
    ('Sevilla', 'Krasnodar', '3-2'),
    ('Chelsea', 'Rennes', '3-0'),
    ('RB Leipzig', 'PSG', '2-1'),('Borussia Mönchengladbach', 'Shakhtar Donetsk', '4-0'),
    ('Atlético Madrid', 'Lokomotiv Moscú', '0-0'),
    ('Bayern Múnich', 'Salzburg', '3-1'),
    ('Inter Milan', 'Real Madrid', '0-2'),
    ('Olympiacos', 'Manchester City', '0-1'),
    ('Marsella', 'Porto', '0-2'),
    ('Ajax', 'Midtjylland', '3-1'),
    ('Liverpool', 'Atalanta', '0-2'),
    ('Lazio', 'Zenit', '3-1'),
    ('Manchester United', 'İstanbul Başakşehir', '4-1'),
    ('Dinamo Kiev', 'Barcelona', '0-4'),
    ('Juventus', 'Ferencváros', '2-1'),
    ('Borussia Dortmund', 'Club Brugge', '3-0'),
    ('Krasnodar', 'Sevilla', '1-2'),
    ('Rennes', 'Chelsea', '1-2'),
    ('PSG', 'RB Leipzig', '1-0'),

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
db_file_path = '19-20/SQL/champions(19-20).db'
print(db_file_path)
