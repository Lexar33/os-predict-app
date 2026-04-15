from setuptools import find_packages, setup  # Importando funciones de setuptools

from typing import List                      # Importando el tipo Lista


## Crea una función que abra requirment.txt y brinde una lista de pre-requisitos
def get_requirements(file_path:str)->List[str]:
    """ This function will return a list of all requirments """
    
    requirments = []
    with open(file_path) as f:
        requirments = f.readlines()                                   
        requirments = [req.replace("\n" ,"") for req in requirments] 
        
        if "-e ." in requirments:        
            requirments.remove("-e .")  
    
    return requirments                 # devuelve la lista de pre-requisitos


## Agregamos metadatos de nuestro proyecto de  Python package
setup(

    name = "Modelo de Sistema Operativo",                             # Nombre
    version = "0.1.1",                                      # Versión del módulo
    author = "Jose ALcantara",                              # Autor
    author_email = "jalcantararivera@gmail.com",                 # Correo del Author
    packages = find_packages(),                             # Automáticamente encuentra librerías en el directorio actual
    install_requires = get_requirements("requirements.txt")   # Especificar las dependencias en requirements.txt

)
