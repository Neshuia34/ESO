import flet as ft

def main(page: ft.Page):
    page.title = "Clara 100: Mi 'eso-click'"
    page.window_width = 800
    page.window_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # Nombres y colores de los bloques
    bloques = [
        {"nombre": "B6", "color": ft.Colors.BLUE_200, "contenido": "Bloque B6: Documentación básica y asignaturas."},
        {"nombre": "P6", "color": ft.Colors.GREEN_200, "contenido": "Bloque P6: Profesores."},
        {"nombre": "A4", "color": ft.Colors.ORANGE_200, "contenido": "Bloque A4: Alumnos participantes."},
        {"nombre": "Act", "color": ft.Colors.PURPLE_200, "contenido": "Bloque Act: Actividades del proyecto."}
    ]

    # Diccionario para mostrar el contenido al hacer click
    contenido_labels = {}
    for bloque in bloques:
        contenido_labels[bloque["nombre"]] = ft.Text(
            bloque["contenido"], size=18, visible=False
        )

    # Función para mostrar el contenido del bloque seleccionado
    def mostrar_contenido(nombre):
        for b in bloques:
            contenido_labels[b["nombre"]].visible = (b["nombre"] == nombre)
        page.update()

    # Crear los bloques visuales
    bloques_ui = []
    for bloque in bloques:
        bloques_ui.append(
            ft.Container(
                content=ft.Text(bloque["nombre"], size=22, weight=ft.FontWeight.BOLD),
                width=150,
                height=100,
                bgcolor=bloque["color"],
                border_radius=12,
                alignment=ft.alignment.center,
                ink=True,
                on_click=lambda e, n=bloque["nombre"]: mostrar_contenido(n),
                border=ft.border.all(2, ft.Colors.BLUE_GREY_400),
            )
        )

    # Layout principal
    page.add(
        ft.Column(
            [
                ft.Text("Clara 100: Mi 'eso-click'", size=30, weight=ft.FontWeight.BOLD),
                ft.Row(bloques_ui, alignment=ft.MainAxisAlignment.CENTER, spacing=30),
                ft.Divider(height=20, color="transparent"),
                *contenido_labels.values()
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)