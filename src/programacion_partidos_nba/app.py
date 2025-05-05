import streamlit as st
import ObtenerTemporada
import CargarDatos

def main():
    st.title("Programación de Partidos NBA")
    st.subheader("Consulta los partidos de la NBA en tiempo real")
    st.write("Bienvenidos a este proyecto personal el cual tiene como objetivo mostrar información util sore los partidos de la temporada actual de la NBA. Datos como el horario, los equipos que juegan y donde ver.") 
    temporada=ObtenerTemporada.obtener_temporada_actual()
    st.write(f"Temporada actual: {temporada}")
    st.dataframe(CargarDatos.cargar_datos(temporada),hide_index=True,use_container_width=True,
                column_order=['ID del juego','Texto del estado del juego','Fecha','Hora_12h','Fecha y hora formateada','Nombre del equipo local','Nombre del equipo visitante','Canal de TV del equipo local','Canal de TV del equipo visitante'])

if __name__ == "__main__":
    main()