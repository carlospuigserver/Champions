import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import random
import numpy as np


# Función para unificar nombres
def unificar_nombres(df):
    mapeo_equipos = {
    'Man City': 'Manchester City',
    'Paris': 'Paris Saint-Germain',
    'FC Porto': 'Porto',
    'FCSB': 'Steaua Bucharest',
    'CSKA Moskva': 'CSKA Moscow',
    'Shakhtar Donetsk': 'Shakhtar',
    'BATE Borisov': 'BATE',
    'Sporting CP': 'Sporting Lisbon',
    'APOEL': 'APOEL Nicosia',
    'Malmö': 'Malmo FF',
    'Ludogorets': 'Ludogorets Razgrad',
    'Dynamo Kyiv': 'Dynamo Kiev',
    'Olympiacos': 'Olympiakos',
    'Mönchengladbach': 'Borussia Monchengladbach',
    'Galatasaray': 'Galatasaray A.S.',
    'Zenit': 'Zenit Saint Petersburg',
    'Dinamo Zagreb': 'Dinamo Zagreb',
    'Legia': 'Legia Warsaw',
    'Rostov': 'FC Rostov',
    'Beşiktaş': 'Besiktas',
    'Leicester': 'Leicester City',
    'Bayern München': 'Bayern Munich',
    'Bayern': 'Bayern Munich',  
    'Qarabağ': 'Qarabag',
    'Atlético Madrid': 'Atletico Madrid',
    'Atlético': 'Atletico Madrid',
    'Spartak Moskva': 'Spartak Moscow',
    'Inter Milan': 'Inter',
    'Inter': 'Inter',
    'Lyon': 'Olympique Lyonnais',
    'Nápoles': 'Napoli',
    'Salzburgo': 'RB Salzburg',
    'Estrella Roja': 'Red Star Belgrade',
    'Lokomotiv Moscú': 'Lokomotiv Moscow',
    'Genk': 'KRC Genk',
    'Crvena zvezda': 'Red Star Belgrade',
    'RB Leipzig': 'RB Leipzig',
    'Slavia Praga': 'Slavia Prague',
    'Bayer Leverkusen': 'Bayer 04 Leverkusen',
    'Valencia': 'Valencia CF',
    'Chelsea': 'Chelsea FC',
    'Sevilla': 'Sevilla FC',
    'Rennes': 'Stade Rennais FC',
    'Krasnodar': 'FC Krasnodar',
    'İstanbul Başakşehir': 'Istanbul Basaksehir',
    'Marsella': 'Olympique de Marseille',
    'Midtjylland': 'FC Midtjylland',
    'Ferencváros': 'Ferencvarosi TC',
    'Club Brugge': 'Club Brugge KV',
    'Royal Antwerp': 'Royal Antwerp FC',
    'Union Berlin': 'Union Berlin',
    'Newcastle': 'Newcastle United',
    'Feyenoord': 'Feyenoord Rotterdam',
    'Celtic': 'Celtic FC',
    'PSV Eindhoven': 'PSV Eindhoven',
    'Lens': 'RC Lens',
    'Braga': 'SC Braga',
    'Salzburg': 'RB Salzburg',
    'Real Sociedad': 'Real Sociedad',
    'Copenhagen': 'FC Copenhagen',
    # Añadiendo mapeos adicionales para nombres alternativos encontrados en la lista
    'AEK Athens': 'AEK Athens',
    'AFC Ajax': 'Ajax',
    'Ajax': 'Ajax',
    'Anderlecht': 'Anderlecht',
    'Arsenal': 'Arsenal',
    'Astana': 'Astana',
    'Atalanta': 'Atalanta',
    'Athletic Club': 'Athletic Bilbao',  # Asumiendo que es Athletic Bilbao
    'Atletico Madrid': 'Atletico Madrid',
    'Atlético de Madrid': 'Atletico Madrid',
    'Barcelona': 'FC Barcelona',
    'Basel': 'FC Basel',
    'Benfica': 'SL Benfica',
    'Borussia Dortmund': 'Borussia Dortmund',
    'Brugge': 'Club Brugge KV',
    'Maccabi Haifa': 'Maccabi Haifa',
    'Besiktas': 'Besiktas',
    'Schalke': 'FC Schalke 04',
    'Viktoria Plzeň': 'Viktoria Plzen',
    'Dortmund': 'Borussia Dortmund',
    'Maccabi Tel Aviv': 'Maccabi Tel Aviv',
    'Leverkusen': 'Bayer Leverkusen',
    'Liverpool': 'Liverpool',
    'Villarreal': 'Villarreal',
    'Milan': 'Milan',
    'Milán': 'Milan',
    'AC Milan': 'Milan',
    'Tottenham': 'Tottenham Hotspur',
    'Roma': 'AS Roma',
    'Inter de Milán': 'Inter Milan',
    'PSV': 'PSV Eindhoven',
    'PSG': 'Paris Saint-Germain',
    'Maribor': 'NK Maribor',
    'Gent': 'KAA Gent',
    'Manchester City': 'Manchester City',
    'Kobenhavn': 'FC Copenhagen',
    'Lokomotiv Moskva': 'Lokomotiv Moscow',
    'Red Bull Salzburg': 'RB Salzburg',
    'Real Madrid': 'Real Madrid',
    'Schalke 04': 'FC Schalke 04',
    'Napoli': 'SSC Napoli',
    'Liverpool FC': 'Liverpool',
    'Lille': 'Lille OSC',
    'Crvena Zvezda': 'Red Star Belgrade',
    'Olympique de Marseille': 'Olympique Marseille',
    'Tottenham Hotspur': 'Tottenham Hotspur',
    'Borussia Mönchengladbach': 'Borussia Monchengladbach',
    'FC Barcelona': 'FC Barcelona',
    'Porto': 'FC Porto',
    'Rangers': 'Rangers FC',
    'Man United': 'Manchester United',
    'Manchester United': 'Manchester United',
    'Bayern Munich': 'FC Bayern Munich',
    'Dinamo Kiev': 'Dynamo Kyiv',
    'Bayern Múnich': 'FC Bayern Munich',
    'Red Star Belgrade': 'Red Star Belgrade',
    'Sheriff Tiraspol': 'Sheriff Tiraspol',
    'Juventus': 'Juventus FC',
    'Marseille': 'Olympique Marseille',
    'Monaco': 'AS Monaco',
    'Paris Saint-Germain': 'Paris Saint-Germain',
    'Sporting de Portugal': 'Sporting Lisbon',
    'Eintracht Frankfurt': 'Eintracht Frankfurt',
    'Mónaco': 'AS Monaco',
    'Lazio': 'SS Lazio',
    'Austria Wien': 'Austria Vienna',
    'Wolfsburg': 'VfL Wolfsburg',
    'Hoffenheim': 'TSG 1899 Hoffenheim',
    'Young Boys': 'BSC Young Boys',
    # Continuar con el mapeo para el resto de equipos según sea necesario
}
    df['equipo_local'] = df['equipo_local'].apply(lambda x: mapeo_equipos.get(x, x))
    df['equipo_visitante'] = df['equipo_visitante'].apply(lambda x: mapeo_equipos.get(x, x))
    return df

def simular_penaltis():
    return random.choice(['local', 'visitante'])
# Cargar y combinar todos los datos de entrenamiento necesarios
archivos_temporadas = [
    '13-14/13-14.csv', '14-15/14-15.csv', '15-16/15-16.csv', '16-17/16-17.csv', 
    '17-18/17-18.csv', '18-19/18-19.csv', '19-20/19-20.csv', '20-21/20-21.csv', 
    '21-22/21-22.csv', '22-23/22-23.csv'
]

df_todas_temporadas = pd.concat([pd.read_csv(archivo).pipe(unificar_nombres) for archivo in archivos_temporadas])
df_23_24_octavos_ida = pd.read_csv('OCTAVOS/OctavosIda.csv').pipe(unificar_nombres)
df_23_24_octavos_vuelta = pd.read_csv('OCTAVOS/OctavosVuelta.csv').pipe(unificar_nombres)
df_23_24_cuartos_ida = pd.read_csv('CUARTOS/CuartosIdaPredicciones.csv').pipe(unificar_nombres)
df_23_24_cuartos_vuelta = pd.read_csv('CUARTOS/CuartosVuelta.csv').pipe(unificar_nombres)
df_23_24_semis_ida = pd.read_csv('SEMIS/SemisIdaPredicciones.csv').pipe(unificar_nombres)

# Preprocesamiento para eliminar filas con NaN en 'resultado_vuelta'
df_entrenamiento_total = pd.concat([
    df_todas_temporadas, df_23_24_octavos_ida, df_23_24_octavos_vuelta, df_23_24_cuartos_ida, df_23_24_cuartos_vuelta, df_23_24_semis_ida
]).dropna(subset=['resultado_vuelta'])

# Preparar las características (X) y las etiquetas (y) para el entrenamiento
X_total = df_entrenamiento_total[['equipo_local', 'equipo_visitante']]
y_total = df_entrenamiento_total['resultado_vuelta'].astype(str)

# Crear el pipeline con OneHotEncoder y RandomForestClassifier
column_transformer = ColumnTransformer([
    ('one_hot', OneHotEncoder(handle_unknown='ignore'), ['equipo_local', 'equipo_visitante'])
], remainder='passthrough')

pipeline = Pipeline([
    ('one_hot_encoder', column_transformer),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Entrenar el modelo con estos datos
pipeline.fit(X_total, y_total)

# Realizar predicciones para la vuelta de cuartos de final
df_semis_vuelta = df_23_24_semis_ida.copy()  # Asegura trabajar sobre una copia para no modificar el original
X_semis_vuelta = df_semis_vuelta[['equipo_local', 'equipo_visitante']]
predicciones_vuelta_semis = pipeline.predict(X_semis_vuelta)

df_semis_vuelta['resultado_vuelta'] = predicciones_vuelta_semis


ganadores_semis = []

for index, row in df_semis_vuelta.iterrows():
    if row['fase'] == 'semis':
        resultado = row['resultado_vuelta'].split('-')
        local = int(resultado[0])
        visitante = int(resultado[1])
        
        if local > visitante:
            ganador = row['equipo_local']
        elif visitante > local:
            ganador = row['equipo_visitante']
        else:
            ganador_penaltis = simular_penaltis()
            ganador = row['equipo_local'] if ganador_penaltis == 'local' else row['equipo_visitante']
            
        ganadores_semis.append(ganador)

# Ahora que tenemos los ganadores, los mezclamos y creamos los emparejamientos para semifinales
random.shuffle(ganadores_semis)
final = [(ganadores_semis[i], ganadores_semis[i + 1]) for i in range(0, len(ganadores_semis), 2)]

# Creamos el DataFrame de la final
df_final = pd.DataFrame(final, columns=['equipo_local', 'equipo_visitante'])
df_final['fase'] = 'final'
df_final['resultado_ida'] = np.nan
df_final['resultado_vuelta'] = np.nan

# Opcional: Puedes combinar df_cuartos y df_semifinales si necesitas un solo DataFrame
df_combinado = pd.concat([df_semis_vuelta, df_final]).reset_index(drop=True)

# Guardamos el nuevo DataFrame que incluye cuartos actualizados y semifinales
df_combinado.to_csv('SEMIS/SemisVuelta.csv', index=False)

print("Los cuartos actualizados y las semifinales han sido guardados en 'SEMIS/SemisVuelta.csv'.")