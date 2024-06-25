import json
import os

from usuarios import agregar_usuario, editar_usuario, eliminar_usuario, buscar_usuario
from reportes import generar_reporte
def mostrar_menu():
  print("********************************")
  print("*      MUNDO LIBRO    *")
  print("********************************")
  print("[1] - Mantenedor de usuarios")
  print("[2] - Reportes")
  print("[3] - Salir")
def mantenedor_usuarios_menu():
  print("********************************")
  print("*    MANTENEDOR USUARIO   *")
  print("********************************")
  print("[1] - Agregar usuario")
  print("[2] - Editar usuario")
  print("[3] - Eliminar usuario")
  print("[4] - Buscar usuario")
  print("[5] - Volver")
def main():
  while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
      while True:
        mantenedor_usuarios_menu()
        sub_opcion = input("Seleccione una opción: ")
        if sub_opcion == '1':
          agregar_usuario()
        elif sub_opcion == '2':
          editar_usuario()
        elif sub_opcion == '3':
          eliminar_usuario()
        elif sub_opcion == '4':
          buscar_usuario()
        elif sub_opcion == '5':
          break
        else:
          print("Opción no válida, intente nuevamente.")
    elif opcion == '2':
      generar_reporte()
    elif opcion == '3':
      print("Saliendo...")
      break
    else:
      print("Opción no válida, intente nuevamente.")
if __name__ == "__main__":
  main()