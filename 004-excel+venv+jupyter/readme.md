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
    ****
    
    3. Para descargar librerias en el entorno virtual:

    `pip install -r requirements.txt`
    ****

    4. Para ejecutar jupyter en el navegador:
    `jupyter notebook`  (para crear archivo nuevo)
    `jupyter notebook main.ipynb`  (si es un archivo ya existente)

     . O bien escribir directamente con vscode en `main.ipynb`
    ****
    
    5. Si se incluyen nuevas dependencias actualizar requirements.txt:
    `pip freeze > requirements.txt`
    ****

    6. Para cerrar el venv
    `deactivate`
