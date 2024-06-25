import json
import os
def cargar_libros():
  if os.path.exists("biblioteca.json"):
    with open("biblioteca.json", "r") as archivo:
      data = json.load(archivo)
      return data["libros"]
  return []
def cargar_categorias():
  if os.path.exists("biblioteca.json"):
    with open("biblioteca.json", "r") as archivo:
      data = json.load(archivo)
      return data["categorias"]
  return []
def generar_reporte():
  libros = cargar_libros()
  categorias = cargar_categorias()
  categorias_dict = {categoria["id"]: categoria["nombre"] for categoria in categorias}
  conteo_categorias = {categoria["nombre"]: 0 for categoria in categorias}
  for libro in libros:
    categoria_nombre = categorias_dict.get(libro["categoria_id"], "Desconocida")
    conteo_categorias[categoria_nombre] += 1
  with open("Reportes_biblioteca_mundo_libro.json", "w") as archivo:
    json.dump(conteo_categorias, archivo, indent=4)
  print("Reporte generado exitosamente. Ver 'Reportes_biblioteca_mundo_libro.json'")
  for categoria, cantidad in conteo_categorias.items():
    print(f"{categoria}: {cantidad} libros")