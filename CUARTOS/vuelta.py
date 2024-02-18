import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Asumiendo que el mapeo de equipos ya está definido en mapeo_equipos
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

# Función para simular una tanda de penaltis y decidir el ganador
def simular_penaltis():
    return random.choice(['local', 'visitante'])

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
df_todas_temporadas.dropna(subset=['resultado_vuelta', 'equipo_local', 'equipo_visitante'], inplace=True)

# Cargando los datos específicos de la temporada 23-24
ruta_archivo_23_24 = 'OCTAVOS/OctavosIda.csv'
df_23_24 = pd.read_csv(ruta_archivo_23_24)
df_23_24['equipo_local'] = df_23_24['equipo_local'].apply(unificar_nombres)
df_23_24['equipo_visitante'] = df_23_24['equipo_visitante'].apply(unificar_nombres)

# Filtrando para octavos de final de la temporada 23-24
df_23_24_octavos = df_23_24[df_23_24['fase'] == 'octavos']

# Preparación de los datos para el modelo
X = df_todas_temporadas[['equipo_local', 'equipo_visitante']]
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

# Preparando los datos de octavos para la predicción
X_23_24_octavos = df_23_24_octavos[['equipo_local', 'equipo_visitante']]

# Realizando predicciones
predicciones_vuelta_23_24 = pipeline.predict(X_23_24_octavos)

# Crear un DataFrame temporal para las predicciones
df_predicciones = pd.DataFrame({
    'id_partido': df_23_24_octavos['id_partido'].values,
    'resultado_vuelta_pred': predicciones_vuelta_23_24
})

# Fusionar el DataFrame original de la temporada 23-24 con las predicciones
df_23_24 = pd.merge(df_23_24, df_predicciones, on='id_partido', how='left')

# Actualizar solo las filas de los octavos de final con las predicciones de 'resultado_vuelta'
df_23_24.loc[df_23_24['fase'] == 'octavos', 'resultado_vuelta'] = df_23_24.loc[df_23_24['fase'] == 'octavos', 'resultado_vuelta_pred']

# Eliminar la columna temporal de predicciones
df_23_24.drop(columns=['resultado_vuelta_pred'], inplace=True)

# Aquí inicia la nueva sección para simular los cuartos de final
clasificados = []
for _, row in df_23_24.iterrows():
    if row['fase'] == 'octavos':
        local, visitante = map(int, row['resultado_vuelta'].split('-'))
        if local > visitante:
            clasificados.append(row['equipo_local'])
        elif visitante > local:
            clasificados.append(row['equipo_visitante'])
        else:  # Empate, decidir por penaltis
            ganador_penaltis = simular_penaltis()
            if ganador_penaltis == 'local':
                clasificados.append(row['equipo_local'])
            else:
                clasificados.append(row['equipo_visitante'])

random.shuffle(clasificados)
cruces_cuartos = [(clasificados[i], clasificados[i+1]) for i in range(0, len(clasificados), 2)]

# Añadir los cruces de cuartos al DataFrame original
for local, visitante in cruces_cuartos:
    nuevo_registro = pd.Series({'equipo_local': local, 'equipo_visitante': visitante, 'fase': 'cuartos', 'resultado_vuelta': np.nan})
    df_23_24 = df_23_24._append(nuevo_registro, ignore_index=True)

# Guardar el DataFrame actualizado en un nuevo archivo CSV
df_23_24.to_csv('OCTAVOS/OctavosVuelta.csv', index=False)





# Ahora, cargamos el DataFrame actualizado para trabajar con los cruces de cuartos de final
df_cuartos_actualizado = pd.read_csv('OCTAVOS/OctavosVuelta.csv')

# Filtramos solo las filas correspondientes a los cuartos de final
df_cuartos = df_cuartos_actualizado[df_cuartos_actualizado['fase'] == 'cuartos'].reset_index(drop=True)

# Preparamos los datos para la predicción de la ida de cuartos
X_cuartos_ida = df_cuartos[['equipo_local', 'equipo_visitante']]

# Realizamos las predicciones de la ida de los cuartos de final
predicciones_ida_cuartos = pipeline.predict(X_cuartos_ida)

# Creamos un DataFrame para las predicciones de la ida de cuartos
df_predicciones_ida_cuartos = pd.DataFrame({
    'equipo_local': df_cuartos['equipo_local'],
    'equipo_visitante': df_cuartos['equipo_visitante'],
    'resultado_ida_pred': predicciones_ida_cuartos
})

# Mostramos las predicciones para la ida de los cuartos de final
print(df_predicciones_ida_cuartos)

# Si deseas actualizar el DataFrame original con estas predicciones:
df_cuartos_actualizado = pd.merge(df_cuartos_actualizado, df_predicciones_ida_cuartos, on=['equipo_local', 'equipo_visitante'], how='left')

# Para aquellos partidos en la fase de cuartos, actualizamos 'resultado_ida' con las predicciones
df_cuartos_actualizado.loc[df_cuartos_actualizado['fase'] == 'cuartos', 'resultado_ida'] = df_cuartos_actualizado.loc[df_cuartos_actualizado['fase'] == 'cuartos', 'resultado_ida_pred']

# Eliminamos la columna de predicciones temporales
df_cuartos_actualizado.drop(columns=['resultado_ida_pred'], inplace=True)

# Guardamos el DataFrame actualizado en un nuevo archivo CSV
df_cuartos_actualizado.to_csv('CUARTOS/CuartosIdaPredicciones.csv', index=False)

print("Las predicciones para la ida de los cuartos de final han sido guardadas en 'CUARTOS/CuartosIdaPredicciones.csv'.")


#ahora, cargamos el DataFrame actualizado para trabajar con los cruces de cuartos de final
df_cuartos_actualizado = pd.read_csv('CUARTOS/CuartosIdaPredicciones.csv')

#filtramos solo las filas correspondientes a los cuartos de final
df_cuartos = df_cuartos_actualizado[df_cuartos_actualizado['fase'] == 'cuartos'].reset_index(drop=True)

#preparamos los datos para la predicción de la vuelta de cuartos
X_cuartos_vuelta = df_cuartos[['equipo_local', 'equipo_visitante']]
y_cuartos_vuelta = df_cuartos['resultado_vuelta']

#realizamos las predicciones de la vuelta de los cuartos de final
predicciones_vuelta_cuartos = pipeline.predict(X_cuartos_vuelta)

#creamos un DataFrame para las predicciones de la vuelta de cuartos

df_predicciones_vuelta_cuartos = pd.DataFrame({
    'equipo_local': df_cuartos['equipo_local'],
    'equipo_visitante': df_cuartos['equipo_visitante'],
    'resultado_vuelta_pred': predicciones_vuelta_cuartos
})

#mostramos las predicciones para la vuelta de los cuartos de final
print(df_predicciones_vuelta_cuartos)

#si deseas actualizar el DataFrame original con estas predicciones:
df_cuartos_actualizado = pd.merge(df_cuartos_actualizado, df_predicciones_vuelta_cuartos, on=['equipo_local', 'equipo_visitante'], how='left')

#para aquellos partidos en la fase de cuartos, actualizamos 'resultado_vuelta' con las predicciones
df_cuartos_actualizado.loc[df_cuartos_actualizado['fase'] == 'cuartos', 'resultado_vuelta'] = df_cuartos_actualizado.loc[df_cuartos_actualizado['fase'] == 'cuartos', 'resultado_vuelta_pred']

#eliminamos la columna de predicciones temporales
df_cuartos_actualizado.drop(columns=['resultado_vuelta_pred'], inplace=True)

#guardamos el DataFrame actualizado en un nuevo archivo CSV
df_cuartos_actualizado.to_csv('CUARTOS/CuartosVueltaPredicciones.csv', index=False)

