import os
from PIL import Image

def listar_formatos_soportados():
'''Muestra los formatos de imagen soportados '''
  formatos = ["JPG", "JPEG", "PNG", "GIF", "BMP", "TIFF", "WEBP"]
  print("Formatos soportados")
  for formato in formatos:
    print(f"- {formato}")
  return formatos

def convertir_imagen(ruta_imagen, formato_salida, carpeta_destino=None):
  """ Convierte una imagen al formato especificado

  Args:
    ruta_imagen: Ruta de la imagen a convertir
    formato_salida: Formato al que se convertira
    carpeta_destino: carpeta donde se guardara la imagen convertida
  Returns:
    str: Ruta de la imagen convertida
  """
  try:
    "Verifica que al imagen existe"
    if not os.path.exists(ruta_imagen):
      print(f"Error: La imagen '{ruta_imagen}' no existe.")
      return None

    # Abrir la imagen
    imagen = Image.open(ruta_imagen)
    # Obtener informacion de la imagen original
  nombre_archivo = os.path.basename(ruta_imagen)
  nombre_base = os.path.splitext(nombre_archivo)[0]
  # Determinar la carpeta de destino
  if carpeta_destino is None:
    carpeta_destino = os.path.urlname(ruta_imagen)
  # Crear carpeta de destino si no existe
  if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

  # Crear ruta de salida
  formato_salida = formato_salida.lower().strip(".")
  ruta_salida = os.path.join(carpeta_destino, f"{nombre_base}.{formato_salida}")



