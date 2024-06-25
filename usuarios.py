import json
import os
def cargar_usuarios():
  if os.path.exists("biblioteca.json"):
    with open("biblioteca.json", "r") as archivo:
      data = json.load(archivo)
      return data.get("usuarios", [])
  return []
def guardar_usuarios(usuarios):
  data = {}
  if os.path.exists("biblioteca.json"):
    with open("biblioteca.json", "r") as archivo:
      data = json.load(archivo)
  data["usuarios"] = usuarios
  with open("biblioteca.json", "w") as archivo:
    json.dump(data, archivo, indent=4)
def agregar_usuario():
  usuarios = cargar_usuarios()
  nuevo_usuario = {
    "id": input("ID: "),
    "nombre": input("Nombre: "),
    "email": input("Email: "),
    "fecha_registro": input("Fecha de Registro (YYYY-MM-DD): ")
  }
  usuarios.append(nuevo_usuario)
  guardar_usuarios(usuarios)
  print("Usuario agregado exitosamente.")
def editar_usuario():
  usuarios = cargar_usuarios()
  id_usuario = input("Ingrese el ID del usuario a editar: ")
  for usuario in usuarios:
    if usuario["id"] == id_usuario:
      usuario["nombre"] = input(f"Nuevo nombre ({usuario['nombre']}): ") or usuario["nombre"]
      usuario["email"] = input(f"Nuevo email ({usuario['email']}): ") or usuario["email"]
      usuario["fecha_registro"] = input(f"Nueva fecha de registro ({usuario['fecha_registro']}): ") or usuario["fecha_registro"]
      guardar_usuarios(usuarios)
      print("Usuario editado exitosamente.")
      return
  print("Usuario no encontrado.")
def eliminar_usuario():
  usuarios = cargar_usuarios()
  id_usuario = input("Ingrese el ID del usuario a eliminar: ")
  usuarios = [usuario for usuario in usuarios if usuario["id"] != id_usuario]
  guardar_usuarios(usuarios)
  print("Usuario eliminado exitosamente.")
def buscar_usuario():
  usuarios = cargar_usuarios()
  id_usuario = input("Ingrese el ID del usuario a buscar: ")
  for usuario in usuarios:
    if usuario["id"] == id_usuario:
      print(f"ID: {usuario['id']}")
      print(f"Nombre: {usuario['nombre']}")
      print(f"Email: {usuario['email']}")
      print(f"Fecha de Registro: {usuario['fecha_registro']}")
      return
  print("Usuario no encontrado.")