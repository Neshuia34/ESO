import flet as ft
import re

# --- Mapeo de Asignaturas ---
# Mapea los nombres en los checkboxes a las secciones del archivo LOMLOE
ASIGNATURA_MAPPING = {
    "Inglés avanzado": "Lengua Extranjera (Inglés)",
    "Digitalización": "Digitalización",
    "Castellano": "Lengua y Literatura Españolas",
    "Matemáticas": "Matemáticas",
    "Tecnología": "Tecnología",
    "Física y Química": "Física y Química",
    "Biología": "Biología y Geología",
    "Geografía": "Geografía e Historia",
    "Historia": "Geografía e Historia",
    "Música": "Expresión Artística",
    "Dibujo Técnico": "Expresión Artística",
    "Valores Éticos": "Economía y Emprendimiento" # Mejor ajuste por contenido de RSC/ODS
}

# --- Parsing del Contenido LOMLOE ---

def parse_asignaturas_content(file_content):
    """
    Procesa el contenido del archivo de asignaturas para mapear cada tema 
    LOMLOE con su contenido detallado.
    """
    sections = {}
    current_subject = None
    current_content = []

    # Patrón para identificar el inicio de una nueva asignatura (Ej: '1. Geografía e Historia')
    subject_pattern = re.compile(r'^\s*\d+\.\s*(.+?)\s*$') 

    # --- CORRECCIÓN APLICADA: USAR file_content DIRECTAMENTE ---
    lines = file_content.splitlines()
    # -----------------------------------------------------------

    for line in lines:
        line = line.strip()
        if not line:
            continue

        match = subject_pattern.search(line)
        
        if match and "Enfoque Curricular" in line:
            # Es el inicio de una nueva sección de asignatura
            if current_subject and current_content:
                sections[current_subject.strip()] = "\n".join(current_content).strip()
            
            # Usar solo el nombre de la asignatura sin el número
            current_subject = match.group(1).split("Enfoque Curricular")[0].strip()
            
            # Iniciar nuevo contenido, incluyendo la línea de enfoque curricular
            current_content = [line]
        elif current_subject:
            # Continuar acumulando contenido para la asignatura actual
            # Excluir la línea de encabezado de tabla si aparece
            if line != 'Bloque de Saberes Básicos	Contenidos Detallados':
                current_content.append(line)

    # Añadir la última sección
    if current_subject and current_content:
        sections[current_subject.strip()] = "\n".join(current_content).strip()

    return sections

# Contenido del archivo B-ESO-asignaturas.txt para ser parseado en memoria
LOMLOE_FILE_CONTENT = """
los Saberes Básicos (Contenidos) y el enfoque curricular de 4º de ESO según la LOMLOE para el curso 2025-2026.

La LOMLOE enfatiza el desarrollo de Competencias Específicas y el uso de Situaciones de Aprendizaje, por lo que los contenidos se presentan siempre de forma contextualizada.

1. Geografía e Historia 

Enfoque Curricular: El currículo se estructura en torno a los Retos del Mundo Actual y el análisis de la interacción de las sociedades con sus territorios a lo largo del tiempo, fomentando una ciudadanía crítica y responsable.
Bloque de Saberes Básicos	Contenidos Detallados
Retos del Mundo Actual	Objetivos de Desarrollo Sostenible (ODS): El papel de la juventud en la consecución de los 17 ODS.
Emergencia climática, sostenibilidad, y la relación entre factores naturales y humanos.
Globalización y Desigualdad: Flujos migratorios, interculturalidad, y análisis de la desigualdad e injusticia a nivel local y global.
Geopolítica y Conflictos: Estudio de conflictos actuales, terrorismo, genocidios y el papel de las instituciones internacionales (ONU, alianzas).
Igualdad de Género: Análisis histórico y actual de la desigualdad de género y las formas de violencia.
Sociedad de la Información y Digitalización	Fuentes de Información: Búsqueda, tratamiento, contraste y evaluación de la fiabilidad de fuentes en entornos digitales.
El problema de la desinformación (fake news). Tecnologías Geográficas: Uso de Tecnologías de la Información Geográfica (TIG) para interpretar mapas, gráficos e imágenes.
Economía y Territorio	Estructuras Económicas: Agentes y flujo circular de la renta.
Cambios en los sectores productivos y funcionamiento de los mercados. Dilemas del crecimiento y la sustentabilidad.
Análisis Territorial: Estudio comparado del espacio natural, rural y urbano. Despoblación y el reto del desarrollo urbano sostenible.
Complejidad Social y Autoridad	Análisis de las estructuras sociales históricas (familia, clan, estamento) y la disputa por el poder desde la Antigüedad hasta la Edad Moderna.
Las distintas formulaciones estatales: democracias, repúblicas, imperios y reinos.

2. Lengua y Literatura Españolas 
Enfoque Curricular: Profundizar en el dominio de las diferentes destrezas comunicativas (escucha, habla, lectura, escritura) y desarrollar la conciencia de la variación lingüística y el conocimiento de la literatura española de los siglos contemporáneos.
Bloque de Saberes Básicos	Contenidos Detallados
Educación Lingüística (Gramática y Léxico)	Variedades de la Lengua: Análisis comparado de las variedades dialectales del español (con énfasis en la modalidad autonómica) y variedades diastráticas (nivel culto, coloquial, vulgar).
Historia de la Lengua: Origen del léxico español. Estudio del contacto de lenguas (bilingüismo, préstamos, interferencias) y desmantelamiento de prejuicios lingüísticos.
Comunicación Oral	Componentes del Acto Comunicativo: Análisis del grado de formalidad, distancia social y propósitos comunicativos.
Géneros Discursivos: Práctica de la conversación, la entrevista, el debate y el uso estratégico de los actos de habla (discrepancia, reprobación).
Comunicación Escrita	Géneros Textuales: Producción y análisis de textos propios del ámbito académico y social (ensayo, monografía, reseña).
Uso de recursos de cohesión y coherencia. Escritura Creativa: Desarrollo de la imaginación y la expresión personal a través de diversos géneros (poesía, relato corto, etc.).
Educación Literaria	Estudio del siglo XVIII (Neoclasicismo e Ilustración), el Romanticismo (Bécquer, Larra) y el Realismo/Naturalismo (Galdós, Clarín).
Se incluye también un acercamiento al Modernismo y las Vanguardias, así como autores contemporáneos (incluyendo mujeres).
Lectura e interpretación de obras completas y fragmentos clave.

3. Lengua y Literatura Catalana 
Enfoque Curricular: Consolidación de la competencia comunicativa en catalán, tanto oral como escrita, el respeto por la diversidad lingüística del territorio, y el conocimiento de la literatura catalana en su contexto histórico y cultural.
Bloque de Saberes Básicos	Contenidos Detallados
Comunicación y Discurso	Textos Orales: Técnicas de expresión oral formal e informal.
Importancia de la prosodia y la correcta pronunciación. Textos Escritos: Análisis y producción de textos expositivos y argumentativos (estructura, recursos y características lingüísticas).
Reflexión sobre la Lengua	Normativa: Profundización en las normas ortográficas, incluyendo el uso de mayúsculas, signos de puntuación complejos y la correcta adaptación de préstamos léxicos.
Léxico y Semántica: Homónimos, parónimos y cambio semántico. Sintaxis: Revisión de la estructura de la oración simple y compleja (coordinación, subordinación).
Conciencia Lingüística y Plurilingüismo	Valoración de la diversidad de lenguas en España.
Exploración y cuestionamiento de prejuicios lingüísticos y estereotipos asociados al catalán y sus variantes dialectales (valenciano/balear).
Educación Literaria	Contexto Histórico-Literario: Desde el movimiento de la Renaixença hasta las corrientes contemporáneas.
Estudio de las Vanguardias, el Novecentismo y la literatura durante el Franquismo (incluyendo la producción en el exilio y la clandestinidad).
Análisis de géneros (novela, poesía, teatro) y autores clave.

4. Lengua Extranjera (Inglés) 
Enfoque Curricular: Desarrollo de la competencia comunicativa en todas sus vertientes (comprensión, expresión, interacción y mediación) en situaciones comunicativas variadas y auténticas, con una orientación a la preparación para la vida post-obligatoria.
Bloque de Saberes Básicos	Contenidos Detallados
Ejes Temáticos Culturales y Globales	Medio Ambiente y Sostenibilidad: Vocabulario sobre emergencia climática, energías renovables, ODS y el papel individual en el cambio.
Sociedad Digital: Impacto de las redes sociales, la moda y las tendencias (Trending Now).
Conciencia Mental y Cuerpo: Vocabulario relacionado con los sentidos, la memoria, las emociones y los miedos (All in the Mind).
Historia y Viajes: Narración de experiencias personales y hechos pasados.
Comunicación Lingüística (Gramática)	Tiempos Verbales Avanzados: Uso estratégico de Present Perfect, Past Simple y Past Perfect para narrar y conectar acciones pasadas.
Construcciones Verbales: Uso de gerundio e infinitivo tras diferentes verbos.
Oraciones Complejas: Dominio de los verbos modales (obligación, permiso, posibilidad) y las oraciones condicionales (tipos 1, 2 y 3).
Estilo Indirecto: Transformación de enunciados, preguntas y órdenes.
Destrezas y Mediación	Interacción Oral: Participación en debates, entrevistas, y presentaciones estructuradas.
Producción Escrita: Redacción de artículos de opinión, reseñas, correos formales e informales, y descripciones detalladas.
Mediación Lingüística: Capacidad de traducir o explicar, de forma concisa, información relevante entre compañeros, actuando como puente entre la lengua extranjera y la propia.

5. Matemáticas 
Enfoque Curricular: Se trabaja el razonamiento matemático, la resolución de problemas en contextos reales y la elección del itinerario (Matemáticas A, Aplicadas, o B, Académicas) se realiza en este curso.
Los contenidos son comunes o complementarios en ambos.
Bloque de Saberes Básicos	Contenidos Detallados
Aritmética	Números Reales: Representación, operaciones, error y aproximación.
Notación Científica para magnitudes muy grandes/pequeñas. Proporcionalidad: Problemas de razón, tasas de cambio y porcentajes (aumentos y descuentos).
Matemáticas Financieras: Introducción a los intereses simples y compuestos (inversiones y préstamos).
Álgebra	Polinomios y Factorización: Identidades notables, regla de Ruffini y teorema del resto.
Ecuaciones y Sistemas: Resolución de ecuaciones de segundo grado y sistemas de ecuaciones lineales y no lineales (por reducción, sustitución, igualación).
Sucesiones: Análisis de las progresiones aritméticas y geométricas y sus aplicaciones.
Funciones	Representación y Análisis: Concepto de función.
Cálculo y determinación de dominio y recorrido. Estudio de la variación, crecimiento, decrecimiento y extremos.
Tipos de Funciones: Estudio de las funciones lineales, cuadráticas (parábola), exponenciales y logarítmicas, y su aplicación a modelos reales (crecimiento demográfico, intereses).
Geometría	Trigonometría Básica: Razones trigonométricas en triángulos rectángulos. Aplicación del Teorema de Pitágoras a problemas de la vida real.
Figuras y Transformaciones: Cálculo de perímetros, áreas y volúmenes de figuras planas y cuerpos geométricos.
Transformaciones en el plano (simetría, traslación, giro).
Estadística y Probabilidad	Estadística Descriptiva: Análisis de datos, tablas de frecuencia, gráficas y diagramas.
Cálculo e interpretación de medidas de centralización (media, mediana, moda) y dispersión (rango, desviación típica).
Probabilidad: Cálculo de probabilidades en experimentos aleatorios simples y compuestos.

6. Tecnología 
Enfoque Curricular: Desarrollo de la capacidad de análisis y resolución técnica de problemas, abarcando desde sistemas de instalaciones domésticas hasta la automatización, la electrónica y la iniciación a la programación de control.
Bloque de Saberes Básicos	Contenidos Detallados
Sistemas Técnicos y Diseño	Diseño y Prototipado: Fases del proceso tecnológico (identificación del problema, diseño, planificación, construcción, evaluación).
Diseño e Impresión 3D: Modelado básico y principios de la fabricación aditiva.
Documentación: Normalización, simbología y representación gráfica de soluciones técnicas.
Electrónica y Control	Electrónica Digital: El sistema binario.
Aplicación del Álgebra de Boole y funcionamiento de las Puertas Lógicas. Análisis de circuitos electrónicos sencillos.
Sistemas Automáticos: Componentes básicos (sensores digitales/analógicos, actuadores). Introducción a la robótica (diseño y construcción).
Programación y Hardware de Control	Lenguajes de Programación: Conceptos básicos (algoritmos, variables, estructuras de control).
Uso de plataformas de hardware de control (placas programables) para la experimentación y el control de prototipos.
Ventajas del Hardware Libre.
Tecnologías de la Vivienda	Instalaciones Domésticas: Análisis y simbología de las instalaciones eléctricas, de agua y saneamiento.
Introducción a la Domótica y el control de dispositivos. Eficiencia Energética: Estrategias de ahorro energético y sostenibilidad en el hogar.

7. Biología y Geología 
Enfoque Curricular: Fomenta la cultura científica y la comprensión del mundo a través del estudio de la vida, la herencia, la evolución y la dinámica del planeta Tierra y el universo, desde una perspectiva de investigación.
Bloque de Saberes Básicos	Contenidos Detallados
Genética y Evolución	Base Molecular de la Herencia: Relación entre el ADN, los genes, las mutaciones y la biodiversidad.
Leyes de la Herencia: Resolución de problemas de herencia genética monohíbrida y dihíbrida, incluyendo herencia ligada al sexo.
Teorías Evolutivas: Análisis de las evidencias de la evolución y comparación de la teoría neodarwinista con otras teorías históricas (Lamarck, Darwin).
La Dinámica de la Geosfera	Tectónica de Placas: Los efectos globales de la dinámica interna de la Tierra.
Procesos Geológicos: Diferencias y relación entre procesos externos (erosión, sedimentación) e internos (vulcanismo, sismicidad).
Riesgos Naturales: Estudio de riesgos geológicos y climáticos. Medidas de prevención y elaboración de mapas de riesgos.
La Tierra en el Universo	Cosmología: Teorías sobre el origen del universo y del sistema solar.
Movimientos y composición de los astros.
Proyecto Científico y Salud	Investigación: Desarrollo de destrezas científicas básicas (formular hipótesis, diseñar experimentos, analizar resultados).
La Mujer en la Ciencia: Reconocimiento de las contribuciones de mujeres científicas.
Salud y Cuerpo Humano: Repaso de los niveles de organización.
Salud y enfermedad, higiene, prevención y el papel del sistema inmunitario.

8. Digitalización 
Enfoque Curricular: Dirigido a formar una ciudadanía digital crítica, segura y competente, que domina las herramientas digitales y es consciente de su huella en la red y los riesgos asociados a la tecnología.
Bloque de Saberes Básicos	Contenidos Detallados
Dispositivos y Comunicación	Arquitectura de Ordenadores: Componentes internos, montaje y configuración básica.
Sistemas Operativos: Instalación, configuración de usuario y uso de sistemas operativos libres. Redes: Configuración de redes domésticas.
Dispositivos Conectados (IoT): Configuración y conexión de dispositivos inteligentes y wearables.
Creación y Edición de Contenidos	Productividad: Uso avanzado de aplicaciones ofimáticas.
Diseño Web Básico: Fundamentos de HTML y CSS para la creación de páginas web sencillas.
Programación de Aplicaciones: Conceptos de programación orientada a la creación de aplicaciones móviles o web básicas.
Tecnologías Inmersivas: Introducción a la Realidad Virtual, Aumentada y Mixta.
Seguridad y Bienestar Digital	Protección de Datos: Análisis de la identidad, reputación y huella digital.
Medidas preventivas en la configuración de redes sociales y la gestión de identidades virtuales.
Ciberseguridad: Medidas preventivas y correctivas frente a virus, malware y ataques.
Riesgos y Amenazas: Concienciación sobre el ciberacoso, la sextorsión, la dependencia tecnológica y prácticas de uso saludable.
Ciudadanía Digital Crítica	Educación Mediática: Herramientas para detectar la desinformación (fake news), el fraude y el uso crítico de la red.
Derechos Digitales: Libertad de expresión, propiedad intelectual y licencias de uso.
Administración Electrónica: Servicios públicos en línea, registros digitales y uso de certificados oficiales para gestiones.

9. Economía y Emprendimiento 
Enfoque Curricular: Desarrollo de la mentalidad emprendedora y de las habilidades necesarias para la vida profesional y personal, con especial atención a la gestión económica responsable y la comprensión del entorno empresarial y social.
Bloque de Saberes Básicos	Contenidos Detallados
La Persona Emprendedora	Autoconocimiento y Habilidades: Autoconfianza, empatía, resiliencia y perseverancia.
Técnicas de diagnóstico de fortalezas y debilidades. Innovación: Desarrollo de la creatividad, generación de ideas y aplicación de metodologías ágiles como el Design Thinking.
Liderazgo: Comunicación asertiva, negociación y trabajo en equipo.
Entorno Económico y Social	Agentes y Flujo: Los agentes económicos y el flujo circular de la renta.
Funcionamiento de los mercados. El Sistema Financiero: Instituciones, instrumentos y mercados financieros.
Empresa y Tipologías: Clasificación de empresas (por forma jurídica, tamaño, sector).
Sostenibilidad y Responsabilidad	Responsabilidad Social Corporativa (RSC).
Economía Circular y la huella ecológica. Economía Colaborativa y Social.
El papel de la economía en la reducción de la pobreza y las desigualdades, alineado con los ODS.
Finanzas Personales y del Proyecto	Gestión del Dinero: Necesidades económicas en las diferentes etapas de la vida.
Fuentes y control de ingresos y gastos. Presupuesto personal o familiar.
Fuentes de Financiación: Recursos financieros a corto y largo plazo (créditos, préstamos, ahorro). Obligaciones fiscales básicas.

10. Expresión Artística 
Enfoque Curricular: Se centra en la exploración, experimentación y creación con diversos lenguajes artísticos, fomentando la sensibilidad estética, la conciencia crítica y la producción responsable y sostenible.
Bloque de Saberes Básicos	Contenidos Detallados
Creación Bidimensional	Técnicas Gráfico-Plásticas: Experimentación con técnicas secas (lápiz, carboncillo, ceras) y húmedas (acuarela, acrílico).
Estampación: Procedimientos directos, aditivos y sustractivos. Composición: Elementos y principios básicos del lenguaje visual y de la percepción (color, ritmo, textura).
Creación Tridimensional y Sostenible	Técnicas de Volumen: Modelado, ensamblaje y técnicas de escultura básica.
Arte y Reciclaje: Desarrollo de proyectos de arte sostenible, empleando materiales reciclados y promoviendo el consumo responsable.
Arte y Naturaleza: Concienciación sobre la conservación del patrimonio natural a través de la creación artística.
Imagen Fija y en Movimiento	Lenguaje Fotográfico: Narrativa de la imagen fija (encuadre, planificación, angulación, punto de vista).
Cine y Vídeo-Arte: Creación de guiones y proyectos de imagen secuenciada (animación básica).
Multimedia: Creación de recursos digitales y el diseño de la interfaz visual.
Análisis y Diseño	Arte y Crítica Social: Análisis de la publicidad y su uso de recursos persuasivos, estereotipos y cánones corporales y sexuales.
Campos del Diseño: Introducción al diseño gráfico, de producto, de moda, de interiores y escenografía, y sus referentes históricos y actuales.

11. Física y Química 
Enfoque Curricular: Desarrollo de las destrezas científicas para la comprensión de los fenómenos naturales desde el movimiento y las fuerzas hasta la composición de la materia y las transformaciones químicas, con una mirada a la sostenibilidad energética.
Bloque de Saberes Básicos	Contenidos Detallados
La Materia	Estructura Atómica y Enlace: Revisión de los modelos atómicos y los tipos de enlace químico.
Tabla Periódica: Propiedades periódicas y su relación con la configuración electrónica.
Formulación y Nomenclatura: Dominio de la formulación inorgánica (óxidos, hidruros, sales). Introducción a la formulación orgánica.
El Cambio Químico	Reacciones Químicas: Tipos de reacciones. Ajuste de Reacciones y estequiometría (cálculos con masas y volúmenes).
Disoluciones: Concentración y cálculos de disoluciones. El pH y su importancia (ej. acidificación de los océanos).
La Interacción y el Movimiento	Cinemática: Estudio y resolución de problemas de Movimiento Rectilíneo Uniforme (MRU) y Uniformemente Acelerado (MRUA).
Caída Libre. Dinámica: Las Leyes de Newton y su aplicación para la comprensión del movimiento y las fuerzas (fuerzas de rozamiento, peso).
Gravitación: Leyes de Kepler.
La Energía	Tipos de Energía: Energía mecánica, térmica, eléctrica. Transformaciones y Conservación.
Energía y Sostenibilidad: Análisis de las distintas fuentes de energía y su impacto ambiental, promoviendo el uso de energías renovables y la eficiencia.
Destrezas Científicas	Adquisición del método científico (observación, hipótesis, experimentación, análisis de resultados). Uso de medidas y unidades (Sistema Internacional).
Realización de trabajos prácticos de laboratorio.

12. Segunda lengua extranjera. a eleccion.
"""


def get_carpetas(nombre_bloque, nombre_sub, B_NAME=None, P_NAME=None):
    """Función para obtener la estructura de carpetas según el bloque/sub-bloque."""
    if nombre_bloque == "My":
        if nombre_sub == "ESO-Baleares": return ["LOMLOE"]
        elif nombre_sub == "Clara-eso": return ["Asignaturas"]
        return []
    elif nombre_bloque == B_NAME:
        if nombre_sub.endswith("00"): return ["B00", "B00-01", "Clara-m"]
        else: return ["Datos ESO-Clara", "Datos Clara100"] # <--- "Datos ESO-Clara" en B0X
    elif nombre_bloque == P_NAME:
        if nombre_sub.endswith("00"): return ["actualizar B00", "crear Actividades", "Clara-m"]
        else: return ["myClara100", "myAct", "myClara-m"]
    elif nombre_bloque == "A4":
        if nombre_sub == "A00": return ["myReadme", "Blog", "Clara-m"]
        else: return ["mi perfil", "mytools", "myact", "myClara-m"]
    elif nombre_bloque == "Act":
        if nombre_sub == "Act00": return ["Readme.md", "GestorAct", "Clara-m"]
        else: return ["Act01 all", "Act02 new"]
    return []


def main(page: ft.Page):
    # --- Cargar Contenido LOMLOE ---
    ASIGNATURA_CONTENIDO_MAP = parse_asignaturas_content(LOMLOE_FILE_CONTENT)
    
    page.title = "Clara 100: Mi 'eso-click'"
    page.window_width = 800
    page.window_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    # --- Variables Globales/Iniciales ---
    ASIGNATURAS_DISPONIBLES = [
        "Inglés avanzado", "Digitalización", "Castellano", "Matemáticas",
        "Tecnología", "Física y Química", "Biología", "Geografía",
        "Historia", "Música", "Dibujo Técnico", "Valores Éticos"
    ]
    
    bloque_style = {
        "width": 150, "height": 100, "border_radius": 12, "alignment": ft.alignment.center,
        "ink": True, "border": ft.border.all(2, ft.Colors.BLUE_GREY_400),
    }

    sub_bloque_style = {
        "width": 120, "height": 70, "border_radius": 10, "alignment": ft.alignment.center,
        "ink": True, "border": ft.border.all(2, ft.Colors.BLUE_GREY_200),
        "visible": False
    }

    # --- Estructura de Datos (Inicial y Dinámica) ---
    
    bloques_data = [
        {"nombre": "My", "display_name": "Myeso-click", "color": ft.Colors.RED_400, "contenido": "Bloque My: Mi espacio personal del proyecto."},
        {"nombre": "A4", "display_name": "A4", "color": ft.Colors.ORANGE_200, "contenido": "Bloque A4: Alumnos participantes."},
        {"nombre": "Act", "display_name": "Act", "color": ft.Colors.PURPLE_200, "contenido": "Bloque Act: Actividades del proyecto."}
    ]
    
    sub_bloques_dict = {
        "My": [
            {"nombre": "ESO-Baleares", "color": ft.Colors.RED_100, "contenido": "ESO-Baleares: Material curricular Baleares."},
            {"nombre": "Clara-eso", "color": ft.Colors.RED_100, "contenido": "Clara-eso: Configuración de asignaturas y creación de proyecto."}
        ],
        "A4": [
            {"nombre": "A00", "color": ft.Colors.ORANGE_100, "contenido": "A00: Alumno-super."},
            {"nombre": "A01", "color": ft.Colors.ORANGE_100, "contenido": "A01: Alumno/a 1."},
            {"nombre": "A02", "color": ft.Colors.ORANGE_100, "contenido": "A02: Alumno/a 2."},
            {"nombre": "A03", "color": ft.Colors.ORANGE_100, "contenido": "A03: Alumno/a 3."},
            {"nombre": "A04", "color": ft.Colors.ORANGE_100, "contenido": "A04: Alumno/a 4."}
        ],
        "Act": [
            {"nombre": "Act00", "color": ft.Colors.PURPLE_100, "contenido": "Act00: Gestor de actividades."},
            {"nombre": "Act01-all", "color": ft.Colors.PURPLE_100, "contenido": "Act01: Actividad todas."},
            {"nombre": "Act02-new", "color": ft.Colors.PURPLE_100, "contenido": "Act02: Actividades recientes."}
        ]
    }
    
    # Diccionarios para UI y contenido
    contenido_labels = {}
    sub_bloques_ui_dict = {}
    sub_bloques_labels_dict = {}
    carpetas_ui_dict = {}
    carpetas_labels_dict = {}
    
    # Controles dinámicos para el área de contenido
    bloques_row = ft.Row([], alignment=ft.MainAxisAlignment.CENTER, spacing=30)
    contenido_col = ft.Column([], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    # Variables de estado para el proyecto actual
    current_B_NAME = None
    current_P_NAME = None

    # --- UI DE CONFIGURACIÓN DE CLARA-ESO ---
    
    status_msg = ft.Text("", color=ft.Colors.BLUE_GREY_400, size=16) 
    
    # Nuevo control para la vista previa del contenido LOMLOE
    contenido_preview_label = ft.Container(
        content=ft.Column([
            ft.Text("Haz clic en una asignatura para ver su Enfoque Curricular (LOMLOE)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_600),
            ft.Text("", size=14, font_family="monospace", selectable=True, color=ft.Colors.BLACK, visible=False) # Contenido real
        ], horizontal_alignment=ft.CrossAxisAlignment.START, spacing=5),
        padding=ft.padding.all(10),
        margin=ft.margin.only(top=10),
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=8,
        width=600,
        visible=True 
    )

    def mostrar_contenido_asignatura(e):
        """Muestra el contenido LOMLOE de la asignatura seleccionada."""
        cb_label = e.control.label
        
        # Ocultar el contenido si se desmarca
        if not e.control.value:
            contenido_preview_label.content.controls[1].value = ""
            contenido_preview_label.content.controls[1].visible = False
            contenido_preview_label.content.controls[0].value = f"Haz clic en una asignatura para ver su Enfoque Curricular (LOMLOE)"
            page.update()
            return

        # Buscar el nombre clave en el archivo LOMLOE
        target_subject = ASIGNATURA_MAPPING.get(cb_label)
        contenido = ASIGNATURA_CONTENIDO_MAP.get(target_subject)

        if contenido:
            contenido_preview_label.content.controls[0].value = f"Enfoque Curricular: {target_subject}"
            contenido_preview_label.content.controls[1].value = contenido
            contenido_preview_label.content.controls[1].visible = True
        else:
            contenido_preview_label.content.controls[0].value = f"Enfoque Curricular: {cb_label}"
            contenido_preview_label.content.controls[1].value = "Contenido LOMLOE no encontrado para esta asignatura."
            contenido_preview_label.content.controls[1].visible = True
        page.update()


    asignaturas_checkboxes = []
    for a in ASIGNATURAS_DISPONIBLES:
        cb = ft.Checkbox(label=a, value=False, on_change=mostrar_contenido_asignatura)
        asignaturas_checkboxes.append(cb)

    proyecto_name_field = ft.TextField(label="Nombre del Proyecto (e.g., 'Clara100-2024')", width=400, visible=True)
    
    confirm_button = ft.ElevatedButton(
        "Crear Proyecto Clara 100 on-click",
        icon=ft.Icons.AUTO_AWESOME_OUTLINED,
    )
    
    clara_eso_config_ui = ft.Column(
        [
            ft.Text("Selecciona tus asignaturas (max 6 sugerido):", size=18, weight=ft.FontWeight.BOLD),
            ft.Row(asignaturas_checkboxes[:6], alignment=ft.MainAxisAlignment.CENTER, wrap=True, spacing=20),
            ft.Row(asignaturas_checkboxes[6:], alignment=ft.MainAxisAlignment.CENTER, wrap=True, spacing=20),
            contenido_preview_label, # Nueva vista previa
            proyecto_name_field,
            confirm_button,
            status_msg, 
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        visible=False
    )

    # ----------------------------------------------------
    # Funciones de Manejo de Eventos (UI)
    # ----------------------------------------------------

    def mostrar_carpeta(nombre_bloque, nombre_sub, carpeta):
        for lbl in carpetas_labels_dict.get(nombre_bloque, {}).get(nombre_sub, {}).values():
            lbl.visible = False
        
        if carpeta in carpetas_labels_dict.get(nombre_bloque, {}).get(nombre_sub, {}):
            lbl_control = carpetas_labels_dict[nombre_bloque][nombre_sub][carpeta]
            lbl_control.visible = True
            
            # --- LÓGICA PARA LOMLOE ---
            if nombre_bloque == "My" and nombre_sub == "ESO-Baleares" and carpeta == "LOMLOE":
                lbl_control.value = "B-ESO-Baleares.txt"
                lbl_control.italic = False
                lbl_control.color = ft.Colors.RED_ACCENT_700
            
            # --- LÓGICA PARA DATOS ESO-CLARA (Contenido LOMLOE precargado) ---
            elif carpeta == "Datos ESO-Clara" and nombre_bloque.startswith("B"):
                # Si el contenido ya está precargado, solo ajustamos el estilo.
                lbl_control.italic = False
                lbl_control.color = ft.Colors.BLUE_GREY_800
            
            # --- Restaurar el valor por defecto si no es un archivo específico
            else:
                contenido_default = f"{carpeta} de {nombre_sub} ({nombre_bloque})"
                # Solo restaurar el valor si no es el contenido largo de LOMLOE
                if lbl_control.value != contenido_default:
                     lbl_control.value = contenido_default
                lbl_control.italic = True
                lbl_control.color = ft.Colors.BLACK

        page.update()

    def mostrar_sub_bloque(nombre_bloque, nombre_sub):
        clara_eso_config_ui.visible = False
        status_msg.value = "" 
        
        for b in bloques_data:
            nombre_b = b["nombre"]
            for key in sub_bloques_labels_dict.get(nombre_b, {}):
                sub_bloques_labels_dict[nombre_b][key].visible = False
                for btn in carpetas_ui_dict.get(nombre_b, {}).get(key, []):
                    btn.visible = False
                for lbl in carpetas_labels_dict.get(nombre_b, {}).get(key, {}).values():
                    lbl.visible = False

        if nombre_bloque == "My" and nombre_sub == "Clara-eso":
            clara_eso_config_ui.visible = True
            sub_bloques_labels_dict[nombre_bloque][nombre_sub].visible = False 
            # Resetear la vista previa al entrar a Clara-eso
            contenido_preview_label.content.controls[0].value = "Haz clic en una asignatura para ver su Enfoque Curricular (LOMLOE)"
            contenido_preview_label.content.controls[1].value = ""
            contenido_preview_label.content.controls[1].visible = False
        elif nombre_sub in sub_bloques_labels_dict.get(nombre_bloque, {}):
            sub_bloques_labels_dict[nombre_bloque][nombre_sub].visible = True
            for btn in carpetas_ui_dict[nombre_bloque][nombre_sub]:
                btn.visible = True

        page.update()


    def mostrar_contenido(nombre):
        clara_eso_config_ui.visible = False
        status_msg.value = "" 

        for b in bloques_data:
            nombre_b = b["nombre"]
            contenido_labels[nombre_b].visible = (nombre_b == nombre)
            
            for i in range(len(sub_bloques_ui_dict.get(nombre_b, []))):
                sub_bloques_ui_dict[nombre_b][i].visible = (nombre_b == nombre)
            
            for sub in sub_bloques_dict.get(nombre_b, []):
                sub_name = sub["nombre"]
                if nombre_b in sub_bloques_labels_dict and sub_name in sub_bloques_labels_dict[nombre_b]:
                    sub_bloques_labels_dict[nombre_b][sub_name].visible = False
                    for btn in carpetas_ui_dict.get(nombre_b, {}).get(sub_name, []):
                        btn.visible = False
                    for lbl in carpetas_labels_dict.get(nombre_b, {}).get(sub_name, {}).values():
                        lbl.visible = False
        
        page.update()
    
    # --- Lógica de Creación Dinámica del Proyecto ---

    def crear_proyecto_clara100(e):
        nonlocal current_B_NAME, current_P_NAME 
        
        is_initial_call = (e is None)
        
        selected_asignaturas = [cb.label for cb in asignaturas_checkboxes if cb.value]
        num_asignaturas = len(selected_asignaturas)
        proyecto_name = proyecto_name_field.value.strip()

        # -------------------------------------------------------------------
        # 1. VALIDACIONES Y DEFINICIÓN DE NOMBRES
        # -------------------------------------------------------------------

        if is_initial_call:
            num_asignaturas = 0
            B_name = "B0"
            P_name = "P0" # Mantener P0 para no romper la lógica existente que usa P_NAME
            proyecto_name = "Proyecto NO CREADO"
        else:
            # Lógica para un click de usuario real (NO es la llamada inicial)
            if not selected_asignaturas:
                status_msg.value = "⚠️ Debes seleccionar al menos una asignatura para crear el proyecto."
                status_msg.color = ft.Colors.YELLOW_ACCENT_400
                page.update()
                return 
            
            if num_asignaturas > 6:
                status_msg.value = f"⚠️ Sugerencia: Elige menos de 6 asignaturas por proyecto. Has elegido {num_asignaturas}."
                status_msg.color = ft.Colors.RED_400
                page.update()
                return
            
            if not proyecto_name:
                status_msg.value = "⚠️ Por favor, dale un nombre al proyecto antes de confirmarlo."
                status_msg.color = ft.Colors.YELLOW_ACCENT_400
                page.update()
                return
            
            B_name = f"B{num_asignaturas}"
            P_name = f"P{num_asignaturas}" # Mantener P#

        current_B_NAME = B_name
        current_P_NAME = P_name

        # 2. GENERACIÓN DE NUEVOS BLOQUES DINÁMICOS (B# y P#)
        
        # Eliminar B y P anteriores si existen 
        bloques_data[:] = [b for b in bloques_data if not (b["nombre"].startswith("B") or b["nombre"].startswith("P"))]
        
        # Definiciones de los nuevos bloques (B0 y P0 en el inicio)
        nuevo_B = {"nombre": B_name, "display_name": B_name, "color": ft.Colors.BLUE_200, "contenido": f"Bloque {B_name}: Documentación básica para {proyecto_name} ({num_asignaturas} asignaturas)."}
        nuevo_P = {"nombre": P_name, "display_name": P_name, "color": ft.Colors.GREEN_200, "contenido": f"Bloque {P_name}: Profesores para {proyecto_name} ({num_asignaturas} asignaturas)."}

        bloques_data.insert(1, nuevo_B)
        bloques_data.insert(2, nuevo_P)
        
        # 3. GENERACIÓN DE SUB-BLOQUES DINÁMICOS

        sub_bloques_dict[B_name] = [{"nombre": "B00", "color": ft.Colors.BLUE_300, "contenido": "B00: Datos básicos del proyecto."}]
        sub_bloques_dict[P_name] = [{"nombre": "P00", "color": ft.Colors.GREEN_100, "contenido": "P00: Profesor-super."}]

        for i, asig in enumerate(selected_asignaturas, start=1):
            sub_B_name = f"B0{i}"
            
            sub_bloques_dict[B_name].append({
                "nombre": sub_B_name, "color": ft.Colors.BLUE_300, 
                "contenido": f"{sub_B_name}: {asig} (Documentación)."
            })
            
            sub_P_name = f"P0{i}"
            sub_bloques_dict[P_name].append({
                "nombre": sub_P_name, "color": ft.Colors.GREEN_100, 
                "contenido": f"{sub_P_name}: Profesor/a de {asig}."
            })

        # 4. RECONSTRUCCIÓN DE LA UI (Generar elementos visuales para B# y P#)
        
        # --- Lógica de B# ---
        
        name = B_name
        bloque_def = nuevo_B
        
        contenido_labels[name] = ft.Text(bloque_def["contenido"], size=18, visible=False)
        sub_bloques_ui_dict[name] = []
        sub_bloques_labels_dict[name] = {}
        carpetas_ui_dict[name] = {}
        carpetas_labels_dict[name] = {}
        
        for i, sub in enumerate(sub_bloques_dict[name]):
            nombre_sub = sub["nombre"]
            
            sub_bloques_ui_dict[name].append(
                ft.Container(
                    content=ft.Text(nombre_sub, size=18, weight=ft.FontWeight.BOLD),
                    bgcolor=sub["color"],
                    on_click=lambda e, n=name, s=nombre_sub: mostrar_sub_bloque(n, s),
                    **sub_bloque_style
                )
            )
            
            sub_bloques_labels_dict[name][nombre_sub] = ft.Text(sub["contenido"], size=16, visible=False)
            
            carpetas_ui_dict[name][nombre_sub] = []
            carpetas_labels_dict[name][nombre_sub] = {}
            
            current_carpetas = get_carpetas(name, nombre_sub, B_name, P_name)

            # Asignatura real correspondiente al sub-bloque B0X
            asig_name = selected_asignaturas[i-1] if i > 0 and i <= len(selected_asignaturas) else None
            lomloe_key = ASIGNATURA_MAPPING.get(asig_name)
            lomloe_content = ASIGNATURA_CONTENIDO_MAP.get(lomloe_key, f"No se encontró contenido LOMLOE para {asig_name}.")

            for carpeta in current_carpetas:
                is_interactive = nombre_sub.startswith("B0") and nombre_sub != "B00"
                
                if is_interactive:
                    carpeta_control = ft.ElevatedButton(
                        carpeta,
                        on_click=lambda e, nb=name, s=nombre_sub, c=carpeta: mostrar_carpeta(nb, s, c),
                        visible=False
                    )
                else:
                    carpeta_control = ft.Text(f"📁 {carpeta}", size=15, visible=False)
                
                carpetas_ui_dict[name][nombre_sub].append(carpeta_control)
                
                if carpeta == "Datos ESO-Clara" and nombre_sub != "B00":
                    # CARGAR CONTENIDO LOMLOE EN EL VALOR DEL LABEL
                    contenido_label_value = lomloe_content
                    is_italic = False
                else:
                    contenido_label_value = f"{carpeta} de {nombre_sub} ({name})"
                    is_italic = True
                    
                carpetas_labels_dict[name][nombre_sub][carpeta] = ft.Text(
                    contenido_label_value, size=15, italic=is_italic, visible=False
                )
        
        # --- Lógica de P# (Se reconstruye para mantener el flujo) ---
        
        name = P_name
        bloque_def = nuevo_P
        
        contenido_labels[name] = ft.Text(bloque_def["contenido"], size=18, visible=False)
        sub_bloques_ui_dict[name] = []
        sub_bloques_labels_dict[name] = {}
        carpetas_ui_dict[name] = {}
        carpetas_labels_dict[name] = {}
        
        for sub in sub_bloques_dict[name]:
            nombre_sub = sub["nombre"]
            
            sub_bloques_ui_dict[name].append(
                ft.Container(
                    content=ft.Text(nombre_sub, size=18, weight=ft.FontWeight.BOLD),
                    bgcolor=sub["color"],
                    on_click=lambda e, n=name, s=nombre_sub: mostrar_sub_bloque(n, s),
                    **sub_bloque_style
                )
            )
            
            sub_bloques_labels_dict[name][nombre_sub] = ft.Text(sub["contenido"], size=16, visible=False)
            
            carpetas_ui_dict[name][nombre_sub] = []
            carpetas_labels_dict[name][nombre_sub] = {}
            
            current_carpetas = get_carpetas(name, nombre_sub, B_name, P_name)

            for carpeta in current_carpetas:
                # Los P# no tienen "Datos ESO-Clara"
                carpeta_control = ft.Text(f"📁 {carpeta}", size=15, visible=False)
                
                carpetas_ui_dict[name][nombre_sub].append(carpeta_control)
                
                contenido = f"{carpeta} de {nombre_sub} ({name})"
                carpetas_labels_dict[name][nombre_sub][carpeta] = ft.Text(
                    contenido, size=15, italic=True, visible=False
                )


        # 5. ACTUALIZACIÓN DEL LAYOUT PRINCIPAL (Re-dibujar Rows y Columna de contenido)
        
        bloques_row.controls.clear()
        for bloque in bloques_data:
            display_name = "Myeso-click" if bloque["nombre"] == "My" else bloque["display_name"]
            bloques_row.controls.append(
                ft.Container(
                    content=ft.Text(display_name, size=22, weight=ft.FontWeight.BOLD),
                    bgcolor=bloque["color"],
                    on_click=lambda e, n=bloque["nombre"]: mostrar_contenido(n),
                    **bloque_style
                )
            )

        contenido_col.controls.clear()
        contenido_col.controls.append(clara_eso_config_ui)
        
        for b in bloques_data:
            nombre_b = b["nombre"]
            
            contenido_col.controls.append(contenido_labels[nombre_b])
            
            sub_bloques_row = ft.Row(sub_bloques_ui_dict.get(nombre_b, []), alignment=ft.MainAxisAlignment.CENTER, spacing=10)
            contenido_col.controls.append(sub_bloques_row)
            
            for sub in sub_bloques_dict.get(nombre_b, []):
                nombre_sub = sub["nombre"]
                if nombre_b in sub_bloques_labels_dict and nombre_sub in sub_bloques_labels_dict[nombre_b]:
                    contenido_col.controls.append(sub_bloques_labels_dict[nombre_b][nombre_sub])
                    
                    carpetas_row = ft.Row(carpetas_ui_dict[nombre_b][nombre_sub], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
                    contenido_col.controls.append(carpetas_row)
                    
                    for lbl in carpetas_labels_dict[nombre_b][nombre_sub].values():
                        contenido_col.controls.append(lbl)

        # 6. CONFIGURACIÓN FINAL DE VISIBILIDAD Y MENSAJE

        if is_initial_call:
            contenido_labels["My"].visible = True 
            for sub in sub_bloques_ui_dict["My"]:
                sub.visible = True
            
            status_msg.value = "¡Bienvenido! Haz clic en Myeso-click y luego en 'Clara-eso' para comenzar tu proyecto."
            status_msg.color = ft.Colors.BLUE_GREY_400
        else:
            clara_eso_config_ui.visible = False
            status_msg.value = f"✅ ¡Proyecto '{B_name} - {proyecto_name}' creado con éxito! Tienes el nuevo bloque {B_name}. Haz clic para ver el contenido curricular."
            status_msg.color = ft.Colors.GREEN_400
            
            for cb in asignaturas_checkboxes:
                cb.value = False
            
        page.update()

    confirm_button.on_click = crear_proyecto_clara100
    
    # --- Setup Inicial de la UI (Solo crea los controles fijos) ---
    
    for bloque in bloques_data:
        nombre_bloque = bloque["nombre"]
        
        sub_bloques = sub_bloques_dict.get(nombre_bloque, [])
        sub_bloques_ui_dict[nombre_bloque] = []
        sub_bloques_labels_dict[nombre_bloque] = {}
        carpetas_ui_dict[nombre_bloque] = {}
        carpetas_labels_dict[nombre_bloque] = {}
        
        contenido_labels[nombre_bloque] = ft.Text(bloque["contenido"], size=18, visible=False)


        for sub in sub_bloques:
            nombre_sub = sub["nombre"]
            
            sub_bloques_labels_dict[nombre_bloque][nombre_sub] = ft.Text(
                sub["contenido"], size=16, visible=False
            )
            
            sub_bloques_ui_dict[nombre_bloque].append(
                ft.Container(
                    content=ft.Text(nombre_sub, size=18, weight=ft.FontWeight.BOLD),
                    bgcolor=sub["color"],
                    on_click=lambda e, n=nombre_bloque, s=nombre_sub: mostrar_sub_bloque(n, s),
                    **sub_bloque_style
                )
            )

            carpetas_ui_dict[nombre_bloque][nombre_sub] = []
            carpetas_labels_dict[nombre_bloque][nombre_sub] = {}
            current_carpetas = get_carpetas(nombre_bloque, nombre_sub)

            for carpeta in current_carpetas:
                # LÓGICA AGREGADA/MODIFICADA PARA CARPETAS FIJAS (solo LOMLOE aquí)
                is_interactive_lo_ml_oe = (nombre_bloque == "My" and nombre_sub == "ESO-Baleares" and carpeta == "LOMLOE")
                
                if is_interactive_lo_ml_oe:
                    carpeta_control = ft.ElevatedButton(
                        carpeta,
                        on_click=lambda e, nb=nombre_bloque, s=nombre_sub, c=carpeta: mostrar_carpeta(nb, s, c),
                        visible=False
                    )
                else:
                    carpeta_control = ft.Text(f"📁 {carpeta}", size=15, visible=False)
                
                carpetas_ui_dict[nombre_bloque][nombre_sub].append(carpeta_control)
                
                contenido = f"{carpeta} de {nombre_sub} ({nombre_bloque})"
                carpetas_labels_dict[nombre_bloque][nombre_sub][carpeta] = ft.Text(
                    contenido, size=15, italic=True, visible=False
                )

    # 7. Ejecutar la construcción del layout (el corazón de la solución)
    crear_proyecto_clara100(None)
    
    page.add(
        ft.Column(
            [
                ft.Text("Clara 100: Mi 'eso-click'", size=30, weight=ft.FontWeight.BOLD),
                ft.Container(
                    content=ft.Text(
                        "Clara 100 es una app educativa para organizar y aprender ESO de forma divertida y personalizada. "
                        "Explora los bloques, accede a recursos, actividades y... crea tu propio camino de aprendizaje.",
                        size=18,
                        color=ft.Colors.WHITE,
                        italic=True
                    ),
                    padding=ft.padding.all(12),
                    bgcolor=ft.Colors.BLUE_GREY_700,
                    border_radius=8,
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(bottom=10)
                ),
                bloques_row, # Fila de los bloques principales
                ft.Divider(height=20, color="transparent"),
                contenido_col
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)