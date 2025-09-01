import flet as ft

def main(page: ft.Page):
    page.title = "Clara 100 00 - Lección Python/Flet"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    page.padding = 20

    # ESTILOS reutilizables
    COLOR_BLOQUE = ft.Colors.BLUE_100
    COLOR_BORDE_BLOQUE = ft.Colors.BLUE_400
    COLOR_CARPETA = ft.Colors.AMBER_100
    COLOR_BORDE_CARPETA = ft.Colors.AMBER_400
    TEXT_COLOR = ft.Colors.BLACK

    # Crea un "icono" tipo carpeta como Container
    def carpeta(nombre: str) -> ft.Container:
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(name=ft.Icons.FOLDER, color=TEXT_COLOR, size=18),
                    ft.Text(nombre, color=TEXT_COLOR, size=14, weight=ft.FontWeight.W_500),
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=COLOR_CARPETA,
            border=ft.border.all(1, COLOR_BORDE_CARPETA),
            border_radius=6,
            padding=8,
            # futuro: on_click para abrir carpeta o gestionar datos
        )

    # Construye un bloque con su número y dos "carpetas" internas
    def bloque_interno(numero: int) -> ft.Container:
        titulo = ft.Text(f"{numero:02d}", size=18, weight=ft.FontWeight.BOLD, color=TEXT_COLOR)

        # Dos carpetas dentro del bloque
        carpetas = ft.Column(
            [
                carpeta("Eso Clara 3ro"),
                carpeta("Material Clara 100"),
            ],
            spacing=6,
            tight=True,
        )

        # Estructura del bloque
        return ft.Container(
            content=ft.Column(
                [
                    titulo,
                    carpetas,
                ],
                spacing=8,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            width=180,
            bgcolor=COLOR_BLOQUE,
            border=ft.border.all(1, COLOR_BORDE_BLOQUE),
            border_radius=8,
            padding=10,
        )

    # Los seis bloques (01 a 06)
    bloques_internos = [bloque_interno(i) for i in range(1, 7)]

    # Contenido que se muestra/oculta al hacer clic en "Clara 100 00"
    clara_100_00_content = ft.Column(
    controls=bloques_internos,
    spacing=12,
    visible=False,  # inicialmente oculto
)


    # Alternar visibilidad al hacer clic
    def on_clara_100_00_click(e):
        clara_100_00_content.visible = not clara_100_00_content.visible
        page.update()

    # Bloque principal "Clara 100 00"
    clara_100_00_block = ft.Container(
        content=ft.Column(
            [
                ft.Text("Clara 100 00", size=24, weight=ft.FontWeight.BOLD, color=TEXT_COLOR),
                ft.Text("(Haz click para ver su contenido)", color=TEXT_COLOR),
                clara_100_00_content,  # Aquí van los 6 bloques con sus "carpetas"
            ],
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        width=700,
        bgcolor=ft.Colors.BLUE_GREY_100,
        alignment=ft.alignment.top_center,
        border_radius=10,
        on_click=on_clara_100_00_click,
        ink=True,
        border=ft.border.all(2, ft.Colors.BLUE_GREY_400),
        padding=16,
    )

    page.add(clara_100_00_block)

ft.app(target=main)
