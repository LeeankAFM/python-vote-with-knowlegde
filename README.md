# Votar con Conocimiento (Flask)

Esta es una versión mínima para ejecutar las plantillas con Flask.

Requisitos
- Python 3.8+

Instalación y ejecución (PowerShell)

```powershell
cd 'C:\Users\leean\Desktop\Python\python-vote-with-knowlegde'
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Luego abre en el navegador:

http://127.0.0.1:5000/

Notas
- Las plantillas HTML están en la carpeta `templates/`.
- Los cambios en las plantillas se reflejarán al recargar la página (el servidor corre en debug por defecto en `app.py`).
