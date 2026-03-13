from manim import *
from manim_slides import Slide
import random

FUENTE = "sans-serif"

class Presentacion(Slide):
    def construct(self):
        self.camera.background_color = WHITE
        
        # # --- INTRODUCCIÓN Y MOTIVACIÓN ---
        # self.slide_memoria_computador() # Jerónimo Hoyos
        # self.slide_por_que_jerarquia() # Jerónimo Hoyos
        # self.slide_motivacion() # Jerónimo Hoyos

        # # --- CONCEPTOS BASE ---
        # self.slide_memoria_primaria() # Mateo
        # self.slide_memoria_secundaria() # Mateo

        # # --- NIVELES DE JERARQUÍA (PRIMARIA) ---
        # self.slide_registers() # Jerónimo Hoyos
        # self.slide_cache() # Jerónimo Hoyos
        # self.slide_ram() # Jerónimo Hoyos
        # self.slide_ram_escalabilidad() # Jerónimo Hoyos

        # # --- ALMACENAMIENTO (SECUNDARIA) ---
        # self.almacenamiento_secundario() # Mateo

        # # --- DISCOS DUROS (HDD) ---
        # self.diapositiva_detalles_hdd() # Juan
        # self.slide_funcionamiento_hdd() # Juan
        # self.slide_delay_hdd() # Juan
        # self.slide_comparativa_hdd() # Juan

        # # --- ESTADO SÓLIDO (SSD) Y FLASH ---
        self.slide_ssd_unidades() # Jerónimo Restrepo
        # self.slide_ssd_funcionamiento() # Jerónimo Restrepo
        # self.slide_tipos_memoria_flash() # Jerónimo Restrepo
        # self.slide_comparativa_ssd() # Jerónimo Restrepo

        # # --- CONCLUSIONES Y COMPARATIVAS ---
        # self.slide_caracteristicas() # Mateo
        # self.slide_comparativa_jerarquia() # Mateo
        # self.slide_memory_standards() # Mateo

        # # --- PRÁCTICA / SIMULACIÓN ---
        # self.slide_simulador_nand2tetris() # Jerónimo Hoyos

        # # --- CIERRE ---
        # self.slide_despedida()

    def crear_titulo(self, texto, palabra_clave=None, color_clave=DARK_GRAY, font_size=42):
        t2c = {palabra_clave: color_clave} if palabra_clave else {}
        titulo = Text(texto, font=FUENTE, font_size=font_size, color=BLACK, t2c=t2c, weight=BOLD).to_edge(UP, buff=0.5)
        linea = Underline(titulo, color=BLACK, stroke_width=4, buff=0.15)
        return titulo, linea

    def limpiar_pantalla(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def slide_memoria_computador(self):
        titulo, linea = self.crear_titulo("Memoria en computador moderno", palabra_clave="moderno")
        self.play(Write(titulo), Create(linea))

        titulo_enunciado = Text("Enunciado", font=FUENTE, font_size=24, color=BLACK, weight=BOLD)
        
        texto_enunciado = VGroup(
            Text("Investigar los distintos tipos", font=FUENTE, font_size=18, color=DARK_GRAY),
            Text("de arreglos de memoria que usa", font=FUENTE, font_size=18, color=DARK_GRAY),
            Text("un PC de última generación en", font=FUENTE, font_size=18, color=DARK_GRAY),
            Text("sus registros, caché, RAM y disco.", font=FUENTE, font_size=18, color=DARK_GRAY),
            Text("Relacionarlo con los diseños", font=FUENTE, font_size=18, color=DARK_GRAY),
            Text("vistos en clase. Incluir en la", font=FUENTE, font_size=18, color=DARK_GRAY),
            Text("discusión aspectos tales como", font=FUENTE, font_size=18, color=DARK_GRAY),
            Text("costo y velocidad.", font=FUENTE, font_size=18, color=DARK_GRAY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        bloque_izquierdo = VGroup(titulo_enunciado, texto_enunciado).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        
        linea_acento = Line(
            bloque_izquierdo.get_corner(UL) + LEFT * 0.3 + UP * 0.1,
            bloque_izquierdo.get_corner(DL) + LEFT * 0.3 + DOWN * 0.1,
            color=GRAY, stroke_width=4
        )
        
        grupo_enunciado = VGroup(linea_acento, bloque_izquierdo).to_edge(LEFT, buff=0.6).shift(UP * 0.2)

        niveles = [
            "CPU", 
            "Caché", 
            "Memoria RAM", 
            "Disco"
        ]
        anchos = [2.2, 3.4, 4.6, 5.8]
        colores_fondo = [WHITE, LIGHT_GRAY, GRAY, DARK_GRAY]
        colores_texto = [BLACK, BLACK, WHITE, WHITE]

        piramide = VGroup()
        for i in range(4):
            rect = RoundedRectangle(
                corner_radius=0.15, 
                width=anchos[i], 
                height=0.8, 
                fill_color=colores_fondo[i], 
                fill_opacity=1, 
                stroke_color=BLACK, 
                stroke_width=2
            )
            label = Text(niveles[i], font=FUENTE, font_size=18, color=colores_texto[i], weight=BOLD).move_to(rect)
            piramide.add(VGroup(rect, label))

        piramide.arrange(DOWN, buff=0.1).to_edge(RIGHT, buff=1.8).shift(UP * 0.2)

        flecha_vel = Arrow(
            start=piramide.get_corner(DR) + RIGHT * 0.3, 
            end=piramide.get_corner(UR) + RIGHT * 0.3, 
            color=BLACK, stroke_width=3, tip_length=0.2
        )
        label_vel = Text("+ Velocidad y Costo", font=FUENTE, font_size=14, color=BLACK, weight=BOLD)\
            .next_to(flecha_vel, RIGHT, buff=0.15).rotate(PI/2)

        flecha_cap = Arrow(
            start=piramide.get_corner(UL) + LEFT * 0.3, 
            end=piramide.get_corner(DL) + LEFT * 0.3, 
            color=BLACK, stroke_width=3, tip_length=0.2
        )
        label_cap = Text("+ Capacidad", font=FUENTE, font_size=14, color=BLACK, weight=BOLD)\
            .next_to(flecha_cap, LEFT, buff=0.15).rotate(PI/2)

        diagrama_completo = VGroup(piramide, flecha_vel, label_vel, flecha_cap, label_cap)

        integrantes = VGroup(
            Text("Integrantes:", font=FUENTE, font_size=18, color=BLACK, weight=BOLD),
            Text("Jerónimo Hoyos B. | Juan Manuel Teherán M. | Jerónimo Restrepo R. | Mateo Úsuga Zapata", font=FUENTE, font_size=18, color=DARK_GRAY)
        ).arrange(RIGHT, buff=0.3).to_edge(DOWN, buff=0.8)

        self.play(FadeIn(grupo_enunciado, shift=RIGHT))
        self.play(LaggedStart(*[FadeIn(nivel, shift=UP) for nivel in reversed(piramide)], lag_ratio=0.2))
        self.play(
            GrowArrow(flecha_vel), FadeIn(label_vel),
            GrowArrow(flecha_cap), FadeIn(label_cap)
        )
        self.play(FadeIn(integrantes, shift=UP * 0.3))

        self.next_slide()
        self.limpiar_pantalla()

    def slide_por_que_jerarquia(self):
        titulo = Text(
            "¿Por qué es necesaria la\njerarquía de memoria?", 
            font=FUENTE, font_size=40, color=BLACK, weight=BOLD, line_spacing=1.2
        ).to_edge(UP, buff=0.4)
        
        self.play(Write(titulo))

        textos_niveles = ["0", "Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4", "Nivel 5"]
        descripciones = [
            "Registros de la CPU", 
            "Memoria Caché", 
            "Memoria Principal", 
            "Disco Magnético", 
            "Disco Óptico", 
            "Cinta Magnética"
        ]
        
        anchos_sup = [0.2, 1.0, 1.8, 2.6, 3.4, 4.2]
        anchos_inf = [1.0, 1.8, 2.6, 3.4, 4.2, 5.0]
        alto_trapecio = 0.55
        
        colores_trapecio = ["#EAEAEA", "#D3D3D3", "#A9A9A9", "#787878", "#505050", "#282828"]
        colores_texto_trapecio = [BLACK, BLACK, BLACK, BLACK, WHITE, WHITE]

        piramide_trapecios = VGroup()
        columna_cajas = VGroup()

        for i in range(6):
            p1 = np.array([-anchos_sup[i]/2, alto_trapecio/2, 0])
            p2 = np.array([anchos_sup[i]/2, alto_trapecio/2, 0])
            p3 = np.array([anchos_inf[i]/2, -alto_trapecio/2, 0])
            p4 = np.array([-anchos_inf[i]/2, -alto_trapecio/2, 0])
            
            trapecio = Polygon(
                p1, p2, p3, p4, 
                fill_color=colores_trapecio[i], fill_opacity=1, 
                stroke_color=BLACK, stroke_width=1.5
            )
            
            texto_trap = Text(textos_niveles[i], font=FUENTE, font_size=16, color=colores_texto_trapecio[i], weight=BOLD)
            if i == 0:
                texto_trap.shift(DOWN * 0.1)
            else:
                texto_trap.move_to(trapecio)
                
            piramide_trapecios.add(VGroup(trapecio, texto_trap))

            caja = RoundedRectangle(
                corner_radius=0.1, width=3.8, height=alto_trapecio, 
                fill_color=WHITE, fill_opacity=1, stroke_color=GRAY, stroke_width=1.5
            )
            texto_caja = Text(descripciones[i], font=FUENTE, font_size=14, color=BLACK).move_to(caja)
            columna_cajas.add(VGroup(caja, texto_caja))

        piramide_trapecios.arrange(DOWN, buff=0.05)
        columna_cajas.arrange(DOWN, buff=0.05).next_to(piramide_trapecios, RIGHT, buff=0.1)
        diagrama_jerarquia = VGroup(piramide_trapecios, columna_cajas).to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)

        personaje = ImageMobject("assets/chica_pensando.png").scale(1).to_edge(RIGHT, buff=1.0).shift(DOWN * 0.5)

        burbuja_principal = Ellipse(width=2.5, height=1.5, fill_color=WHITE, fill_opacity=1, stroke_color=GRAY, stroke_width=2)
        texto_burbuja = Text("¿Y esto\npara qué?", font=FUENTE, font_size=20, color=BLACK, weight=BOLD, line_spacing=1).move_to(burbuja_principal)
        
        circulo1 = Circle(radius=0.12, fill_color=WHITE, fill_opacity=1, stroke_color=GRAY, stroke_width=2)
        circulo2 = Circle(radius=0.08, fill_color=WHITE, fill_opacity=1, stroke_color=GRAY, stroke_width=2)
        circulo3 = Circle(radius=0.04, fill_color=WHITE, fill_opacity=1, stroke_color=GRAY, stroke_width=2)
        
        burbuja_completa = VGroup(burbuja_principal, texto_burbuja).next_to(personaje, UP + LEFT, buff=0.1).shift(RIGHT * 0.5)
        circulo1.next_to(burbuja_principal, DOWN + RIGHT, buff=-0.3)
        circulo2.next_to(circulo1, DOWN + RIGHT, buff=0.05)
        circulo3.next_to(circulo2, DOWN + RIGHT, buff=0.05)
        
        globo_pensamiento = VGroup(burbuja_completa, circulo1, circulo2, circulo3)

        self.play(LaggedStart(*[FadeIn(nivel, shift=UP) for nivel in piramide_trapecios], lag_ratio=0.15))
        self.play(LaggedStart(*[FadeIn(caja, shift=LEFT) for caja in columna_cajas], lag_ratio=0.15))
        
        self.play(FadeIn(personaje, shift=LEFT * 0.5))
        self.play(
            LaggedStart(
                GrowFromCenter(circulo3),
                GrowFromCenter(circulo2),
                GrowFromCenter(circulo1),
                GrowFromCenter(burbuja_completa),
                lag_ratio=0.2
            )
        )

        self.next_slide()
        self.limpiar_pantalla()

    def slide_motivacion(self):
        titulo, linea = self.crear_titulo("La analogía de la memoria", palabra_clave="analogía")
        self.play(Write(titulo), Create(linea))

        img_1 = VGroup(Rectangle(width=9, height=5.5, color=LIGHT_GRAY, fill_color=LIGHT_GRAY, fill_opacity=0.5), Text("Imagen 1", font=FUENTE, font_size=36, color=DARK_GRAY)).shift(DOWN * 0.4)
        img_2 = VGroup(Rectangle(width=9, height=5.5, color=LIGHT_GRAY, fill_color=LIGHT_GRAY, fill_opacity=0.5), Text("Imagen 2", font=FUENTE, font_size=36, color=DARK_GRAY)).shift(DOWN * 0.4)
        img_3 = VGroup(Rectangle(width=9, height=5.5, color=LIGHT_GRAY, fill_color=LIGHT_GRAY, fill_opacity=0.5), Text("Imagen 3", font=FUENTE, font_size=36, color=DARK_GRAY)).shift(DOWN * 0.4)
        img_4 = VGroup(Rectangle(width=9, height=5.5, color=LIGHT_GRAY, fill_color=LIGHT_GRAY, fill_opacity=0.5), Text("Imagen 3", font=FUENTE, font_size=36, color=DARK_GRAY)).shift(DOWN * 0.4)

        imagenes = [img_1, img_2, img_3,img_4]

        imagenes = [
             ImageMobject("assets/motivacion_01.png").scale_to_fit_height(5.5).shift(DOWN * 0.4),
             ImageMobject("assets/motivacion_02.png").scale_to_fit_height(5.5).shift(DOWN * 0.4),
             ImageMobject("assets/motivacion_03.png").scale_to_fit_height(5.5).shift(DOWN * 0.4),
             ImageMobject("assets/motivacion_04.png").scale_to_fit_height(5.5).shift(DOWN * 0.4)
        ]

        self.play(FadeIn(imagenes[0], shift=UP * 0.5))
        self.next_slide()

        for i in range(1, len(imagenes)):
            self.play(
                FadeOut(imagenes[i-1]),
                FadeIn(imagenes[i], shift=UP * 0.5)
            )
            self.next_slide() 

        self.limpiar_pantalla()

    def slide_intro_tipos_jerarquia(self):
        titulo = Text(
            "Tipos de jerarquía de memoria", 
            font=FUENTE, font_size=40, color=BLACK, weight=BOLD
        ).to_edge(UP, buff=0.3)
        
        subtitulo = Text(
            "El diseño moderno se divide en dos tipos principales:", 
            font=FUENTE, font_size=28, color=DARK_GRAY
        ).next_to(titulo, DOWN, buff=0.2)
        
        self.play(Write(titulo))
        self.play(Write(subtitulo))

        estilo_caja = {"color": BLACK, "fill_color": WHITE, "fill_opacity": 1, "stroke_width": 2}
        
        caja_cpu = Rectangle(width=2.5, height=3.5, **estilo_caja).move_to(LEFT * 4.6 + DOWN * 0.2)
        txt_cpu = Text("CPU", font=FUENTE, font_size=24, color=DARK_GRAY).move_to(caja_cpu)
        bloque_cpu = VGroup(caja_cpu, txt_cpu)

        caja_cache = Rectangle(width=2.2, height=1.2, **estilo_caja).move_to(LEFT * 1.5 + UP * 0.6)
        txt_cache = Text("Cache Memory", font=FUENTE, font_size=18, color=DARK_GRAY).move_to(caja_cache)
        bloque_cache = VGroup(caja_cache, txt_cache)

        caja_primaria = Rectangle(width=2.6, height=3.5, **estilo_caja).move_to(RIGHT * 1.6 + DOWN * 0.2)
        txt_primaria = Text("Primary Memory", font=FUENTE, font_size=20, color=DARK_GRAY).move_to(caja_primaria)
        bloque_primaria = VGroup(caja_primaria, txt_primaria)

        caja_secundaria = Rectangle(width=2.6, height=3.5, **estilo_caja).move_to(RIGHT * 4.9 + DOWN * 0.2)
        txt_secundaria = Text("Secondary Memory", font=FUENTE, font_size=18, color=DARK_GRAY).move_to(caja_secundaria)
        bloque_secundaria = VGroup(caja_secundaria, txt_secundaria)

        estilo_flecha = {"color": BLACK, "stroke_width": 2, "max_stroke_width_to_length_ratio": 5, "max_tip_length_to_length_ratio": 0.15}
        
        x_cpu_der = -3.35
        x_cache_izq = -2.6
        x_cache_der = -0.4
        x_prim_izq = 0.3
        x_prim_der = 2.9
        x_sec_izq = 3.6

        flechas = VGroup(
            # CPU <-> Cache (Arriba)
            Arrow(start=[x_cpu_der, 0.9, 0], end=[x_cache_izq, 0.9, 0], buff=0.05, **estilo_flecha),
            Arrow(start=[x_cache_izq, 0.4, 0], end=[x_cpu_der, 0.4, 0], buff=0.05, **estilo_flecha),
            
            # Cache <-> Primaria (Arriba)
            Arrow(start=[x_cache_der, 0.9, 0], end=[x_prim_izq, 0.9, 0], buff=0.05, **estilo_flecha),
            Arrow(start=[x_prim_izq, 0.4, 0], end=[x_cache_der, 0.4, 0], buff=0.05, **estilo_flecha),
            
            # CPU <-> Primaria (Abajo - ByPass)
            Arrow(start=[x_cpu_der, -0.9, 0], end=[x_prim_izq, -0.9, 0], buff=0.05, **estilo_flecha),
            Arrow(start=[x_prim_izq, -1.3, 0], end=[x_cpu_der, -1.3, 0], buff=0.05, **estilo_flecha),
            
            # Primaria <-> Secundaria
            Arrow(start=[x_prim_der, 0.5, 0], end=[x_sec_izq, 0.5, 0], buff=0.05, **estilo_flecha),
            Arrow(start=[x_sec_izq, -0.9, 0], end=[x_prim_der, -0.9, 0], buff=0.05, **estilo_flecha)
        )

        diagrama_base = VGroup(bloque_cpu, bloque_cache, bloque_primaria, bloque_secundaria, flechas)

        grupo_interna = VGroup(bloque_cpu, bloque_cache, bloque_primaria)
        marco_interna = SurroundingRectangle(grupo_interna, color=DARK_GRAY, buff=0.3, stroke_width=4)
        marco_interna_punteado = DashedVMobject(marco_interna, num_dashes=40)
        
        txt_interna = Text(
            "Memoria primaria", 
            font=FUENTE, font_size=20, color=DARK_GRAY, weight=BOLD
        ).next_to(marco_interna, UP, buff=0.15)

        grupo_externa = VGroup(bloque_secundaria)
        marco_externa = SurroundingRectangle(grupo_externa, color=GRAY, buff=0.3, stroke_width=4)
        marco_externa_punteado = DashedVMobject(marco_externa, num_dashes=20)

        txt_externa = Text(
            "Memoria secundaria", 
            font=FUENTE, font_size=20, color=GRAY, weight=BOLD, line_spacing=1
        ).next_to(marco_externa, UP, buff=0.15)

        self.play(FadeIn(diagrama_base, shift=UP * 0.3))
        self.next_slide() 

        self.play(
            Create(marco_interna_punteado),
            Write(txt_interna)
        )
        self.next_slide() 

        self.play(
            Create(marco_externa_punteado),
            Write(txt_externa)
        )
        
        self.next_slide()
        self.limpiar_pantalla()

    def slide_memoria_primaria(self):
        titulo = Text(
            "Memoria interna o primaria", 
            font=FUENTE, font_size=40, color=BLACK, weight=BOLD
        ).to_edge(UP, buff=0.4)
        
        desc_1 = Text(
            "Compuesta por la memoria principal, la memoria caché y los registros de la CPU.", 
            font=FUENTE, font_size=24, color=DARK_GRAY
        )
        desc_2 = Text(
            "El procesador tiene acceso directo a esta.", 
            font=FUENTE, font_size=24, color=DARK_GRAY
        )
        descripcion = VGroup(desc_1, desc_2).arrange(DOWN, buff=0.2).next_to(titulo, DOWN, buff=0.4)

        self.play(Write(titulo))
        self.play(FadeIn(descripcion, shift=UP * 0.3))
        self.next_slide() 

        def crear_fila(y_pos, width_izq, color_izq, txt_izq, txt_der):
            center_x_izq = -2.5 
            buff = 0.15
            right_x_align = 4.5

            bloque_izq = RoundedRectangle(
                width=width_izq, height=0.9, corner_radius=0.2, 
                fill_color=color_izq, fill_opacity=1, stroke_width=0
            )
            bloque_izq.move_to([center_x_izq, y_pos, 0])
            label_izq = Text(txt_izq, font=FUENTE, font_size=28, color=BLACK, weight=BOLD).move_to(bloque_izq)
            grupo_izq = VGroup(bloque_izq, label_izq)
            
            left_x_der = center_x_izq + (width_izq / 2) + buff
            width_der = right_x_align - left_x_der
            center_x_der = (left_x_der + right_x_align) / 2
            
            bloque_der = RoundedRectangle(
                width=width_der, height=0.9, corner_radius=0.2, 
                fill_color=WHITE, fill_opacity=1, stroke_width=2, stroke_color=GRAY
            )
            bloque_der.move_to([center_x_der, y_pos, 0])
            label_der = Text(txt_der, font=FUENTE, font_size=20, color=BLACK, weight=BOLD).move_to(bloque_der)
            grupo_der = VGroup(bloque_der, label_der)
            
            return VGroup(grupo_izq, grupo_der)

        color_n0 = "#E0E0E0"
        color_n1 = "#C0C0C0" 
        color_n2 = "#9E9E9E" 

        y_n0 = 0.5
        y_n1 = -0.6
        y_n2 = -1.7

        fila_0 = crear_fila(y_n0, 1.2, color_n0, "0", "Registros de la CPU")
        fila_1 = crear_fila(y_n1, 2.4, color_n1, "Nivel 1", "Memoria Caché (SRAMS)")
        fila_2 = crear_fila(y_n2, 3.6, color_n2, "Nivel 2", "Memoria Principal (DRAMS)")

        self.play(FadeIn(fila_0, shift=UP * 0.3))
        self.next_slide()
        
        self.play(FadeIn(fila_1, shift=UP * 0.3))
        self.next_slide()
        
        self.play(FadeIn(fila_2, shift=UP * 0.3))
        
        self.next_slide()
        self.limpiar_pantalla()

    def slide_memoria_secundaria(self):
        titulo = Text(
            "Memoria externa o secundaria", 
            font=FUENTE, font_size=40, color=BLACK, weight=BOLD
        ).to_edge(UP, buff=0.4)

        desc_1 = Text(
            "Comprende el disco magnético, el disco óptico y la cinta magnética,", 
            font=FUENTE, font_size=22, color=DARK_GRAY
        )
        desc_2 = Text(
            "es decir, dispositivos de almacenamiento periféricos a los que el", 
            font=FUENTE, font_size=22, color=DARK_GRAY
        )
        desc_3 = Text(
            "procesador puede acceder a través de un módulo de E/S.", 
            font=FUENTE, font_size=22, color=DARK_GRAY
        )
        descripcion = VGroup(desc_1, desc_2, desc_3).arrange(DOWN, buff=0.15).next_to(titulo, DOWN, buff=0.3)

        self.play(Write(titulo))
        self.play(FadeIn(descripcion, shift=UP * 0.3))
        self.next_slide() 

        def crear_fila(y_pos, width_izq, color_izq, txt_izq, txt_der, color_txt_izq=BLACK, font_size_der=20):
            center_x_izq = -2.5 
            buff = 0.15 
            right_x_align = 4.5 
      
            bloque_izq = RoundedRectangle(
                width=width_izq, height=0.9, corner_radius=0.2, 
                fill_color=color_izq, fill_opacity=1, stroke_width=0
            )
            bloque_izq.move_to([center_x_izq, y_pos, 0])
            label_izq = Text(txt_izq, font=FUENTE, font_size=28, color=color_txt_izq, weight=BOLD).move_to(bloque_izq)
            grupo_izq = VGroup(bloque_izq, label_izq)
  
            left_x_der = center_x_izq + (width_izq / 2) + buff
            width_der = right_x_align - left_x_der
            center_x_der = (left_x_der + right_x_align) / 2
            
            bloque_der = RoundedRectangle(
                width=width_der, height=0.9, corner_radius=0.2, 
                fill_color=WHITE, fill_opacity=1, stroke_width=2, stroke_color=GRAY
            )
            bloque_der.move_to([center_x_der, y_pos, 0])
            

            label_der = Text(txt_der, font=FUENTE, font_size=font_size_der, color=BLACK, weight=BOLD, line_spacing=1).move_to(bloque_der)
            grupo_der = VGroup(bloque_der, label_der)
            
            return VGroup(grupo_izq, grupo_der)

    
        color_n3 = "#808080"
        color_n4 = "#555555"
        color_n5 = "#333333"

        y_n3 = 0.2
        y_n4 = -0.9
        y_n5 = -2.0

        fila_3 = crear_fila(y_n3, 4.8, color_n3, "Nivel 3", "Disco Magnético\n(Almacenamiento en Disco)", color_txt_izq=BLACK, font_size_der=18)
        
        fila_4 = crear_fila(y_n4, 6.0, color_n4, "Nivel 4", "Disco Óptico", color_txt_izq=WHITE)
        fila_5 = crear_fila(y_n5, 7.2, color_n5, "Nivel 5", "Cinta Magnética", color_txt_izq=WHITE)

        self.play(FadeIn(fila_3, shift=UP * 0.3))
        self.next_slide()
        
        self.play(FadeIn(fila_4, shift=UP * 0.3))
        self.next_slide()
        
        self.play(FadeIn(fila_5, shift=UP * 0.3))
        
        self.next_slide()
        self.limpiar_pantalla()

    def slide_registers(self):
        # --- 1. PALETA DE COLORES B&W ---
        fuente = "sans-serif"
        color_texto = BLACK
        color_secundario = GRAY_D
        color_acento = BLACK  # Se usa negro para máximo contraste en escala de grises
        color_lineas = GRAY_C
        color_bg_suave = "#F4F4F4" # Gris muy claro para el fondo del diagrama
        
        # --- 2. TÍTULO CENTRADO Y VIÑETAS ---
        # Título centrado en la parte superior
        titulo = Text("REGISTERS", font=fuente, font_size=45, color=color_texto, weight=BOLD)
        titulo.to_edge(UP, buff=0.4)
        
        linea_subtitulo = Line(LEFT, RIGHT, color=color_acento, stroke_width=3).scale(1.5)
        linea_subtitulo.next_to(titulo, DOWN, buff=0.1)

        viñetas_textos = [
            "Pequeñas unidades de memoria.",
            "Ubicadas dentro de la CPU.",
            "Alta velocidad de operación.",
            "Guardan datos e instrucciones.",
            "Almacenan la información\nde uso más frecuente."
        ]
        
        # Viñetas alineadas a la izquierda (independientes del título centrado)
        grupo_texto = VGroup(
            *[VGroup(Dot(radius=0.05, color=color_acento), Text(linea, font=fuente, font_size=22, color=color_secundario)).arrange(RIGHT, buff=0.2) 
              for linea in viñetas_textos]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        grupo_texto.to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)

        # --- 3. ESQUEMA DEL REGISTRO (Ajustado para que nada se salga) ---
        centro_diag = RIGHT * 3.2 + DOWN * 0.4
        
        # Fondo ampliado para contener bien las flechas
        fondo_circuito = RoundedRectangle(
            width=6.8, height=4.5, corner_radius=0.3,
            fill_color=color_bg_suave, fill_opacity=1, 
            stroke_width=1.5, stroke_color=color_lineas
        ).move_to(centro_diag)

        caja_registro = RoundedRectangle(
            width=3.0, height=1.6, corner_radius=0.15,
            fill_color=WHITE, fill_opacity=1, 
            stroke_width=3, stroke_color=color_texto
        ).move_to(centro_diag)
        
        txt_registro = Text("Register", font=fuente, font_size=26, color=color_texto, weight=BOLD).move_to(caja_registro)
        
        reloj = Triangle(color=color_texto, fill_opacity=0, stroke_width=2).scale(0.15)
        reloj.move_to(caja_registro.get_bottom(), aligned_edge=DOWN)

        # Bus ajustado para que quepa dentro de 'fondo_circuito'
        def crear_bus(start, end, label_str, color=color_texto):
            flecha = Arrow(start=start, end=end, buff=0, color=color, stroke_width=4, max_tip_length_to_length_ratio=0.15)
            label = Text(label_str, font=fuente, font_size=20, color=color).next_to(flecha, UP, buff=0.1)
            slash = Line(DL, UR, color=color, stroke_width=2).scale(0.15).move_to(flecha.get_center())
            txt_16 = Text("16", font=fuente, font_size=14, color=color).next_to(slash, DOWN, buff=0.05).shift(RIGHT*0.1)
            return VGroup(flecha, label, slash, txt_16), flecha

        grupo_in, flecha_in = crear_bus(caja_registro.get_left() + LEFT * 1.4, caja_registro.get_left(), "in")
        grupo_out, flecha_out = crear_bus(caja_registro.get_right(), caja_registro.get_right() + RIGHT * 1.4, "out")

        flecha_load = Arrow(start=caja_registro.get_top() + UP * 0.8, end=caja_registro.get_top(), buff=0, color=color_secundario, stroke_width=3)
        label_load = Text("load", font=fuente, font_size=18, color=color_secundario).next_to(flecha_load, RIGHT, buff=0.1)
        grupo_load = VGroup(flecha_load, label_load)

        # --- 4. SECUENCIA DE ANIMACIONES ---
        self.play(Write(titulo), Create(linea_subtitulo), run_time=1)
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=RIGHT * 0.2) for item in grupo_texto],
                lag_ratio=0.15
            ),
            run_time=2
        )
        self.next_slide() 

        self.play(FadeIn(fondo_circuito, shift=UP * 0.1))
        self.play(
            Create(caja_registro),
            Write(txt_registro),
            Create(reloj),
            run_time=1.5
        )
        self.play(FadeIn(grupo_in, shift=RIGHT * 0.2))
        self.play(FadeIn(grupo_load, shift=DOWN * 0.2))
        self.next_slide() 

        # Datos en negro
        datos_entrada = Text("1010", font="monospace", font_size=18, color=BLACK, weight=BOLD)
        datos_entrada.move_to(flecha_in.get_start() + UP * 0.3)
        
        self.play(FadeIn(datos_entrada))
        
        # Animación ajustada: el dato ahora entra hasta el centro de la caja para no quedarse en el borde
        self.play(datos_entrada.animate.move_to(caja_registro.get_center()), run_time=1)
        self.next_slide() 

        self.play(
            flecha_load.animate.set_color(BLACK),
            label_load.animate.set_color(BLACK),
            run_time=0.5
        )
        
        # Parpadeo en gris oscuro para indicar guardado
        self.play(
            FadeOut(datos_entrada, scale=0.5), 
            Indicate(caja_registro, color=GRAY_D, scale_factor=1.05), 
            run_time=0.8
        )
        self.next_slide() 

        self.play(FadeIn(grupo_out, shift=RIGHT * 0.2))
        
        datos_salida = Text("1010", font="monospace", font_size=18, color=BLACK, weight=BOLD)
        # El dato ahora sale desde el centro de la caja hacia la flecha
        datos_salida.move_to(caja_registro.get_center())
        
        self.play(FadeIn(datos_salida, scale=0.5))
        self.play(
            datos_salida.animate.move_to(flecha_out.get_end() + RIGHT * 0.2), 
            run_time=1.2
        )
        self.play(FadeOut(datos_salida, shift=RIGHT*0.2))

        # Comandos finales activos
        self.next_slide()
        self.limpiar_pantalla()

    def slide_cache(self):
        # --- 1. PALETA DE COLORES B&W ---
        fuente = "sans-serif"
        color_texto = BLACK
        color_secundario = GRAY_D
        color_acento = BLACK
        
        # Tonos de gris para diferenciar la jerarquía
        color_cpu = BLACK
        color_cache = GRAY_D
        color_memoria = GRAY_B

        # --- 2. TÍTULO CENTRADO CON TILDE ---
        titulo = Text("CACHÉ", font=fuente, font_size=45, color=color_texto, weight=BOLD)
        titulo.to_edge(UP, buff=0.4)
        
        linea_subtitulo = Line(LEFT, RIGHT, color=color_acento, stroke_width=3).scale(1.5)
        linea_subtitulo.next_to(titulo, DOWN, buff=0.1)

        # --- 3. VIÑETAS ---
        viñetas_textos = [
            "Unidad de memoria pequeña y muy rápida.",
            "Ubicada estratégicamente cerca de la CPU.",
            "Almacena datos e instrucciones recientes.",
            "Evita viajes lentos a la Memoria Principal.",
            "Minimiza drásticamente el tiempo de acceso."
        ]
        
        grupo_texto = VGroup(
            *[VGroup(Dot(radius=0.05, color=color_acento), Text(linea, font=fuente, font_size=20, color=color_secundario)).arrange(RIGHT, buff=0.2) 
              for linea in viñetas_textos]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        grupo_texto.to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)

        # --- 4. ESQUEMA JERÁRQUICO ---
        centro_x = 3.5
        
        caja_cpu = RoundedRectangle(width=3.5, height=1.2, corner_radius=0.15, fill_color=color_cpu, fill_opacity=0.8, stroke_color=BLACK)
        txt_cpu = Text("CPU", font=fuente, font_size=26, color=WHITE, weight=BOLD).move_to(caja_cpu)
        grupo_cpu = VGroup(caja_cpu, txt_cpu).move_to([centro_x, 1.8, 0])

        caja_cache = RoundedRectangle(width=2.8, height=1.0, corner_radius=0.1, fill_color=color_cache, fill_opacity=0.9, stroke_color=BLACK)
        txt_cache = Text("Caché", font=fuente, font_size=24, color=WHITE, weight=BOLD).move_to(caja_cache)
        grupo_cache = VGroup(caja_cache, txt_cache).move_to([centro_x, 0, 0])

        caja_mem = RoundedRectangle(width=4.8, height=1.2, corner_radius=0.1, fill_color=color_memoria, fill_opacity=0.8, stroke_color=BLACK)
        txt_mem = Text("Memoria Principal", font=fuente, font_size=22, color=BLACK, weight=BOLD).move_to(caja_mem)
        grupo_mem = VGroup(caja_mem, txt_mem).move_to([centro_x, -1.8, 0])

        flecha_palabras = DoubleArrow(start=caja_cache.get_top(), end=caja_cpu.get_bottom(), buff=0.1, color=color_secundario, stroke_width=4)
        txt_flecha_palabras = Text("Transferencia\nde Palabras", font=fuente, font_size=16, color=color_texto, line_spacing=0.8).next_to(flecha_palabras, RIGHT, buff=0.2)

        flecha_bloques = DoubleArrow(start=caja_mem.get_top(), end=caja_cache.get_bottom(), buff=0.1, color=color_secundario, stroke_width=4)
        txt_flecha_bloques = Text("Transferencia\nde Bloques", font=fuente, font_size=16, color=color_texto, line_spacing=0.8).next_to(flecha_bloques, RIGHT, buff=0.2)

        # --- 5. SECUENCIA DE ANIMACIONES ---
        self.play(Write(titulo), Create(linea_subtitulo), run_time=1)
        self.play(
            LaggedStart(*[FadeIn(texto, shift=RIGHT * 0.2) for texto in grupo_texto], lag_ratio=0.15),
            run_time=2
        )
        self.next_slide() 

        self.play(FadeIn(grupo_cpu, shift=DOWN*0.2))
        self.play(FadeIn(grupo_mem, shift=UP*0.2))
        self.next_slide()

        self.play(FadeIn(grupo_cache, scale=0.8), run_time=1.2)
        self.next_slide()

        self.play(GrowArrow(flecha_bloques), FadeIn(txt_flecha_bloques))
        
        bloque_datos = VGroup(
            Text("1010", font="monospace", font_size=14, color=BLACK, weight=BOLD),
            Text("1100", font="monospace", font_size=14, color=BLACK, weight=BOLD),
            Text("0011", font="monospace", font_size=14, color=BLACK, weight=BOLD)
        ).arrange(RIGHT, buff=0.1)
        
        fondo_bloque = BackgroundRectangle(bloque_datos, color=WHITE, fill_opacity=1, buff=0.1)
        bloque_visual = VGroup(fondo_bloque, bloque_datos).move_to(caja_mem.get_center())
        
        # Animación de transferencia de bloque (Lenta)
        self.play(FadeIn(bloque_visual, scale=0.5))
        self.play(bloque_visual.animate.move_to(caja_cache.get_center()), run_time=2, rate_func=linear)
        self.play(
            FadeOut(bloque_visual, scale=0.5),
            Indicate(caja_cache, color=WHITE, scale_factor=1.05),
            run_time=0.8
        )
        self.next_slide() 

        self.play(GrowArrow(flecha_palabras), FadeIn(txt_flecha_palabras))

        palabra_visual = Text("1010", font="monospace", font_size=16, color=BLACK, weight=BOLD)
        fondo_palabra = BackgroundRectangle(palabra_visual, color=WHITE, fill_opacity=1, buff=0.1)
        palabra_completa = VGroup(fondo_palabra, palabra_visual).move_to(caja_cache.get_center())
        
        # Animación de transferencia de palabra (Rápida)
        self.play(FadeIn(palabra_completa, scale=0.5))
        self.play(palabra_completa.animate.move_to(caja_cpu.get_center()), run_time=0.5)
        self.play(
            FadeOut(palabra_completa, scale=0.5),
            Indicate(caja_cpu, color=GRAY_C, scale_factor=1.05),
            run_time=0.6
        )
        
        self.next_slide()
        
        # Limpieza usando tu función
        self.limpiar_pantalla()

    def slide_ram(self):
        # --- 1. PALETA DE COLORES B&W ---
        fuente = "sans-serif"
        color_texto = BLACK
        color_secundario = GRAY_D
        color_acento = BLACK
        color_bg_suave = "#F4F4F4" # Gris muy claro para el fondo
        
        # --- 2. TÍTULO CENTRADO ---
        titulo = Text("RAM", font=fuente, font_size=40, color=color_texto, weight=BOLD)
        titulo.to_edge(UP, buff=0.4)
        
        linea_subtitulo = Line(LEFT, RIGHT, color=color_acento, stroke_width=3).scale(2)
        linea_subtitulo.next_to(titulo, DOWN, buff=0.1)

        # --- 3. VIÑETAS (Alineadas a la izquierda) ---
        viñetas_textos = [
            "Es la memoria principal del sistema.",
            "Mayor capacidad que la caché,\npero con una velocidad menor.",
            "Almacena los datos e instrucciones\nque la CPU utiliza en ese momento.",
            "Acceso directo a cualquier dirección."
        ]
        
        grupo_texto = VGroup(
            *[VGroup(Dot(radius=0.05, color=color_acento), Text(linea, font=fuente, font_size=20, color=color_secundario, line_spacing=0.8)).arrange(RIGHT, buff=0.2) 
              for linea in viñetas_textos]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        grupo_texto.to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)

        # --- 4. ESQUEMA DE LA RAM (Lado Derecho) ---
        centro_diag = RIGHT * 3.4 + DOWN * 0.3
        
        # Fondo ampliado para contener todo el circuito y buses
        fondo_circuito = RoundedRectangle(
            width=6.7, height=6.0, corner_radius=0.3,
            fill_color=color_bg_suave, fill_opacity=1, 
            stroke_width=1.5, stroke_color=GRAY_C
        ).move_to(centro_diag)

        # Caja principal de la RAM
        caja_ram = RoundedRectangle(
            width=3.4, height=4.4, corner_radius=0.15,
            fill_color=WHITE, fill_opacity=1, 
            stroke_width=3, stroke_color=BLACK
        ).move_to(centro_diag)
        
        txt_ram = Text("RAM", font=fuente, font_size=24, color=BLACK, weight=BOLD).next_to(caja_ram.get_top(), DOWN, buff=0.15)
        
        reloj = Triangle(color=BLACK, fill_opacity=0, stroke_width=2).scale(0.15)
        reloj.move_to(caja_ram.get_bottom(), aligned_edge=DOWN)

        # Caja Lógica (Direct Access Logic) dentro de la RAM en la parte inferior
        caja_logica = Rectangle(width=2.8, height=0.6, fill_color=WHITE, fill_opacity=1, stroke_width=2, stroke_color=BLACK)
        caja_logica.move_to(caja_ram.get_bottom() + UP * 0.5)
        txt_logica = Text("Direct Access Logic", font=fuente, font_size=14, color=BLACK).move_to(caja_logica)
        grupo_logica = VGroup(caja_logica, txt_logica)

        # Registros internos de la RAM
        def crear_registro(y_offset, texto_num):
            caja_reg = Rectangle(width=2.2, height=0.45, stroke_width=2, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK)
            caja_reg.move_to(caja_ram.get_center() + UP * y_offset)
            txt_reg = Text("Register", font=fuente, font_size=16, color=BLACK).move_to(caja_reg)
            num_reg = Text(texto_num, font=fuente, font_size=14, color=BLACK).next_to(caja_reg, RIGHT, buff=0.15)
            return VGroup(caja_reg, txt_reg, num_reg)

        reg_0 = crear_registro(1.1, "0")
        reg_1 = crear_registro(0.5, "1")
        puntos = Text("...", font=fuente, font_size=24, color=BLACK).move_to(caja_ram.get_center() + DOWN * 0.1)
        reg_n = crear_registro(-0.6, "n-1")

        grupo_registros = VGroup(reg_0, reg_1, puntos, reg_n)

        # Buses de conexión ajustados para no salirse
        def crear_bus(start, end, label_text, width_text):
            flecha = Arrow(start=start, end=end, buff=0, color=BLACK, stroke_width=4, max_tip_length_to_length_ratio=0.15)
            label = Text(label_text, font=fuente, font_size=18, color=BLACK).next_to(flecha, UP, buff=0.1)
            slash = Line(DL, UR, color=BLACK, stroke_width=2).scale(0.15).move_to(flecha.get_center())
            width_lbl = Text(width_text, font=fuente, font_size=14, color=BLACK).next_to(slash, DOWN, buff=0.05).shift(RIGHT*0.1)
            return VGroup(flecha, label, slash, width_lbl), flecha

        # Posiciones de los buses
        y_addr = caja_logica.get_center()[1]
        grupo_addr, flecha_addr = crear_bus(caja_ram.get_left() + LEFT * 1.3 + UP * y_addr, caja_ram.get_left() + UP * y_addr, "address", "k")

        y_in = reg_1.get_center()[1] # Apunta hacia el área de registros
        grupo_in, flecha_in = crear_bus(caja_ram.get_left() + LEFT * 1.3 + UP * y_in, caja_ram.get_left() + UP * y_in, "in", "w")

        y_out = reg_n.get_center()[1] + 0.2
        grupo_out, flecha_out = crear_bus(caja_ram.get_right() + UP * y_out, caja_ram.get_right() + RIGHT * 1.3 + UP * y_out, "out", "w")

        flecha_load = Arrow(start=caja_ram.get_top() + UP * 0.6, end=caja_ram.get_top(), buff=0, color=GRAY_D, stroke_width=3)
        label_load = Text("load", font=fuente, font_size=16, color=GRAY_D).next_to(flecha_load, RIGHT, buff=0.1)
        grupo_load = VGroup(flecha_load, label_load)

        # --- 5. SECUENCIA DE ANIMACIONES ---
        
        # Título y Viñetas
        self.play(Write(titulo), Create(linea_subtitulo), run_time=1)
        self.play(
            LaggedStart(*[FadeIn(texto, shift=RIGHT * 0.2) for texto in grupo_texto], lag_ratio=0.15),
            run_time=2
        )
        self.next_slide() 

        # Hardware Base
        self.play(FadeIn(fondo_circuito, shift=UP * 0.1))
        self.play(Create(caja_ram), Write(txt_ram), Create(reloj))
        self.play(Create(grupo_logica))
        self.play(LaggedStart(*[FadeIn(mob, shift=DOWN*0.1) for mob in [reg_0, reg_1, puntos, reg_n]], lag_ratio=0.15))
        self.next_slide() 
        
        # Conexiones (Buses)
        self.play(
            FadeIn(grupo_addr, shift=RIGHT*0.2),
            FadeIn(grupo_in, shift=RIGHT*0.2),
            FadeIn(grupo_out, shift=LEFT*0.2),
            FadeIn(grupo_load, shift=DOWN*0.2)
        )
        self.next_slide() 

        # Animación Dinámica: OPERACIÓN DE ESCRITURA (WRITE)
        # 1. Llega la dirección de memoria
        addr_dato = Text("0...01", font="monospace", font_size=16, color=BLACK, weight=BOLD).move_to(flecha_addr.get_start() + UP*0.3)
        self.play(FadeIn(addr_dato))
        self.play(addr_dato.animate.move_to(caja_logica.get_center()), run_time=1)
        
        # 2. La lógica selecciona el registro 1
        self.play(
            FadeOut(addr_dato, scale=0.5), 
            Indicate(caja_logica, color=GRAY_D, scale_factor=1.05), 
            run_time=0.6
        )
        self.play(reg_1[0].animate.set_fill(GRAY_C, opacity=1), run_time=0.4)
        
        # 3. Entra el dato a guardar
        in_dato = Text("1011...0", font="monospace", font_size=16, color=BLACK, weight=BOLD).move_to(flecha_in.get_start() + UP*0.3)
        self.play(FadeIn(in_dato))
        self.play(in_dato.animate.move_to(reg_1.get_center()), run_time=1)
        
        # 4. Señal de Load activa y guarda
        self.play(flecha_load.animate.set_color(BLACK), label_load.animate.set_color(BLACK), run_time=0.3)
        self.play(
            FadeOut(in_dato, scale=0.5), 
            Indicate(reg_1[0], color=WHITE, scale_factor=1.05), 
            run_time=0.8
        )
        self.next_slide()

        # Animación Dinámica: OPERACIÓN DE LECTURA (READ)
        # Sale el dato del registro seleccionado
        out_dato = Text("1011...0", font="monospace", font_size=16, color=BLACK, weight=BOLD).move_to(reg_1.get_center())
        self.play(FadeIn(out_dato, scale=0.5))
        self.play(out_dato.animate.move_to(flecha_out.get_end() + RIGHT*0.2), run_time=1.2)
        
        # Limpieza de la animación interna
        self.play(
            FadeOut(out_dato, shift=RIGHT*0.2),
            reg_1[0].animate.set_fill(WHITE, opacity=1), # El registro vuelve a su estado normal
            flecha_load.animate.set_color(GRAY_D),
            label_load.animate.set_color(GRAY_D)
        )
        self.next_slide()

        # Limpieza final de la pantalla
        self.limpiar_pantalla()

    def slide_ram_escalabilidad(self):
        # --- 1. PALETA DE COLORES B&W ---
        fuente = "sans-serif"
        color_texto = BLACK
        color_secundario = GRAY_D
        color_acento = BLACK
        
        # --- 2. TÍTULO CENTRADO ---
        titulo = Text("Escalabilidad de la RAM", font=fuente, font_size=36, color=color_texto, weight=BOLD)
        titulo.to_edge(UP, buff=0.4)
        
        linea_subtitulo = Line(LEFT, RIGHT, color=color_acento, stroke_width=3).scale(4.5)
        linea_subtitulo.next_to(titulo, DOWN, buff=0.1)

        # --- 3. CONSTRUCCIÓN RAM (Lado Izquierdo) ---
        caja_base = RoundedRectangle(width=3.2, height=0.8, corner_radius=0.15, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=2)
        txt_base = Text("RAM8", font=fuente, font_size=20, color=BLACK, weight=BOLD).move_to(caja_base)
        ram8_base = VGroup(caja_base, txt_base).move_to(LEFT * 3.5 + DOWN * 0.2)

        # Creación de los 8 chips apilados
        ram8_blocks = VGroup(*[
            VGroup(
                RoundedRectangle(width=3.2, height=0.45, corner_radius=0.1, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=1.5),
                Text(f"RAM8 (Chip {i})", font=fuente, font_size=16, color=BLACK)
            ) for i in range(8)
        ]).arrange(DOWN, buff=0.1).move_to(LEFT * 3.5 + DOWN * 0.2)

        # Contenedor RAM64
        caja_ram64 = SurroundingRectangle(ram8_blocks, color=BLACK, stroke_width=3, buff=0.2, corner_radius=0.15)
        txt_ram64 = Text("RAM64", font=fuente, font_size=24, color=BLACK, weight=BOLD).next_to(caja_ram64, UP, buff=0.2)

        # --- 4. TABLA Y EXPLICACIÓN (Lado Derecho) ---
        tabla = Table(
            [["RAM8", "8", "3"],
             ["RAM64", "64", "6"],
             ["RAM512", "512", "9"],
             ["RAM4K", "4096", "12"],
             ["RAM16K", "16384", "14"]],
            col_labels=[
                Text("Chip Name", font=fuente, font_size=24), 
                Text("n (Registros)", font=fuente, font_size=24), 
                Text("k (Bits Address)", font=fuente, font_size=24)
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 2, "color": BLACK}
        ).scale(0.38).move_to(RIGHT * 3.2 + UP * 0.5)

        # Estilizar el interior de la tabla
        tabla.get_col_labels().set_color(BLACK)
        for elem in tabla.get_entries():
            elem.set_color(GRAY_D)

        explicacion_k = VGroup(
            Text("Al multiplicar n x 8", font=fuente, font_size=20, color=BLACK, weight=BOLD),
            Text("sumamos 3 bits a k", font=fuente, font_size=20, color=GRAY_D)
        ).arrange(DOWN, buff=0.1).next_to(tabla, DOWN, buff=0.6)
        
        flecha_explicacion = Arrow(start=explicacion_k.get_top(), end=tabla.get_bottom(), buff=0.15, color=BLACK, stroke_width=3)

        # --- 5. SECUENCIA DE ANIMACIONES ---
        self.play(Write(titulo), Create(linea_subtitulo), run_time=1)
        self.next_slide() 

        self.play(FadeIn(ram8_base, shift=UP*0.2))
        self.next_slide() 

        # Cambio visual del bloque único a los 8 bloques
        self.play(ReplacementTransform(ram8_base, ram8_blocks), run_time=1.5)
        self.next_slide()
   
        self.play(Create(caja_ram64), Write(txt_ram64))
        self.next_slide()

        self.play(FadeIn(tabla, shift=LEFT*0.3))
        self.next_slide()

        self.play(FadeIn(explicacion_k, shift=UP*0.2), GrowArrow(flecha_explicacion))
        self.next_slide()

        # Limpieza final de la pantalla usando tu método
        self.limpiar_pantalla()

    def slide_memory_standards(self):
        # --- 1. PALETA DE COLORES B&W ---
        fuente = "sans-serif"
        color_texto = BLACK
        color_secundario = GRAY_D
        color_acento = BLACK
        
        # --- 2. TÍTULO CENTRADO ---
        titulo = Text("Resumen de Jerarquía", font=fuente, font_size=38, color=color_texto, weight=BOLD)
        titulo.to_edge(UP, buff=0.4)
        
        linea_subtitulo = Line(LEFT, RIGHT, color=color_acento, stroke_width=3).scale(3.5)
        linea_subtitulo.next_to(titulo, DOWN, buff=0.1)

        self.play(Write(titulo), Create(linea_subtitulo))
        self.next_slide()

        # --- 3. DATOS DE LA TABLA ---
        encabezados = ["Nivel", "Nombre", "Tamaño", "Hardware", "T. Acceso", "Ancho Banda", "Gestión", "Respaldo"]
        datos = [
            ["1", "Registros", "< 1 KB", "Multi-puerto", "0.25-0.5 ns", "20-100k MB/s", "Compilador", "Caché"],
            ["2", "Caché", "< 16 MB", "SRAM", "0.5-25 ns", "5k-15k MB/s", "Hardware", "RAM"],
            ["3", "Mem. RAM", "< 16 GB", "DRAM", "80-250 ns", "1k-5k MB/s", "Sist. Op.", "Disco"],
            ["4", "Disco", "> 100 GB", "Magnética", "5M ns", "20-150 MB/s", "Sist. Op.", "E/S"]
        ]

        def crear_fila_cuadritos(textos, es_encabezado=False):
            fila = VGroup()
            for txt in textos:
                color_fondo = BLACK if es_encabezado else WHITE
                color_txt = WHITE if es_encabezado else BLACK
                peso = BOLD if es_encabezado else NORMAL
                
                caja = RoundedRectangle(
                    width=1.55, height=0.65, corner_radius=0.1, 
                    fill_color=color_fondo, fill_opacity=1, 
                    stroke_color=BLACK, stroke_width=2
                )
                
                # Ajuste dinámico de fuente para que el texto quepa en el cuadro
                font_s = 14 if es_encabezado else 13
                if len(txt) >= 10: font_s = 11  
                
                texto = Text(txt, font=fuente, font_size=font_s, color=color_txt, weight=peso)
                texto.move_to(caja.get_center())
                
                cuadrito = VGroup(caja, texto)
                fila.add(cuadrito)
            
            fila.arrange(RIGHT, buff=0.08) 
            return fila

        # Construcción de la cuadrícula completa
        cuadricula_final = VGroup()
        
        fila_headers = crear_fila_cuadritos(encabezados, es_encabezado=True)
        cuadricula_final.add(fila_headers)
        
        for fila_datos in datos:
            cuadricula_final.add(crear_fila_cuadritos(fila_datos, es_encabezado=False))
            
        # Centrar la tabla en el espacio disponible
        cuadricula_final.arrange(DOWN, buff=0.1).move_to(DOWN * 0.2)
        
        f_headers = cuadricula_final[0]
        f_datos_finales = cuadricula_final[1:]

        # --- 4. SECUENCIA DE ANIMACIONES ---
        # Mostrar encabezados
        self.play(FadeIn(f_headers, shift=DOWN*0.2))
        self.next_slide() 
        
        # Mostrar cada nivel individualmente con un texto temporal explicativo
        for i, fila_data in enumerate(datos):
            fila_temp = crear_fila_cuadritos(fila_data, es_encabezado=False)
            fila_temp.move_to(DOWN * 0.8) # Posición central para enfoque
            
            lbl_temp = Text(f"Nivel {fila_data[0]}: {fila_data[1]}", font=fuente, font_size=20, weight=BOLD, color=GRAY_D)
            lbl_temp.next_to(fila_temp, UP, buff=0.3)
            grupo_temp = VGroup(lbl_temp, fila_temp)

            self.play(
                FadeIn(lbl_temp, shift=UP*0.1), 
                LaggedStart(*[FadeIn(c, shift=UP*0.2) for c in fila_temp], lag_ratio=0.05)
            )
            self.next_slide()
            self.play(FadeOut(grupo_temp, shift=UP*0.2))

        # Al final, mostramos toda la tabla completa para el cierre
        self.play(LaggedStart(*[FadeIn(f, shift=DOWN*0.1) for f in f_datos_finales], lag_ratio=0.15))
        self.next_slide() 

        # Limpieza final
        self.limpiar_pantalla()

    def slide_caracteristicas(self):
        # Título en Blanco y Negro
        titulo, linea = self.crear_titulo("Características de la jerarquía", palabra_clave="Características", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        # Definición de textos
        txt_cap = "Volumen global de información que se puede almacenar.\nAumenta a medida que bajamos en la jerarquía."
        txt_tie = "Tiempo entre la solicitud y la entrega de datos.\nTambién aumenta al bajar en los niveles."
        txt_ren = "Asegura que los datos frecuentes estén en memorias\nmás rápidas para optimizar el sistema global."
        txt_cos = "El costo por bit aumenta al subir en la pirámide.\nLa memoria interna es la más costosa."

        # Iconos en Negro Sólido
        icon_cap = VGroup(*[
            RoundedRectangle(corner_radius=0.05, width=0.6, height=0.15, fill_color=BLACK, fill_opacity=1, stroke_width=0) 
            for _ in range(3)
        ]).arrange(UP, buff=0.08)
        
        reloj_base = Circle(radius=0.3, color=BLACK, stroke_width=3)
        manecilla = Line(reloj_base.get_center(), reloj_base.get_center() + UP*0.2, color=BLACK, stroke_width=3)
        icon_tie = VGroup(reloj_base, manecilla)
        
        icon_ren = Star(n=5, outer_radius=0.3, inner_radius=0.15, color=BLACK, fill_opacity=1, stroke_width=0)
        
        icon_cos = Text("$", font_size=36, color=BLACK, weight=BOLD)

        datos = [
            ("Capacidad", txt_cap, icon_cap),
            ("Tiempo de Acceso", txt_tie, icon_tie),
            ("Rendimiento", txt_ren, icon_ren),
            ("Costo por bit", txt_cos, icon_cos)
        ]

        tarjetas_finales = VGroup()
        
        for tit, txt, icono in datos:
            # Estilo B&W: Fondo blanco, borde negro
            base = RoundedRectangle(
                width=9, height=1.3, corner_radius=0.1, 
                fill_color=WHITE, fill_opacity=1, 
                stroke_color=BLACK, stroke_width=2
            )
            # Detalle lateral negro
            borde_izq = Rectangle(
                width=0.15, height=1.3, 
                fill_color=BLACK, fill_opacity=1, 
                stroke_width=0
            ).align_to(base, LEFT)
            
            lbl_tit = Text(tit, font_size=20, weight=BOLD, color=BLACK)
            lbl_txt = Text(txt, font_size=14, color=BLACK, line_spacing=0.8)
            grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            
            contenido = VGroup(icono.copy(), grupo_txt).arrange(RIGHT, buff=0.4).move_to(base.get_center()).align_to(base, LEFT).shift(RIGHT*0.5)
            
            tarjeta = VGroup(base, borde_izq, contenido)
            tarjetas_finales.add(tarjeta)

        # Organización en columna
        tarjetas_finales.arrange(DOWN, buff=0.2).shift(DOWN*0.2)

        # Animación: Entrada de todo el listado de una vez
        self.play(
            FadeIn(tarjetas_finales, shift=UP*0.3),
            run_time=1.5
        )

        self.next_slide()
        self.limpiar_pantalla()

    def slide_comparativa_jerarquia(self):
        # Título principal
        titulo, linea = self.crear_titulo("Jerarquía de Memoria: Pros vs Contras", palabra_clave="vs", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        # --- DEFINICIÓN DE CONTENIDOS (Texto más limpio) ---
        v_datos = [
            ("Rendimiento", "Reduce el tiempo de acceso usando\nmemorias rápidas cerca del CPU.", 
             VGroup(Line(ORIGIN, RIGHT*0.3), Line(RIGHT*0.3, RIGHT*0.3+UP*0.3)).set_stroke(BLACK, 3)),
            
            ("Rentabilidad", "Equilibra costo y velocidad usando\ntecnologías caras y masivas baratas.", 
             VGroup(*[Circle(radius=0.1, color=BLACK, fill_opacity=1).shift(UP*0.1*i) for i in range(3)])),
            
            ("Optimización", "Maximiza el desempeño global sin\ncuellos de botella tecnológicos.", 
             Star(n=8, outer_radius=0.2, inner_radius=0.1, color=BLACK, fill_opacity=1)),
            
            ("Gestión", "Mantiene datos críticos a mano y\nrelega lo innecesario a niveles bajos.", 
             VGroup(*[Line(LEFT*0.2, RIGHT*0.2).shift(UP*0.1*i) for i in range(3)]).set_color(BLACK))
        ]

        d_datos = [
            ("Complejidad", "La coordinación de niveles agrega\ndificultad al diseño del sistema.", 
             Triangle().scale(0.15).set_color(BLACK).set_fill(BLACK, 1)),
            
            ("Costo Alto", "Las memorias superiores son muy\ncostosas por cada bit almacenado.", 
             Text("$", font_size=24, color=BLACK, weight=BOLD)),
            
            ("Latencia", "El acceso a niveles inferiores (discos)\nes mucho más lento.", 
             Arc(radius=0.2, angle=TAU*0.75, color=BLACK, stroke_width=4)),
            
            ("Sobrecarga", "Sincronizar niveles genera un gasto\nextra de recursos de hardware.", 
             Text("!", font_size=24, color=BLACK, weight=BOLD))
        ]

        # --- CONSTRUCTOR DE TARJETAS MEJORADO ---
        def crear_tarjeta(tit, txt, icono):
            # Tarjeta un poco más alta para que el texto no esté apretado
            base = RoundedRectangle(width=6.6, height=1.3, corner_radius=0.1, 
                                   fill_color=WHITE, fill_opacity=1, 
                                   stroke_color=BLACK, stroke_width=2)
            
            borde_izq = Rectangle(width=0.15, height=1.3, fill_color=BLACK, 
                                 fill_opacity=1, stroke_width=0).align_to(base, LEFT)
            
            # Aumentamos font_size y mejoramos line_spacing
            lbl_tit = Text(tit, font_size=18, weight=BOLD, color=BLACK)
            lbl_txt = Text(txt, font_size=14, color=GRAY_E, line_spacing=1.2) # 1.2 es ideal
            
            grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            
            # Icono con contenedor para centrado consistente
            contenedor_icono = Square(side_length=0.8, stroke_width=0).move_to(LEFT*2.6)
            icono.move_to(contenedor_icono.get_center())
            
            contenido = VGroup(icono, grupo_txt).arrange(RIGHT, buff=0.4)
            contenido.align_to(base, LEFT).shift(RIGHT*0.4)
            
            return VGroup(base, borde_izq, contenido)

        # --- ORGANIZACIÓN ---
        col_ventajas = VGroup(*[crear_tarjeta(t, tx, i) for t, tx, i in v_datos]).arrange(DOWN, buff=0.2)
        col_desventajas = VGroup(*[crear_tarjeta(t, tx, i) for t, tx, i in d_datos]).arrange(DOWN, buff=0.2)
        
        # Centramos la tabla en pantalla
        tabla = VGroup(col_ventajas, col_desventajas).arrange(RIGHT, buff=0.4).shift(DOWN*0.6)

        sub_v = Text("Ventajas", font_size=24, weight=BOLD, color=BLACK).next_to(col_ventajas, UP, buff=0.1)
        sub_d = Text("Desventajas", font_size=24, weight=BOLD, color=BLACK).next_to(col_desventajas, UP, buff=0.1)

        # --- ANIMACIÓN ---
        self.play(
            FadeIn(VGroup(tabla, sub_v, sub_d), shift=UP*0.3),
            run_time=1.5
        )
        self.next_slide()
        self.limpiar_pantalla()

    def slide_despedida(self):
        # --- CONFIGURACIÓN GLOBAL B&W ---
        color_texto_principal = BLACK
        color_acento = GRAY 

        # --- 1. TÍTULO CENTRADO (EN MAYÚSCULAS) ---
        texto_muchas = Text("¡MUCHAS", font_size=72, weight=BOLD, slant=ITALIC, color=color_texto_principal)
        texto_gracias = Text("GRACIAS!", font_size=72, color=color_texto_principal)
        
        titulo = VGroup(texto_muchas, texto_gracias).arrange(RIGHT, buff=0.4)
        titulo.to_edge(UP, buff=0.8)

        # --- 2. CÓDIGO QR Y TEXTO GITHUB (A la izquierda) ---
        qr_image = ImageMobject("assets/memoria_en_computador_moderno_qr.png") 
        qr_image.height = 3.5 
            
        marco_qr = SurroundingRectangle(qr_image, color=color_texto_principal, stroke_width=3, corner_radius=0.1, buff=0.15)
        grupo_qr = Group(marco_qr, qr_image)
        
        # Nuevo texto del repositorio
        texto_repo = Text("REPOSITORIO GITHUB", font_size=24, color=color_texto_principal, weight=BOLD)
        texto_repo.next_to(grupo_qr, UP, buff=0.3)
        
        # Agrupamos todo el bloque izquierdo para posicionarlo junto
        grupo_izquierdo = Group(texto_repo, grupo_qr)
        grupo_izquierdo.next_to(titulo, DOWN, buff=1.2).to_edge(LEFT, buff=2)

        # --- 3. DISEÑO DE JERARQUÍA EN B&W (A la derecha) ---
        plato1 = Ellipse(width=3, height=0.8, color=GRAY_E, fill_opacity=0.8) 
        plato2 = Ellipse(width=3, height=0.8, color=GRAY_D, fill_opacity=0.9).shift(UP * 0.2)
        plato3 = Ellipse(width=3, height=0.8, color=GRAY_C, fill_opacity=1.0).shift(UP * 0.4) 
        
        grupo_platos = VGroup(plato1, plato2, plato3)
        txt_disco = Text("Disco Magnético", font_size=20, color=BLACK, weight=BOLD).next_to(grupo_platos, DOWN)
        disco_completo = VGroup(grupo_platos, txt_disco)

        bloque_ram = RoundedRectangle(corner_radius=0.15, width=2.5, height=0.8, color=GRAY_D, fill_opacity=0.8)
        txt_ram = Text("RAM", font_size=22, color=WHITE, weight=BOLD).move_to(bloque_ram)
        ram_completo = VGroup(bloque_ram, txt_ram)

        bloque_cache = RoundedRectangle(corner_radius=0.1, width=1.8, height=0.6, color=BLACK, fill_opacity=1.0)
        txt_cache = Text("CPU", font_size=20, color=WHITE, weight=BOLD).move_to(bloque_cache)
        cache_completo = VGroup(bloque_cache, txt_cache)

        jerarquia = VGroup(disco_completo, ram_completo, cache_completo).arrange(UP, buff=0.8)
        jerarquia.next_to(titulo, DOWN, buff=0.8).to_edge(RIGHT, buff=2.5)

        linea_disco_ram = Line(disco_completo.get_top(), ram_completo.get_bottom(), color=color_acento, stroke_width=2)
        linea_ram_cache = Line(ram_completo.get_top(), cache_completo.get_bottom(), color=color_acento, stroke_width=2)

        # --- 4. PREPARACIÓN DEL DATO ANIMADO B&W ---
        dato_nucleo = Dot(color=BLACK, radius=0.1)
        dato_brillo = Dot(color=GRAY_B, radius=0.25, fill_opacity=0.4)
        dato = VGroup(dato_brillo, dato_nucleo)
        dato.move_to(disco_completo.get_center())

        estela = TracedPath(dato_nucleo.get_center, stroke_color=BLACK, stroke_width=4, dissipating_time=0.4)

        # --- 5. SECUENCIA DE ANIMACIONES ---
        self.play(Write(titulo), run_time=1.2)
        
        # Animación del QR incluyendo el nuevo texto
        self.play(
            Write(texto_repo),
            FadeIn(qr_image, shift=UP * 0.3),
            Create(marco_qr),
            run_time=1
        )
        
        self.play(
            AnimationGroup(
                Create(disco_completo),
                Create(linea_disco_ram),
                Create(ram_completo),
                Create(linea_ram_cache),
                Create(cache_completo),
                lag_ratio=0.3
            ),
            run_time=2.5
        )

        self.add(estela)
        self.play(FadeIn(dato, scale=0.5))
        
        self.play(dato.animate.move_to(ram_completo.get_center()), run_time=1)
        self.play(dato.animate.move_to(cache_completo.get_center()), run_time=0.8)
        
        self.play(
            Flash(cache_completo, color=BLACK, line_length=0.4, num_lines=12, flash_radius=1.2),
            FadeOut(dato),
            run_time=0.8
        )
        
        self.wait(0.5)
        self.remove(estela)

        self.next_slide()
        self.limpiar_pantalla()
        
    def slide_simulador_nand2tetris(self):
        titulo, linea = self.crear_titulo("Simulador de Nand2tetris", palabra_clave="Nand2tetris", color_clave=BLACK)
        self.play(Write(titulo), GrowFromCenter(linea))

        browser_window = RoundedRectangle(corner_radius=0.2, width=10, height=5.5, color=DARK_GRAY, fill_color=WHITE, fill_opacity=1)
        browser_header = Rectangle(width=10, height=0.5, color=DARK_GRAY, fill_color=LIGHT_GRAY, fill_opacity=1).align_to(browser_window, UP)
        
        dot_1 = Circle(radius=0.08, color=GRAY, fill_opacity=1).move_to(browser_header.get_left() + RIGHT*0.4)
        dot_2 = Circle(radius=0.08, color=GRAY, fill_opacity=1).next_to(dot_1, RIGHT, buff=0.15)
        dot_3 = Circle(radius=0.08, color=GRAY, fill_opacity=1).next_to(dot_2, RIGHT, buff=0.15)

        url_bar = RoundedRectangle(corner_radius=0.1, width=6, height=0.25, color=GRAY, fill_color=WHITE, fill_opacity=1).move_to(browser_header)
        url_text = Text("https://nand2tetris.github.io/web-ide/chip", font_size=12, color=BLACK).move_to(url_bar) 
        
        browser_ui = VGroup(browser_window, browser_header, dot_1, dot_2, dot_3, url_bar, url_text)
        browser_ui.next_to(linea, DOWN, buff=0.4)

        self.play(FadeIn(browser_ui, shift=UP))

        logo_simulador = Text("Simulator", font_size=42, color=BLACK, weight=BOLD).move_to(browser_window.get_center() + UP*1)
        subtitulo_web = Text("Exploración de las memorias", font_size=20, color=DARK_GRAY).next_to(logo_simulador, DOWN, buff=0.3)
        
        prompt_box = RoundedRectangle(corner_radius=0.1, width=7, height=0.8, color=GRAY, fill_color=WHITE, fill_opacity=1).next_to(subtitulo_web, DOWN, buff=0.6)
        prompt_text = Text("Ingresa una dirección de memoria (ej. 0x00A4)...", font_size=16, color=GRAY).move_to(prompt_box).align_to(prompt_box.get_left(), LEFT).shift(RIGHT*0.3)
        
        btn_generar = RoundedRectangle(corner_radius=0.1, width=2.5, height=0.5, color=BLACK, fill_color=BLACK, fill_opacity=1).next_to(prompt_box, DOWN, buff=0.4)
        btn_text = Text("Leer / Escribir", font_size=16, color=WHITE, weight=BOLD).move_to(btn_generar)
        grupo_btn = VGroup(btn_generar, btn_text)

        web_content = VGroup(logo_simulador, subtitulo_web, prompt_box, prompt_text, grupo_btn)

        self.play(LaggedStart(
            FadeIn(logo_simulador, shift=DOWN),
            FadeIn(subtitulo_web),
            Create(prompt_box),
            Write(prompt_text),
            FadeIn(grupo_btn, shift=UP),
            lag_ratio=0.15
        ))
        
        self.next_slide()

        transicion_lbl = Text("Abriendo simulador...", font_size=24, color=BLACK, weight=BOLD)
        caja_transicion = SurroundingRectangle(transicion_lbl, color=BLACK, fill_color=WHITE, fill_opacity=1, buff=0.4)
        grupo_transicion = VGroup(caja_transicion, transicion_lbl).move_to(browser_window.get_center())

        self.play(web_content.animate.set_opacity(0.1), FadeIn(grupo_transicion, scale=0.8))
        
        self.next_slide()
        self.limpiar_pantalla()
        
    def almacenamiento_secundario(self):
        # --- 1. PALETA DE COLORES Y FUENTE B&W ---
        fuente = "sans-serif"
        color_texto = BLACK
        color_secundario = DARK_GRAY
        
        # --- 2. TÍTULO CENTRADO (Sin ser full mayúsculas) ---
        titulo = Text("Almacenamiento secundario", font=fuente, font_size=42, color=color_texto, weight=BOLD)
        titulo.to_edge(UP, buff=0.4)
        
        linea_subtitulo = Line(LEFT, RIGHT, color=BLACK, stroke_width=3).scale(3.5)
        linea_subtitulo.next_to(titulo, DOWN, buff=0.1)

        # --- 3. CONTENIDO DE TEXTO (Centrado) ---
        # Al escribir en múltiples líneas con \n, Manim centra el texto por defecto
        txt_1 = Text(
            "Es una unidad de memoria \"no volátil\" la cual posee una capacidad de\nalmacenamiento mucho más grande que la memoria principal.", 
            font=fuente, font_size=22, color=color_texto, line_spacing=0.8
        )
        txt_2 = Text(
            "Sin embargo, esta tiene un tiempo de acceso a la información más lento\ny también es la memoria menos costosa en la jerarquía.", 
            font=fuente, font_size=22, color=color_secundario, line_spacing=0.8
        )
        txt_3_tit = Text("Se cuentan con dos tipos principales:", font=fuente, font_size=22, color=color_texto, weight=BOLD)
        
        # Agrupamos y centramos todo el bloque de texto
        contenido = VGroup(txt_1, txt_2, txt_3_tit).arrange(DOWN, buff=0.4)
        contenido.next_to(linea_subtitulo, DOWN, buff=0.5)

        # --- 4. DIBUJOS GENERADOS CON CÓDIGO (Centrados y Simétricos) ---
        
        # A) Dibujo del Disco Duro (HDD) - Izquierda
        hdd_case = RoundedRectangle(width=2.4, height=3.2, corner_radius=0.15, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=2)
        hdd_platter = Circle(radius=0.9, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=1.5).move_to(hdd_case).shift(UP*0.35)
        hdd_platter_inner = Circle(radius=0.3, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=1).move_to(hdd_platter)
        
        # CORREGIDO: El borde que salía rojo ahora es GRIS (color=GRAY)
        hdd_spindle = Circle(radius=0.1, fill_color=BLACK, fill_opacity=1, color=GRAY).move_to(hdd_platter)
        
        # Brazo mecánico del HDD
        # CORREGIDO: El borde que salía rojo ahora es GRIS (color=GRAY)
        hdd_arm_base = Circle(radius=0.15, fill_color=BLACK, fill_opacity=1, color=GRAY).move_to(hdd_case.get_corner(DL) + UP*0.5 + RIGHT*0.4)
        hdd_arm = Line(hdd_arm_base.get_center(), hdd_platter.get_center() + DOWN*0.15 + RIGHT*0.2, stroke_color=BLACK, stroke_width=3)
        hdd_head = Dot(radius=0.06, color=BLACK).move_to(hdd_arm.get_end())
        brazo_y_cabeza = VGroup(hdd_arm, hdd_head)
        
        lbl_hdd = Text("Disco duro (HDD)", font=fuente, font_size=18, color=BLACK, weight=BOLD).next_to(hdd_case, DOWN, buff=0.25)
        hdd_completo = VGroup(hdd_case, hdd_platter, hdd_platter_inner, hdd_spindle, hdd_arm_base, brazo_y_cabeza, lbl_hdd)
        hdd_completo.scale(0.85).move_to(DOWN * 1.8 + LEFT * 3) # Ubicado a la izquierda

        # B) Dibujo del Disco de Estado Sólido (SSD) - Derecha
        ssd_case = RoundedRectangle(width=2.4, height=3.2, corner_radius=0.1, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=2)
        
        # Chips de memoria flash
        chips = VGroup(*[
            RoundedRectangle(width=0.8, height=1.1, corner_radius=0.05, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=1.5)
            for _ in range(4)
        ]).arrange_in_grid(2, 2, buff=0.25).move_to(ssd_case).shift(UP*0.15)
        
        # Conector SATA/M.2 simulado abajo
        connector = Rectangle(width=1.3, height=0.15, fill_color=BLACK, fill_opacity=1, stroke_width=0).move_to(ssd_case.get_bottom())
        
        lbl_ssd = Text("Estado sólido (SSD)", font=fuente, font_size=18, color=BLACK, weight=BOLD).next_to(ssd_case, DOWN, buff=0.25)
        ssd_completo = VGroup(ssd_case, chips, connector, lbl_ssd)
        ssd_completo.scale(0.85).move_to(DOWN * 1.8 + RIGHT * 3) # Ubicado a la derecha

        # --- 5. SECUENCIA DE ANIMACIONES ---
        
        # Título y Textos principales
        self.play(Write(titulo), Create(linea_subtitulo))
        self.play(FadeIn(contenido, shift=UP * 0.2))
        self.next_slide()
        
        # Animando aparición del HDD
        self.play(Create(hdd_case), FadeIn(lbl_hdd, shift=UP*0.1))
        self.play(
            Create(hdd_platter), Create(hdd_platter_inner), FadeIn(hdd_spindle),
            Create(hdd_arm_base), Create(brazo_y_cabeza),
            run_time=1.5
        )
        
        # Animación del brazo del HDD "leyendo" el disco
        self.play(Rotate(brazo_y_cabeza, angle=PI/12, about_point=hdd_arm_base.get_center()), run_time=0.4)
        self.play(Rotate(brazo_y_cabeza, angle=-PI/8, about_point=hdd_arm_base.get_center()), run_time=0.4)
        self.play(Rotate(brazo_y_cabeza, angle=PI/24, about_point=hdd_arm_base.get_center()), run_time=0.4)
        self.next_slide()

        # Animando aparición del SSD
        self.play(Create(ssd_case), FadeIn(connector), FadeIn(lbl_ssd, shift=UP*0.1))
        
        # Los chips aparecen uno por uno
        self.play(LaggedStart(*[Create(chip) for chip in chips], lag_ratio=0.2), run_time=1.5)

        self.wait(1)
        self.next_slide()
        self.limpiar_pantalla()
        
    def diapositiva_detalles_hdd(self):
        # --- CONFIGURACIÓN INICIAL ---
        fuente = "sans-serif"
        color_texto = BLACK
        
        titulo = Text("Hard Disk Drive", font=fuente, font_size=42, color=color_texto, weight=BOLD)
        titulo.to_edge(UP, buff=0.4)
        
        linea_subtitulo = Line(LEFT, RIGHT, color=BLACK, stroke_width=3).scale(3.5)
        linea_subtitulo.next_to(titulo, DOWN, buff=0.1)

        # --- DIBUJO DEL DISCO DURO GENERADO CON CÓDIGO ---
        hdd_case = RoundedRectangle(width=2.4, height=3.2, corner_radius=0.15, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=2)
        hdd_platter = Circle(radius=0.9, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=1.5).move_to(hdd_case).shift(UP*0.35)
        hdd_platter_inner = Circle(radius=0.3, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=1).move_to(hdd_platter)
        
        hdd_spindle = Circle(radius=0.1, fill_color=BLACK, fill_opacity=1, color=GRAY).move_to(hdd_platter)
        
        hdd_arm_base = Circle(radius=0.15, fill_color=BLACK, fill_opacity=1, color=GRAY).move_to(hdd_case.get_corner(DL) + UP*0.5 + RIGHT*0.4)
        hdd_arm = Line(hdd_arm_base.get_center(), hdd_platter.get_center() + DOWN*0.15 + RIGHT*0.2, stroke_color=BLACK, stroke_width=3)
        hdd_head = Dot(radius=0.06, color=BLACK).move_to(hdd_arm.get_end())
        brazo_y_cabeza = VGroup(hdd_arm, hdd_head)
        
        # Agrupamos los platos para facilitar la animación luego
        grupo_platters = VGroup(hdd_platter, hdd_platter_inner)
        
        hdd_completo = VGroup(hdd_case, grupo_platters, hdd_spindle, hdd_arm_base, brazo_y_cabeza)
        
        # Lo hacemos más grande y lo ponemos a la derecha
        hdd_completo.scale(1.8).to_edge(RIGHT, buff=1.0).shift(DOWN * 0.2)

        # --- TEXTOS Y DESCRIPCIONES (Lado Izquierdo) ---
        texto_general = Text(
            "Consiste en un disco giratorio cubierto\n"
            "de material magnético y un cabezal de\n"
            "escritura que se encarga de consultar y\n"
            "modificar la información en la\n"
            "superficie del disco.", 
            font=fuente, font_size=24, color=color_texto, line_spacing=0.8
        ).to_edge(LEFT, buff=0.8).shift(UP * 0.5)

        # Textos de la estructura
        estilo_estruct = {"font": fuente, "font_size": 20, "color": color_texto, "line_spacing": 0.8}
        
        tit_estructura = Text("Estructura principal:", font=fuente, font_size=24, color=color_texto, weight=BOLD).to_edge(LEFT, buff=0.8).shift(UP * 1.5)
        
        t_platters = Text("• Platters: Placas magnéticas de vidrio/aluminio\n  donde se almacena la información.", **estilo_estruct)
        t_spindle = Text("• Spindle: Eje central que hace rotar los platos.\n  La velocidad se mide en RPM.", **estilo_estruct)
        t_arm = Text("• Actuator Arm: Motor que controla el movimiento\n  del brazo sobre los platos.", **estilo_estruct)
        t_head = Text("• Read/write Head: Cabezal que realiza la lectura\n  y escritura física de datos.", **estilo_estruct)

        grupo_textos_estructura = VGroup(t_platters, t_spindle, t_arm, t_head).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        grupo_textos_estructura.next_to(tit_estructura, DOWN, aligned_edge=LEFT, buff=0.3)


        # --- SECUENCIA DE ANIMACIONES ---
        
        # 1. Entrada del título y el HDD
        self.play(Write(titulo), Create(linea_subtitulo))
        self.play(FadeIn(texto_general, shift=RIGHT * 0.5), Create(hdd_case))
        self.play(
            Create(grupo_platters), FadeIn(hdd_spindle),
            Create(hdd_arm_base), Create(brazo_y_cabeza),
            run_time=1.5
        )
        self.next_slide()

        # 2. Transición a la estructura
        self.play(
            FadeOut(texto_general, shift=UP * 0.5),
            FadeIn(tit_estructura, shift=UP * 0.5)
        )
        
        # 3. Explicando Platters
        self.play(FadeIn(t_platters, shift=RIGHT * 0.2))
        self.play(Indicate(grupo_platters, color=GRAY, scale_factor=1.1)) # Resalta los platos
        self.next_slide()

        # 4. Explicando Spindle
        self.play(FadeIn(t_spindle, shift=RIGHT * 0.2))
        self.play(Indicate(hdd_spindle, color=GRAY, scale_factor=1.5)) # Resalta el centro
        self.next_slide()

        # 5. Explicando Actuator Arm
        self.play(FadeIn(t_arm, shift=RIGHT * 0.2))
        self.play(Indicate(hdd_arm_base, color=GRAY, scale_factor=1.3)) # Resalta la base del brazo
        self.next_slide()

        # 6. Explicando Read/Write Head
        self.play(FadeIn(t_head, shift=RIGHT * 0.2))
        self.play(Indicate(brazo_y_cabeza, color=GRAY, scale_factor=1.2)) # Resalta el brazo y la cabeza
        
        # Animación extra de lectura para cerrar
        self.play(Rotate(brazo_y_cabeza, angle=PI/12, about_point=hdd_arm_base.get_center()), run_time=0.4)
        self.play(Rotate(brazo_y_cabeza, angle=-PI/8, about_point=hdd_arm_base.get_center()), run_time=0.4)
        self.play(Rotate(brazo_y_cabeza, angle=PI/24, about_point=hdd_arm_base.get_center()), run_time=0.4)

        self.wait(1)
        self.next_slide()
        self.limpiar_pantalla()
        
    def slide_delay_hdd(self):
        # --- 1. CONFIGURACIÓN GENERAL ---
        self.camera.background_color = WHITE
        
        # Paleta estricta de escala de grises
        C_TEXTO = BLACK
        C_DESTAQUE = GRAY
        C_PISTA = GRAY_B
        C_SECTOR = GRAY_C
        C_BRAZO = GRAY_D
        C_BASE = BLACK
        FUENTE = "sans-serif"

        # --- 2. ELEMENTOS DE TEXTO (TÍTULO) ---
        titulo = Text("DELAY EN HDD", font=FUENTE, font_size=38, weight=BOLD, color=C_TEXTO)
        titulo.to_edge(UP, buff=0.4)
        linea_subtitulo = Line(LEFT, RIGHT, color=C_TEXTO, stroke_width=3).scale(3.5)
        linea_subtitulo.next_to(titulo, DOWN, buff=0.1)

        # --- 3. CREACIÓN DEL DIAGRAMA DEL DISCO (Izquierda) ---
        # Movemos el centro del disco hacia la izquierda de la pantalla
        centro_disco = LEFT * 3.5  
        
        # Base y pistas (escala ligeramente aumentada al tener más espacio)
        platter = Circle(radius=2.0, color=C_BASE, fill_color=LIGHT_GRAY, fill_opacity=0.1, stroke_width=2)
        pistas = VGroup(*[
            Circle(radius=r, color=C_PISTA, stroke_width=1, stroke_opacity=0.6) 
            for r in [0.75, 1.15, 1.5]
        ])
        
        # Sector objetivo
        sector = AnnularSector(
            inner_radius=1.0, outer_radius=1.35, angle=30*DEGREES, start_angle=0*DEGREES, 
            color=C_SECTOR, fill_opacity=0.7, stroke_color=C_BASE, stroke_width=1
        )
        disco_completo = VGroup(platter, pistas, sector).move_to(centro_disco)

        # Brazo y cabezal (las posiciones relativas se mantienen con respecto al nuevo centro)
        pivot = centro_disco + LEFT * 2.6 + UP * 1.8
        base_pivot = Dot(pivot, color=C_BASE, radius=0.15)
        punto_lectura = centro_disco + UP * 1.15 
        
        brazo = Line(pivot, punto_lectura, color=C_BRAZO, stroke_width=6)
        cabezal = Square(side_length=0.15, color=C_BASE, fill_opacity=1).move_to(punto_lectura)
        actuador = VGroup(brazo, cabezal)
        
        # Posición inicial (retraído)
        angulo_offset = 35 * DEGREES
        actuador.rotate(angulo_offset, about_point=pivot)

        # --- 4. CONCEPTOS Y FÓRMULA (Derecha) ---
        conceptos_textos = [
            "• Seek Time (T_s)",
            "• Latencia Rotacional (T_l)",
            "• Tiempo de Transferencia (T_t)",
            "• Tiempo del Controlador (T_c)"
        ]
        conceptos = VGroup(*[Text(t, font=FUENTE, font_size=26, color=C_TEXTO) for t in conceptos_textos])
        
        # Alineamos el texto a la izquierda, pero lo movemos al lado derecho de la pantalla
        conceptos.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        conceptos.move_to(RIGHT * 2.5 + UP * 0.3)

        # Fórmula final
        formula = MathTex(r"T_{total} = T_{s} + T_{l} + T_{t} + T_{c}", font_size=42, color=C_TEXTO)
        formula.next_to(conceptos, DOWN, buff=0.8) # Más espacio entre conceptos y fórmula
        caja_formula = SurroundingRectangle(formula, color=C_DESTAQUE, buff=0.2, stroke_width=2)

        # --- 5. SECUENCIA DE ANIMACIÓN ---
        self.play(Write(titulo), Create(linea_subtitulo))
        
        # Aparece el disco a la izquierda
        self.play(
            FadeIn(disco_completo), 
            Create(base_pivot), 
            Create(actuador)
        )
        
        # El texto aparece deslizando suavemente hacia la derecha
        self.play(FadeIn(conceptos, shift=LEFT))
        self.wait(1)

        # Paso 1: Seek Time
        self.play(
            Indicate(conceptos[0], color=C_DESTAQUE, scale_factor=1.1),
            Rotate(actuador, angle=-angulo_offset, about_point=pivot),
            run_time=1.5, rate_func=smooth
        )
        self.wait(0.5)

        # Paso 2: Latencia Rotacional
        self.play(
            Indicate(conceptos[1], color=C_DESTAQUE, scale_factor=1.1),
            Rotate(disco_completo, angle=90*DEGREES, about_point=centro_disco),
            run_time=2, rate_func=linear
        )
        self.wait(0.5)

        # Paso 3: Tiempo de Transferencia
        self.play(
            Indicate(conceptos[2], color=C_DESTAQUE, scale_factor=1.1),
            Flash(cabezal, color=C_DESTAQUE, line_length=0.3, flash_radius=0.4),
            sector.animate.set_fill(C_DESTAQUE, opacity=0.8),
            run_time=1.5
        )
        self.wait(0.5)

        # Paso 4: Tiempo del Controlador
        self.play(
            Indicate(conceptos[3], color=C_DESTAQUE, scale_factor=1.1),
            Create(caja_formula), 
            Write(formula)
        )
        
        self.next_slide()
        self.limpiar_pantalla()
        
    def slide_comparativa_hdd(self):
        # Título principal en Blanco y Negro
        titulo, linea = self.crear_titulo("Ventajas vs Desventajas del HDD", palabra_clave="vs", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        # --- TEXTOS ---
        # Ventajas (4)
        txt_cap = "Alta capacidad de almacenamiento (hasta 36TB)\ny excelente relación costo-beneficio."
        txt_rec = "Retienen información sin energía y tienen\nmúltiples herramientas de recuperación."
        txt_com = "Sencillos de expandir (swappear) y\ncompatibles con casi cualquier sistema."
        txt_esc = "No tienen límite de ciclos de escritura,\nideales para reescribir datos constantemente." # Nueva ventaja
        
        # Desventajas (4)
        txt_len = "Más lentos que los SSD en archivos\ngrandes o multitarea compleja."
        txt_con = "Las partes mecánicas requieren mucha\nmás energía que los chips flash."
        txt_dur = "Las partes móviles los hacen muy frágiles\nante caídas (pérdida de datos)."
        txt_rui = "Las placas giratorias generan calor\ny ruido, afectando la eficiencia."

        # --- ICONOS ---
        # Iconos Ventajas
        icon_cap = VGroup(RoundedRectangle(width=0.6, height=0.8, corner_radius=0.1, color=BLACK), Text("TB", font_size=14, color=BLACK).move_to(ORIGIN))
        icon_rec = VGroup(Circle(radius=0.35, color=BLACK, stroke_width=4), Line(ORIGIN, UP*0.25, color=BLACK), Line(ORIGIN, RIGHT*0.2, color=BLACK))
        icon_com = VGroup(Line(LEFT*0.3, RIGHT*0.3, color=BLACK), Triangle(color=BLACK).scale(0.1).rotate(-PI/2).shift(RIGHT*0.3), Triangle(color=BLACK).scale(0.1).rotate(PI/2).shift(LEFT*0.3)).add(Text("USB", font_size=10, color=BLACK).shift(DOWN*0.2))
        icon_esc = VGroup(Circle(radius=0.15, color=BLACK).shift(LEFT*0.14), Circle(radius=0.15, color=BLACK).shift(RIGHT*0.14)) # Icono de infinito para la escritura
        
        # Iconos Desventajas
        icon_len = VGroup(Arc(radius=0.3, angle=PI*1.5, color=BLACK), Dot(color=BLACK).scale(0.5))
        icon_con = VGroup(Circle(radius=0.3, color=BLACK), Dot(color=BLACK)).scale(0.8)
        icon_dur = VGroup(Line(UP*0.3, DOWN*0.3, color=BLACK), Line(LEFT*0.3, RIGHT*0.3, color=BLACK).rotate(PI/4))
        icon_rui = VGroup(*[Arc(radius=0.15*i, angle=PI/2, color=BLACK) for i in range(1,4)])

        # --- DATOS ---
        datos_ventajas = [
            ("Gran Capacidad", txt_cap, icon_cap),
            ("Recuperabilidad", txt_rec, icon_rec),
            ("Compatibilidad", txt_com, icon_com),
            ("Escritura Ilimitada", txt_esc, icon_esc) # Agregado a la lista
        ]
        datos_desventajas = [
            ("Rendimiento lento", txt_len, icon_len),
            ("Consumo energético", txt_con, icon_con),
            ("Menor durabilidad", txt_dur, icon_dur),
            ("Ruido y Calor", txt_rui, icon_rui)
        ]

        # --- FUNCIÓN CONSTRUCTORA DE TARJETAS ---
        def crear_tarjeta(tit, txt, icono):
            # Tarjeta optimizada para 4 filas
            base = RoundedRectangle(
                width=6.5, height=1.1, corner_radius=0.1, 
                fill_color=WHITE, fill_opacity=1, 
                stroke_color=BLACK, stroke_width=2
            )
            borde_izq = Rectangle(
                width=0.15, height=1.1, fill_color=BLACK, fill_opacity=1, stroke_width=0
            ).align_to(base, LEFT)
            
            lbl_tit = Text(tit, font_size=16, weight=BOLD, color=BLACK)
            lbl_txt = Text(txt, font_size=12, color=BLACK, line_spacing=0.8)
            
            grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            contenido = VGroup(icono.copy(), grupo_txt).arrange(RIGHT, buff=0.3).move_to(base.get_center()).align_to(base, LEFT).shift(RIGHT*0.3)
            
            return VGroup(base, borde_izq, contenido)

        # --- ENSAMBLAJE DE COLUMNAS ---
        # Usamos un buff ligeramente menor (0.15) para que las 4 filas quepan bien verticalmente
        columna_ventajas = VGroup(*[crear_tarjeta(tit, txt, icono) for tit, txt, icono in datos_ventajas])
        columna_ventajas.arrange(DOWN, buff=0.15)

        columna_desventajas = VGroup(*[crear_tarjeta(tit, txt, icono) for tit, txt, icono in datos_desventajas])
        columna_desventajas.arrange(DOWN, buff=0.15)

        # Agrupar ambas columnas lado a lado
        pantalla_dividida = VGroup(columna_ventajas, columna_desventajas).arrange(RIGHT, buff=0.4, aligned_edge=UP)
        
        # Subtítulos de las columnas
        sub_ven = Text("Pros", font_size=20, weight=BOLD, color=BLACK).next_to(columna_ventajas, UP, buff=0.2)
        sub_des = Text("Contras", font_size=20, weight=BOLD, color=BLACK).next_to(columna_desventajas, UP, buff=0.2)
        pantalla_dividida.add(sub_ven, sub_des)

        # Ajuste vertical general para centrar todo bajo el título
        pantalla_dividida.shift(DOWN * 0.4) 

        # --- ANIMACIÓN ---
        self.play(
            FadeIn(pantalla_dividida, shift=UP*0.3),
            run_time=1.5
        )
        
        self.next_slide()
        self.limpiar_pantalla()

    def slide_funcionamiento_hdd(self):
        # --- 1. CONFIGURACIÓN Y TÍTULO ---
        fuente = "sans-serif"
        color_texto = BLACK
        
        titulo = Text("Funcionamiento del HDD", font=fuente, font_size=42, color=color_texto, weight=BOLD)
        titulo.to_edge(UP, buff=0.4)
        linea_subtitulo = Line(LEFT, RIGHT, color=BLACK, stroke_width=3).scale(3.5)
        linea_subtitulo.next_to(titulo, DOWN, buff=0.1)

        # --- 2. TEXTOS DESCRIPTIVOS (Anclados a la Izquierda) ---
        estilo_texto = {"font": fuente, "font_size": 22, "color": color_texto, "line_spacing": 0.8}
        
        p1 = Text("• Los platters giran a gran velocidad.", **estilo_texto)
        p2 = Text("• El cabezal busca el 'track' y el 'sector'.", **estilo_texto)
        p3 = Text("• Lectura/Escritura mediante magnetismo.", **estilo_texto)
        p4 = Text("• El controlador transfiere los datos al PC.", **estilo_texto)

        puntos = VGroup(p1, p2, p3, p4).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        puntos.to_edge(LEFT, buff=1.0) 

        # --- 3. DIAGRAMA DEL DISCO (Anclado a la Derecha) ---
        centro_disco = RIGHT * 3.5 + DOWN * 0.5
        
        platter_base = Circle(radius=2.0, color=BLACK, fill_color=WHITE, fill_opacity=1, stroke_width=2).move_to(centro_disco)
        centro_hueco = Circle(radius=0.3, color=BLACK, fill_color=WHITE, fill_opacity=1, stroke_width=2).move_to(centro_disco)
        
        # Pistas (Anillos de referencia)
        pistas = VGroup(*[
            Circle(radius=r, color=GRAY_C, stroke_width=1).move_to(centro_disco) 
            for r in np.arange(0.7, 2.0, 0.4)
        ])
        
        # Sectores (Líneas radiales)
        lineas_sectores = VGroup(*[
            Line(centro_disco, platter_base.point_at_angle(angle), color=GRAY_B, stroke_width=1) 
            for angle in np.arange(0, TAU, TAU/8)
        ])

        # --- 4. RESALTADOS (Partes del funcionamiento) ---
        # CORRECCIÓN: Usar .shift() en lugar de .move_to()
        
        # Track: El camino circular
        track_res = Annulus(inner_radius=1.1, outer_radius=1.5, color=GRAY_A, fill_opacity=0.4, stroke_width=0).shift(centro_disco)
        
        # Disk Sector: La "rebanada" 
        sector_res = AnnularSector(inner_radius=0.3, outer_radius=2.0, angle=TAU/8, start_angle=TAU/8, color=GRAY_B, fill_opacity=0.3).shift(centro_disco)
        
        # Track Sector: El dato específico (Intersección)
        dato_res = AnnularSector(inner_radius=1.1, outer_radius=1.5, angle=TAU/8, start_angle=TAU/8, color=GRAY_E, fill_opacity=0.9).shift(centro_disco)

       # --- 5. ETIQUETAS Y FLECHAS ---
        estilo_lbl = {"font": fuente, "font_size": 18, "color": BLACK, "weight": BOLD}
        
        # 1. Track: Apunta al cuadrante superior izquierdo (radio ~1.3, dentro del Annulus de 1.1 a 1.5)
        lbl_track = Text("Track", **estilo_lbl).move_to(centro_disco + UP * 2.0 + LEFT * 2.0)
        arr_track = Arrow(lbl_track.get_bottom(), centro_disco + UP * 0.92 + LEFT * 0.92, color=BLACK, tip_length=0.15)

        # 2. Disk Sector: Apunta al cuadrante superior derecho, en la parte exterior de la "rebanada" (radio ~1.8)
        lbl_sector = Text("Disk Sector", **estilo_lbl).move_to(centro_disco + UP * 2.5 + RIGHT * 1.5)
        arr_sector = Arrow(lbl_sector.get_bottom(), centro_disco + UP * 1.65 + RIGHT * 0.68, color=BLACK, tip_length=0.15)

        # 3. Track Sector (Dato): Apunta exactamente al centro geométrico de la intersección usando el método de Manim
        lbl_dato = Text("Track Sector", **estilo_lbl).move_to(centro_disco + UP * 0.3 + RIGHT * 2.8)
        arr_dato = Arrow(lbl_dato.get_left(), dato_res.get_center(), color=BLACK, tip_length=0.15)

        # --- 6. BRAZO ACTUADOR ---
        base_brazo = Dot(centro_disco + DOWN * 2.2 + LEFT * 2.2, color=BLACK, radius=0.15)
        # Ahora que dato_res está bien posicionado, get_center() apuntará correctamente al sector
        brazo = Line(base_brazo.get_center(), dato_res.get_center(), color=BLACK, stroke_width=5)
        cabezal = Square(side_length=0.15, color=BLACK, fill_opacity=1).move_to(brazo.get_end())
        actuador = VGroup(base_brazo, brazo, cabezal)

        # --- 7. ANIMACIÓN ---
        self.play(Write(titulo), Create(linea_subtitulo))
        self.play(FadeIn(puntos, shift=RIGHT * 0.3))
        
        self.play(Create(platter_base), Create(pistas), Create(lineas_sectores), Create(centro_hueco))
        
        self.play(FadeIn(track_res), Write(lbl_track), Create(arr_track))
        self.play(FadeIn(sector_res), Write(lbl_sector), Create(arr_sector))
        self.play(FadeIn(dato_res), Write(lbl_dato), Create(arr_dato))
        
        self.play(Create(actuador))

        self.next_slide()
        self.limpiar_pantalla()

    def slide_ssd_unidades(self):
        # --- 1. CONFIGURACIÓN Y TÍTULO ---
        self.camera.background_color = WHITE
        FUENTE = "sans-serif"
        
        # Usaré un título estándar aquí, pero puedes volver a usar tu self.crear_titulo()
        titulo = Text("Unidades de Estado Sólido (SSD)", font=FUENTE, font_size=40, weight=BOLD, color=BLACK)
        titulo.to_edge(UP, buff=0.4)
        linea_titulo = Line(LEFT, RIGHT, color=BLACK, stroke_width=3).scale(4).next_to(titulo, DOWN, buff=0.2)
        
        # --- 2. DIBUJO VECTORIAL DEL SSD (Izquierda) ---
        ssd_case = RoundedRectangle(width=2.8, height=3.8, corner_radius=0.15, fill_color=LIGHT_GRAY, fill_opacity=0.2, stroke_color=BLACK, stroke_width=3)
        
        # Chips de memoria flash
        chips = VGroup(*[
            RoundedRectangle(width=0.9, height=1.3, corner_radius=0.05, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=2)
            for _ in range(4)
        ]).arrange_in_grid(2, 2, buff=0.3).move_to(ssd_case).shift(UP*0.2)
        
        # Detalle extra: pequeñas líneas simulando circuitos dentro de los chips
        for chip in chips:
            pines = VGroup(*[Line(LEFT*0.1, RIGHT*0.1, color=GRAY, stroke_width=2) for _ in range(3)]).arrange(DOWN, buff=0.2)
            pines.move_to(chip)
            chip.add(pines)

        # Conector inferior simulado
        connector = Rectangle(width=1.5, height=0.2, fill_color=DARK_GRAY, fill_opacity=1, stroke_width=0).next_to(ssd_case.get_bottom(), UP, buff=0)
        pines_conector = VGroup(*[Line(UP*0.05, DOWN*0.05, color=WHITE, stroke_width=1) for _ in range(10)]).arrange(RIGHT, buff=0.1).move_to(connector)
        connector_group = VGroup(connector, pines_conector)

        lbl_ssd = Text("Estado sólido (SSD)", font=FUENTE, font_size=20, color=BLACK, weight=BOLD).next_to(ssd_case, DOWN, buff=0.3)
        
        ssd_completo = VGroup(ssd_case, chips, connector_group, lbl_ssd)
        # Lo ubicamos a la izquierda, reemplazando la imagen original
        ssd_completo.to_edge(LEFT, buff=1.5).shift(DOWN*0.2)


        # --- 3. TARJETAS DE INFORMACIÓN (Derecha) ---
        txt_flash = "Utilizan memoria \"flash\" en lugar de un\ndisco giratorio para almacenar datos."
        txt_eeprom = "Trabaja bajo el principio EEPROM:\nElectrical Erasable Programmable ROM."
        txt_versat = "Permite que la información sea borrada\ny actualizada múltiples veces electrónicamente."

        # Iconos
        icon_flash = VGroup(*[Line(ORIGIN, UP*0.3).rotate(a*DEGREES, about_point=ORIGIN) for a in range(0, 360, 45)], Dot(radius=0.05)).set_color(BLACK).scale(0.5)
        icon_eeprom = VGroup(Rectangle(width=0.6, height=0.4, color=BLACK), Text("E2", font_size=12, color=BLACK, weight=BOLD).move_to(ORIGIN))
        icon_versat = VGroup(Arc(radius=0.3, start_angle=0, angle=300*DEGREES, color=BLACK), Triangle(color=BLACK).scale(0.1).move_to(ORIGIN + RIGHT*0.3).rotate(-30*DEGREES)).scale(0.8)

        datos = [
            ("Memoria Flash", txt_flash, icon_flash),
            ("Principio EEPROM", txt_eeprom, icon_eeprom),
            ("Alta Versatilidad", txt_versat, icon_versat)
        ]

        tarjetas = VGroup()
        for i, (tit, txt, icono) in enumerate(datos):
            base = RoundedRectangle(width=7.5, height=1.3, corner_radius=0.1, fill_color=LIGHT_GRAY, fill_opacity=0.2, stroke_width=0)
            borde_izq = Rectangle(width=0.15, height=1.3, fill_color=DARK_GRAY, fill_opacity=1, stroke_width=0).align_to(base, LEFT)
            
            lbl_tit = Text(tit, font=FUENTE, font_size=20, weight=BOLD, color=BLACK)
            lbl_txt = Text(txt, font_size=14, color=DARK_GRAY, line_spacing=0.8)
            grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            contenido = VGroup(icono, grupo_txt).arrange(RIGHT, buff=0.4).move_to(base.get_center()).align_to(base, LEFT).shift(RIGHT*0.5)
            
            # NOTA: Agrupamos todo para que sea una sola tarjeta
            tarjeta_completa = VGroup(base, borde_izq, contenido)
            tarjetas.add(tarjeta_completa)

        tarjetas.arrange(DOWN, buff=0.3).to_edge(RIGHT, buff=0.5).shift(DOWN*0.2)


        # --- 4. SECUENCIA DE ANIMACIÓN ---
        self.play(Write(titulo), Create(linea_titulo))
        
        # Primero dibujamos el SSD
        self.play(Create(ssd_case))
        self.play(FadeIn(connector_group, shift=UP), Write(lbl_ssd))
        self.play(Create(chips), run_time=1.5)

        # ¡AQUÍ ESTÁ LA SOLUCIÓN! Animamos las tarjetas para que aparezcan
        self.play(FadeIn(tarjetas, shift=LEFT))

        self.next_slide()
        self.limpiar_pantalla()
        
    def slide_tipos_memoria_flash(self):
        # Título principal
        titulo = Text("Tipos de memoria flash", font_size=48, weight=BOLD, color=BLACK)
        titulo.to_edge(UP, buff=0.5)

        # Posición base unificada para todos los subtítulos (Izquierda)
        pos_subtitulo = UP * 1.5 + LEFT * 3.5

        # Función auxiliar para cargar imágenes y evitar repetir código
        def cargar_imagen(ruta):
            try:
                img = ImageMobject(ruta).scale(1.2)
            except Exception:
                img = Rectangle(width=4, height=4, color=BLACK)
            return img.to_edge(RIGHT, buff=1.0).shift(DOWN * 0.5)

        # --- 1. Memoria NAND ---
        sub_nand = Text("Memoria flash NAND", font_size=32, weight=BOLD, color=BLACK).move_to(pos_subtitulo)
        txt_nand = Paragraph(
            "La memoria flash NAND se caracteriza por",
            "tener alta densidad de celdas, lo que",
            "permite almacenar grandes cantidades de",
            "datos. Es la tecnología utilizada en",
            "tarjetas de memoria, unidades USB y SSD,",
            "debido a su bajo consumo de energía y",
            "alta capacidad de almacenamiento.",
            alignment="left", font_size=24, color=BLACK
        ).next_to(sub_nand, DOWN, aligned_edge=LEFT, buff=0.4)
        
        img_nand = cargar_imagen("assets/nand_diagram.png")

        # --- 2. Memoria NOR ---
        sub_nor = Text("Memoria flash NOR", font_size=32, weight=BOLD, color=BLACK).move_to(pos_subtitulo)
        txt_nor = Paragraph(
            "La memoria flash NOR está basada en",
            "transistores FGMOS, dispositivos",
            "capaces de almacenar información binaria.",
            "En esta tecnología, las celdas de",
            "memoria se organizan en paralelo,",
            "lo que permite mayores velocidades de",
            "lectura en comparación con otras.",
            alignment="left", font_size=24, color=BLACK
        ).next_to(sub_nor, DOWN, aligned_edge=LEFT, buff=0.4)
        
        img_nor = cargar_imagen("assets/nor_diagram.png")

        # --- 3. Memoria 3D ---
        sub_3d = Text("Memoria flash 3D", font_size=32, weight=BOLD, color=BLACK).move_to(pos_subtitulo)
        txt_3d = Paragraph(
            "La memoria flash 3D es una",
            "tecnología más reciente que",
            "incrementa la densidad de celdas",
            "mediante una estructura tridimensional.",
            "Ofrece mayor capacidad de almacenamiento",
            "que la memoria NAND tradicional,",
            "siendo clave en SSD de alta capacidad.",
            alignment="left", font_size=24, color=BLACK
        ).next_to(sub_3d, DOWN, aligned_edge=LEFT, buff=0.4)
        
        img_3d = cargar_imagen("assets/3d_diagram.png")

        # --- Animaciones ---
        
        # Entrada Inicial (NAND)
        self.play(Write(titulo))
        self.play(
            FadeIn(sub_nand, shift=RIGHT),
            FadeIn(txt_nand, shift=RIGHT),
            FadeIn(img_nand, shift=LEFT)
        )
        self.wait(2)
        self.next_slide()

        # Transición a NOR
        self.play(
            ReplacementTransform(sub_nand, sub_nor),
            ReplacementTransform(txt_nand, txt_nor),
            FadeOut(img_nand, shift=UP),
            FadeIn(img_nor, shift=UP)
        )
        self.wait(2)
        self.next_slide()

        # Transición a 3D
        self.play(
            ReplacementTransform(sub_nor, sub_3d),
            ReplacementTransform(txt_nor, txt_3d),
            FadeOut(img_nor, shift=UP),
            FadeIn(img_3d, shift=UP)
        )
        self.wait(2)
        self.next_slide()

        # Salida de todos los elementos
        self.play(
            FadeOut(titulo),
            FadeOut(sub_3d),
            FadeOut(txt_3d),
            FadeOut(img_3d)
        )
        self.next_slide()
        self.limpiar_pantalla()
        

    def slide_comparativa_ssd(self):
        # 1. Título General
        titulo, linea = self.crear_titulo("Ventajas vs Desventajas del SSD", palabra_clave="Comparativa", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        # --- DEFINICIÓN DE ICONOS (Ajustados para escala 2 columnas) ---
        icon_ren = VGroup(Arrow(LEFT*0.2, RIGHT*0.2, color=BLACK, buff=0).shift(UP*0.05), Line(LEFT*0.2, RIGHT*0.2, color=BLACK).shift(DOWN*0.05))
        icon_dur = VGroup(Square(side_length=0.3, color=BLACK).rotate(PI/4), Text("✔", font_size=12, color=BLACK))
        icon_con = VGroup(RoundedRectangle(width=0.4, height=0.2, corner_radius=0.05, color=BLACK), Rectangle(width=0.04, height=0.08, fill_color=BLACK, fill_opacity=1).move_to(RIGHT*0.22))

        icon_cos = Text("$", font_size=24, weight=BOLD, color=BLACK)
        icon_cap = VGroup(Line(DOWN*0.2, UP*0.2, color=BLACK), Arrow(start=DOWN*0.1+LEFT*0.1, end=UP*0.1+RIGHT*0.2, color=BLACK, buff=0))
        icon_cor = VGroup(Triangle(color=BLACK).scale(0.25), Text("!", font_size=16, weight=BOLD, color=BLACK).shift(DOWN*0.04))

        # --- DATOS ---
        datos_v = [
            ("Mayor rendimiento", "Arranque y acceso\nmás rápidos.", icon_ren),
            ("Mayor durabilidad", "Sin partes móviles,\nresistente a golpes.", icon_dur),
            ("Menor consumo", "Aumenta la batería\nen portátiles.", icon_con)
        ]

        datos_d = [
            ("Mayor costo", "Precio por GB más\nalto que en HDD.", icon_cos),
            ("Capacidad cara", "Precios suben mucho\nen altas capacidades.", icon_cap),
            ("Riesgo eléctrico", "Cortes de luz pueden\ncorromper datos.", icon_cor)
        ]

        # --- FUNCIÓN PARA CREAR COLUMNAS CORREGIDA ---
        def crear_columna(lista_datos, texto_titulo, color_borde):
            # Grupo principal de la columna
            columna = VGroup()
            
            # 1. Subtítulo (Encabezado)
            subtitulo = Text(texto_titulo, font_size=26, weight=BOLD, color=BLACK)
            sub_linea = Line(LEFT, RIGHT, color=color_borde, stroke_width=2).scale(0.5)
            encabezado = VGroup(subtitulo, sub_linea).arrange(DOWN, buff=0.1)
            
            # 2. Grupo de tarjetas
            tarjetas = VGroup()
            for tit, txt, icono in lista_datos:
                base = RoundedRectangle(width=6.2, height=1.1, corner_radius=0.1, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK, stroke_width=1.5)
                borde_izq = Rectangle(width=0.12, height=1.1, fill_color=color_borde, fill_opacity=1, stroke_width=0).align_to(base, LEFT)
                
                lbl_tit = Text(tit, font_size=17, weight=BOLD, color=BLACK)
                lbl_txt = Text(txt, font_size=13, color=BLACK, line_spacing=0.8)
                grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
                
                contenido = VGroup(icono.copy(), grupo_txt).arrange(RIGHT, buff=0.3).move_to(base.get_center()).align_to(base, LEFT).shift(RIGHT*0.4)
                tarjetas.add(VGroup(base, borde_izq, contenido))
            
            tarjetas.arrange(DOWN, buff=0.25)
            
            # Unimos encabezado y tarjetas asegurando que el encabezado esté ARRIBA
            columna.add(encabezado, tarjetas)
            columna.arrange(DOWN, buff=0.4) # Esto pone el encabezado arriba de las tarjetas
            
            return columna

        # Crear columnas
        col_v = crear_columna(datos_v, "VENTAJAS", BLACK)
        col_d = crear_columna(datos_d, "DESVENTAJAS", GREY_D)

        # Organizar comparativa en pantalla
        comparativa = VGroup(col_v, col_d).arrange(RIGHT, buff=0.6, aligned_edge=UP).shift(DOWN*0.6)

        # 2. Animación
        self.play(
            FadeIn(col_v, shift=UP*0.3),
            FadeIn(col_d, shift=UP*0.3),
            run_time=2
        )

        self.next_slide()
        self.limpiar_pantalla()
        
    def slide_medios_magneticos(self):
        titulo, linea = self.crear_titulo("Almacenamiento Magnético", palabra_clave="Magnético", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        try:
            img_disco = ImageMobject("assets/disco_magnetico.png")
            img_disco.next_to(linea, DOWN, buff=0.4)
        except Exception:
            img_disco = Rectangle(width=8, height=4.5, color=BLACK).next_to(linea, DOWN, buff=0.4)

        try:
            img_cinta = ImageMobject("assets/cinta_magnetica.png")
            img_cinta.next_to(linea, DOWN, buff=0.4)
        except Exception:
            img_cinta = Rectangle(width=8, height=4.5, color=BLACK).next_to(linea, DOWN, buff=0.4)

        self.play(FadeIn(img_disco, shift=UP*0.2))
        self.next_slide()

        self.play(
            FadeOut(img_disco, shift=LEFT*0.5), 
            FadeIn(img_cinta, shift=LEFT*0.5)
        )
        self.next_slide()

        self.limpiar_pantalla()

        
    def slide_ssd_funcionamiento(self):
        # --- 1. CONFIGURACIÓN GENERAL ---
        self.camera.background_color = WHITE
        FUENTE = "sans-serif"
        
        # Paleta en escala de grises
        C_TEXTO = BLACK
        C_LINEAS = BLACK
        C_SUSTRATO = LIGHT_GRAY
        C_SD = GRAY
        C_PUERTA_CONTROL = DARK_GRAY
        
        # --- 2. TÍTULO ---
        titulo = Text("Funcionamiento de los SSD", font=FUENTE, font_size=40, weight=BOLD, color=C_TEXTO)
        titulo.to_edge(UP, buff=0.4)
        linea_titulo = Line(LEFT, RIGHT, color=C_TEXTO, stroke_width=3).scale(4).next_to(titulo, DOWN, buff=0.2)
        
        self.play(Write(titulo), Create(linea_titulo))
        
        # --- 3. CONSTRUCCIÓN DETALLADA DEL TRANSISTOR ---
        # Componentes base
        sustrato = Rectangle(width=6.5, height=1.5, fill_color=C_SUSTRATO, fill_opacity=0.3, color=C_LINEAS)
        label_sustrato = Text("Sustrato", font=FUENTE, font_size=18, color=C_TEXTO).move_to(sustrato.get_bottom() + UP*0.3)
        
        source = Rectangle(width=1.2, height=0.8, fill_color=C_SD, fill_opacity=0.5, color=C_LINEAS)
        source.move_to(sustrato.get_left() + RIGHT * 0.7 + UP * 0.35)
        # Añadido shift para subir el texto
        label_source = Text("Source", font=FUENTE, font_size=14, color=C_TEXTO).move_to(source).shift(UP * 0.4)
        
        drain = Rectangle(width=1.2, height=0.8, fill_color=C_SD, fill_opacity=0.5, color=C_LINEAS)
        drain.move_to(sustrato.get_right() + LEFT * 0.7 + UP * 0.35)
        # Añadido shift para subir el texto
        label_drain = Text("Drain", font=FUENTE, font_size=14, color=C_TEXTO).move_to(drain).shift(UP * 0.4)

        # Capas de óxido y puertas
        oxido_inf = Rectangle(width=2.6, height=0.2, fill_color=WHITE, fill_opacity=1, color=C_LINEAS)
        oxido_inf.next_to(sustrato, UP, buff=0)
        
        puerta_flotante = Rectangle(width=2.6, height=0.9, fill_color=WHITE, fill_opacity=1, color=C_LINEAS)
        puerta_flotante.next_to(oxido_inf, UP, buff=0)
        # Añadido shift para subir el texto
        label_pf = Text("Floating Gate", font=FUENTE, font_size=16, weight=BOLD, color=WHITE).move_to(puerta_flotante).shift(UP * 0.15)
        
        oxido_sup = Rectangle(width=2.6, height=0.2, fill_color=WHITE, fill_opacity=1, color=C_LINEAS)
        oxido_sup.next_to(puerta_flotante, UP, buff=0)
        
        puerta_control = Rectangle(width=2.8, height=0.6, fill_color=C_PUERTA_CONTROL, fill_opacity=1, color=C_LINEAS)
        puerta_control.next_to(oxido_sup, UP, buff=0)
        label_pc = Text("Control Gate", font=FUENTE, font_size=16, color=WHITE).move_to(puerta_control)

        # Terminales
        term_source = Line(source.get_top(), source.get_top() + UP*0.6, color=C_LINEAS, stroke_width=3)
        term_drain = Line(drain.get_top(), drain.get_top() + UP*0.6, color=C_LINEAS, stroke_width=3)
        term_control = Line(puerta_control.get_top(), puerta_control.get_top() + UP*0.5, color=C_LINEAS, stroke_width=3)

        # Agrupar y posicionar
        transistor = VGroup(
            sustrato, source, drain, oxido_inf, puerta_flotante, oxido_sup, puerta_control,
            term_source, term_drain, term_control
        ).move_to(UP * 0.5)
        
        labels_transistor = VGroup(label_sustrato, label_source, label_drain, label_pf, label_pc)

        # Texto base para las explicaciones
        texto_explicacion = Text(
            "La memoria flash utiliza transistores de puerta flotante.", 
            font=FUENTE, font_size=24, color=C_TEXTO
        ).next_to(transistor, DOWN, buff=1.0)

        # Animación de entrada: Estructura básica
        self.play(FadeIn(transistor, shift=UP), Write(labels_transistor))
        self.play(Write(texto_explicacion))
        self.next_slide() # [PAUSA 1: Estructura base]

        # --- 4. EXPLICACIÓN DE LA PUERTA FLOTANTE ---
        texto_pf = Text(
            "La 'Floating Gate' almacena la información reteniendo electrones.", 
            font=FUENTE, font_size=24, color=C_TEXTO
        ).move_to(texto_explicacion)

        self.play(
            ReplacementTransform(texto_explicacion, texto_pf),
            Indicate(puerta_flotante, color=GRAY, scale_factor=1.1),
            Indicate(label_pf, color=BLACK, scale_factor=1.1)
        )
        self.next_slide() # [PAUSA 2: Foco en la puerta flotante]

        # --- 5. ESTADO PROGRAMADO (BINARIO 0) ---
        texto_prog = Text(
            "PROGRAMACIÓN (0): Un voltaje atrae electrones hacia la puerta flotante.", 
            font=FUENTE, font_size=24, color=C_TEXTO
        ).move_to(texto_pf)

        # Rayo de voltaje
        rayo = Polygon(
            [0.15, 0.4, 0], [-0.15, 0.1, 0], [0.05, 0.1, 0], [-0.2, -0.4, 0], [0.05, -0.05, 0], [-0.15, -0.05, 0],
            color=C_TEXTO, fill_color=C_TEXTO, fill_opacity=1
        ).scale(0.8).next_to(term_control, LEFT, buff=0.4)
        label_voltaje = Text("Voltaje", font=FUENTE, font_size=14, color=C_TEXTO).next_to(rayo, LEFT, buff=0.1)
        grupo_voltaje = VGroup(rayo, label_voltaje)

        # Indicador de estado UI
        estado_ui = VGroup(
            Text("ESTADO PROGRAMADO", font=FUENTE, font_size=16, weight=BOLD, color=C_TEXTO),
            Text("Binario 0", font=FUENTE, font_size=32, weight=BOLD, color=C_TEXTO)
        ).arrange(DOWN, buff=0.1).to_edge(RIGHT, buff=0.5).shift(UP*1.5)
        caja_estado = SurroundingRectangle(estado_ui, color=C_LINEAS, buff=0.2, corner_radius=0.1)
        ui_0 = VGroup(estado_ui, caja_estado)

        self.play(
            ReplacementTransform(texto_pf, texto_prog), 
            FadeIn(ui_0, shift=LEFT),
            FadeIn(grupo_voltaje, shift=RIGHT)
        )

        # Creación y movimiento de electrones
        import random
        random.seed(10)
        electrones = VGroup(*[Dot(radius=0.07, color=C_TEXTO) for _ in range(30)])
        for e in electrones:
            e.move_to(sustrato.get_center() + DOWN*0.2 + RIGHT*random.uniform(-1.5, 1.5))
        
        self.play(FadeIn(electrones, shift=UP))
        
        animaciones_electrones = []
        for e in electrones:
            nueva_pos = puerta_flotante.get_center() + RIGHT*random.uniform(-1.1, 1.1) + UP*random.uniform(-0.35, 0.35)
            animaciones_electrones.append(e.animate.move_to(nueva_pos))
            
        self.play(*animaciones_electrones, label_pf.animate.set_opacity(0.3), run_time=1.5, rate_func=smooth)
        self.next_slide() # [PAUSA 3: Electrones atrapados (Estado 0)]

        # --- 6. ESTADO BORRADO (BINARIO 1) ---
        texto_borrado = Text(
            "BORRADO (1): Un impulso eléctrico expulsa los electrones atrapados.", 
            font=FUENTE, font_size=24, color=C_TEXTO
        ).move_to(texto_prog)

        # Impulso de borrado (Onda cuadrada)
        pulso = VMobject(color=C_TEXTO, stroke_width=3)
        pulso.set_points_as_corners([[-0.3, -0.2, 0], [-0.1, -0.2, 0], [-0.1, 0.3, 0], [0.1, 0.3, 0], [0.1, -0.2, 0], [0.3, -0.2, 0]])
        pulso.next_to(term_control, RIGHT, buff=0.4)
        label_pulso = Text("Impulso", font=FUENTE, font_size=14, color=C_TEXTO).next_to(pulso, RIGHT, buff=0.1)
        grupo_pulso = VGroup(pulso, label_pulso)

        # Actualizar UI a Estado 1
        estado_ui_1 = VGroup(
            Text("ESTADO BORRADO", font=FUENTE, font_size=16, weight=BOLD, color=C_TEXTO),
            Text("Binario 1", font=FUENTE, font_size=32, weight=BOLD, color=C_TEXTO)
        ).arrange(DOWN, buff=0.1).move_to(estado_ui)
        
        self.play(
            ReplacementTransform(texto_prog, texto_borrado), 
            FadeOut(grupo_voltaje), 
            FadeIn(grupo_pulso, shift=LEFT),
            ReplacementTransform(estado_ui, estado_ui_1)
        )

        # Electrones abandonan la puerta
        animaciones_salida = []
        for e in electrones:
            pos_salida = sustrato.get_center() + DOWN*0.5 + RIGHT*random.uniform(-2.5, 2.5)
            animaciones_salida.append(e.animate.move_to(pos_salida).set_opacity(0))
            
        self.play(*animaciones_salida, label_pf.animate.set_opacity(1), run_time=1.5)
        self.remove(electrones)
        self.next_slide() # [PAUSA 4: Puerta vacía (Estado 1)]

        # --- 7. PROCESO DE LECTURA ---
        texto_lectura = Text(
            "LECTURA: Se mide si la corriente puede fluir entre Source y Drain.", 
            font=FUENTE, font_size=24, color=C_TEXTO
        ).move_to(texto_borrado)

        self.play(
            ReplacementTransform(texto_borrado, texto_lectura),
            FadeOut(grupo_pulso),
            FadeOut(ui_0[1]), # Caja
            FadeOut(estado_ui_1) # Texto
        )

        # Flecha de corriente
        flecha_corriente = Arrow(
            start=source.get_right() + RIGHT*0.1 + UP*0.2, 
            end=drain.get_left() + LEFT*0.1 + UP*0.2, 
            color=C_TEXTO, buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.15
        )
        label_corriente = Text("Flujo de Corriente", font=FUENTE, font_size=16, color=C_TEXTO).next_to(flecha_corriente, DOWN, buff=0.3)
        grupo_corriente = VGroup(flecha_corriente, label_corriente)

        self.play(GrowArrow(flecha_corriente), FadeIn(label_corriente, shift=UP))
        self.play(Indicate(flecha_corriente, color=GRAY, scale_factor=1.1))
        
        # --- 8. CIERRE LIMPIO ---
        self.next_slide() # [PAUSA 5: Fin de la explicación de lectura]
        self.limpiar_pantalla()
    