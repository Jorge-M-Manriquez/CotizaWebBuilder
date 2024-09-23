import os
import asyncio
import flet as ft
from google.cloud import firestore

import os
from google.cloud import firestore

# Asegúrate de que la variable de entorno esté configurada
if "GOOGLE_CREDENTIALS" not in os.environ:
    raise EnvironmentError("GOOGLE_CREDENTIALS no está configurada")

# Establecer la variable de entorno para las credenciales
# print("Estableciendo la variable de entorno para las credenciales...")
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/jorge/OneDrive/Documents/Proyectos_Personales/AplicacionesFlet/CotizaWebBuilder/precios-cotizawebbuilder-366c9592643a.json"

# Inicializar el cliente Firestore
print("Inicializando el cliente Firestore...")
db = firestore.Client()

# Función para obtener los precios desde Firestore
def fetch_prices_from_firestore():
    print("Intentando obtener el documento de Firestore...")

    # Referencia al documento en Firestore
    doc_ref = db.collection("precios").document("lista_precios")
    
    try:
        # Obtener el documento
        doc = doc_ref.get()
        if doc.exists:
            print("Documento encontrado en Firestore.")
            return doc.to_dict()  # Devolver los datos como diccionario
        else:
            print("No se encontró el documento.")
            return {}
    except Exception as e:
        # Capturar cualquier excepción que ocurra durante la obtención de datos
        print(f"Error al obtener el documento: {e}")
        return {}

# Obtener los precios al inicio del script
print("Obteniendo los precios desde Firestore al inicio del script...")
precios = fetch_prices_from_firestore()

# Imprimir los precios obtenidos para verificar los datos
print("Precios obtenidos:", precios)


def main(page: ft.Page):
    page.title = "CotizaWebBuilder"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    # Mostrar un indicador de carga
    loading = ft.ProgressRing()
    page.add(loading)
    
    # Remover el indicador de carga
    page.remove(loading)

    title = ft.Text(
        "Seleccion de Servicios",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    title_container = ft.Container(
        content=title,
        alignment=ft.alignment.center,
        padding=ft.padding.only(top=20, bottom=20)
    )

    page.add(title_container)

    def format_option_with_price(option_key, price_key="valor_ofrecido"):
        price = precios[option_key][price_key]
        return f"{option_key.replace('_', ' ').title()} - ${price:,}"
    

    def format_option_with_price(option_key, price_key="valor_ofrecido"):
        if option_key in precios:
            price = precios[option_key].get(price_key, 0)  # Usa get para evitar KeyError
            return f"{option_key.replace('_', ' ').title()} - ${price:,}"
        else:
            print(f"Clave {option_key} no encontrada en los precios.")
            return f"{option_key.replace('_', ' ').title()} - Precio no disponible"

    
    # Descripciones
    descripcion_g1 = ft.Text("\n "
    "Descripción de las opciones:\n"
    "1. Adaptación de plantilla: Uso y ajuste de una plantilla preexistente.\n"
    "   - Ajuste de diseño y estructura según las necesidades del cliente.\n"
    "   - Implementación de contenido proporcionado por el cliente.\n"
    "2. Personalización de plantilla: Modificación de una plantilla existente según requerimientos específicos.\n"
    "   - Modificación de estilos y funcionalidades de la plantilla.\n"
    "   - Integración de características adicionales según las necesidades del cliente.\n"
    "3. Creación personalizada desde cero: Diseño y desarrollo de un sitio web totalmente a medida.\n"
    "   - Diseño único y exclusivo basado en los requerimientos del cliente.\n"
    "   - Desarrollo de funcionalidades específicas y personalizadas.\n")
    
    descripcion_g2 = ft.Text("\n "
    "4. SEO Básico: Optimización básica para motores de búsqueda.\n"
    "   - Optimización de metaetiquetas y contenido.\n"
    "   - Configuración de herramientas básicas de análisis SEO.\n"
    "5. SEO Avanzado: Optimización avanzada para motores de búsqueda, incluyendo creación de blogs.\n"
    "   - Estrategia de palabras clave y optimización de contenido.\n"
    "   - Creación y publicación de blogs optimizados para SEO.\n"
    "12. Blogs: Creación de contenido de blogs, sólo disponible con SEO Avanzado.\n"
    "    - Redacción y publicación de artículos optimizados para SEO.\n")
    
    descripcion_g3 = ft.Text("\n "
    "6. Mantenimiento Básico: Soporte básico y actualizaciones periódicas.\n"
    "   - Soporte básico: Resolución de problemas menores y consultas generales.\n"
    "   - Actualizaciones periódicas: Actualización de plugins, temas y CMS.\n"
    "   - Incluye 5 horas de soporte al mes.\n"
    "7. Mantenimiento Estándar: Soporte intermedio con actualizaciones más frecuentes.\n"
    "   - Soporte intermedio: Asistencia más frecuente y detallada.\n"
    "   - Actualizaciones más frecuentes: Mejoras de rendimiento y optimización.\n"
    "   - Incluye 15 horas de soporte al mes.\n"
    "8. Mantenimiento Avanzado: Soporte completo con actualizaciones regulares y soporte prioritario dentro del horario laboral. Incluye creación de un blog al mes.\n"
    "   - Soporte completo: Atención prioritaria y resolución de cualquier tipo de problema.\n"
    "   - Actualizaciones regulares: Monitoreo continuo y mejoras constantes.\n"
    "   - Soporte prioritario: Respuesta rápida y atención preferencial.\n"
    "   - Creación de un blog al mes.\n"
    "   - Incluye 6 horas de soporte a la semana (no acumulables).\n")
    
    descripcion_g4 = ft.Text("\n "
    "9. Limite de Productos: Restricción en el número de productos gestionables en la web.\n"
    "   - Gestión de un número limitado de productos según el plan contratado.\n")
    
    descripcion_g5 = ft.Text("\n "
    "10. Dominio: Incluye la gestión del dominio.\n"
    "    - Registro, renovación y configuración del dominio.\n")
    
    descripcion_g6 = ft.Text("\n "
    "11. Hosting: Incluye el servicio de hosting para la web.\n"
    "    - Alojamiento web con características según el plan contratado.\n")

    creacion_dropdown = ft.Dropdown(
        label="Creación",
        expand=True,
        options=[
            ft.dropdown.Option(key=key, text=format_option_with_price(key))
            for key in ["adaptacion_plantilla", "personalizacion_plantilla", "creacion_personalizada"]
        ],
    )

    seo_dropdown = ft.Dropdown(
        label="SEO",
        expand=True,
        options=[
            ft.dropdown.Option(key="seo_basico", text=format_option_with_price("seo_basico")),
            ft.dropdown.Option(key="seo_avanzado", text=format_option_with_price("seo_avanzado")),
            ft.dropdown.Option(key="sin_seo", text="Sin SEO ($0)")
        ],
    )

    mantenimiento_dropdown = ft.Dropdown(
        label="Mantenimiento",
        expand=True,
        options=[
            ft.dropdown.Option(key=key, text=format_option_with_price(key))
            for key in ["mantenimiento_basico", "mantenimiento_estandar", "mantenimiento_avanzado"]
        ] + [ft.dropdown.Option(key="sin_mantenimiento", text="Sin Mantenimiento ($0)")],
    )

    productos_dropdown = ft.Dropdown(
        label="Productos",
        expand=True,
        options=[
            ft.dropdown.Option(key=key, text=format_option_with_price(key))
            for key in ["limite_25_productos", "limite_50_productos", "limite_100_productos", 
                        "limite_150_productos", "limite_500_productos", "ilimitado_productos"]
        ],
    )

    dominio_dropdown = ft.Dropdown(
        label="Dominio",
        expand=True,
        options=[
            ft.dropdown.Option(key="dominio_previo", text="Con Dominio Previo ($0)"),
            ft.dropdown.Option(key="sin_dominio_previo", text=format_option_with_price("sin_dominio_previo"))
        ],
    )

    hosting_dropdown = ft.Dropdown(
        label="Hosting",
        expand=True,
        options=[
            ft.dropdown.Option(key="hosting_previo", text="Con Hosting Previo ($0)"),
            ft.dropdown.Option(key="sin_hosting_previo", text=format_option_with_price("sin_hosting_previo"))
        ],
    )

    blogs_dropdown = ft.Dropdown(
        label="Blogs",
        expand=True,
        visible=False,
        options=[
            ft.dropdown.Option(key="0_blogs", text="0 Blogs"),
            ft.dropdown.Option(key="1_blog", text=format_option_with_price("1_blog")),
            ft.dropdown.Option(key="2_blog", text=format_option_with_price("2_blog")),
            ft.dropdown.Option(key="3_blog", text=format_option_with_price("3_blog")),
            ft.dropdown.Option(key="4_blog", text=format_option_with_price("4_blog"))
        ],
    )

    resumen_texto = ft.TextField(
        multiline=True,
        read_only=True,
        min_lines=10,
        max_lines=25,
        expand=True,
    )

    def calcular_precio(selecciones):
        precio_valor_ofrecido = 0
        precio_nacional = 0
        precio_internacional = 0

        for seleccion in selecciones:
            if seleccion in precios:
                precio_valor_ofrecido += precios[seleccion]["valor_ofrecido"]
                precio_nacional += precios[seleccion]["nacional"]
                precio_internacional += precios[seleccion]["internacional"]

        return precio_valor_ofrecido, precio_nacional, precio_internacional

    def mostrar_resultado(e):
        creacion = creacion_dropdown.value
        seo = seo_dropdown.value
        mantenimiento = mantenimiento_dropdown.value
        productos = productos_dropdown.value
        dominio = dominio_dropdown.value
        hosting = hosting_dropdown.value
        blogs = blogs_dropdown.value

        selecciones = {
            "Creación": creacion,
            "SEO": seo,
            "Mantenimiento": mantenimiento,
            "Productos": productos,
            "Dominio": dominio,
            "Hosting": hosting
        }

        if seo == "seo_avanzado":
            selecciones["Blogs"] = blogs

        campos_faltantes = [campo for campo, valor in selecciones.items() if not valor]

        if campos_faltantes:
            mensaje = "Por favor, selecciona una opción en los siguientes campos antes de continuar:\n"
            mensaje += ", ".join(campos_faltantes)
            resumen_texto.value = mensaje
            page.update()
            return

        precio_valor_ofrecido, precio_nacional, precio_internacional = calcular_precio(
            [valor for valor in selecciones.values() if valor != "0_blogs"]
        )

        def format_option(option):
            return option.replace('_', ' ').title()

        blogs_texto = next((opcion.text.split('-')[0].strip() for opcion in blogs_dropdown.options if opcion.key == blogs), "0 Blogs")

        resumen_texto.value = (
            f"Opción de Creación: {format_option(creacion)}\n"
            f"Optimización SEO: {format_option(seo)}\n"
            f"Mantenimiento: {format_option(mantenimiento)}\n"
            f"Límite de Productos: {format_option(productos)}\n"
            f"Dominio: {format_option(dominio)}\n"
            f"Hosting: {format_option(hosting)}\n"
            f"Blogs: {blogs_texto if seo == 'seo_avanzado' else 'No incluido'}\n\n"
            f"Precios:\n"
            f"Valor Ofrecido: CLP {precio_valor_ofrecido:,}\n"
            f"Precio Nacional: CLP {precio_nacional:,}\n"
            f"Precio Internacional: USD {precio_internacional:,}"
        )
        page.update()

    def toggle_blogs_visibility(e):
        blogs_dropdown.visible = seo_dropdown.value == "seo_avanzado"
        page.update()

    seo_dropdown.on_change = toggle_blogs_visibility

    calcular_button = ft.Container(
        ft.ElevatedButton(text="Calcular", on_click=mostrar_resultado),
        width=page.width * 0.8,
        height=50,  
    )
    button_centered = ft.Row([calcular_button], alignment=ft.MainAxisAlignment.CENTER)

    scrollable_content = ft.Column(
        controls=[
            descripcion_g1,
            creacion_dropdown,
            descripcion_g2,
            seo_dropdown,
            blogs_dropdown,
            descripcion_g3,
            mantenimiento_dropdown,
            descripcion_g4,
            productos_dropdown,
            descripcion_g5,
            dominio_dropdown,
            descripcion_g6,
            hosting_dropdown,
            button_centered,
            resumen_texto
        ],
        spacing=20,
        scroll=ft.ScrollMode.ALWAYS
    )

    page.add(
        ft.Container(
            content=scrollable_content,
            expand=True
        )
    )

asyncio.run(ft.app(target=main))
