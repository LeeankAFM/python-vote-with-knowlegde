from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
import os
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURACIÓN ---
client = Client()
client.set_endpoint(os.getenv('APPWRITE_ENDPOINT'))
client.set_project(os.getenv('APPWRITE_PROJECT_ID'))
client.set_key(os.getenv('APPWRITE_API_KEY'))

databases = Databases(client)
DB_ID = os.getenv('APPWRITE_DB_ID')
COLL_CONCEPTOS = os.getenv('APPWRITE_COLLECTION_CONCEPTOS_ID')

# --- LISTA DE 8 CONCEPTOS (ULTRA DETALLADOS) ---
CONCEPTOS_FINAL = [
    # 1. LIBRE MERCADO (Versión detallada)
    {
        "titulo": "Libre Mercado (Capitalismo)",
        "etiqueta": "Economía",
        "descripcion": "Sistema económico donde el gobierno interviene lo mínimo posible. Los precios, la producción y los salarios se deciden libremente por la oferta y la demanda entre empresas y consumidores.",
        
        "ejemplo_bueno_titulo": "El Milagro del Crecimiento",
        "ejemplo_bueno_desc": "La apertura de mercados ha sacado a millones de la pobreza. Ejemplo: La reforma económica de China en 1978 permitió la propiedad privada y el comercio, logrando que 800 millones de personas salieran de la pobreza extrema en solo 40 años.",
        
        "ejemplo_malo_titulo": "La 'Gilded Age' y los Monopolios",
        "ejemplo_malo_desc": "Sin regulación, el mercado puede volverse salvaje. En EE.UU. (1890), empresas como Standard Oil eliminaron a toda su competencia creando monopolios. Los trabajadores sufrían jornadas de 16 horas sin seguridad ni derechos, creando una desigualdad abismal."
    },
    # 2. ESTADO DE BIENESTAR (Versión detallada)
    {
        "titulo": "Estado de Bienestar",
        "etiqueta": "Política Social",
        "descripcion": "El Estado recauda altos impuestos para financiar servicios públicos universales (salud, educación, pensiones), buscando que todos tengan las mismas oportunidades sin importar su origen.",
        
        "ejemplo_bueno_titulo": "El Modelo Nórdico",
        "ejemplo_bueno_desc": "Países como Noruega o Suecia cobran impuestos altos (cerca del 50%), pero a cambio ofrecen salud de primer nivel y educación universitaria gratuita. Esto ha creado sociedades con muy baja criminalidad y alta movilidad social.",
        
        "ejemplo_malo_titulo": "Colapso por Ineficiencia (Crisis Venezolana)",
        "ejemplo_malo_desc": "Cuando la intervención es excesiva y se expropian empresas productivas, la economía colapsa. En Venezuela, el control total de precios y divisas destruyó la producción nacional, generando escasez de comida y una hiperinflación histórica que empobreció al 90% del país."
    },
    # 3. POPULISMO (Versión detallada)
    {
        "titulo": "Populismo",
        "etiqueta": "Estrategia Política",
        "descripcion": "No es una ideología de izquierda o derecha, sino una estrategia. Divide al país en dos: el 'pueblo puro' vs. una 'élite corrupta'. Promete soluciones mágicas y rápidas a problemas muy complejos.",
        
        "ejemplo_bueno_titulo": "Visibilidad de los Olvidados",
        "ejemplo_bueno_desc": "Surge cuando la política tradicional falla. Permite que sectores históricamente discriminados se sientan representados y escuchados, poniendo en la agenda pública temas de pobreza y exclusión que antes se ignoraban.",
        
        "ejemplo_malo_titulo": "Erosión de la Democracia",
        "ejemplo_malo_desc": "Para 'defender al pueblo', el líder populista suele atacar a la prensa y a los jueces independientes. Ejemplo: El desmantelamiento de las instituciones en Nicaragua, donde bajo la excusa de la revolución, se eliminó la oposición y se perpetuó el poder indefinidamente."
    },
    # 4. GLOBALIZACIÓN (Versión detallada)
    {
        "titulo": "Globalización",
        "etiqueta": "Geopolítica",
        "descripcion": "Proceso de interconexión mundial donde bienes, servicios, personas e información cruzan fronteras con facilidad. El mundo funciona como un solo mercado.",
        
        "ejemplo_bueno_titulo": "Acceso y Tecnología",
        "ejemplo_bueno_desc": "Gracias a ella, puedes tener tecnología avanzada a bajo costo. Permite el intercambio científico rápido, como ocurrió con la colaboración global entre laboratorios de distintos países para desarrollar vacunas COVID en tiempo récord.",
        
        "ejemplo_malo_titulo": "Desempleo en el 'Rust Belt'",
        "ejemplo_malo_desc": "Hizo que muchas fábricas en países desarrollados (como Detroit en EE.UU.) se mudaran a Asia buscando mano de obra barata. Esto dejó ciudades enteras sin empleo, generando decadencia urbana y resentimiento en la clase trabajadora local."
    },
    # 5. NACIONALISMO (Versión MEJORADA y detallada)
    {
        "titulo": "Nacionalismo",
        "etiqueta": "Identidad",
        "descripcion": "Ideología que pone a la propia nación como el valor supremo, buscando preservar su cultura, soberanía e intereses por encima de cualquier tratado internacional.",
        
        "ejemplo_bueno_titulo": "La Lucha de Gandhi",
        "ejemplo_bueno_desc": "El nacionalismo fue el motor de la descolonización. En la India, Gandhi unió a millones de personas bajo una identidad nacional común para resistir pacíficamente al Imperio Británico y lograr su independencia y dignidad.",
        
        "ejemplo_malo_titulo": "Las Guerras Mundiales",
        "ejemplo_malo_desc": "Llevado al extremo, se convierte en odio hacia lo extranjero. El ultranacionalismo europeo del siglo XX convenció a las poblaciones de que sus vecinos eran enemigos inferiores, desencadenando la Primera y Segunda Guerra Mundial con millones de muertos."
    },
    # 6. LIBERTAD DE EXPRESIÓN (Versión MEJORADA y detallada)
    {
        "titulo": "Libertad de Expresión",
        "etiqueta": "Derechos Civiles",
        "descripcion": "El derecho fundamental a buscar, recibir y difundir opiniones e información sin censura, represalias o sanciones por parte del gobierno.",
        
        "ejemplo_bueno_titulo": "El Movimiento por los Derechos Civiles",
        "ejemplo_bueno_desc": "En los años 60 en EE.UU., la libertad de prensa permitió mostrar al mundo la brutalidad policial contra los afroamericanos. Poder criticar abiertamente las leyes racistas fue la única herramienta para lograr cambiarlas.",
        
        "ejemplo_malo_titulo": "El Genocidio en Ruanda",
        "ejemplo_malo_desc": "La libertad de expresión tiene límites éticos peligrosos. En 1994, la radio 'RTLM' en Ruanda usó las ondas libremente para deshumanizar a la etnia Tutsi, llamándolos 'cucarachas' e incitando directamente a la población a cometer un genocidio."
    },
    # 7. MERITOCRACIA (Versión MEJORADA y detallada)
    {
        "titulo": "Meritocracia",
        "etiqueta": "Sociedad",
        "descripcion": "Sistema ideal donde las posiciones de poder, riqueza y estatus se otorgan exclusivamente según el talento, la educación y el esfuerzo individual, no por herencia.",
        
        "ejemplo_bueno_titulo": "La Transformación de Singapur",
        "ejemplo_bueno_desc": "Singapur pasó de ser una isla pobre y sin recursos a una potencia económica mundial en 30 años. Lo logró combatiendo la corrupción y promoviendo a los funcionarios públicos más estudiosos y capaces, sin importar sus conexiones familiares.",
        
        "ejemplo_malo_titulo": "La Ilusión de la Igualdad",
        "ejemplo_malo_desc": "Puede ignorar las desventajas de origen. Un niño que debe trabajar para comer no compite igual que uno con tutores privados. Si el sistema ignora esto, la meritocracia se usa para culpar a los pobres de su pobreza, asumiendo que 'no se esforzaron lo suficiente'."
    },
    # 8. DIVISIÓN DE PODERES (Versión MEJORADA y detallada)
    {
        "titulo": "División de Poderes",
        "etiqueta": "Institucional",
        "descripcion": "Principio republicano que separa al Estado en tres ramas: Ejecutivo (administra), Legislativo (crea leyes) y Judicial (juzga), para que se vigilen mutuamente.",
        
        "ejemplo_bueno_titulo": "Freno a la Tiranía (Watergate)",
        "ejemplo_bueno_desc": "Evita el poder absoluto. Cuando el presidente Nixon (EE.UU.) abusó de su poder espiando opositores, el sistema judicial y el congreso lo investigaron y obligaron a renunciar, demostrando que nadie está por encima de la ley.",
        
        "ejemplo_malo_titulo": "Parálisis Política (Perú/Italia)",
        "ejemplo_malo_desc": "Cuando los poderes se usan para sabotearse en lugar de fiscalizar, el país se detiene. En países como Perú, el conflicto constante entre Congreso y Presidente ha causado que se destituyan mandatarios repetidamente, generando caos e inestabilidad crónica."
    }
]

print("--- SUBIENDO CONCEPTOS DETALLADOS (VERSIÓN FINAL) ---")

for c in CONCEPTOS_FINAL:
    try:
        databases.create_document(
            database_id=DB_ID,
            collection_id=COLL_CONCEPTOS,
            document_id=ID.unique(),
            data={
                "titulo": c['titulo'],
                "etiqueta": c['etiqueta'],
                "descripcion": c['descripcion'],
                "ejemplo_bueno_titulo": c['ejemplo_bueno_titulo'],
                "ejemplo_bueno_desc": c['ejemplo_bueno_desc'],
                "ejemplo_malo_titulo": c['ejemplo_malo_titulo'],
                "ejemplo_malo_desc": c['ejemplo_malo_desc']
            }
        )
        print(f"Subido: {c['titulo']}")
    except Exception as e:
        print(f"Error en {c['titulo']}: {e}")

print("¡Listo! Base de datos actualizada con 8 conceptos profundos.")