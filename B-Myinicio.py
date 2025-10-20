import flet as ft

# --- Variables Globales/Iniciales ---

# Definición de las 12 asignaturas base disponibles para elegir
ASIGNATURAS_DISPONIBLES = [
    "Inglés avanzado", "Digitalización", "Castellano", "Matemáticas",
    "Tecnología", "Física y Química", "Biología", "Geografía",
    "Historia", "Música", "Dibujo Técnico", "Valores Éticos"
]

# Estilos comunes para los contenedores
bloque_style = {
    "width": 150, "height": 100, "border_radius": 12, "alignment": ft.alignment.center,
    "ink": True, "border": ft.border.all(2, ft.Colors.BLUE_GREY_400),
}

sub_bloque_style = {
    "width": 120, "height": 70, "border_radius": 10, "alignment": ft.alignment.center,
    "ink": True, "border": ft.border.all(2, ft.Colors.BLUE_GREY_200),
    "visible": False
}


def get_carpetas(nombre_bloque, nombre_sub, B_NAME=None, P_NAME=None):
    """Función para obtener la estructura de carpetas según el bloque/sub-bloque."""
    if nombre_bloque == "My":
        if nombre_sub == "ESO-Baleares": return ["LOMLOE"]
        elif nombre_sub == "Clara-eso": return ["Asignaturas"]
        return []
    elif nombre_bloque == B_NAME:
        if nombre_sub.endswith("00"): return ["B00", "B00-01", "Clara-m"]
        else: return ["Datos ESO-Baleares", "Datos Clara100"]
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
    page.title = "Clara 100: Mi 'eso-click'"
    page.window_width = 800
    page.window_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

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

    asignaturas_checkboxes = [
        ft.Checkbox(label=a, value=False) for a in ASIGNATURAS_DISPONIBLES
    ]
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
            carpetas_labels_dict[nombre_bloque][nombre_sub][carpeta].visible = True
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
            # Estado por defecto para la construcción inicial: B0 y P0
            num_asignaturas = 0
            B_name = "B0"
            P_name = "P0"
            proyecto_name = "Proyecto NO CREADO"
        else:
            # Lógica para un click de usuario real (NO es la llamada inicial)
            
            # Validaciones para el click del usuario
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

            # Nombres del proyecto creado
            B_name = f"B{num_asignaturas}"
            P_name = f"P{num_asignaturas}"
            
        current_B_NAME = B_name
        current_P_NAME = P_name

        # 2. GENERACIÓN DE NUEVOS BLOQUES DINÁMICOS (B# y P#)
        
        # Eliminar B y P anteriores si existen 
        bloques_data[:] = [b for b in bloques_data if not (b["nombre"].startswith("B") or b["nombre"].startswith("P"))]
        
        # Definiciones de los nuevos bloques (B0 y P0 en el inicio)
        nuevo_B = {"nombre": B_name, "display_name": B_name, "color": ft.Colors.BLUE_200, "contenido": f"Bloque {B_name}: Documentación básica para {proyecto_name} ({num_asignaturas} asignaturas)."}
        nuevo_P = {"nombre": P_name, "display_name": P_name, "color": ft.Colors.GREEN_200, "contenido": f"Bloque {P_name}: Profesores para {proyecto_name} ({num_asignaturas} asignaturas)."}

        # Insertar los nuevos bloques después de 'My'
        bloques_data.insert(1, nuevo_B)
        bloques_data.insert(2, nuevo_P)
        
        # 3. GENERACIÓN DE SUB-BLOQUES DINÁMICOS

        sub_bloques_dict[B_name] = [{"nombre": "B00", "color": ft.Colors.BLUE_300, "contenido": "B00: Datos básicos del proyecto."}]
        sub_bloques_dict[P_name] = [{"nombre": "P00", "color": ft.Colors.GREEN_100, "contenido": "P00: Profesor-super."}]

        for i, asig in enumerate(selected_asignaturas, start=1):
            sub_B_name = f"B0{i}"
            sub_P_name = f"P0{i}"
            
            sub_bloques_dict[B_name].append({
                "nombre": sub_B_name, "color": ft.Colors.BLUE_300, 
                "contenido": f"{sub_B_name}: {asig} (Documentación)."
            })
            
            sub_bloques_dict[P_name].append({
                "nombre": sub_P_name, "color": ft.Colors.GREEN_100, 
                "contenido": f"{sub_P_name}: Profesor/a de {asig}."
            })


        # 4. RECONSTRUCCIÓN DE LA UI (Generar elementos visuales para B# y P#)
        
        for name in [B_name, P_name]:
            bloque_def = nuevo_B if name == B_name else nuevo_P
            
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
                    is_interactive = name == B_name and nombre_sub.startswith("B0") and nombre_sub != "B00"
                    
                    if is_interactive:
                        carpeta_control = ft.ElevatedButton(
                            carpeta,
                            on_click=lambda e, nb=name, s=nombre_sub, c=carpeta: mostrar_carpeta(nb, s, c),
                            visible=False
                        )
                    else:
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
        # La UI de configuración se añade siempre primero
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
            # Mostrar el contenido del bloque "My" por defecto.
            contenido_labels["My"].visible = True 
            for sub in sub_bloques_ui_dict["My"]:
                sub.visible = True
            
            status_msg.value = "¡Bienvenido! Haz clic en Myeso-click y luego en 'Clara-eso' para comenzar tu proyecto."
            status_msg.color = ft.Colors.BLUE_GREY_400
        else:
            # Mostrar mensaje de éxito tras la creación del proyecto
            clara_eso_config_ui.visible = False
            status_msg.value = f"✅ ¡Proyecto '{B_name} - {proyecto_name}' creado con éxito! Tienes los nuevos bloques {B_name} y {P_name}. Haz clic en ellos para ver los sub-bloques."
            status_msg.color = ft.Colors.GREEN_400
            
            # Resetear checkboxes
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