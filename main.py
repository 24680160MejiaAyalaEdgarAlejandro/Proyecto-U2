import flet as ft

# 1. MODELO DE DATOS (Capa de Lógica)
# Definimos la lista de diccionarios con los productos tecnológicos
PRODUCTOS = [
    {
        "id": 1, 
        "nombre": "GeForce RTX 5060", 
        "desc": "Tarjeta gráfica Gigabyte con tecnología DLSS y Ray Tracing.", 
        "precio": 450.00, 
        "img": "gpu.png"
    },
    {
        "id": 2, 
        "nombre": "Razer Cobra Mouse", 
        "desc": "Mouse gaming ligero con switches ópticos y RGB personalizable.", 
        "precio": 60.00, 
        "img": "mouse.png"
    },
    {
        "id": 3, 
        "nombre": "Corsair RAM 32GB", 
        "desc": "Memoria Vengeance RGB PRO optimizada para alto rendimiento.", 
        "precio": 120.00, 
        "img": "ram.png"
    },
    {
        "id": 4, 
        "nombre": "AMD Ryzen 9 9000", 
        "desc": "Procesador con tecnología 3D V-Cache para gaming extremo.", 
        "precio": 550.00, 
        "img": "cpu.png"
    },
    {
        "id": 5, 
        "nombre": "Teclado Mecánico RGB", 
        "desc": "Teclado compacto con retroiluminación y respuesta rápida.", 
        "precio": 85.00, 
        "img": "teclado.png"
    },
]

# 2. EL COMPONENTE REUTILIZABLE (Custom Card)
# Clase que aplica HERENCIA de ft.Container
class ProductoCard(ft.Container):
    def __init__(self, producto):
        super().__init__()
        self.width = 250
        self.bgcolor = ft.colors.BLACK12
        self.border_radius = 15
        self.padding = 15
        self.shadow = ft.BoxShadow(blur_radius=10, color=ft.colors.BLACK26)
        self.alignment = ft.alignment.center

        # Diseño interno de la tarjeta
        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # Área de Imagen (desde carpeta local /assets)
              ft.Image(
    src=producto['img'], # Sin la barra "/" al principio
    height=140, 
    fit=ft.ImageFit.CONTAIN
),
                # Cuerpo de Texto
                ft.Text(producto["nombre"], weight="bold", size=16),
                ft.Text(producto["desc"], size=11, text_align=ft.TextAlign.CENTER),
                # Precio destacado en color diferente
                ft.Text(f"${producto['precio']}", size=20, weight="bold", color=ft.colors.GREEN_ACCENT),
                # Barra de Acciones
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.IconButton(ft.icons.FAVORITE_BORDER, icon_color="red"),
                        ft.ElevatedButton("Comprar", icon=ft.icons.SHOPPING_CART, bgcolor=ft.colors.BLUE_700, color="white")
                    ]
                )
            ]
        )

# 3. INTERFAZ DE USUARIO PRINCIPAL (GUI)
def main(page: ft.Page):
    page.title = "TechCatalog - Edgar"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 30

    # Encabezado con Identidad Visual
    header = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("TECNOLOGÍA ELITE", size=40, weight="bold", color="blue"),
            ft.Text("Catálogo de Componentes Profesionales", size=16, color="white70"),
            ft.Divider(height=20, color="blue")
        ]
    )

    # Layout: Cuadrícula que se ajusta al ancho (Fila con envoltura)
    lista_productos = ft.Row(
        wrap=True,
        spacing=30,
        run_spacing=30,
        alignment=ft.MainAxisAlignment.CENTER,
        # Creamos las tarjetas dinámicamente desde el modelo de datos
        controls=[ProductoCard(p) for p in PRODUCTOS]
    )

    # Añadir todo a la página
    page.add(header, lista_productos)

# Ejecución de la App con carpeta de recursos configurada
ft.app(target=main, assets_dir="assets")