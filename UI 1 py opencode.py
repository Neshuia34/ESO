import flet as ft

def main(page: ft.Page):
    page.title = "ESO-Clara 100: La ESO de Bolsillo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 800
    page.window_height = 600

    # Contenido del bloque Clara 100 00 (inicialmente vacío)
    clara_100_00_content = ft.Text(
        "Clara 100 00 está vacío por ahora. ¡Es nuestro cerebro del proyecto!",
        visible=False, # Inicialmente oculto
        text_align=ft.TextAlign.CENTER
    )

    # Función que se ejecuta al hacer click en el bloque
    def on_clara_100_00_click(e):
        clara_100_00_content.visible = not clara_100_00_content.visible # Alternar visibilidad
        page.update() # Actualizar la página para que se vea el cambio

    # El bloque Clara 100 00 como un Contenedor clickeable
    clara_100_00_block = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Clara 100 00",
                    size=24,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Text(" (Haz click para ver su contenido)"),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        width=300,
        height=150,
        bgcolor=ft.Colors.BLUE_GREY_100,
        alignment=ft.alignment.center,
        border_radius=10,
        on_click=on_clara_100_00_click, # Asignar la función al click
        ink=True, # Efecto visual al clickear
        border=ft.border.all(2, ft.Colors.BLUE_GREY_400),
    )

    # Añadir los elementos a la página
    page.add(
        ft.Column(
            [
                ft.Text(
                    "ESO-Clara 100: La ESO de Bolsillo",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(height=30, color="transparent"), # Espacio
                clara_100_00_block, # El bloque clickeable
                ft.Divider(height=20, color="transparent"), # Espacio
                clara_100_00_content # El contenido que aparece/desaparece
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
    )

if __name__ == "__main__":
    ft.app(target=main)