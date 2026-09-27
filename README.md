Objetivo

Determinar la funcionalidad de Matplotlib y Seaborn para el análisis de datos orientado a la toma de decisiones en organizaciones, mediante la elaboración de 10 gráficos (5 por librería) sobre un dataset compartido por el grupo.

Dataset

Archivo: Restaurantes_y_Domicilios_20260912.csv

Registro de 173 establecimientos de expendio de comidas preparadas, con las siguientes columnas:

Columna	Descripción	Tipo
NOMBRE	Nombre comercial del establecimiento	Texto
DIR-COMERCIAL	Dirección comercial	Texto
TELEFONO	Número de contacto (10 dígitos)	Numérico
CIIU-1	Código y categoría CIIU de actividad económica	Categórico
CIIU-4	Descripción libre de la actividad (5 valores nulos)	Texto

Nota de privacidad: el dataset contiene datos de contacto de negocios (registro público de actividad comercial), no de personas naturales. Si este repositorio es público, ten en cuenta que esa información queda accesible.

Estructura del repositorio
.
├── README.md
├── requirements.txt
├── actividad4_visualizacion.py
└── Restaurantes_y_Domicilios_20260912.csv
Requisitos
pandas
numpy
matplotlib
seaborn

Instalación:

bash
pip install -r requirements.txt
Ejecución
bash
python actividad4_visualizacion.py

Aclaración sobre la ruta del archivo: el script fija explícitamente el directorio de trabajo (os.chdir(...)) antes de leer el .csv. Esto es necesario porque, según el equipo desde el que se ejecute, la terminal puede abrirse en una unidad de disco distinta a la del proyecto (por ejemplo, la terminal integrada de VS Code inicia en C:\ mientras el script y el dataset están en D:\Programacion). Si no se especifica la ruta, Python busca el .csv en el directorio equivocado y lanza FileNotFoundError, aunque el archivo esté "en la misma carpeta" a simple vista en el explorador de Windows. Si clonas este repositorio en otra máquina, ajusta esa ruta según la ubicación real de la carpeta del proyecto en tu equipo.

El script:

Carga y limpia el dataset (extrae la categoría CIIU-1, calcula la longitud del nombre comercial y el prefijo telefónico como variables numéricas derivadas).
Genera 5 gráficos con Matplotlib: barras, barras horizontales, pastel, histograma y línea.
Genera 5 gráficos con Seaborn: countplot, boxplot, histplot con densidad, violinplot y heatmap.
Gráficos generados
#	Librería	Tipo de gráfico	Variable(s) analizada(s)
1	Matplotlib	Barras verticales	Conteo por categoría CIIU-1
2	Matplotlib	Barras horizontales	Top 10 descripciones de actividad (CIIU-4)
3	Matplotlib	Pastel	Proporción por categoría CIIU-1
4	Matplotlib	Histograma	Longitud del nombre comercial
5	Matplotlib	Línea	Frecuencia por prefijo telefónico (top 10)
6	Seaborn	Countplot	Conteo por categoría CIIU-1
7	Seaborn	Boxplot	Longitud del nombre según categoría CIIU-1
8	Seaborn	Histplot + KDE	Distribución de longitud del nombre
9	Seaborn	Violinplot	Longitud del nombre según categoría CIIU-1
10	Seaborn	Heatmap	Prefijo telefónico vs categoría CIIU-1
Conclusiones del análisis
El código CIIU predominante corresponde a "Expendio a la mesa de comidas preparadas", concentrando la mayoría de los establecimientos.
La columna CIIU-4 presenta inconsistencias de digitación (mayúsculas/minúsculas, errores ortográficos), lo que evidencia la necesidad de limpieza de texto antes de cualquier análisis agregado.
El dataset no cuenta con variables numéricas continuas nativas; las variables derivadas (longitud de nombre, prefijo telefónico) se construyeron para poder aplicar la variedad de gráficos requerida, y su valor analítico para la toma de decisiones organizacionales es limitado en comparación con variables como ventas, ingresos o ubicación geográfica.
