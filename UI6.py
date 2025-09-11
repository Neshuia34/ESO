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

    # Diccionario para guardar el contenido visible de cada bloque
    bloques_contenido = {}

    # Función para alternar visibilidad del contenido de cada bloque
    def make_on_click(bloque_nombre):
        def on_click(e):
            for nombre, contenido in bloques_contenido.items():
                contenido.visible = (nombre == bloque_nombre)
            page.update()
        return on_click

    # Crear los bloques y su contenido
    bloques_ui = []
    for nombre in bloques_nombres:
        contenido = ft.Text(
            f"¡Contenido de {nombre}!",
            visible=False,
            text_align=ft.TextAlign.CENTER
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
            width=150,
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
    #Hoy 'Add documents', .txt.
# ...existing code...