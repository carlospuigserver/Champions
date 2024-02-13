import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Mapeo de equipos proporcionado
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
    'Bayern': 'Bayern Munich',  # Añadido para considerar variaciones
    'Qarabağ': 'Qarabag',
    'Atlético Madrid': 'Atletico Madrid',
    'Atlético': 'Atletico Madrid', 
    'Spartak Moskva': 'Spartak Moscow',
    'Inter Milan': 'Inter Milan',
    'Inter': 'Inter Milan',
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
}


# Función para aplicar el mapeo a los nombres de los equipos
def unificar_nombres(equipo):
    return mapeo_equipos.get(equipo, equipo)

# Cargar y procesar datos de temporadas anteriores
def cargar_y_procesar_temporada(ruta_archivo):
    df_temp = pd.read_csv(ruta_archivo)
    df_temp['equipo_local'] = df_temp['equipo_local'].apply(unificar_nombres)
    df_temp['equipo_visitante'] = df_temp['equipo_visitante'].apply(unificar_nombres)
    return df_temp

# Lista de rutas de archivos CSV para temporadas anteriores
archivos_temporadas = [
    '13-14/13-14.csv', '14-15/14-15.csv', '15-16/15-16.csv', '16-17/16-17.csv', '17-18/17-18.csv', '18-19/18-19.csv', '19-20/19-20.csv', '20-21/20-21.csv', '21-22/21-22.csv', '22-23/22-23.csv'
]


# Cargar, procesar y concatenar todos los datos de temporadas anteriores
df_todas_temporadas = pd.concat([cargar_y_procesar_temporada(archivo) for archivo in archivos_temporadas])

# Preprocesamiento: Convertir nombres de equipos a valores numéricos
le = LabelEncoder()
df_todas_temporadas['equipo_local_encoded'] = le.fit_transform(df_todas_temporadas['equipo_local'])
df_todas_temporadas['equipo_visitante_encoded'] = le.transform(df_todas_temporadas['equipo_visitante'])

# Asumimos que 'resultado_ida' es la columna objetivo para predecir
df_todas_temporadas['resultado_ida_encoded'] = le.fit_transform(df_todas_temporadas['resultado_ida'])

# Preparación de los datos para el entrenamiento
X = df_todas_temporadas[['equipo_local_encoded', 'equipo_visitante_encoded']]
y = df_todas_temporadas['resultado_ida_encoded']

# División de los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenamiento del modelo RandomForest
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Cargar y procesar datos de la temporada 23-24 para predicción
df_23_24 = cargar_y_procesar_temporada('23-24/23-24.csv')
df_23_24['equipo_local'] = df_23_24['equipo_local'].apply(unificar_nombres)
df_23_24['equipo_visitante'] = df_23_24['equipo_visitante'].apply(unificar_nombres)
df_23_24['equipo_local_encoded'] = le.transform(df_23_24['equipo_local'])
df_23_24['equipo_visitante_encoded'] = le.transform(df_23_24['equipo_visitante'])

X_23_24 = df_23_24[['equipo_local_encoded', 'equipo_visitante_encoded']]


# Realizar predicciones para la temporada 23-24
predicciones_ida_23_24 = modelo.predict(X_23_24)

# Convertir predicciones numéricas a etiquetas legibles
predicciones_ida_23_24 = le.inverse_transform(predicciones_ida_23_24)

# Mostrar predicciones
print("Predicciones de resultados de ida para octavos de final de la temporada 23-24:")
for i, pred in enumerate(predicciones_ida_23_24):
    print(f"Partido {i+1}: Resultado de ida predicho - {pred}")
