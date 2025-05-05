from nba_api.stats.endpoints.scheduleleaguev2 import ScheduleLeagueV2
import pandas as pd
from pytz import timezone

def cargar_datos(temporada):
    #Instancia para obtener los datos de la API
    instancia=ScheduleLeagueV2(season=temporada)
    #Obtenemos los datos de la API
    df=instancia.season_games.get_data_frame()
    #Guardar solo los datos necesarios
    df_juegos = df[['gameId', 'gameStatus','gameStatusText','gameDateTimeUTC','day','monthNum','weekName','arenaName','homeTeam_teamId','homeTeam_teamName','homeTeam_teamCity','homeTeam_teamTricode','homeTeam_wins','homeTeam_losses','homeTeam_score','awayTeam_teamId','awayTeam_teamName','awayTeam_teamCity','awayTeam_teamTricode','awayTeam_wins','awayTeam_losses','awayTeam_score','homeTvBroadcasters_broadcasterDisplay','awayTvBroadcasters_broadcasterDisplay']]
    #Diccionario para traducir
    traducciones = {
    'gameId': 'ID del juego',
    'gameStatus': 'Estado del juego',
    'gameStatusText': 'Texto del estado del juego',
    'gameDateTimeUTC': 'Fecha y hora del juego (UTC)',
    'day': 'Día',
    'monthNum': 'Número del mes',
    'weekName': 'Nombre de la semana',
    'arenaName': 'Nombre del estadio',
    'homeTeam_teamId': 'ID del equipo local',
    'homeTeam_teamCity': 'Ciudad del equipo local',
    'homeTeam_teamName': 'Nombre del equipo local',
    'homeTeam_teamTricode': 'Código corto del equipo local',
    'homeTeam_wins': 'Victorias del equipo local',
    'homeTeam_losses': 'Derrotas del equipo local',
    'homeTeam_score': 'Puntaje del equipo local',
    'awayTeam_teamId': 'ID del equipo visitante',
    'awayTeam_teamName': 'Nombre del equipo visitante',
    'awayTeam_teamCity': 'Ciudad del equipo visitante',
    'awayTeam_teamTricode': 'Código corto del equipo visitante',
    'awayTeam_wins': 'Victorias del equipo visitante',
    'awayTeam_losses': 'Derrotas del equipo visitante',
    'awayTeam_score': 'Puntaje del equipo visitante',
    'homeTvBroadcasters_broadcasterDisplay': 'Canal de TV del equipo local',
    'awayTvBroadcasters_broadcasterDisplay': 'Canal de TV del equipo visitante'
    }
    #Renombrar las columnas del DataFrame
    df_juegos.rename(columns=traducciones,inplace=True)
    #Cambiar el formato de la fecha y hora para mostrar en formato UTC-5
    df_juegos['Fecha y hora del juego (UTC)']= pd.to_datetime(df_juegos['Fecha y hora del juego (UTC)'])
    df_juegos['Fecha'] = df_juegos['Fecha y hora del juego (UTC)'].dt.tz_convert('America/Lima').dt.date
    df_juegos['Hora_12h'] = df_juegos['Fecha y hora del juego (UTC)'].dt.tz_convert('America/Lima').dt.strftime('%I:%M %p')    #df_juegos['Fecha_local UTC-5'] = df_juegos['Fecha_local'].dt.strftime('%d/%m/%Y %I:%M:%S %p')

    return df_juegos
    #Retornar el DataFrame
