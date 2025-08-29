# ...existing code...
# Incorporamos contenido en B.6 a partir del .txt.
import flet as ft

def main(page: ft.Page):
    page.title = "ESO-Clara 100: La ESO de Bolsillo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 800
    page.window_height = 600

    # Nombres de los 7 bloques con asignaturas
    bloques_nombres = [
        "B.00",
        "B.01 Inglés avanzado",
        "B.02 Català",
        "B.03 Castellano",
        "B.04 Matemáticas",
        "B.05 Tecnología y Digitalización",
        "B.06 Física y Química"
    ]

    carpetas = ["ESO-Clara", "Clara 100", "Clara 100_in"]

    # Contenido real para la carpeta ESO-Clara de cada asignatura (extraído de B.6 asignaturas.txt)
    contenido_eso_clara = {
        "B.01 Inglés avanzado": """Objetivos de Aprendizaje:
- Comprender y producir textos orales y escritos complejos.
- Usar tiempos verbales avanzados (Past Perfect, Future Continuous, etc.).
- Aplicar estructuras gramaticales avanzadas (oraciones de relativo, estilo indirecto).
- Participar en debates y presentaciones.
- Producir textos escritos extensos y coherentes.
- Ampliar vocabulario sobre temas abstractos, sociales y culturales.

Contenidos Clave:
- Gramática avanzada: Past Perfect, Future Continuous, Future Perfect, Third Conditional, Relative Clauses, Reported Speech.
- Habilidades comunicativas: comprensión oral y escrita, producción oral y escrita.
- Léxico: vocabulario temático, expresiones para opinar, sugerir, predecir.

Actividades Didácticas:
- Ejercicios de gramática avanzada.
- Role-plays usando estilo indirecto y oraciones de relativo.
- Comprensión auditiva y lectora con preguntas de inferencia.
- Debates y presentaciones.
- Redacción de resúmenes y ensayos.
- Visual storytelling y "chain story".
""",
        "B.02 Català": """Objetivos de Aprendizaje:
- Analizar textos literarios catalanes y su contexto.
- Realizar análisis sintáctico de oraciones complejas.
- Exponer temas sociolingüísticos.
- Consolidar la norma lingüística y ampliar el léxico.

Contenidos Clave:
- Literatura catalana, análisis sintáctico, sociolingüística, vocabulario avanzado.

Actividades Didácticas:
- Comentarios de texto.
- Ejercicios de análisis sintáctico.
- Debates sobre temas sociolingüísticos.
- Redacción de textos argumentativos.
""",
        "B.03 Castellano": """Objetivos de Aprendizaje:
- Analizar textos literarios y no literarios.
- Profundizar en la gramática y sintaxis del español.
- Desarrollar la expresión oral y escrita.

Contenidos Clave:
- Literatura española, gramática avanzada, comprensión lectora y auditiva.

Actividades Didácticas:
- Análisis de textos.
- Ejercicios de gramática y sintaxis.
- Exposiciones orales y debates.
- Escritura de ensayos y relatos.
""",
        "B.04 Matemáticas": """Objetivos de Aprendizaje:
- Resolver problemas matemáticos complejos.
- Aplicar conceptos de álgebra, geometría y estadística.
- Desarrollar el razonamiento lógico y abstracto.

Contenidos Clave:
- Álgebra, geometría, funciones, estadística y probabilidad.

Actividades Didácticas:
- Resolución de problemas.
- Proyectos matemáticos.
- Uso de herramientas digitales.
- Presentación de soluciones.
""",
        "B.05 Tecnología y Digitalización": """Objetivos de Aprendizaje:
- Comprender los fundamentos de la tecnología y la informática.
- Aplicar conocimientos en proyectos digitales.
- Desarrollar habilidades de programación y robótica.

Contenidos Clave:
- Hardware, software, programación, robótica, seguridad digital.

Actividades Didácticas:
- Proyectos de programación.
- Montaje de circuitos.
- Simulaciones y uso de software.
- Debates sobre tecnología y sociedad.
""",
        "B.06 Física y Química": """Objetivos de Aprendizaje:
- Comprender los principios básicos de la física y la química.
- Aplicar el método científico en experimentos.
- Analizar fenómenos naturales y tecnológicos.

Contenidos Clave:
- Mecánica, electricidad, química inorgánica y orgánica.

Actividades Didácticas:
- Experimentos de laboratorio.
- Resolución de problemas.
- Proyectos de investigación.
- Presentaciones orales.
"""
    }

    # Contenido de ejemplo para cada carpeta de cada bloque
    contenido_carpetas = {}
    for nombre in bloques_nombres:
        if nombre == "B.00":
            continue
        contenido_carpetas[nombre] = {
            "ESO-Clara": contenido_eso_clara.get(nombre, "Sin contenido aún."),
            "Clara 100": f"Contenidos de Clara 100 para {nombre.split(' ',1)[1]}.",
            "Clara 100_in": f"Contenidos de Clara 100_in para {nombre.split(' ',1)[1]}."
        }

    # Diccionario para guardar el contenido visible de cada bloque
    bloques_contenido = {}

    # Estado para saber qué carpeta está activa en cada bloque
    carpetas_activas = {}

    # Función para alternar visibilidad del contenido de cada bloque
    def make_on_click(bloque_nombre):
        def on_click(e):
            for nombre, contenido in bloques_contenido.items():
                contenido.visible = (nombre == bloque_nombre)
            page.update()
        return on_click

    # Función para manejar click en carpeta
    def make_on_carpeta_click(bloque_nombre, carpeta_nombre, contenido_label):
        def on_click(e):
            carpetas_activas[bloque_nombre] = carpeta_nombre
            contenido_label.value = contenido_carpetas[bloque_nombre][carpeta_nombre]
            page.update()
        return on_click

    # Crear los bloques y su contenido
    bloques_ui = []
    for nombre in bloques_nombres:
        if nombre == "B.00":
            contenido = ft.Text(
                "¡Contenido de B.00!",
                visible=False,
                text_align=ft.TextAlign.CENTER
            )
        else:
            # Por defecto, carpeta activa es la primera
            carpetas_activas[nombre] = carpetas[0]
            contenido_label = ft.Text(
                contenido_carpetas[nombre][carpetas[0]],
                size=14
            )
            carpetas_row = ft.Row(
                [
                    ft.ElevatedButton(
                        carpeta,
                        on_click=make_on_carpeta_click(nombre, carpeta, contenido_label),
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.BLUE_GREY_200,
                            color=ft.Colors.BLACK
                        )
                    ) for carpeta in carpetas
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            )
            contenido = ft.Column(
                [
                    ft.Text("Carpetas:", size=16, weight=ft.FontWeight.BOLD),
                    carpetas_row,
                    ft.Divider(height=10, color="transparent"),
                    contenido_label
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                visible=False
            )
        bloques_contenido[nombre] = contenido

        bloque = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        nombre,
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            width=180,
            height=100,
            bgcolor=ft.Colors.BLUE_GREY_100,
            alignment=ft.alignment.center,
            border_radius=10,
            on_click=make_on_click(nombre),
            ink=True,
            border=ft.border.all(2, ft.Colors.BLUE_GREY_400),
        )
        bloques_ui.append(bloque)

    # Layout principal
    page.add(
        ft.Column(
            [
                ft.Text(
                    "ESO-Clara 100: La ESO de Bolsillo",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30, color="transparent"),
                ft.Row(
                    bloques_ui,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Divider(height=20, color="transparent"),
                # Mostrar el contenido del bloque seleccionado
                *bloques_contenido.values()
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
    )

if __name__ == "__main__":
    ft.app(target=main)

    # Muy bien, ya tenemos la UI.
    # Ahora creamos contenido en las carpetas desde el '.txt' .
# ...existing code...  