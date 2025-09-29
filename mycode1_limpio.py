import flet as ft

def main(page: ft.Page):
    page.title = "Clara 100: Mi 'eso-click'"
    page.window_width = 800
    page.window_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # Bloques principales
    bloques = [
        {"nombre": "B6", "color": ft.Colors.BLUE_200, "contenido": "Bloque B6: Documentación básica y asignaturas."},
        {"nombre": "P6", "color": ft.Colors.GREEN_200, "contenido": "Bloque P6: Profesores."},
        {"nombre": "A4", "color": ft.Colors.ORANGE_200, "contenido": "Bloque A4: Alumnos participantes."},
        {"nombre": "Act", "color": ft.Colors.PURPLE_200, "contenido": "Bloque Act: Actividades del proyecto."}
    ]

    # Sub-bloques de cada bloque principal
    sub_bloques_dict = {
        "B6": [
            {"nombre": "B00", "color": ft.Colors.BLUE_100, "contenido": "B00: Datos básicos del proyecto."},
            {"nombre": "B01", "color": ft.Colors.BLUE_100, "contenido": "B01: Inglés avanzado."},
            {"nombre": "B02", "color": ft.Colors.BLUE_100, "contenido": "B02: Digitalización."},
            {"nombre": "B03", "color": ft.Colors.BLUE_100, "contenido": "B03: Castellano."},
            {"nombre": "B04", "color": ft.Colors.BLUE_100, "contenido": "B04: Matemáticas."},
            {"nombre": "B05", "color": ft.Colors.BLUE_100, "contenido": "B05: Tecnología ."},
            {"nombre": "B06", "color": ft.Colors.BLUE_100, "contenido": "B06: Física y Química."}
        ],
        "P6": [
            {"nombre": "P00", "color": ft.Colors.GREEN_100, "contenido": "P00: Profesor-super."},
            {"nombre": "P01", "color": ft.Colors.GREEN_100, "contenido": "P01: Profesor/a de Inglés."},
            {"nombre": "P02", "color": ft.Colors.GREEN_100, "contenido": "P02: Profesor/a de Digitalización"},
            {"nombre": "P03", "color": ft.Colors.GREEN_100, "contenido": "P03: Profesor/a de Castellano."},
            {"nombre": "P04", "color": ft.Colors.GREEN_100, "contenido": "P04: Profesor/a de Matemáticas."},
            {"nombre": "P05", "color": ft.Colors.GREEN_100, "contenido": "P05: Profesor/a de Tecnología ."},
            {"nombre": "P06", "color": ft.Colors.GREEN_100, "contenido": "P06: Profesor/a de Física y Química."}
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

    # Carpetas para los sub-bloques
    carpetas = ["Datos_oficiles", "Datos Clara 100", "Clara_m"]

    # Diccionarios para UI y contenido
    contenido_labels = {}
    sub_bloques_ui_dict = {}
    sub_bloques_labels_dict = {}
    carpetas_ui_dict = {}
    carpetas_labels_dict = {}

    for bloque in bloques:
        nombre_bloque = bloque["nombre"]
        contenido_labels[nombre_bloque] = ft.Text(
            bloque["contenido"], size=18, visible=False
        )
        sub_bloques = sub_bloques_dict.get(nombre_bloque, [])
        sub_bloques_ui = []
        sub_bloques_labels = {}
        carpetas_ui = {}
        carpetas_labels = {}

        for sub in sub_bloques:
            sub_bloques_labels[sub["nombre"]] = ft.Text(
                sub["contenido"], size=16, visible=False
            )
            sub_bloques_ui.append(
                ft.Container(
                    content=ft.Text(sub["nombre"], size=18, weight=ft.FontWeight.BOLD),
                    width=120,
                    height=70,
                    bgcolor=sub["color"],
                    border_radius=10,
                    alignment=ft.alignment.center,
                    ink=True,
                    on_click=lambda e, n=nombre_bloque, s=sub["nombre"]: mostrar_sub_bloque(n, s),
                    border=ft.border.all(2, ft.Colors.BLUE_GREY_200),
                    visible=False
                )
            )
            # Carpetas por bloque y sub-bloque
            if nombre_bloque == "B6":
                if sub["nombre"] == "B00":
                    carpetas_ui[sub["nombre"]] = []
                    carpetas_labels[sub["nombre"]] = {}
                    b00_carpetas = ["B00", "B00-01", "Clara-m"]
                    for carpeta in b00_carpetas:
                        carpetas_ui[sub["nombre"]].append(ft.Text(f"{carpeta}", size=15, visible=True))
                        carpetas_labels[sub["nombre"]][carpeta] = ft.Text(f"{carpeta} de {sub['nombre']} ({nombre_bloque})", size=15, visible=True)
                else:
                    carpetas_ui[sub["nombre"]] = []
                    carpetas_labels[sub["nombre"]] = {}
                    for carpeta in carpetas:
                        carpetas_ui[sub["nombre"]].append(
                            ft.ElevatedButton(
                                carpeta,
                                on_click=lambda e, nb=nombre_bloque, s=sub["nombre"], c=carpeta: mostrar_carpeta(nb, s, c),
                                visible=False
                            )
                        )
                        contenido = f"{carpeta} de {sub['nombre']} ({nombre_bloque})"
                        carpetas_labels[sub["nombre"]][carpeta] = ft.Text(
                            contenido, size=15, visible=False
                        )
            elif nombre_bloque == "P6":
                if sub["nombre"] == "P00":
                    carpetas_ui[sub["nombre"]] = []
                    carpetas_labels[sub["nombre"]] = {}
                    p00_carpetas = ["actualizar B00", "crear Actividades", "Clara-m"]
                    for carpeta in p00_carpetas:
                        carpetas_ui[sub["nombre"]].append(ft.Text(f"{carpeta}", size=15, visible=True))
                        carpetas_labels[sub["nombre"]][carpeta] = ft.Text(f"{carpeta} de {sub['nombre']} ({nombre_bloque})", size=15, visible=True)
                else:
                    carpetas_ui[sub["nombre"]] = []
                    carpetas_labels[sub["nombre"]] = {}
                    p_carpetas = ["myClara100", "myAct", "myClara-m"]
                    for carpeta in p_carpetas:
                        carpetas_ui[sub["nombre"]].append(ft.Text(f"{carpeta}", size=15, visible=True))
                        carpetas_labels[sub["nombre"]][carpeta] = ft.Text(f"{carpeta} de {sub['nombre']} ({nombre_bloque})", size=15, visible=True)
            elif nombre_bloque == "A4":
                carpetas_ui[sub["nombre"]] = []
                carpetas_labels[sub["nombre"]] = {}
                if sub["nombre"] == "A00":
                    a00_carpetas = ["myReadme", "Clara-m"]
                    for carpeta in a00_carpetas:
                        carpetas_ui[sub["nombre"]].append(ft.Text(f"{carpeta}", size=15, visible=True))
                        carpetas_labels[sub["nombre"]][carpeta] = ft.Text(f"{carpeta} de {sub['nombre']}", size=15, visible=True)
                else:
                    a_carpetas = ["mi perfil", "mytools", "myact"]
                    for carpeta in a_carpetas:
                        carpetas_ui[sub["nombre"]].append(ft.Text(f"{carpeta}", size=15, visible=True))
                        carpetas_labels[sub["nombre"]][carpeta] = ft.Text(f"{carpeta} de {sub['nombre']}", size=15, visible=True)
            elif nombre_bloque == "Act":
                carpetas_ui[sub["nombre"]] = []
                carpetas_labels[sub["nombre"]] = {}
                if sub["nombre"] == "Act00":
                    act00_carpetas = ["Act00"]
                    for carpeta in act00_carpetas:
                        carpetas_ui[sub["nombre"]].append(ft.Text(f"{carpeta}", size=15, visible=True))
                        carpetas_labels[sub["nombre"]][carpeta] = ft.Text(f"{carpeta} de {sub['nombre']} ({nombre_bloque})", size=15, visible=True)
                else:
                    act_carpetas = ["Act01 all", "Act02 new"]
                    for carpeta in act_carpetas:
                        carpetas_ui[sub["nombre"]].append(ft.Text(f"{carpeta}", size=15, visible=True))
                        carpetas_labels[sub["nombre"]][carpeta] = ft.Text(f"{carpeta} de {sub['nombre']} ({nombre_bloque})", size=15, visible=True)

        sub_bloques_ui_dict[nombre_bloque] = sub_bloques_ui
        sub_bloques_labels_dict[nombre_bloque] = sub_bloques_labels
        carpetas_ui_dict[nombre_bloque] = carpetas_ui
        carpetas_labels_dict[nombre_bloque] = carpetas_labels

    # Función para mostrar el contenido del bloque seleccionado
    def mostrar_contenido(nombre):
        for b in bloques:
            contenido_labels[b["nombre"]].visible = (b["nombre"] == nombre)
            # Mostrar sub-bloques solo para el bloque seleccionado
            for i, sub in enumerate(sub_bloques_dict.get(b["nombre"], [])):
                sub_bloques_ui_dict[b["nombre"]][i].visible = (b["nombre"] == nombre)
                sub_bloques_labels_dict[b["nombre"]][sub["nombre"]].visible = False
                for btn in carpetas_ui_dict[b["nombre"]][sub["nombre"]]:
                    btn.visible = False
                for lbl in carpetas_labels_dict[b["nombre"]][sub["nombre"]].values():
                    lbl.visible = False
        page.update()

    # Función para mostrar el contenido del sub-bloque seleccionado
    def mostrar_sub_bloque(nombre_bloque, nombre_sub):
        for key in sub_bloques_labels_dict[nombre_bloque]:
            sub_bloques_labels_dict[nombre_bloque][key].visible = (key == nombre_sub)
            # Mostrar carpetas solo para el sub-bloque seleccionado
            for btn in carpetas_ui_dict[nombre_bloque][key]:
                btn.visible = (key == nombre_sub)
            for lbl in carpetas_labels_dict[nombre_bloque][key].values():
                lbl.visible = False
        page.update()

    # Función para mostrar el contenido de la carpeta seleccionada
    def mostrar_carpeta(nombre_bloque, nombre_sub, carpeta):
        for lbl in carpetas_labels_dict[nombre_bloque][nombre_sub].values():
            lbl.visible = False
        carpetas_labels_dict[nombre_bloque][nombre_sub][carpeta].visible = True
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
                *contenido_labels.values(),
                # Sub-bloques y carpetas para todos los bloques principales
                *[ft.Row(sub_bloques_ui_dict[b["nombre"]], alignment=ft.MainAxisAlignment.CENTER, spacing=10) for b in bloques],
                *[lbl for b in bloques for lbl in sub_bloques_labels_dict[b["nombre"]].values()],
                *[btn for b in bloques for sub in sub_bloques_dict.get(b["nombre"], []) for btn in carpetas_ui_dict[b["nombre"]][sub["nombre"]]],
                *[lbl for b in bloques for sub in sub_bloques_dict.get(b["nombre"], []) for lbl in carpetas_labels_dict[b["nombre"]][sub["nombre"]].values()]
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)
