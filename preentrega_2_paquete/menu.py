from ModeloDeClientes.modulo_preentrega2 import Persona
from ModeloDeClientes.modulo_preentrega2 import Cliente


def main():
  
  #creando instancias de clases
  mi_persona:Persona=Persona("Julio", 34,"asdasdgmail", "Japón")
  mi_cliente:Cliente=Cliente("Ramiro",24,"correoatcorreo.com","España",["Aleman", "Portugués, Mandarin, Japonés, Swahili"],  "superman1", 123)
  
  #obteniendo los cursos del cliente
  cursos:list=mi_cliente.obtener_cursos()

  #imprimiendo
  print("Persona: ",mi_persona)
  print("Cliente: ",mi_cliente)
  print("Cursos del cliente: ",cursos)
  
  #Llamando a método para eliminar uno de los cursos
  mi_cliente.eliminar_curso("Aleman")
  #Imprimiendo la lista de cursos, para verificar que se haya eliminado
  print("Cursos del cliente despues de eliminar uno: ",cursos)

  #cambiando datos del usuario para probar los métodos
  mi_cliente.cambiar_correo("elon@tesla.com")
  mi_cliente.cambiar_usuario("soymuyempatico123")
  
  #Imprimiendo los datos después de los cambios que se hicieron con los métodos
  print("Cliente despues de los cambios: ", mi_cliente)
  
  #Llamando al método guardar cursos, para persistir los cursos
  mi_cliente.guardar_cursos_a_json()

main()