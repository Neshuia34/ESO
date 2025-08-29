# ...existing code...
# Incorporamos contenido en B.6
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

    # Contenido de ejemplo para cada carpeta de cada bloque (puedes personalizar)
    contenido_carpetas = {
        "B.01 Inglés avanzado": {
            "ESO-Clara": "Contenidos de ESO-Clara para Inglés avanzado.",
            "Clara 100": "Contenidos de Clara 100 para Inglés avanzado.",
            "Clara 100_in": "Contenidos de Clara 100_in para Inglés avanzado."
        },
        "B.02 Català": {
            "ESO-Clara": "Contenidos de ESO-Clara para Català.",
            "Clara 100": "Contenidos de Clara 100 para Català.",
            "Clara 100_in": "Contenidos de Clara 100_in para Català."
        },
        "B.03 Castellano": {
            "ESO-Clara": "Contenidos de ESO-Clara para Castellano.",
            "Clara 100": "Contenidos de Clara 100 para Castellano.",
            "Clara 100_in": "Contenidos de Clara 100_in para Castellano."
        },
        "B.04 Matemáticas": {
            "ESO-Clara": "Contenidos de ESO-Clara para Matemáticas.",
            "Clara 100": "Contenidos de Clara 100 para Matemáticas.",
            "Clara 100_in": "Contenidos de Clara 100_in para Matemáticas."
        },
        "B.05 Tecnología y Digitalización": {
            "ESO-Clara": "Contenidos de ESO-Clara para Tecnología y Digitalización.",
            "Clara 100": "Contenidos de Clara 100 para Tecnología y Digitalización.",
            "Clara 100_in": "Contenidos de Clara 100_in para Tecnología y Digitalización."
        },
        "B.06 Física y Química": {
            "ESO-Clara": "Contenidos de ESO-Clara para Física y Química.",
            "Clara 100": "Contenidos de Clara 100 para Física y Química.",
            "Clara 100_in": "Contenidos de Clara 100_in para Física y Química."
        }
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
#creando carpetas dentro de B.6.
     # ...existing code...