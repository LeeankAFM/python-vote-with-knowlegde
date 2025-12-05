import os
from flask import Flask, render_template, request
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)

# --- CONFIGURACIÓN APPWRITE ---
client = Client()
client.set_endpoint(os.getenv('APPWRITE_ENDPOINT'))
client.set_project(os.getenv('APPWRITE_PROJECT_ID'))
client.set_key(os.getenv('APPWRITE_API_KEY'))

databases = Databases(client)

# IDs definidos en tu archivo .env
DB_ID = os.getenv('APPWRITE_DB_ID')
COLL_PREGUNTAS_BASICO = os.getenv('APPWRITE_COLLECTION_BASICO_ID')
COLL_PUNTAJES = os.getenv('APPWRITE_COLLECTION_PUNTAJES_ID')
COLL_CONCEPTOS = os.getenv('APPWRITE_COLLECTION_CONCEPTOS_ID')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nivel_basico', methods=['GET', 'POST'])
def nivel_basico():
    # 1. Traer preguntas de la DB
    try:
        result = databases.list_documents(
            database_id=DB_ID, 
            collection_id=COLL_PREGUNTAS_BASICO,
            queries=[] 
        )
        preguntas_db = []
        for doc in result['documents']:
            # Asegúrate que 'id_pregunta', 'pregunta', 'opciones' coincidan con tu DB
            preguntas_db.append({
                "id": doc.get('id_pregunta', doc['$id']), 
                "pregunta": doc.get('pregunta', 'Pregunta sin texto'),
                "opciones": doc.get('opciones', []),
                "correcta": doc.get('correcta', '')
            })
    except Exception as e:
        print(f"Error conectando con Appwrite: {e}")
        preguntas_db = []

    # 2. Procesar respuestas (Si el usuario envió el formulario)
    if request.method == 'POST':
        puntaje = 0
        respuestas_usuario = request.form
        nickname = respuestas_usuario.get('nickname', 'Anónimo')
        
        resultados_detalle = []
        
        for p in preguntas_db:
            id_preg = p['id']
            respuesta_dada = respuestas_usuario.get(id_preg)
            es_correcta = (respuesta_dada == p['correcta'])
            
            if es_correcta:
                puntaje += 1
            
            resultados_detalle.append({
                "pregunta": p['pregunta'],
                "correcta": p['correcta'],
                "dada": respuesta_dada if respuesta_dada else "No respondida",
                "es_correcta": es_correcta
            })

        # 3. Guardar puntaje en Appwrite
        try:
            databases.create_document(
                database_id=DB_ID,
                collection_id=COLL_PUNTAJES,
                document_id=ID.unique(),
                data={
                    "nickname": nickname,
                    "puntaje": puntaje,
                    "nivel": "basico",
                    "fecha": datetime.now().isoformat()
                }
            )
        except Exception as e:
            print(f"Error guardando puntaje: {e}")

        # 4. Ir a la pantalla de resultados (usamos 'resultado.html' singular)
        return render_template('resultado.html', 
                               nivel="Nivel Básico",
                               nickname=nickname,
                               puntaje=puntaje, 
                               total=len(preguntas_db), 
                               detalles=resultados_detalle)

    # Si es GET, mostramos el examen
    return render_template('nivel_basico.html', preguntas=preguntas_db)

@app.route('/conceptos_reforzar')
def conceptos_reforzar():
    try:
        result = databases.list_documents(
            database_id=DB_ID,
            collection_id=COLL_CONCEPTOS
        )
        lista_conceptos = []
        for doc in result['documents']:
            lista_conceptos.append({
                "titulo": doc.get('titulo', ''),
                "etiqueta": doc.get('etiqueta', ''),
                "descripcion": doc.get('descripcion', ''),
                "bueno_titulo": doc.get('ejemplo_bueno_titulo', ''),
                "bueno_desc": doc.get('ejemplo_bueno_desc', ''),
                "malo_titulo": doc.get('ejemplo_malo_titulo', ''),
                "malo_desc": doc.get('ejemplo_malo_desc', '')
            })
        return render_template('conceptos_reforzar.html', conceptos=lista_conceptos)
    except Exception as e:
        print(f"Error conceptos: {e}")
        return render_template('conceptos_reforzar.html', conceptos=[])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)