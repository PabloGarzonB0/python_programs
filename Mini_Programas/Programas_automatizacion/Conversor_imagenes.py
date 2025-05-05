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


