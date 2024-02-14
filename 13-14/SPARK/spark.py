from pyspark.sql import SparkSession

# Inicializar SparkSession
spark = SparkSession.builder.appName("13-14").getOrCreate()

# Ruta al archivo CSV
csv_file_path = '13-14/13-14.csv'  # Asegúrate de cambiar esta ruta a la ubicación actual de tu archivo

# Cargar el CSV en un DataFrame de Spark
spark_df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

# Para mostrar el esquema del DataFrame
spark_df.printSchema()

# Para ver las primeras filas del DataFrame y confirmar que los datos se han cargado correctamente
spark_df.show()
