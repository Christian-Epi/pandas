#Vamos a importar la biblioteca Pandas y la llamamos pd
import pandas as pd

# Creamos una serie de pandas usando una lista
psg_players = pd.Series(
    ['Navas', 'Mbappe', 'Neymar', 'Messi'], # Lista de jugadores
    )

# Creamos un diccionario que asocia el numero de la camiseta con el nombre del jugador
psg_dict = { 1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi'}

# Creamos una serie de pandas usando el diccionario
psg_players_dict = pd.Series(psg_dict)

# Imprimimos la serie de pandas creada con el diccionario
print(psg_players_dict)

# Imprimimos el nombre del jugador con la camiseta 7
print(psg_players_dict[7])
print(psg_players_dict[0:3])

# Diccionario con datos de jugadores
dict_jugadores = {'Jugador': ['Navas', 'Mbappe', 'Neymar', 'Messi'],
                  'Altura': [1.91, 1.95, 1.78, 1.93],
                  'goles': [2, 200, 150, 300]}

# Creamos un dataframe de pandas con el diccionario e indices personalizados
df = pd.DataFrame(dict_jugadores, index=[1, 7, 10, 30])

# Imprimimos el dataframe
print(df)