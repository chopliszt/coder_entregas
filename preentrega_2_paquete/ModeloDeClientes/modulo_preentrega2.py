import json
import os 

class Persona:
  def __init__(self,nombre:str, edad:int,correo:str, país:str):
    self.__nombre=nombre
    self.__correo=correo
    self.__edad=edad
    self.__país=país #Profe una duda: ¿está bien poner nombres en español o debí haber escrito pais sin tilde o country?
  
  #Magic method
  def __str__(self):
    return f"Nombre: {self.__nombre}, edad:{self.__edad}, correo: {self.__correo}, país: {self.__país}"
  
  #métodos getters
  def obtener_nombre(self)->str: 
    """
    Obtener el nombre. Siempre debo crearlo en la clase principal, no en las que lo heredan(eso creo)
    """
    return self.__nombre
  
  def obtener_edad(self)->int:
    return self.__edad
  
  def obtener_correo(self):
    return self.__correo
  
  def obtener_país(self):
    return self.__país
  
  #Un método setter
  def cambiar_correo(self,correo_nuevo)->None:
    self.__correo=correo_nuevo

class Cliente(Persona):
  """
  Se asume que es un cliente de una plataforma de aprendizaje de idiomas. Como Coder, pero para idiomas. 
  """
  
  tipo_de_usuario:str="usuario digital"
  archivo:str="db_lista_de_cursos.json"

  def __init__(self, nombre:str,edad:int, correo:str, país:str, cursos:list[str], usuario:str, id:int):
    super().__init__(nombre, edad, correo, país)
    self.__cursos=cursos
    self.__usuario=usuario
    self.__id=id
  
  #Magic method
  def __str__(self):
    return f"Nombre: {self.obtener_nombre()}, Edad: {self.obtener_edad()}, cursos comprados: {self.__cursos}, usuario: {self.__usuario}"
  
  def obtener_cursos(self)->list:
    return self.__cursos
  
  def obtener_id(self)->int:
    return self.__id
  
  def obtener_usuario(self)->str:
    return self.__usuario

  def cambiar_usuario(self,nuevo_usuario)->None:
    self.__usuario=nuevo_usuario

  def eliminar_curso(self,curso)->None:
    try:
      self.__cursos.remove(curso) 
    except Exception as objeto_excepcion:
      print("Hubo un error: ", repr(objeto_excepcion))  


  def agregar_curso(self,curso:str)->None:
    self.__cursos.append(curso)

  def guardar_cursos_a_json(self)->None:
    """
    Este método guarda cada cliente creado, en un Json. Es un historial de objetos.
    """
    data={
      "usuario": self.__usuario,
      "cursos": self.__cursos
    }

    #Ahora vamos a revisar si existe el archivo y si existe, a cargarlo
    if os.path.exists(self.archivo) and os.path.getsize(self.archivo)>0:
      with open(self.archivo,"r",encoding="utf-8") as file:
        datos_existentes=json.load(file)     
    else:
      datos_existentes=[]   
    
    datos_existentes.append(data)
    #esta es la parte que guarda el archivo
    with open(self.archivo, "w", encoding="utf-8") as mi_archivo:
         json.dump(datos_existentes, mi_archivo,ensure_ascii=False, indent=4)

  
  def definir_ingresos_por_compras_de_cliente(self)->float:
    """
    Supone que todos los cursos cuestan lo mismo mensualmente. Este método calcula lo que el cliente gasta mensualmente
    """
    precio_mensual_por_curso:int=10
    ingreso_de_cursos:float=len(self.__cursos)*precio_mensual_por_curso
    return  ingreso_de_cursos


