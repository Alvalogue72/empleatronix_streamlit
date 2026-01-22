# EMPLEATRONIX

**Empleatronix** es una aplicación web desarrollada con Streamlit para visualizar y gestionar datos de empleados. Permite analizar la información salarial de forma gráfica e interactiva.

## Descripción

La aplicación carga los datos de los empleados desde un archivo CSV (`data/employees.csv`) y presenta la información de dos formas principales:
1. **Tabla de datos:** Muestra el listado completo de empleados.
2. **Gráfico de barras:** Visualiza los salarios de los empleados.

## Características

- **Visualización de datos:** Tabla interactiva con la información de los empleados.
- **Gráfico interactivo:** Gráfico de barras horizontales que compara los salarios.
- **Personalización:**
  - **Selector de color:** Permite cambiar el color de las barras del gráfico.
  - **Mostrar/Ocultar Nombres:** Opción para visualizar o esconder los nombres en el eje Y.
  - **Mostrar/Ocultar Sueldos:** Opción para mostrar el valor exacto del salario sobre las barras.

## Tecnologías utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

## Instalación y Ejecución

### Ejecución con Docker Compose

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Alvalogue72/empleatronix_streamlit.git
   cd empleatronix_streamlit
   ```

2. **Construir y ejecutar el contenedor:**
   ```bash
   docker-compose up --build
   ```

3. **Acceder a la aplicación:**
   
   Abre tu navegador y navega a:
   ```
   http://localhost:8501
   ```

4. **Detener la aplicación:**
   
   Presiona `Ctrl+C` en la terminal o ejecuta:
   ```bash
   docker-compose down
   ```

## ✒️ Autor

**Álvaro López Guerrero** - CPIFP Alan Turing
