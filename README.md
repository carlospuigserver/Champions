# PRIMERA ENTREGA CHAMPIONS

## LINK
El link de este repositorio es el siguiente: [GitHub](https://github.com/carlospuigserver/Champions.git)


## REQUERIMENTS
Existe un archivo requieriments.txt el cual contiene todo lo que se debe instalar previamente a poder usar el modelo, tan sencillo como en el mismo archivo ejecutar el siguiente comando en terminal, y todo será instalado: pip install -r requirements.txt

## BASE DE DATOS
Para esta primera entrega, he decidido realizar una base de datos con las temporadas de la 13-14 a la 22-23 completas, y la fase de grupos de la 23-24. cada temporada tiene una carpeta con su csv, una carpeta llamada Python, y otra SQL. En la carpeta Python, hay un codigo que crea la base de datos, donde cada tabla es una fase del torneo, y otro codigo que pasa esa base de datos al csv. Los csv de cada temporada tienen las siguientes columnas: id_partido,equipo_local,equipo_visitante,resultado_final,fase,resultado_ida,resultado_vuelta
Ahora proporcionaré un ejemplo con la temporada 13-14 para entender por completo la estructura de las carpetas de la base de datos: 

### datos.py ( crear la base de datos.db): 
![codeuno](https://github.com/carlospuigserver/Champions/assets/91721643/7be059d3-7ad9-45ff-b45b-e96351b685e3)





### pasar_a_csv.py ( conseguir el csv a partir de la base de datos creada):

![codedos](https://github.com/carlospuigserver/Champions/assets/91721643/4945727e-c901-4908-9789-6a52093fbd6d)


Y así con todas las temporadas de la 13-14 a la 23-24, cabe destacar que se ha creado una base de datos y un csv para mejorar la comprension y estructura de los datos de dichas temporadas.




## PREDICCIONES



### Preparación de Datos y Mapeo de Nombres:
El proceso comienza con la definición de una función unificar_nombres(df), que estandariza los nombres de los equipos en los datos. Esta función utiliza un diccionario para mapear variantes de nombres de equipos a un nombre estándar y uniforme. Este paso es crucial para asegurar que los datos sean consistentes y que no haya discrepancias debidas a diferentes denominaciones o errores tipográficos de los nombres de los equipos. Al aplicar esta función a los conjuntos de datos cargados, se garantiza que todos los registros utilicen los mismos nombres para los equipos, lo que es fundamental para el análisis posterior.

### Carga y Combinación de Datos de Temporadas Anteriores: 
Se cargan los datos de múltiples temporadas anteriores desde archivos CSV, aplicando la función de mapeo de nombres a cada uno para asegurar la consistencia en los nombres de los equipos. Estos datos se combinan en un único DataFrame, df_todas_temporadas, que reúne la información histórica necesaria para entrenar el modelo de aprendizaje automático. Este paso es vital para construir un conjunto de datos amplio y representativo que refleje las variaciones y tendencias a lo largo de varias temporadas, mejorando así la capacidad predictiva del modelo.

### Preprocesamiento y Preparación de Características para el Entrenamiento: 
Tras combinar los datos de diferentes temporadas y fases, se realiza un preprocesamiento para eliminar filas con valores faltantes en la columna resultado_vuelta, asegurando que solo se utilicen datos completos para el entrenamiento. Luego, se preparan las características (X) y las etiquetas (y) necesarias para el modelo. Las características incluyen los equipos locales y visitantes, mientras que las etiquetas son los resultados de los partidos. Este paso es fundamental para definir claramente los inputs y outputs del modelo.

### Entrenamiento del Modelo: 
Se crea un pipeline que incluye un ColumnTransformer con un OneHotEncoder para transformar las características categóricas (nombres de los equipos) en un formato numérico que pueda ser procesado por el modelo, y un RandomForestClassifier como el algoritmo de aprendizaje automático para realizar las predicciones. Este pipeline permite una transformación eficiente de los datos y facilita el entrenamiento del modelo utilizando el conjunto de datos preparado. El modelo se entrena con datos históricos, aprendiendo patrones y relaciones entre los equipos y los resultados de los partidos.

### Predicción de Resultados de Partidos y Análisis Posterior: 
Una vez entrenado el modelo, se utiliza para predecir los resultados de partidos de fases posteriores no incluidas en el entrenamiento, como cuartos de final, semifinales o la final, dependiendo del conjunto de datos específico en uso. Se generan predicciones para los resultados de estos partidos, y luego, basándose en estos resultados, se determinan los ganadores. En algunos casos, si el resultado predicho indica un empate, se simula una decisión por penaltis utilizando una función que elige aleatoriamente entre el equipo local y visitante como ganador. Este enfoque simula la incertidumbre y la naturaleza impredecible de los resultados de los partidos en situaciones de empate.

### Preparación para Fases Siguientes y Salida Final: 
Basándose en los ganadores determinados, se procede a mezclar y emparejar los equipos para las siguientes fases del torneo, creando nuevas predicciones y avanzando en la simulación hasta llegar a la final. Finalmente, se combina toda la información actualizada en un nuevo DataFrame y se guarda en un archivo CSV, proporcionando un registro completo de los partidos simulados, incluyendo predicciones de resultados y los equipos que avanzan a cada ronda.

Este proceso destaca el uso de técnicas de ciencia de datos y aprendizaje automático para simular y predecir los resultados de competiciones deportivas, basándose en datos históricos y aplicando métodos estadísticos y de modelado predictivo.



Ahora enseñaremos un codigo de ejemplo, este es el que se ha usado para predecir la final: 

![codefinal](https://github.com/carlospuigserver/Champions/assets/91721643/c3c652f2-0796-425d-8383-f6a901eb51c0)



## PRESENTACIÓN DE LOS RESULTADOS

En las carpetas OCTAVOS, CUARTOS, SEMIS Y FINAL, están todos los csv actualizados de cada fase de cada ronda, pero por comodidad, los he juntado todos en un csv en la carpeta PREDICCIONES, exixtiendo en dicha carpeta otra carpeta CSV, en la cual estan todas las rondas por separado para una mejor lectura, y en la misma carpeta PREDICCIONES, hay una carpeta SQL, donde he creado una base de datos.db con todas las fases 23-24 predichas para una mejor visión y facilidad de comprensión, ya que ir mirando los CSV de todas las carpetas puede ser lioso. Ahora voy a adjuntar un ejemplo de como se ve los octavos de final predichos en la base de datos: 


<img width="779" alt="image" src="https://github.com/carlospuigserver/Champions/assets/91721643/c003e36f-4ff1-4436-aa0f-f0b52f67d46a">





## PRECISIÓN DEL MODELO

En el archivo FINAL, donde se hace la predicción cargando todas las rondas anteriores, hay un codigo que indica la precisión del modelo en ese punto, a continuación muestro el código empleado y los resultados:

![codepred](https://github.com/carlospuigserver/Champions/assets/91721643/eb3ae4b2-712a-4a18-a743-0daf38c65b8b)


<img width="449" alt="image" src="https://github.com/carlospuigserver/Champions/assets/91721643/3d179f54-efdc-4c42-9e0c-a30cc0570f10">




## CONCLUSIONES

Se que no es el mejor modelo, pero como prueba de toma de contacto con modelos de ML, y una introducción a la IA, me parece que puede ser salvable. He mejorado bastante la precisión, ya que en los últimos días he conseguido subir de un 3.5% a un 50%. Se de sobra que la base de datos es muy pobre, pero ha bastado para por lo menos sacar una base de datos con la predicción de los resultados de la Champions 23-24 coherente.
