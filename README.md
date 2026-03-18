# 📘 Unidad 2: Fundamentos de la Graficación por Computadora 🖥️
## 📈📉 Catálogo de Hardware | Proyecto Integrador | Ingeniería en Sistemas

---

### 🛠️ Tecnologías y Entorno
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flet](https://img.shields.io/badge/Flet-0052FF?style=for-the-badge&logo=flutter&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)
![Netlify](https://img.shields.io/badge/Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)

* **Lenguaje:** Python 👩‍💻🐍
* **Framework:** Flet (UI Framework basado en Flutter)
* **Despliegue:** Netlify (Web Hosting) 🌐
* **Control de Versiones:** Git & GitHub

---

> [!IMPORTANT]
> **DISEÑO REACTIVO:** Este repositorio contiene el desarrollo del Proyecto Integrador de la Unidad 1. Se enfoca en la transición de lógica de programación pura a interfaces gráficas funcionales, aplicando conceptos de **Herencia**, **POO** y **Gestión de Recursos Multimedia**.

![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<div align="center">
  <h3> 📐 1. Diagrama de Clases (Arquitectura del Software) </h3>
</div>

Detrás de la interfaz visual, existe una arquitectura lógica basada en la Programación Orientada a Objetos. El siguiente diagrama muestra cómo la clase personalizada de productos nace de los componentes base de Flet.

<div align="center">
  <img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/0fe2c1d7-0dc2-4b9e-9da4-152b5c86521a" />

</div>

---

<div align="center">
  <h1> 🧬 2. Explicación de la Herencia </h1>
</div>

En este proyecto, la reutilización de código se logró mediante la **Herencia**, un pilar fundamental de la graficación moderna y el desarrollo de software.

* **Clase Base:** Se utilizó la clase `ft.Container` de la librería Flet como clase padre.
* **Justificación:** Al heredar de `ft.Container`, nuestra clase `ProductoCard` obtiene automáticamente propiedades de diseño avanzadas:
    * **Bordes Redondeados (`border_radius`):** Define la estética moderna de las tarjetas.
    * **Sombras (`shadow`):** Aplica profundidad visual (Z-axis) al catálogo.
    * **Contenedor de Contenido:** Permite anidar elementos como texto e imágenes de forma jerárquica.

---

<div align="center">
  <h1> 🎨 3. Gestión de Recursos (Assets) </h1>
</div>

La correcta visualización de las imágenes es vital en la graficación. Se implementó una gestión de recursos eficiente para asegurar que el catálogo sea atractivo y rápido.

* **Configuración del Directorio:** Se utilizó el parámetro `assets_dir="assets"` en `ft.app()`.
* **Tratamiento de Imágenes:** Las imágenes de hardware (GPU, CPU, etc.) se gestionan como recursos locales que Flet empaqueta automáticamente al compilar para web.
* **Despliegue Web:** En la transición a **Netlify**, estos recursos se sirven desde la carpeta `dist`, garantizando que las rutas relativas no se rompan en el entorno de producción.

```python
# Ejemplo de carga de recurso multimedia en el código
ft.Image(
    src=producto['img'], 
    height=140, 
    fit=ft.ImageFit.CONTAIN
)
```
![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<div align="center">
  <h3>  CODIGO DEL CATALOGO</h3>
</div>

```python
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
)
```


<div align="center">
<h1> Despliegue y Evidencia Visual </h1>
</div>

🚀 Link del Proyecto:(https://peppy-heliotrope-64105c.netlify.app)
Captura de la Interfaz Final:
<div align="center">
<img width="1835" height="790" alt="image" src="https://github.com/user-attachments/assets/18a4c9d3-0c05-432d-8b13-49514ba3752f" />

<img width="1850" height="591" alt="image" src="https://github.com/user-attachments/assets/54ed452a-7ed4-4499-bbb5-4d8616251701" />

</div>

<div>
<h2> 📚 Bibliografía y Referencias </h2>
</div>

Flet Documentation. (2024). Python-based framework for interactive apps. Recuperado de https://flet.dev/docs/

Netlify Docs. (2024). Deploying modern web projects. Recuperado de https://docs.netlify.com/

Hearn, D., & Baker, M. P. (2006). Gráficas por computadora. Pearson Educación.
