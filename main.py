from manim import *
from manim_slides import Slide

FUENTE = "sans-serif"

class Presentacion(Slide):
    def construct(self):
        self.camera.background_color = WHITE
        self.slide_memoria_computador()
        self.slide_por_que_jerarquia()
        self.slide_motivacion()
        self.slide_intro_tipos_jerarquia()
        self.slide_memoria_primaria()
        self.slide_memoria_secundaria()
        self.slide_registers()
        self.slide_cache()
        self.slide_ram()
        self.slide_ram_escalabilidad()
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
            "Registros (CPU)", 
            "Caché (L1, L2, L3)", 
            "Memoria RAM", 
            "Disco (SSD / HDD)"
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
            Text("Jerónimo Hoyos B.  |  Juan Manuel Teherán M.  |  Jerónimo Restrepo R.", font=FUENTE, font_size=18, color=DARK_GRAY)
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
            "Memoria Caché (SRAMS)", 
            "Memoria Principal (DRAMS)", 
            "Disco Magnético\n(Almacenamiento en Disco)", 
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
        fuente = "sans-serif"
        color_texto = BLACK
        color_secundario = DARK_GRAY
        color_acento = GRAY
        color_bg_suave = "#F4F4F4"
        titulo = Text(
            "Registers", 
            font=fuente, font_size=45, color=color_texto, weight=BOLD
        ).to_edge(UP, buff=0.4)
        
        linea_subtitulo = Line(LEFT, RIGHT, color=color_acento, stroke_width=2).scale(2).next_to(titulo, DOWN, buff=0.1)

        self.play(Write(titulo))
        self.play(Create(linea_subtitulo))
        self.next_slide() 

        viñetas = [
            "  - Pequeñas unidades de memoria.",
            "  - Ubicadas dentro de la CPU.",
            "  - Alta velocidad de operación.",
            "  - Guardan datos e instrucciones.",
            "  - Para la información de uso más frecuente."
        ]
        
        grupo_texto = VGroup(
            *[Text(linea, font=fuente, font_size=20, color=color_secundario) for linea in viñetas]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        linea_acento_texto = Line(
            grupo_texto.get_corner(UL) + UP*0.1, 
            grupo_texto.get_corner(DL) + DOWN*0.1, 
            color=color_acento, stroke_width=4
        )
        grupo_izquierdo = VGroup(linea_acento_texto, grupo_texto).to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)

        self.play(Create(linea_acento_texto))
        self.play(FadeIn(grupo_texto, shift=RIGHT * 0.2))
        self.next_slide() 

        centro_diag = RIGHT * 3.5 + DOWN * 0.3
        
        fondo_circuito = RoundedRectangle(
            width=6.5, height=4.2, corner_radius=0.2,
            fill_color=color_bg_suave, fill_opacity=0.6, 
            stroke_width=2, stroke_color=GRAY
        ).move_to(centro_diag)

        caja_registro = RoundedRectangle(
            width=3.6, height=1.6, corner_radius=0.1,
            fill_color=WHITE, fill_opacity=1, 
            stroke_width=3, stroke_color=color_texto
        ).move_to(centro_diag)
        
        txt_registro = Text("Register", font=fuente, font_size=26, color=color_texto, weight=BOLD).move_to(caja_registro).shift(UP * 0.1)
        
        reloj = Triangle(color=color_texto, fill_opacity=0, stroke_width=2)
        reloj.stretch_to_fit_width(0.35)
        reloj.stretch_to_fit_height(0.25) 
        reloj.next_to(caja_registro.get_bottom(), UP, buff=0)

        flecha_in_start = caja_registro.get_left() + LEFT * 1.4
        flecha_in_end = caja_registro.get_left()
        flecha_in = Arrow(start=flecha_in_start, end=flecha_in_end, buff=0, color=color_texto, stroke_width=4, max_tip_length_to_length_ratio=0.15)
        
        label_in = Text("in", font=fuente, font_size=22, color=color_texto).next_to(flecha_in, UP, buff=0.12).shift(LEFT*0.3)
        slash_in = Line(DOWN, UP, color=color_acento, stroke_width=2).scale(0.25).rotate(PI/4).move_to(flecha_in.get_center())
        txt_16_in = Text("16", font=fuente, font_size=16, color=color_acento).next_to(slash_in, DOWN, buff=0.1)

        flecha_out_start = caja_registro.get_right()
        flecha_out_end = caja_registro.get_right() + RIGHT * 1.4
        flecha_out = Arrow(start=flecha_out_start, end=flecha_out_end, buff=0, color=color_texto, stroke_width=4, max_tip_length_to_length_ratio=0.15)
        
        label_out = Text("out", font=fuente, font_size=22, color=color_texto).next_to(flecha_out, UP, buff=0.12).shift(RIGHT*0.3)
        slash_out = Line(DOWN, UP, color=color_acento, stroke_width=2).scale(0.25).rotate(PI/4).move_to(flecha_out.get_center())
        txt_16_out = Text("16", font=fuente, font_size=16, color=color_acento).next_to(slash_out, DOWN, buff=0.1)

        flecha_load_start = caja_registro.get_top() + UP * 1.0
        flecha_load_end = caja_registro.get_top()
        flecha_load = Arrow(start=flecha_load_start, end=flecha_load_end, buff=0, color=GRAY, stroke_width=3, max_tip_length_to_length_ratio=0.15)
        label_load = Text("load", font=fuente, font_size=20, color=GRAY).next_to(flecha_load, UP, buff=0.1)
        grupo_load = VGroup(flecha_load, label_load)

        self.play(FadeIn(fondo_circuito, shift=UP * 0.2))
        self.play(
            LaggedStart(
                Create(caja_registro),
                Write(txt_registro),
                Create(reloj),
                lag_ratio=0.2
            )
        )
        self.next_slide() 

        self.play(
            GrowArrow(flecha_in),
            FadeIn(label_in),
            FadeIn(slash_in),
            FadeIn(txt_16_in)
        )
        self.next_slide() 

        self.play(FadeIn(grupo_load, shift=DOWN * 0.1))
        self.next_slide() 

        paquete_entrada = Square(side_length=0.1, color=DARK_GRAY, fill_opacity=1).move_to(flecha_in_start)
        paquete_salida = Square(side_length=0.1, color=DARK_GRAY, fill_opacity=1).move_to(flecha_out_start)

        self.play(
            label_load.animate.set_color(color_texto),
            flecha_load.animate.set_color(color_texto),
            FadeIn(paquete_entrada),
            paquete_entrada.animate.move_to(flecha_in_end + RIGHT*0.2), 
            run_time=1
        )
        self.next_slide() 

        self.play(
            FadeOut(paquete_entrada), 
            GrowArrow(flecha_out),
            FadeIn(label_out),
            FadeIn(slash_out),
            FadeIn(txt_16_out),
            paquete_salida.animate.move_to(flecha_out_end), 
            run_time=1.5
        )
        
        self.next_slide()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    def slide_cache(self):
        fuente = "sans-serif"
        color_texto = BLACK
        color_secundario = DARK_GRAY
        color_acento = GRAY
        
        color_cpu = "#E0E0E0"      
        color_cache = "#B0B0B0"   
        color_memoria = "#D0D0D0" 

        titulo = Text(
            "Cache", 
            font=fuente, font_size=45, color=color_texto, weight=BOLD
        ).to_edge(UP, buff=0.4)
        
        linea_subtitulo = Line(LEFT, RIGHT, color=color_acento, stroke_width=2).scale(2).next_to(titulo, DOWN, buff=0.1)

        self.play(Write(titulo))
        self.play(Create(linea_subtitulo))
        self.next_slide() 

        viñetas = [
            "  - Unidad de memoria pequeña y muy rápida.",
            "  - Ubicada estratégicamente cerca de la CPU.",
            "  - Almacena datos e instrucciones recientes.",
            "  - Evita viajes lentos a la Memoria Principal.",
            "  - Minimiza drásticamente el tiempo de acceso."
        ]
        
        grupo_texto = VGroup(
            *[Text(linea, font=fuente, font_size=20, color=color_secundario) for linea in viñetas]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        linea_acento_texto = Line(
            grupo_texto.get_corner(UL) + UP*0.1, 
            grupo_texto.get_corner(DL) + DOWN*0.1, 
            color=color_acento, stroke_width=4
        )
        grupo_izquierdo = VGroup(linea_acento_texto, grupo_texto).to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)

        self.play(Create(linea_acento_texto))

        self.play(LaggedStart(*[FadeIn(texto, shift=RIGHT * 0.1) for texto in grupo_texto], lag_ratio=0.3))
        self.next_slide() 

        centro_x = 3.5
        
        caja_cpu = RoundedRectangle(width=3.5, height=1.0, corner_radius=0.1, fill_color=color_cpu, fill_opacity=1, stroke_width=2, stroke_color=color_texto)
        caja_cpu.move_to([centro_x, 1.6, 0])
        txt_cpu = Text("CPU", font=fuente, font_size=24, color=color_texto, weight=BOLD).move_to(caja_cpu)
        grupo_cpu = VGroup(caja_cpu, txt_cpu)

        caja_mem = RoundedRectangle(width=5.0, height=1.2, corner_radius=0.1, fill_color=color_memoria, fill_opacity=1, stroke_width=2, stroke_color=color_texto)
        caja_mem.move_to([centro_x, -1.8, 0])
        txt_mem = Text("Memoria Principal", font=fuente, font_size=22, color=color_texto, weight=BOLD).move_to(caja_mem)
        grupo_mem = VGroup(caja_mem, txt_mem)


        caja_cache = RoundedRectangle(width=2.5, height=1.0, corner_radius=0.1, fill_color=color_cache, fill_opacity=1, stroke_width=2, stroke_color=color_texto)
        caja_cache.move_to([centro_x, -0.1, 0])
        txt_cache = Text("Caché", font=fuente, font_size=24, color=color_texto, weight=BOLD).move_to(caja_cache)
        grupo_cache = VGroup(caja_cache, txt_cache)

        flecha_bloques = DoubleArrow(start=caja_mem.get_top(), end=caja_cache.get_bottom(), buff=0.1, color=color_texto, stroke_width=3)
        txt_flecha_bloques = Text("Transferencia\nde Bloques", font=fuente, font_size=16, color=color_secundario, line_spacing=0.8).next_to(flecha_bloques, RIGHT, buff=0.2)
        
        flecha_palabras = DoubleArrow(start=caja_cache.get_top(), end=caja_cpu.get_bottom(), buff=0.1, color=color_texto, stroke_width=3)
        txt_flecha_palabras = Text("Transferencia\nde Palabras", font=fuente, font_size=16, color=color_secundario, line_spacing=0.8).next_to(flecha_palabras, RIGHT, buff=0.2)

        self.play(FadeIn(grupo_cpu, shift=DOWN*0.2))
        self.play(FadeIn(grupo_mem, shift=UP*0.2))
        self.next_slide()

        self.play(FadeIn(grupo_cache, scale=0.8))
        self.next_slide()

        self.play(GrowArrow(flecha_bloques), FadeIn(txt_flecha_bloques))
        

        bloque = VGroup(*[Square(side_length=0.15, fill_color=DARK_GRAY, fill_opacity=1) for _ in range(3)]).arrange(RIGHT, buff=0.05)
        bloque.move_to(caja_mem.get_top())
        
        self.play(FadeIn(bloque))
        self.play(bloque.animate.move_to(caja_cache.get_bottom()), run_time=1.5)
        self.play(FadeOut(bloque))
        self.next_slide() 

        self.play(GrowArrow(flecha_palabras), FadeIn(txt_flecha_palabras))

        palabra = Square(side_length=0.15, fill_color=BLACK, fill_opacity=1)
        palabra.move_to(caja_cache.get_top())
        
        self.play(FadeIn(palabra))
        self.play(palabra.animate.move_to(caja_cpu.get_bottom()), run_time=0.6)
        self.play(FadeOut(palabra))
        
        self.next_slide()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
    def slide_ram(self):
        fuente = "sans-serif"
        color_texto = BLACK
        color_secundario = DARK_GRAY
        color_acento = GRAY
        color_bg_suave = "#F4F4F4"
        titulo = Text(
            "RAM (Random Access Memory)", 
            font=fuente, font_size=42, color=color_texto, weight=BOLD
        ).to_edge(UP, buff=0.4)
        
        linea_subtitulo = Line(LEFT, RIGHT, color=color_acento, stroke_width=2).scale(2.5).next_to(titulo, DOWN, buff=0.1)

        self.play(Write(titulo))
        self.play(Create(linea_subtitulo))
        self.next_slide() 

        viñetas = [
            "  - Es la memoria principal del sistema.",
            "  - Mayor capacidad que la caché,",
            "    pero con una velocidad menor.",
            "  - Almacena los datos e instrucciones",
            "    que la CPU utiliza en ese momento.",
            "  - Acceso directo a cualquier dirección."
        ]
        
        grupo_texto = VGroup(
            *[Text(linea, font=fuente, font_size=20, color=color_secundario) for linea in viñetas]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        linea_acento_texto = Line(
            grupo_texto.get_corner(UL) + UP*0.1, 
            grupo_texto.get_corner(DL) + DOWN*0.1, 
            color=color_acento, stroke_width=4
        )
        grupo_izquierdo = VGroup(linea_acento_texto, grupo_texto).to_edge(LEFT, buff=0.6).shift(DOWN * 0.2)

        self.play(Create(linea_acento_texto))
        self.play(LaggedStart(*[FadeIn(texto, shift=RIGHT * 0.1) for texto in grupo_texto], lag_ratio=0.15))
        self.next_slide() 

        centro_diag = RIGHT * 3.5 + DOWN * 0.3
        
        fondo_circuito = RoundedRectangle(
            width=5.5, height=5.5, corner_radius=0.2,
            fill_color=color_bg_suave, fill_opacity=0.6, 
            stroke_width=2, stroke_color=GRAY
        ).move_to(centro_diag)

        caja_ram = RoundedRectangle(
            width=3.2, height=4.6, corner_radius=0.1,
            fill_color=WHITE, fill_opacity=1, 
            stroke_width=3, stroke_color=color_texto
        ).move_to(centro_diag)
        
        txt_ram = Text("RAM", font=fuente, font_size=22, color=color_texto, weight=BOLD).move_to(caja_ram.get_top() + DOWN * 0.4)
        
        reloj = Triangle(color=color_texto, fill_opacity=0, stroke_width=2)
        reloj.stretch_to_fit_width(0.3)
        reloj.stretch_to_fit_height(0.2) 
        reloj.next_to(caja_ram.get_bottom(), UP, buff=0)


        def crear_registro(y_offset, texto_num):
            caja_reg = Rectangle(width=2.0, height=0.5, stroke_width=2, stroke_color=color_texto).move_to(caja_ram.get_center() + UP * y_offset)
            txt_reg = Text("Register", font=fuente, font_size=16, color=color_texto).move_to(caja_reg)
            num_reg = Text(texto_num, font=fuente, font_size=16, color=color_texto).next_to(caja_reg, RIGHT, buff=0.2)
            return VGroup(caja_reg, txt_reg, num_reg)

        reg_0 = crear_registro(1.1, "0")
        reg_1 = crear_registro(0.4, "1")
        puntos = Text("...", font=fuente, font_size=24, color=color_texto).move_to(caja_ram.get_center() + DOWN * 0.3)
        reg_n = crear_registro(-1.0, "n-1")

        grupo_registros = VGroup(reg_0, reg_1, puntos, reg_n)


        caja_logica = Rectangle(width=2.2, height=0.7, stroke_width=2, stroke_color=color_texto).move_to(caja_ram.get_bottom() + UP * 0.6)
        
        txt_logica = VGroup(
            Text("Direct Access", font=fuente, font_size=14, color=color_texto),
            Text("Logic", font=fuente, font_size=14, color=color_texto)
        ).arrange(DOWN, buff=0.05).move_to(caja_logica)
        
        grupo_logica = VGroup(caja_logica, txt_logica)

        def crear_bus(start, end, label_text, width_text, up_shift=0.12, left_shift=0, right_shift=0):
            flecha = Arrow(start=start, end=end, buff=0, color=color_texto, stroke_width=3, max_tip_length_to_length_ratio=0.15)
            label = Text(label_text, font=fuente, font_size=18, color=color_texto).next_to(flecha, UP, buff=up_shift).shift(LEFT*left_shift + RIGHT*right_shift)
            slash = Line(DOWN, UP, color=color_acento, stroke_width=2).scale(0.2).rotate(PI/4).move_to(flecha.get_center())
            width_lbl = Text(width_text, font=fuente, font_size=14, color=color_acento).next_to(slash, DOWN, buff=0.1)
            return VGroup(flecha, label, slash, width_lbl)

        # Bus in (Datos)
        y_in = caja_ram.get_center()[1] + 0.6
        bus_in = crear_bus(caja_ram.get_left() + LEFT * 1.2 + UP * y_in, caja_ram.get_left() + UP * y_in, "in", "w", left_shift=0.3)

        # Bus address
        y_addr = caja_ram.get_center()[1] - 0.6
        bus_addr = crear_bus(caja_ram.get_left() + LEFT * 1.2 + UP * y_addr, caja_ram.get_left() + UP * y_addr, "address", "k", left_shift=0.3)

        # Bus out
        bus_out = crear_bus(caja_ram.get_right(), caja_ram.get_right() + RIGHT * 1.2, "out", "w", right_shift=0.3)

        # Señal load
        flecha_load = Arrow(start=caja_ram.get_top() + UP * 0.8, end=caja_ram.get_top(), buff=0, color=GRAY, stroke_width=3, max_tip_length_to_length_ratio=0.15)
        label_load = Text("load", font=fuente, font_size=18, color=GRAY).next_to(flecha_load, UP, buff=0.1)
        grupo_load = VGroup(flecha_load, label_load)

        self.play(FadeIn(fondo_circuito, shift=UP * 0.2))
        self.play(Create(caja_ram), Write(txt_ram), Create(reloj))
        self.next_slide()
        self.play(LaggedStart(*[FadeIn(mob, shift=DOWN*0.1) for mob in [reg_0, reg_1, puntos, reg_n]], lag_ratio=0.2))
        self.next_slide() 
        self.play(Create(caja_logica), Write(txt_logica))
        self.play(FadeIn(bus_addr, shift=RIGHT*0.2))
        self.next_slide() 
        self.play(
            FadeIn(bus_in, shift=RIGHT*0.2),
            FadeIn(bus_out, shift=LEFT*0.2),
            FadeIn(grupo_load, shift=DOWN*0.2)
        )
        self.next_slide() 

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
    def slide_ram_escalabilidad(self):
        fuente = "sans-serif"
        color_texto = BLACK
        color_secundario = DARK_GRAY
        color_acento = GRAY
        
        titulo = Text(
            "Escalabilidad: Construyendo RAMs más grandes", 
            font=fuente, font_size=38, color=color_texto, weight=BOLD
        ).to_edge(UP, buff=0.4)
        
        linea_subtitulo = Line(LEFT, RIGHT, color=color_acento, stroke_width=2).scale(3).next_to(titulo, DOWN, buff=0.1)

        self.play(Write(titulo))
        self.play(Create(linea_subtitulo))
        self.next_slide() 

        ram8_base = VGroup(
            RoundedRectangle(width=2.5, height=0.6, corner_radius=0.1, fill_color="#E0E0E0", fill_opacity=1, stroke_color=color_texto),
            Text("RAM8", font=fuente, font_size=18, color=color_texto, weight=BOLD)
        ).shift(LEFT * 3)

        self.play(FadeIn(ram8_base, shift=UP*0.2))
        self.next_slide() 

        ram8_blocks = VGroup(*[
            VGroup(
                RoundedRectangle(width=2.5, height=0.4, corner_radius=0.1, fill_color="#E0E0E0", fill_opacity=1, stroke_color=color_texto),
                Text(f"RAM8 (Chip {i})", font=fuente, font_size=14, color=color_secundario)
            ) for i in range(8)
        ]).arrange(DOWN, buff=0.1).shift(LEFT * 3 + DOWN * 0.2)


        self.play(Transform(ram8_base, ram8_blocks), run_time=1.5)
        self.next_slide()
   
        caja_ram64 = SurroundingRectangle(ram8_blocks, color=color_texto, stroke_width=3, buff=0.2)
        txt_ram64 = Text("RAM64", font=fuente, font_size=24, color=color_texto, weight=BOLD).next_to(caja_ram64, UP, buff=0.2)
        
        self.play(Create(caja_ram64), Write(txt_ram64))
        self.next_slide()

        tabla = Table(
            [["RAM8", "8", "3"],
             ["RAM64", "64", "6"],
             ["RAM512", "512", "9"],
             ["RAM4K", "4096", "12"],
             ["RAM16K", "16384", "14"]],
            col_labels=[Text("Chip Name", font=fuente, font_size=24), 
                        Text("n (Registros)", font=fuente, font_size=24), 
                        Text("k (Bits Address)", font=fuente, font_size=24)],
            include_outer_lines=True,
            line_config={"stroke_width": 2, "color": color_secundario}
        ).scale(0.35).to_edge(RIGHT, buff=0.8).shift(DOWN * 0.2)

        tabla.get_col_labels().set_color(BLACK)
        for elem in tabla.get_entries():
            elem.set_color(DARK_GRAY)

        self.play(FadeIn(tabla, shift=LEFT*0.3))
        self.next_slide()

        explicacion_k = VGroup(
            Text("Al multiplicar n x 8", font=fuente, font_size=18, color=color_texto, weight=BOLD),
            Text("sumamos 3 bits a k", font=fuente, font_size=18, color=color_acento)
        ).arrange(DOWN, buff=0.1).next_to(tabla, DOWN, buff=0.4)
        
        flecha_explicacion = Arrow(start=explicacion_k.get_top(), end=tabla.get_bottom(), buff=0.1, color=color_acento)

        self.play(FadeIn(explicacion_k), GrowArrow(flecha_explicacion))
        self.next_slide()

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )