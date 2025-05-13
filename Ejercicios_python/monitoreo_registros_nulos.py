"""PROGRAMA PARA LA EVALUACION DE NULOS EN DATOS """
# Importacion de librerias
import random

# Diccionario de datos del usuario
datos_complejos = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'nombre': ['Alice', 'Bob', None, 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy', 'Kelly', 'Liam', 'Mia', 'Noah'],
    'edad': [25, '30', 42, None, 35, 28, '48', 22.5, 19, None, 31, '27', 38, 24, None],
    'ciudad': ['New York', 'London', 'Paris', 'Tokyo', None, 'Sydney', 'Berlin', 'Rome', 'Moscow', 'Beijing', 'Seoul', 'Madrid', None, 'Toronto', 'Rio'],
    'puntuacion': [8.5, 9.2, None, 7.8, 6.5, 8.9, None, 9.1, 7.3, 8.0, 9.5, 7.0, 8.8, None, 6.9],
    'activo': [True, False, True, None, False, True, False, True, True, False, True, False, True, None, False],
    'ultima_conexion': ['2024-01-15', None, '2023-11-20', '2024-03-01', '2023/12/10', None, 'ayer', '2024-02-25', 'hace 2 días', None, '2024-04-05', 'semana pasada', None, '2024-01-30', 'hoy'],
    'hobbies': [['leer', 'correr'], ['pintar'], None, ['programar', 'música'], ['viajar'], ['cocinar', None], ['senderismo'], ['fotografía'], ['jugar'], None, ['bailar'], ['escribir'], None, ['nadar'], ['ciclismo', 'escalar']],
    'datos_extra': [{'a': 1, 'b': None}, {'c': 3}, None, {'d': 4, 'e': 5}, {'f': None}, {'g': 7}, {'h': 8}, {'i': None, 'j': 10}, {'k': 11}, None, {'l': 12}, {'m': 13}, None, {'n': 14}, {'o': None}],
    'es_premium': [True, False, None, False, True, False, True, False, True, None, False, True, False, None, True],
    'cantidad_compras': [10, None, 5, 12, 8, None, 15, 7, 9, None, 11, 6, None, 14, 3],
    'promedio_gasto': [150.50, None, 75.20, 210.00, 90.80, None, 180.30, 110.75, 135.90, None, 165.40, 85.15, None, 200.00, 55.60],
    'direccion': ['Calle A', None, 'Avenida B', 'Calle C', 'Avenida D', None, 'Calle E', 'Avenida F', 'Calle G', None, 'Avenida H', 'Calle I', None, 'Avenida J', 'Calle K'],
    'nota': ['Excelente', None, 'Bueno', 'Muy bien', 'Satisfactorio', None, 'Impresionante', 'Aceptable', 'Notable', None, 'Sobresaliente', 'Regular', None, 'Asombroso', 'Flojo'],
    'valor_especial': [None, 0, None, 'abc', None, True, None, [1, 2], None, {'key': None}, None, (3, 4), None, False, None]
}

# Lista de datos columnares
orden_columnas = ('id', 'nombre', 'edad', 'ciudad', 'puntuacion',
                  'activo','ultimo_conexion', 'hobbies', 'dato_extra'
                  'es_premium', 'cantidad_compras','promedio_gasto', 'direccion', 'nota', 'valor_especial')

if __name__ == "__main__":
  "Tratamiento de datos complejos"
  menu()
