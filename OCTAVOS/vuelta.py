import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

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

# Función para aplicar el mapeo a los nombres de los equipos
def unificar_nombres(equipo):
    return mapeo_equipos.get(equipo, equipo)
# Cargar el archivo CSV con la ida y predicciones
df_octavos = pd.read_csv('OCTAVOS/OctavosIda.csv')

# Función para calcular el marcador global
def marcador_global(resultado_ida, resultado_vuelta):
  if resultado_ida > resultado_vuelta:
    return 'Local'
  elif resultado_ida < resultado_vuelta:
    return 'Visitante'
  else:
    return 'Empate'

# Agregar columna con marcador global
df_octavos['marcador_global'] = df_octavos.apply(lambda row: marcador_global(row['resultado_ida'], row['resultado_vuelta_pred']), axis=1)

# Cargar y procesar datos de temporadas anteriores
def cargar_y_procesar_temporada(ruta_archivo):
  df_temp = pd.read_csv(ruta_archivo)
  df_temp['equipo_local'] = df_temp['equipo_local'].apply(unificar_nombres)
  df_temp['equipo_visitante'] = df_temp['equipo_visitante'].apply(unificar_nombres)
  return df_temp

# Lista de rutas de archivos CSV para temporadas anteriores
archivos_temporadas = [
  '13-14/13-14.csv', '14-15/14-15.csv', '15-16/15-16.csv', '16-17/16-17.csv', 
  '17-18/17-18.csv', '18-19/18-19.csv', '19-20/19-20.csv', '20-21/20-21.csv', 
  '21-22/21-22.csv', '22-23/22-23.csv'
]

df_todas_temporadas = pd.concat([cargar_y_procesar_temporada(archivo) for archivo in archivos_temporadas])
df_todas_temporadas.dropna(subset=['resultado_ida', 'equipo_local', 'equipo_visitante'], inplace=True)

# Preparación de los datos para el modelo
X = df_todas_temporadas[['equipo_local', 'equipo_visitante', 'resultado_ida']]
y = df_todas_temporadas['resultado_vuelta']

# División de los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creando el pipeline con OneHotEncoder y RandomForestClassifier
column_transformer = ColumnTransformer([
  ('one_hot', OneHotEncoder(handle_unknown='ignore'), ['equipo_local', 'equipo_visitante'])
], remainder='passthrough')

pipeline = Pipeline([
  ('one_hot_encoder', column_transformer),
  ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Entrenamiento del modelo
pipeline.fit(X_train, y_train)

# Preparando los datos de vuelta para la predicción
X_vuelta = df_octavos[['equipo_local', 'equipo_visitante', 'resultado_ida']]

# Realizando predicciones
predicciones_vuelta = pipeline.predict(X_vuelta)

# Actualizar el DataFrame con las predicciones de vuelta
df_octavos['resultado_vuelta_pred'] = predicciones_vuelta

# Guardar el DataFrame actualizado en un nuevo archivo CSV
df_octavos.to_csv('OCTAVOS/OctavosFinal.csv', index=False)

print("El archivo 'OctavosFinal.csv' ha sido guardado correctamente. Contiene los resultados predichos para la ida y vuelta de los octavos de final.")
