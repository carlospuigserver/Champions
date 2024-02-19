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

