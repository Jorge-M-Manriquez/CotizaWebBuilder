import flet as ft

# Definimos los precios base para cada opción con la nueva opción de blogs añadida
precios = {
    "adaptacion_plantilla": {"valor_ofrecido": 30000, "nacional": 300000, "internacional": 400},
    "personalizacion_plantilla": {"valor_ofrecido": 60000, "nacional": 500000, "internacional": 650},
    "creacion_personalizada": {"valor_ofrecido": 90000, "nacional": 1500000, "internacional": 2000},
    "seo_basico": {"valor_ofrecido": 30000, "nacional": 100000, "internacional": 150},
    "seo_avanzado": {"valor_ofrecido": 75000, "nacional": 200000, "internacional": 300},
    "mantenimiento_basico": {"valor_ofrecido": 25000, "nacional": 50000, "internacional": 70},
    "mantenimiento_estandar": {"valor_ofrecido": 50000, "nacional": 100000, "internacional": 140},
    "mantenimiento_avanzado": {"valor_ofrecido": 75000, "nacional": 150000, "internacional": 210},
    "limite_25_productos": {"valor_ofrecido": 0, "nacional": 0, "internacional": 0},
    "limite_50_productos": {"valor_ofrecido": 25000, "nacional": 50000, "internacional": 100},
    "limite_100_productos": {"valor_ofrecido": 50000, "nacional": 100000, "internacional": 140},
    "limite_150_productos": {"valor_ofrecido": 100000, "nacional": 200000, "internacional": 280},
    "limite_500_productos": {"valor_ofrecido": 200000, "nacional": 400000, "internacional": 560},
    "ilimitado_productos": {"valor_ofrecido": 400000, "nacional": 800000, "internacional": 1000},
    "dominio_previo": {"valor_ofrecido": 0, "nacional": 0, "internacional": 0},
    "sin_dominio_previo": {"valor_ofrecido": 20000, "nacional": 40000, "internacional": 60},
    "hosting_previo": {"valor_ofrecido": 0, "nacional": 0, "internacional": 0},
    "sin_hosting_previo": {"valor_ofrecido": 40000, "nacional": 60000, "internacional": 90},
    "1_blog": {"valor_ofrecido": 15000, "nacional": 60000, "internacional": 90},
    "2_blog": {"valor_ofrecido": 30000, "nacional": 100000, "internacional": 140},
    "3_blog": {"valor_ofrecido": 45000, "nacional": 140000, "internacional": 190},
    "4_blog": {"valor_ofrecido": 60000, "nacional": 180000, "internacional": 240}
}

def main(page: ft.Page):
    page.title = "CotizaWebBuilder"
    # Crear un título centrado
    title = ft.Text(
        "Seleccion de Servicios",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    # Envolver el título en un contenedor para darle padding y centrarlo
    title_container = ft.Container(
        content=title,
        alignment=ft.alignment.center,
        padding=ft.padding.only(top=20, bottom=20)
    )

    # Añadir el título centrado a la página
    page.add(title_container)

    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    def format_option_with_price(option_key, price_key="valor_ofrecido"):
        price = precios[option_key][price_key]
        return f"{option_key.replace('_', ' ').title()} - ${price:,}"
    
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

        # Añadimos blogs a las selecciones si SEO Avanzado está seleccionado
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

    # calcular_button = ft.ElevatedButton(text="Calcular", expand=True, on_click=mostrar_resultado)
    calcular_button = ft.Container(
        ft.ElevatedButton(text="Calcular", on_click=mostrar_resultado),
        width=page.width * 0.8,  # 50% del ancho de la página
        height=50,  
    )
    button_centered = ft.Row([calcular_button], alignment=ft.MainAxisAlignment.CENTER)

    # page.add(
    #     ft.Text("Calculadora de Precios", size=24, weight=ft.FontWeight.BOLD),
    #     ft.Column([
    #         creacion_dropdown,
    #         seo_dropdown,
    #         blogs_dropdown,
    #         mantenimiento_dropdown,
    #         productos_dropdown,
    #         dominio_dropdown,
    #         hosting_dropdown,
    #         calcular_button,
    #         resumen_texto
    #     ], spacing=20)
    # )

    # Añadimos todos los elementos a una columna con desplazamiento
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
        scroll=ft.ScrollMode.ALWAYS  # Cambiado a ALWAYS
    )

    # Agregamos la columna con scroll a la página
    page.add(
        # ft.Text("Seleccion de Servicios", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(
            content=scrollable_content,
            expand=True
        )
    )

ft.app(target=main)