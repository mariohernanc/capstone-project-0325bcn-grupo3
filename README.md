# DSMarket - Análisis de Retail y Forecasting

Este proyecto implementa un análisis completo de datos de retail para una cadena de 10 tiendas, incluyendo clustering de tiendas e items, y modelos de forecasting para predicción de ventas.

## 📋 Descripción del Proyecto

El proyecto DSMarket analiza datos históricos de ventas de una cadena retail para:
- Segmentar tiendas según patrones de comportamiento
- Clasificar productos en clusters similares
- Predecir ventas futuras usando modelos de machine learning

## 🗂️ Estructura del Proyecto

```
02_notebooks/
├── 01_DSMarket_data_preparation.ipynb
├── 02_DSMarket_Clustering.ipynb
└── 03_DSMarket_forecasting.ipynb
```

## 📚 Notebooks

### 1. `01_DSMarket_data_preparation.ipynb`
**Preparación y Limpieza de Datos**

- Carga y exploración de datasets originales
- Limpieza y transformación de datos
- Ingeniería de features para análisis posterior
- Creación de variables derivadas (event_binary, métricas agregadas)
- Preparación de datos para clustering y forecasting

**Outputs principales:**
- Datasets limpios y estructurados

### 2. `02_DSMarket_Clustering.ipynb`
**Análisis de Clustering**

#### Clustering de Tiendas
Segmentación de las 10 tiendas en 4 clusters:

- **Cluster 0 - "Tiendas Irregulares"**: 1 tienda con comportamiento atípico y alta variabilidad
- **Cluster 1 - "Tiendas Estables"**: 6 tiendas estables, base del negocio (60% de la red)
- **Cluster 2 - "Tiendas Premium"**: 1 tienda estelar con máximo rendimiento
- **Cluster 3 - "Tiendas Bajo Renidimiento"**: 2 tiendas con potencial de mejora

#### Clustering de Items
Segmentación de productos por patrones de venta y características.

**Métricas clave analizadas:**
- `mean_sales`: Ventas promedio por período
- `total_sales`: Volumen acumulado
- `cv_revenue`: Coeficiente de variación de ingresos
- `mean_revenue`: Ingresos promedio

### 3. `03_DSMarket_forecasting.ipynb`
**Modelos de Predicción**

- Preparación de features para forecasting
- Implementación de modelo XGBoost para predicción de ventas
- Evaluación de performance con métricas RMSE
- Generación de predicciones futuras
- Análisis de resultados por segmentos

**Características del modelo:**
- Variables predictoras: item, category, department, store_code, region, yearweek, event
- Variable objetivo: n_sales (número de ventas)
- Predicciones redondeadas a enteros para interpretación práctica

## 🔧 Tecnologías Utilizadas

- **Python**: lenguaje de programacion
- **Pandas**: Manipulación de datos
- **NumPy**: Cálculos numéricos
- **Scikit-learn**: Clustering y preprocessing
- **XGBoost**: Modelo de forecasting
- **Matplotlib/Seaborn**: Visualizaciones
- **Jupyter Notebook**: Desarrollo interactivo

## 📊 Resultados Principales

### Segmentación de Tiendas
- **Core Business (60%)**: Tiendas estables y predecibles
- **Flagship Store (10%)**: Modelo de excelencia a replicar
- **En Desarrollo (20%)**: Oportunidades de mejora identificadas
- **Ubicación Especial (10%)**: Caso único a analizar

### Modelo de Forecasting
- Predicciones de ventas con granularidad semanal
- Evaluación por segmentos de tienda
- Identificación de patrones estacionales y de eventos

## 🚀 Cómo Ejecutar

1. **Clonar el repositorio**
```bash
git clone [url-del-repositorio]
cd capstone-project-0325bcn-grupo3
```

2. **Instalar dependencias**
```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn jupyter
```

3. **Ejecutar notebooks en orden**
```bash
notebook 02_notebooks/01_DSMarket_data_preparation.ipynb
notebook 02_notebooks/02_DSMarket_Clustering.ipynb
notebook 02_notebooks/03_DSMarket_forecasting.ipynb
```

## 📈 Casos de Uso

- **Gestión de Inventario**: Predicciones de demanda por tienda
- **Estrategia Comercial**: Segmentación para estrategias diferenciadas
- **Optimización de Recursos**: Identificar tiendas de alto/bajo rendimiento
- **Planificación de Eventos**: Impacto de promociones en ventas

## 👥 Contribuidores

Proyecto desarrollado como parte del programa de Data Science.

## 📝 Notas Técnicas

- Los datos han sido procesados manteniendo la confidencialidad
- Las predicciones están optimizadas para interpretación empresarial
- El modelo considera efectos estacionales y de eventos especiales
