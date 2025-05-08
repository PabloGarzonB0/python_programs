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
      "Verifica que la imagen existe"
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
    
      imagen.save(ruta_salida)
      print(f"Imagen convertida y guardada en : {ruta_salida}")
    
      return ruta_salida

except Exception as e:
    print(f"Error al convertir la imagen: {e}")
    return None

def convertir_multiples_imagenes(carpeta_origen, formato_salida, carpeta_destino=None):
  """ Convertir todas las imagenes en una carpeta al formato especificado
  Args:
    carpeta_origen: Carpeta que contiene las imagenes a convertir
    formato_salida: Formato al que se convertiran las imagenes
    carpeta_destino: Carpeta donde se guardaran las imagenes convertidas
  Returns:
    int: Numero de imagenes convertidas exitosamente
  """
  if not os.path.exists(carpeta_origen):
    print(f"Error: La carpeta '{carpeta_original}' no existe.")
    return 0

  extensiones_imagen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
  # Contador de imagenes a convertir
  contador = 0
  # Recorrer todos los archivos en la carpeta
  for archivo in os.listdir(carpeta_origen):
    ruta_archivo = os.path.join(carpeta_origen, archivo)
    # Verificar si es un archivo y tiene extension de imagen
    if os.path.isfile(ruta_archivo) and any(archivo.lower().endswith(ext) for ext in extensiones_imagen):
      if convertir_imagen(ruta_archivo, formato_salida, carpeta_destino):
        contador += 1
  return contador


def main():
  """FUNCION PRINCIPAL DEL PROGRAMA"""
  print("=== CONVERSOR DE IMAGENES ===")

  listar_formatos_soportados()
  print("\n")
  # Menu de opciones
  print("Opciones:")
  print("1. Convertir una imagen")
  print("2. Convertir todas las imagenes en una carpeta")

  opcion = input("\nSeleccion una opcion (1-2): ")
  if opcion == "1":
    ruta_imagen = input("Ingresa la ruta de la imagen a convertir: ")
    formato_salida = input("Ingresa el formato de salida (ej: PNG): ")
    carpeta_destino = input("Ingresa la carpeta de destino (opcional, deja blanco para usar)")

    if not carpeta_destino:
        carpeta_destino = None
    convertir_imagen(ruta_imagen, formato_salida, carpeta_destino)

  if opcion == "2":
      ruta_imagen = input("Ingresa la ruta de la imagen a convertir: ")
      formato_salida = input("Ingresa el formato de salida (ej: PNG): ")
      carpeta_destino = input("Ingresa la carpeta de destino (opcional, deja blanco para usar)")

    if not carpeta_destino:
        carpeta_destino = None
    num_convertidas = convertir_multiples_imagenes(carpeta_origen, formato_salida, carpeta_destino)
    print(f"\n Se convirtieron {num_convertidas} imagenes exitosamente")
else:
  print("Opcion no valida")


if __name__ == "__main__":
  main()
    


