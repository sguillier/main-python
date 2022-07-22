# Ejemplo virtualenv + Excel

## Requerimientos
1. Python >= 3.10
2. modulo virtualenv instalado

## Pasos para crear el proyecto localmente:


1. Crear ambiente virtual:

    `python -m virtualenv venv`
    ****

2. Para entrar y activar el entorno virtual:

   (WINDOWS):`.\venv\Scripts\activate`

   NOTA: Para ejecutar esto en windows es necesario tener habilitada la ejecución de Scripts. Para ello se pueden ver los permisos existentes con el siguiente comendo:
      Get-ExecutionPolicy -List
   Para poder modificarlo ejecutar siguiente comando (notar que edita CurrentUser):
      Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   
   ****
    
3. Para descargar librerias en el entorno virtual:

   `pip install -r requirements.txt`
   ****

4. Editar el archivo main.py


    
5. Si se incluyen nuevas dependencias actualizar requirements.txt:
   `pip freeze > requirements.txt`
   ****

6. Para cerrar el venv
   `deactivate`
