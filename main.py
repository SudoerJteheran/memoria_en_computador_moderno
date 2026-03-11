from manim import *
from manim_slides import Slide

FUENTE = "sans-serif"

class Presentacion(Slide):
    def construct(self):
        self.camera.background_color = WHITE
        # self.slide_memoria_computador()
        # self.slide_por_que_jerarquia()
        # self.slide_motivacion()
        self.slide_intro_tipos_jerarquia()

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