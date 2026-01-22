# EMPLEATRONIX

**Empleatronix** es una aplicación web desarrollada con Streamlit para visualizar y gestionar datos de empleados. Permite analizar la información salarial de forma gráfica e interactiva.

## 📋 Descripción

La aplicación carga los datos de los empleados desde un archivo CSV (`data/employees.csv`) y presenta la información de dos formas principales:
1. **Tabla de datos:** Muestra el listado completo de empleados.
2. **Gráfico de barras:** Visualiza los salarios de los empleados.

## ✨ Características

- **Visualización de datos:** Tabla interactiva con la información de los empleados.
- **Gráfico interactivo:** Gráfico de barras horizontales que compara los salarios.
- **Personalización:**
  - 🎨 **Selector de color:** Permite cambiar el color de las barras del gráfico.
  - 👁️ **Mostrar/Ocultar Nombres:** Opción para visualizar o esconder los nombres en el eje Y.
  - 💰 **Mostrar/Ocultar Sueldos:** Opción para mostrar el valor exacto del salario sobre las barras.

## 🛠️ Tecnologías utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

## 🚀 Cómo ejecutar la aplicación

### Requisitos previos

Asegúrate de tener Python instalado en tu sistema.

### Instalación local

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Alvalogue72/empleatronix_streamlit.git
   cd empleatronix_streamlit
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   streamlit run streamlit_app.py
   ```

### Ejecución con Docker

Si prefieres usar Docker, puedes levantar el servicio utilizando `docker-compose`:

```bash
docker-compose up --build
```

## ✒️ Autor

**Álvaro López Guerrero** - CPIFP Alan Turing
