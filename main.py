from manim import *
from manim_slides import Slide

FUENTE = "sans-serif"

class Presentacion(Slide):
    def construct(self):
        self.camera.background_color = WHITE
        
        # self.slide_memoria_computador()
        # self.slide_por_que_jerarquia()
        # self.slide_motivacion()

        # self.slide_memoria_primaria()
        # self.slide_memoria_secundaria()
        # self.slide_registers()

        # self.slide_cache()
        # self.slide_ram()
        # self.slide_ram_escalabilidad()

        # self.slide_simulador_nand2tetris()

        # self.slide_caracteristicas()
        # self.slide_ventajas()
        # self.slide_desventajas()

        # self.slide_memory_standards()

        # self.memoria_secundaria1()

        # self.diapositiva_detalles_hdd()

        # self.slide_estructura_hdd()

        # self.slide_delay_hdd()

        # self.slide_funcionamiento_hdd()
        # self.slide_ventajas_hdd()
        # self.slide_desventajas_hdd()
        
        #self.slide_ssd_unidades()
        #self.slide_ssd_funcionamiento()
        #self.slide_tipos_memoria_flash()
        #self.slide_ventajas_ssd()
        #self.slide_desventajas_ssd()
        
        self.slide_medios_magneticos()

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

        y_in = caja_ram.get_center()[1] + 0.6
        bus_in = crear_bus(caja_ram.get_left() + LEFT * 1.2 + UP * y_in, caja_ram.get_left() + UP * y_in, "in", "w", left_shift=0.3)

        y_addr = caja_ram.get_center()[1] - 0.6
        bus_addr = crear_bus(caja_ram.get_left() + LEFT * 1.2 + UP * y_addr, caja_ram.get_left() + UP * y_addr, "address", "k", left_shift=0.3)

        bus_out = crear_bus(caja_ram.get_right(), caja_ram.get_right() + RIGHT * 1.2, "out", "w", right_shift=0.3)

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
    def slide_memory_standards(self):
        titulo, linea = self.crear_titulo("Estándares de memoria", palabra_clave="memoria")
        self.play(Write(titulo), Create(linea))

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
                color_fondo = DARK_GRAY if es_encabezado else LIGHT_GRAY
                color_texto = WHITE if es_encabezado else BLACK
                opacidad = 1 if es_encabezado else 0.3
                peso = BOLD if es_encabezado else NORMAL
                
                caja = RoundedRectangle(width=1.62, height=0.75, corner_radius=0.1, 
                                        fill_color=color_fondo, fill_opacity=opacidad, 
                                        stroke_color=GRAY, stroke_width=2)
                
                font_s = 14 if es_encabezado else 13
                if len(txt) >= 10: font_s = 11  
                
                texto = Text(txt, font=FUENTE, font_size=font_s, color=color_texto, weight=peso)
                texto.move_to(caja.get_center())
                
                cuadrito = VGroup(caja, texto)
                fila.add(cuadrito)
            
            fila.arrange(RIGHT, buff=0.08) 
            return fila

        cuadricula_final = VGroup()
        
        fila_headers = crear_fila_cuadritos(encabezados, es_encabezado=True)
        cuadricula_final.add(fila_headers)
        
        for fila_datos in datos:
            cuadricula_final.add(crear_fila_cuadritos(fila_datos, es_encabezado=False))
            
        cuadricula_final.arrange(DOWN, buff=0.1).shift(DOWN * 0.1)
        
        f_headers = cuadricula_final[0]
        f_datos_finales = cuadricula_final[1:]

        self.play(FadeIn(f_headers, shift=DOWN*0.2))
        self.next_slide() 
        
        for i, fila_data in enumerate(datos):

            fila_temp = crear_fila_cuadritos(fila_data, es_encabezado=False)
            fila_temp.move_to(DOWN * 1.0) 
            
            lbl_temp = Text(f"Nivel {fila_data[0]}: {fila_data[1]}", font=FUENTE, font_size=20, weight=BOLD, color=DARK_GRAY)
            lbl_temp.next_to(fila_temp, UP, buff=0.3)
            grupo_temp = VGroup(lbl_temp, fila_temp)

            self.play(FadeIn(lbl_temp), LaggedStart(*[FadeIn(c, shift=UP*0.2) for c in fila_temp], lag_ratio=0.05))
            
            self.next_slide()
            
            self.play(FadeOut(grupo_temp, shift=UP*0.2))

        self.play(LaggedStart(*[FadeIn(f, shift=DOWN*0.2) for f in f_datos_finales], lag_ratio=0.15))
        self.next_slide() 

        flecha_cap = Arrow(
            start=cuadricula_final.get_corner(DL) + DOWN * 0.4 + RIGHT * 2, 
            end=cuadricula_final.get_corner(DR) + DOWN * 0.4, 
            color=BLACK, stroke_width=4, tip_length=0.2
        )
        label_cap = Text("+ Capacidad de Almacenamiento", font=FUENTE, font_size=14, color=BLACK, weight=BOLD).next_to(flecha_cap, UP, buff=0.1)

        flecha_vel = Arrow(
            start=cuadricula_final.get_corner(UR) + UP * 0.4 + LEFT * 2, 
            end=cuadricula_final.get_corner(UL) + UP * 0.4, 
            color=BLACK, stroke_width=4, tip_length=0.2
        )
        label_vel = Text("+ Velocidad y Costo por Bit", font=FUENTE, font_size=14, color=BLACK, weight=BOLD).next_to(flecha_vel, DOWN, buff=0.1)

        self.play(
            GrowArrow(flecha_cap), FadeIn(label_cap),
            GrowArrow(flecha_vel), FadeIn(label_vel)
        )
        
        self.next_slide() 
        self.limpiar_pantalla()
    def slide_caracteristicas(self):
        titulo, linea = self.crear_titulo("Características de la jerarquía", palabra_clave="Características", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        txt_cap = (
            "Es el volumen global de información\n"
            "que la memoria puede almacenar.\n"
            "A medida que bajamos en la jerarquía,\n"
            "la capacidad de almacenamiento aumenta."
        )
        txt_tie = (
            "Intervalo entre la solicitud de lectura/\n"
            "escritura y la entrega de los datos.\n"
            "A medida que bajamos en la jerarquía,\n"
            "el tiempo de acceso también aumenta."
        )
        txt_ren = (
            "Asegura que los datos de acceso\n"
            "frecuente estén en memorias más\n"
            "rápidas para mejorar significativamente\n"
            "el rendimiento general del sistema."
        )
        txt_cos = (
            "Al avanzar de abajo hacia arriba,\n"
            "el costo aumenta. La memoria interna\n"
            "es sustancialmente más costosa\n"
            "que la memoria externa."
        )

        icon_cap = VGroup(*[RoundedRectangle(corner_radius=0.1, width=0.6, height=0.2, fill_color=GRAY, fill_opacity=0.8, stroke_color=BLACK, stroke_width=2) for _ in range(3)]).arrange(UP, buff=0.1)
        
        reloj_base = Circle(radius=0.3, color=BLACK, stroke_width=4)
        manecilla = Line(reloj_base.get_center(), reloj_base.get_center() + UP*0.2, color=DARK_GRAY, stroke_width=4)
        icon_tie = VGroup(reloj_base, manecilla)
        
        icon_ren = Star(n=5, outer_radius=0.3, inner_radius=0.15, color=BLACK, fill_opacity=0.8, stroke_width=1)
        
        icon_cos = Text("$", font=FUENTE, font_size=36, color=BLACK, weight=BOLD)

        datos = [
            ("Capacidad", txt_cap, icon_cap),
            ("Tiempo de Acceso", txt_tie, icon_tie),
            ("Rendimiento", txt_ren, icon_ren),
            ("Costo por bit", txt_cos, icon_cos)
        ]

        tarjetas_finales = VGroup()
        
        for i, (tit, txt, icono) in enumerate(datos):
            base = RoundedRectangle(width=8, height=1.3, corner_radius=0.1, fill_color=LIGHT_GRAY, fill_opacity=0.3, stroke_width=0)
            borde_izq = Rectangle(width=0.15, height=1.3, fill_color=BLACK, fill_opacity=1, stroke_width=0)
            borde_izq.align_to(base, LEFT)
            caja = VGroup(base, borde_izq)
            
            lbl_tit = Text(tit, font=FUENTE, font_size=20, weight=BOLD, color=BLACK)
            lbl_txt = Text(txt, font=FUENTE, font_size=14, color=DARK_GRAY, line_spacing=0.8)
            grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            
            contenido = VGroup(icono.copy(), grupo_txt).arrange(RIGHT, buff=0.4)
            contenido.move_to(base.get_center()).align_to(base, LEFT).shift(RIGHT*0.5)
            
            tarjeta = VGroup(caja, contenido)
            tarjetas_finales.add(tarjeta)   
        
        tarjetas_finales.arrange(DOWN, buff=0.2).shift(DOWN*0.2)
        for i, tarjeta in enumerate(tarjetas_finales):
            if i % 2 == 0:
                tarjeta.shift(LEFT * 1.5)
            else:
                tarjeta.shift(RIGHT * 1.5)

        for i, tarjeta_base in enumerate(tarjetas_finales):
            tarjeta_centro = tarjeta_base.copy().scale(1.15).move_to(DOWN * 0.2)
            
            caja = tarjeta_centro[0]
            icono_grupo = tarjeta_centro[1][0]
            textos = tarjeta_centro[1][1]
            
            direccion_entrada = LEFT if i % 2 == 0 else RIGHT
            self.play(FadeIn(caja, shift=direccion_entrada), FadeIn(textos, shift=direccion_entrada), SpinInFromNothing(icono_grupo))
            
            if i == 0: 
                self.play(LaggedStart(*[Indicate(rect, color=BLACK, scale_factor=1.2) for rect in icono_grupo], lag_ratio=0.2))
            elif i == 1: 
                centro_reloj = icono_grupo[0].get_center()
                self.play(Rotate(icono_grupo[1], angle=-4*PI, about_point=centro_reloj, run_time=1.5, rate_func=smooth))
            elif i == 2: 
                self.play(Wiggle(icono_grupo, scale_value=1.3, rotation_angle=0.1*PI, run_time=1.5))
            elif i == 3: 
                self.play(icono_grupo.animate.shift(UP*0.2).scale(1.2), rate_func=there_and_back, run_time=1.5)
                
            self.next_slide() 
            
            direccion_salida = RIGHT if i % 2 == 0 else LEFT
            self.play(FadeOut(tarjeta_centro, shift=direccion_salida*0.5))

        self.play(LaggedStart(*[FadeIn(t, shift=DOWN*0.2) for t in tarjetas_finales], lag_ratio=0.15))
        self.next_slide() 
        self.limpiar_pantalla()

    def slide_ventajas(self):
        titulo, linea = self.crear_titulo("Ventajas de la jerarquía", palabra_clave="Ventajas", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        txt_rend = "Almacena datos frecuentes en memorias rápidas (como la caché),\nreduciendo drásticamente el tiempo de acceso del sistema."
        txt_rent = "Equilibra el costo y la velocidad combinando memorias pequeñas\ny rápidas con almacenamiento grande, ahorrando dinero al consumidor."
        txt_util = "Aprovecha las fortalezas de cada tecnología para maximizar\nel desempeño sin cuellos de botella."
        txt_gest = "Mantiene la información crítica cerca de la CPU y relega\nlos datos de menor uso a memorias masivas más lentas."

        icon_rend = VGroup(
            Line(UR, DL, color=BLACK, stroke_width=6),
            Line(DL, RIGHT*0.5+DOWN*0.5, color=BLACK, stroke_width=6),
            Line(RIGHT*0.5+DOWN*0.5, DOWN*1.5+LEFT*0.5, color=BLACK, stroke_width=6)
        ).scale(0.4).center()

        icon_rent = VGroup(*[Ellipse(width=0.8, height=0.3, color=DARK_GRAY, fill_opacity=0.6).shift(UP*0.15*i) for i in range(4)])
        icon_rent.move_to(ORIGIN)

        icon_util = Star(n=8, outer_radius=0.4, inner_radius=0.3, color=BLACK, fill_opacity=0.8)

        icon_gest = VGroup(*[RoundedRectangle(corner_radius=0.1, width=0.8, height=0.25, fill_color=DARK_GRAY, fill_opacity=0.8, stroke_color=BLACK, stroke_width=2) for _ in range(3)]).arrange(DOWN, buff=0.1)

        datos = [
            ("Rendimiento", txt_rend, icon_rend),
            ("Rentabilidad", txt_rent, icon_rent),
            ("Utilización optimizada", txt_util, icon_util),
            ("Gestión eficiente", txt_gest, icon_gest)
        ]

        tarjetas_finales = VGroup()
        
        for i, (tit, txt, icono) in enumerate(datos):
            base = RoundedRectangle(width=8, height=1.3, corner_radius=0.1, fill_color=LIGHT_GRAY, fill_opacity=0.3, stroke_width=0)
            borde_izq = Rectangle(width=0.15, height=1.3, fill_color=BLACK, fill_opacity=1, stroke_width=0)
            borde_izq.align_to(base, LEFT)
            caja = VGroup(base, borde_izq)
            
            lbl_tit = Text(tit, font=FUENTE, font_size=20, weight=BOLD, color=BLACK)
            lbl_txt = Text(txt, font=FUENTE, font_size=14, color=DARK_GRAY, line_spacing=0.8)
            grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            
            contenido = VGroup(icono.copy(), grupo_txt).arrange(RIGHT, buff=0.4)
            contenido.move_to(base.get_center()).align_to(base, LEFT).shift(RIGHT*0.5)
            
            tarjeta = VGroup(caja, contenido)
            tarjetas_finales.add(tarjeta)   
        
        tarjetas_finales.arrange(DOWN, buff=0.2).shift(DOWN*0.2)
        for i, tarjeta in enumerate(tarjetas_finales):
            if i % 2 == 0:
                tarjeta.shift(LEFT * 1.5)
            else:
                tarjeta.shift(RIGHT * 1.5)

        for i, tarjeta_base in enumerate(tarjetas_finales):
            tarjeta_centro = tarjeta_base.copy().scale(1.15).move_to(DOWN * 0.2)
            
            caja = tarjeta_centro[0]
            icono_grupo = tarjeta_centro[1][0]
            textos = tarjeta_centro[1][1]
            
            direccion_entrada = LEFT if i % 2 == 0 else RIGHT
            self.play(FadeIn(caja, shift=direccion_entrada), FadeIn(textos, shift=direccion_entrada), SpinInFromNothing(icono_grupo))
            
            if i == 0:
                self.play(Flash(icono_grupo, color=BLACK, line_length=0.2, num_lines=6), Indicate(icono_grupo, color=BLACK, scale_factor=1.3))
            elif i == 1: 
                self.play(LaggedStart(*[m.animate.shift(DOWN*0.1) for m in reversed(icono_grupo)], lag_ratio=0.2, rate_func=there_and_back))
            elif i == 2: 
                self.play(Rotate(icono_grupo, angle=PI, run_time=1.5, rate_func=smooth))
            elif i == 3: 
                self.play(LaggedStart(*[Wiggle(m, scale_value=1.1, rotation_angle=0.05*PI) for m in icono_grupo], lag_ratio=0.1))
                
            self.next_slide() 
            
            direccion_salida = RIGHT if i % 2 == 0 else LEFT
            self.play(FadeOut(tarjeta_centro, shift=direccion_salida*0.5))

        self.play(LaggedStart(*[FadeIn(t, shift=DOWN*0.2) for t in tarjetas_finales], lag_ratio=0.15))
        self.next_slide() 
        self.limpiar_pantalla()

    def slide_desventajas(self):
        titulo, linea = self.crear_titulo("Desventajas de la jerarquía", palabra_clave="Desventajas", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        txt_comp = "La gestión y coordinación de datos en\nmúltiples niveles agrega gran complejidad\nal diseño y funcionamiento del sistema."
        txt_cost = "Las memorias rápidas (registros, caché)\nson muy costosas, lo que limita su tamaño\ny eleva el precio final del equipo."
        txt_late = "Acceder a datos en niveles inferiores\n(almacenamiento masivo) toma mucho más\ntiempo, creando cuellos de botella."
        txt_mant = "Administrar y sincronizar distintos\ntipos de memoria genera una sobrecarga\ntanto en hardware como en software."

        nodo1 = Dot(UP*0.2 + LEFT*0.2, color=BLACK)
        nodo2 = Dot(DOWN*0.2 + LEFT*0.2, color=BLACK)
        nodo3 = Dot(RIGHT*0.3, color=BLACK)
        lineas_comp = VGroup(Line(nodo1, nodo2), Line(nodo2, nodo3), Line(nodo3, nodo1)).set_color(DARK_GRAY).set_stroke(width=3)
        icon_comp = VGroup(lineas_comp, nodo1, nodo2, nodo3).scale(1.5)

        icon_cost = Text("$$$", font=FUENTE, font_size=32, color=BLACK, weight=BOLD)

        icon_late = Arc(radius=0.3, angle=1.5*PI, color=BLACK, stroke_width=5).rotate(PI/4)
        punto_late = Dot(icon_late.get_start(), color=BLACK)
        icon_late_grupo = VGroup(icon_late, punto_late)

        engranaje = Star(n=6, outer_radius=0.35, inner_radius=0.25, color=DARK_GRAY, fill_opacity=0.8)
        exclamacion = Text("!", font=FUENTE, font_size=24, color=WHITE, weight=BOLD).move_to(engranaje.get_center())
        icon_mant = VGroup(engranaje, exclamacion)

        datos = [
            ("Diseño complejo", txt_comp, icon_comp),
            ("Alto Costo", txt_cost, icon_cost),
            ("Latencia", txt_late, icon_late_grupo),
            ("Gastos de mantenimiento", txt_mant, icon_mant)
        ]

        tarjetas_finales = VGroup()
        
        for i, (tit, txt, icono) in enumerate(datos):
            base = RoundedRectangle(width=8, height=1.3, corner_radius=0.1, fill_color=LIGHT_GRAY, fill_opacity=0.3, stroke_width=0)
            borde_izq = Rectangle(width=0.15, height=1.3, fill_color=BLACK, fill_opacity=1, stroke_width=0)
            borde_izq.align_to(base, LEFT)
            caja = VGroup(base, borde_izq)
            
            lbl_tit = Text(tit, font=FUENTE, font_size=20, weight=BOLD, color=BLACK)
            lbl_txt = Text(txt, font=FUENTE, font_size=14, color=DARK_GRAY, line_spacing=0.8)
            grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            
            contenido = VGroup(icono.copy(), grupo_txt).arrange(RIGHT, buff=0.4)
            contenido.move_to(base.get_center()).align_to(base, LEFT).shift(RIGHT*0.5)
            
            tarjeta = VGroup(caja, contenido)
            tarjetas_finales.add(tarjeta)   
        
        tarjetas_finales.arrange(DOWN, buff=0.2).shift(DOWN*0.2)
        for i, tarjeta in enumerate(tarjetas_finales):
            if i % 2 == 0:
                tarjeta.shift(LEFT * 1.5)
            else:
                tarjeta.shift(RIGHT * 1.5)

        for i, tarjeta_base in enumerate(tarjetas_finales):
            tarjeta_centro = tarjeta_base.copy().scale(1.15).move_to(DOWN * 0.2)
            
            caja = tarjeta_centro[0]
            icono_grupo = tarjeta_centro[1][0]
            textos = tarjeta_centro[1][1]
            
            direccion_entrada = LEFT if i % 2 == 0 else RIGHT
            self.play(FadeIn(caja, shift=direccion_entrada), FadeIn(textos, shift=direccion_entrada), SpinInFromNothing(icono_grupo))
            
            if i == 0: 
                self.play(LaggedStart(*[Indicate(n, scale_factor=1.5, color=DARK_GRAY) for n in icono_grupo[1:]], lag_ratio=0.3))
            elif i == 1:
                self.play(Wiggle(icono_grupo, scale_value=1.2, rotation_angle=0.05*PI))
            elif i == 2: 
                self.play(Rotate(icono_grupo, angle=-PI, run_time=2, rate_func=linear))
            elif i == 3: 
                self.play(Rotate(icono_grupo, angle=PI/4, run_time=0.5), Rotate(icono_grupo, angle=-PI/8, run_time=0.3), Rotate(icono_grupo, angle=PI/4, run_time=0.5))
                
            self.next_slide() 
            
            direccion_salida = RIGHT if i % 2 == 0 else LEFT
            self.play(FadeOut(tarjeta_centro, shift=direccion_salida*0.5))

        self.play(LaggedStart(*[FadeIn(t, shift=DOWN*0.2) for t in tarjetas_finales], lag_ratio=0.15))
        self.next_slide() 
        self.limpiar_pantalla()

    def slide_despedida(self):
        texto_muchas = Text("¡MUCHAS", font_size=72, weight=BOLD, slant=ITALIC, color=BLACK)
        texto_gracias = Text("Gracias!", font_size=72, color=BLACK)
        
        texto_muchas.shift(UP * 2.5 + LEFT * 1.5)
        texto_gracias.next_to(texto_muchas, DOWN, aligned_edge=RIGHT, buff=0.1).shift(RIGHT * 1.5)
        
        grupo_texto_principal = VGroup(texto_muchas, texto_gracias)

        qr_image = ImageMobject("assets\memoria_en_computador_moderno_qr.png") 
        qr_image.height = 3.5 
        marco_qr = SurroundingRectangle(qr_image, color=BLACK, stroke_width=2, buff=0.1)
        
        grupo_qr_completo = Group(marco_qr, qr_image)
        grupo_qr_completo.next_to(DOWN, buff=0.8)

        contenido_total = Group(grupo_texto_principal, grupo_qr_completo)
        contenido_total.move_to(ORIGIN)

        self.play(Write(texto_muchas), run_time=1)
        self.play(FadeIn(texto_gracias, shift=UP * 0.5), run_time=1)
        
        self.play(
            FadeIn(qr_image, shift=UP * 0.2),
            Create(marco_qr),
            run_time=1.5
        )

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
        
    def memoria_secundaria1(self):
        titulo = Text("Almacenamiento secundario", font_size=48, color=BLACK)
        titulo.to_edge(UP, buff=0.5)

        contenido = VGroup(
            Text("Es una unidad de memoria \"no volátil\"\nla cual posee una capacidad de\nalmacenamiento mucho más grande que\nla memoria principal.", font_size=24, color=BLACK),
            Text("Sin embargo, esta tiene un tiempo de\nacceso a la información más lenta y\ntambién es la memoria menos costosa\nen la jerarquía.", font_size=24, color=BLACK),
            VGroup(
                Text("Se cuentan con dos tipos:", font_size=24, color=BLACK),
                Text("• Disco duro (HDD)", font_size=24, color=BLACK),
                Text("• Disco de estado sólido (SSD)", font_size=24, color=BLACK),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6)

        contenido.to_edge(LEFT, buff=1)

        hdd = ImageMobject("assets/hdd.png").scale(0.5)
        hdd.shift(RIGHT * 3 + UP * 1)

        ssd = ImageMobject("assets/ssd.png").scale(0.5)
    
        ssd.next_to(hdd, DOWN, buff=1).shift(RIGHT * 1.5)

        self.play(Write(titulo))
        self.play(FadeIn(contenido, shift=RIGHT))
        self.play(
            FadeIn(hdd), 
            run_time=1.5
        )
        self.play(
            FadeIn(ssd), 
            run_time=1.5
        )

        self.wait(2)
        self.next_slide()
        self.limpiar_pantalla()
        
    def diapositiva_detalles_hdd(self):
        titulo = Text("Disco duro (Hard Disk Drive)", font_size=45, color=BLACK)
        titulo.to_edge(UP, buff=0.5)

        texto_descriptivo = Text(
            "Consiste en un disco giratorio\n"
            "cubierto de material magnético y un\n"
            "cabezal de escritura que se encargará\n"
            "de consultar y modificar la\n"
            "información en la superficie del\n"
            "disco.", 
            font_size=25, color=BLACK, line_spacing=0.8
        )
        texto_descriptivo.to_edge(LEFT, buff=1.0)

        diagrama = ImageMobject("assets/diagrama_hdd.png").scale(1.3)
        diagrama.to_edge(RIGHT, buff=1.0)

        self.play(Write(titulo))
        self.wait(0.5)
        self.play(
            FadeIn(texto_descriptivo, shift=UP * 0.3),
            FadeIn(diagrama, shift=LEFT * 0.5),
            run_time=2.5
        )
        self.wait(4)
        self.next_slide()
        self.limpiar_pantalla()
        
    def slide_estructura_hdd(self):
        titulo = Text("Estructura del HDD", font_size=48, color=BLACK).to_edge(UP, buff=0.5)
        
        p_img = ImageMobject("assets/platters.png").scale(1.5).move_to(ORIGIN).shift(UP*0.5)
        s_img = ImageMobject("assets/spindle.png").scale(1.5).move_to(ORIGIN).shift(UP*0.5)
        a_img = ImageMobject("assets/actuator_arm.png").scale(1.5).move_to(ORIGIN).shift(UP*0.5)
        h_img = ImageMobject("assets/rw_head.png").scale(1.5).move_to(ORIGIN).shift(UP*0.5)

        t1 = Text("Platters: Placas magnéticas en forma de disco y utilizadas para almacenar\nla información. Normalmente se hacen de vidrio o aluminio.", font_size=22, color=BLACK, line_spacing=0.8).to_edge(DOWN, buff=1)
        t2 = Text("Spindle: Mantiene los platters en su lugar y los hace rotar según se requiera.\nLa rotación, la cual se mide en revoluciones por minuto (RPM) controla que tan\nrápido la información se puede escribir o leer.", font_size=22, color=BLACK, line_spacing=0.8).to_edge(DOWN, buff=1)
        t3 = Text("Actuator Arm: También conocido como la cabeza del actuador, es un\npequeño motor que controla el movimiento del cabezal de escritura y\nvigila la transferencia de información entre platters.", font_size=22, color=BLACK, line_spacing=0.8).to_edge(DOWN, buff=1)
        t4 = Text("Read/write Head: El cabezal de escritura, controla el movimiento de\ntodos los cabezales de escritura, que realizan la verdadera\nlabor de lectura y escritura en los platters del disco.", font_size=22, color=BLACK, line_spacing=0.8).to_edge(DOWN, buff=1)

        self.play(Write(titulo))
        self.play(FadeIn(p_img), FadeIn(t1))
        self.wait()
        self.next_slide()

        self.play(FadeOut(p_img), FadeIn(s_img), ReplacementTransform(t1, t2))
        self.wait()
        self.next_slide()

        self.play(FadeOut(s_img), FadeIn(a_img), ReplacementTransform(t2, t3))
        self.wait()
        self.next_slide()

        self.play(FadeOut(a_img), FadeIn(h_img), ReplacementTransform(t3, t4))
        self.wait()
        self.limpiar_pantalla()
        
    def slide_delay_hdd(self):
        titulo = Text("Delay en el HDD", font_size=48, color=BLACK).to_edge(UP, buff=0.5)

        p1 = Text("• Seek time: Tiempo para alcanzar el track.", font_size=22, color=BLACK)
        p2 = Text("• Latencia rotacional: Tiempo para ubicar el sector.", font_size=22, color=BLACK)
        p3 = Text("• Tiempo de transferencia: Depende de la rotación.", font_size=22, color=BLACK)
        p4 = Text("• Tiempo del controlador: Procesamiento hardware.", font_size=22, color=BLACK)

        puntos = VGroup(p1, p2, p3, p4).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        puntos.to_edge(LEFT, buff=1.0)

        llave = Brace(puntos, direction=RIGHT, color=BLUE_D)
        
        texto_acceso = Text("Tiempo de Acceso Medio", font_size=24, color=BLUE_D, weight=BOLD)
        formula = Text("Seek + Lat + Trans + Ctrl", font_size=16, color=GRAY)
        
        resultado_grupo = VGroup(texto_acceso, formula).arrange(DOWN, buff=0.2)
        
        resultado_grupo.next_to(llave, RIGHT, buff=0.2)

        self.play(Write(titulo))
        self.wait(0.5)

        for punto in puntos:
            self.play(FadeIn(punto, shift=RIGHT * 0.2), run_time=0.5)
        
        self.wait(1)

        self.play(GrowFromCenter(llave), run_time=1.5)

        self.play(FadeIn(resultado_grupo, shift=RIGHT * 0.3), run_time=1)
        
        self.wait(4)
        self.next_slide()
        self.limpiar_pantalla()
        
    def slide_ventajas_hdd(self):
        titulo, linea = self.crear_titulo("Ventajas del HDD", palabra_clave="Ventajas", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        txt_cap = "Alta capacidad de almacenamiento (hasta 36TB)\ny una excelente relación costo-beneficio."
        txt_rec = "Retienen información sin energía y cuentan\ncon múltiples herramientas de recuperación."
        txt_com = "Sencillos de expandir o mejorar (swappear),\ncompatibles con casi cualquier sistema."

        icon_cap = VGroup(
            RoundedRectangle(width=0.6, height=0.8, corner_radius=0.1, color=BLACK),
            Text("TB", font_size=14, color=BLACK).move_to(ORIGIN)
        )
        icon_rec = VGroup(
            Circle(radius=0.35, color=BLACK, stroke_width=4),
            Line(ORIGIN, UP*0.25, color=BLACK), Line(ORIGIN, RIGHT*0.2, color=BLACK)
        )
        icon_com = VGroup(
            Line(LEFT*0.3, RIGHT*0.3, color=BLACK), 
            Triangle(color=BLACK).scale(0.1).rotate(-PI/2).shift(RIGHT*0.3),
            Triangle(color=BLACK).scale(0.1).rotate(PI/2).shift(LEFT*0.3)
        ).add(Text("USB", font_size=10, color=BLACK).shift(DOWN*0.2))

        datos = [
            ("Gran Capacidad", txt_cap, icon_cap),
            ("Recuperabilidad", txt_rec, icon_rec),
            ("Compatibilidad", txt_com, icon_com)
        ]

        tarjetas_finales = VGroup()
        for i, (tit, txt, icono) in enumerate(datos):
            base = RoundedRectangle(width=8, height=1.3, corner_radius=0.1, fill_color=LIGHT_GRAY, fill_opacity=0.3, stroke_width=0)
            borde_izq = Rectangle(width=0.15, height=1.3, fill_color=BLUE_D, fill_opacity=1, stroke_width=0).align_to(base, LEFT)
            lbl_tit = Text(tit, font_size=20, weight=BOLD, color=BLACK)
            lbl_txt = Text(txt, font_size=14, color=DARK_GRAY, line_spacing=0.8)
            grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            contenido = VGroup(icono.copy(), grupo_txt).arrange(RIGHT, buff=0.4).move_to(base.get_center()).align_to(base, LEFT).shift(RIGHT*0.5)
            tarjeta = VGroup(VGroup(base, borde_izq), contenido)
            tarjetas_finales.add(tarjeta)

        tarjetas_finales.arrange(DOWN, buff=0.2).shift(DOWN*0.2)
        
        for i, tarjeta_base in enumerate(tarjetas_finales):
            tarjeta_centro = tarjeta_base.copy().scale(1.15).move_to(DOWN * 0.2)
            dir_ent = LEFT if i % 2 == 0 else RIGHT
            self.play(FadeIn(tarjeta_centro, shift=dir_ent))
            
            if i == 0: self.play(Indicate(tarjeta_centro[1][0]))
            elif i == 1: self.play(Rotate(tarjeta_centro[1][0][1:], angle=TAU, run_time=2))
            elif i == 2: self.play(tarjeta_centro[1][0].animate.shift(RIGHT*0.1).set_color(BLUE), run_time=0.5, rate_func=there_and_back)

            self.next_slide()
            self.play(FadeOut(tarjeta_centro, shift=dir_ent*(-0.5)))

        self.play(LaggedStart(*[FadeIn(t, shift=DOWN*0.2) for t in tarjetas_finales], lag_ratio=0.15))
        self.next_slide()
        self.limpiar_pantalla()
        
        
    def slide_desventajas_hdd(self):
        titulo, linea = self.crear_titulo("Desventajas del HDD", palabra_clave="Desventajas", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        txt_len = "Son más lentos que los SSD, especialmente en\narchivos grandes o multitarea compleja."
        txt_con = "Las partes mecánicas requieren mucha más\nenergía para operar que los chips flash."
        txt_dur = "Las partes móviles los hacen muy frágiles\nante caídas o golpes (pérdida de datos)."
        txt_rui = "Las placas giratorias generan calor y ruido,\nafectando la eficiencia del sistema."

        icon_len = VGroup(Arc(radius=0.3, angle=PI*1.5, color=BLACK), Dot().scale(0.5))
        icon_con = VGroup(Circle(radius=0.3, color=BLACK), Dot(color=BLACK)).scale(0.8)
        icon_dur = VGroup(Line(UP*0.3, DOWN*0.3, color=BLACK), Line(LEFT*0.3, RIGHT*0.3, color=BLACK).rotate(PI/4)).set_color(RED)
        icon_rui = VGroup(*[Arc(radius=0.15*i, angle=PI/2, color=BLACK) for i in range(1,4)])

        datos = [
            ("Rendimiento lento", txt_len, icon_len),
            ("Consumo energético", txt_con, icon_con),
            ("Menor durabilidad", txt_dur, icon_dur),
            ("Ruido y Calor", txt_rui, icon_rui)
        ]

        tarjetas_finales = VGroup()
        for i, (tit, txt, icono) in enumerate(datos):
            base = RoundedRectangle(width=8, height=1.3, corner_radius=0.1, fill_color=LIGHT_GRAY, fill_opacity=0.3, stroke_width=0)
            borde_izq = Rectangle(width=0.15, height=1.3, fill_color=RED_D, fill_opacity=1, stroke_width=0).align_to(base, LEFT)
            lbl_tit = Text(tit, font_size=20, weight=BOLD, color=BLACK)
            lbl_txt = Text(txt, font_size=14, color=DARK_GRAY, line_spacing=0.8)
            grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            contenido = VGroup(icono.copy(), grupo_txt).arrange(RIGHT, buff=0.4).move_to(base.get_center()).align_to(base, LEFT).shift(RIGHT*0.5)
            tarjeta = VGroup(VGroup(base, borde_izq), contenido)
            tarjetas_finales.add(tarjeta)

        tarjetas_finales.arrange(DOWN, buff=0.2).shift(DOWN*0.2)

        for i, tarjeta_base in enumerate(tarjetas_finales):
            tarjeta_centro = tarjeta_base.copy().scale(1.15).move_to(DOWN * 0.2)
            dir_ent = RIGHT if i % 2 == 0 else LEFT
            self.play(FadeIn(tarjeta_centro, shift=dir_ent))
            
            if i == 0: self.play(Rotate(tarjeta_centro[1][0], angle=-PI/2, run_time=1.5))
            elif i == 1: self.play(Flash(tarjeta_centro[1][0], color=YELLOW, flash_radius=0.5))
            elif i == 2: self.play(Wiggle(tarjeta_centro[1][0]))
            elif i == 3: self.play(LaggedStart(*[Indicate(m) for m in tarjeta_centro[1][0]], lag_ratio=0.2))

            self.next_slide()
            self.play(FadeOut(tarjeta_centro, shift=dir_ent*(-0.5)))

        self.play(LaggedStart(*[FadeIn(t, shift=DOWN*0.2) for t in tarjetas_finales], lag_ratio=0.15))
        self.next_slide()
        self.limpiar_pantalla()
        
    def slide_funcionamiento_hdd(self):
        titulo, linea = self.crear_titulo("Funcionamiento del HDD", palabra_clave="Funcionamiento", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        disco_fondo = Circle(radius=1.5, color=GRAY_D, fill_opacity=0.1)
        track_externo = Annulus(inner_radius=1.1, outer_radius=1.4, color=GREEN_E, fill_opacity=0.5)
        sector_dato = AnnularSector(inner_radius=1.1, outer_radius=1.4, angle=45*DEGREES, start_angle=90*DEGREES, color=RED_E, fill_opacity=0.8)

        disco_completo = VGroup(disco_fondo, track_externo, sector_dato)
        disco_completo.to_edge(RIGHT, buff=1.0).shift(DOWN*0.5)

        p1 = Text("• Los platters giran entre 5400 y 15000 RPM.", font_size=20, color=BLACK)
        p2 = Text("• El cabezal busca el 'track' y sector correcto.", font_size=20, color=BLACK)
        p3 = Text("• Se leen/escriben señales magnéticas.", font_size=20, color=BLACK)
        p4 = Text("• El controlador transfiere la info al PC.", font_size=20, color=BLACK)

        puntos = VGroup(p1, p2, p3, p4).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        puntos.to_edge(LEFT, buff=1.0).shift(DOWN*0.5)

        brazo = Line(disco_completo.get_center() + UP*2 + RIGHT*1, disco_completo.get_center() + UP*1.2, color=BLACK, stroke_width=6)
        cabezal = Dot(brazo.get_end(), color=BLACK)
        actuador = VGroup(brazo, cabezal)
        
        self.play(FadeIn(puntos, shift=RIGHT))
        self.play(Create(disco_completo), Create(actuador))

        self.play(
            Rotate(disco_completo, angle=2*TAU, run_time=3, rate_func=linear),
            actuador.animate.rotate(10*DEGREES, about_point=brazo.get_start()),
            iteration=2
        )

        self.wait(2)
        self.next_slide()
        self.limpiar_pantalla()
        
    def slide_ssd_unidades(self):
        titulo, linea = self.crear_titulo("Unidades de Estado Sólido (SSD)", palabra_clave="Estado Sólido", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        img_ssd = ImageMobject("assets/image_10d658.png").scale(1.2)
        img_ssd.to_edge(LEFT, buff=1.0).shift(DOWN*0.5)

        txt_flash = "Utilizan memoria \"flash\" en lugar de un\ndisco giratorio para almacenar datos."
        txt_eeprom = "Trabaja bajo el principio EEPROM:\nElectrical Erasable Programmable ROM."
        txt_versat = "Permite que la información sea borrada\ny actualizada múltiples veces electrónicamente."

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
            base = RoundedRectangle(width=7.5, height=1.3, corner_radius=0.1, fill_color=LIGHT_GRAY, fill_opacity=0.3, stroke_width=0)
            borde_izq = Rectangle(width=0.15, height=1.3, fill_color=BLUE_D, fill_opacity=1, stroke_width=0).align_to(base, LEFT)
            lbl_tit = Text(tit, font_size=20, weight=BOLD, color=BLACK)
            lbl_txt = Text(txt, font_size=14, color=DARK_GRAY, line_spacing=0.8)
            grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            contenido = VGroup(icono, grupo_txt).arrange(RIGHT, buff=0.4).move_to(base.get_center()).align_to(base, LEFT).shift(RIGHT*0.5)
            tarjetas.add(VGroup(VGroup(base, borde_izq), contenido))

        tarjetas.arrange(DOWN, buff=0.3).to_edge(RIGHT, buff=0.5).shift(DOWN*0.5)

        self.play(FadeIn(img_ssd, shift=RIGHT))
        for tarjeta in tarjetas:
            self.play(FadeIn(tarjeta, shift=LEFT))
            self.next_slide()

        self.wait(2)
        self.limpiar_pantalla()
        
    def slide_tipos_memoria_flash(self):
        titulo = Text("Tipos de memoria flash", font_size=48, weight=BOLD, color=BLACK)
        titulo.to_edge(UP, buff=0.5)

        sub_nand = Text("Memoria flash NAND", font_size=32, weight=BOLD, color=BLACK)
        sub_nand.move_to(UP * 1.5 + LEFT * 3.5)

        txt_nand = Paragraph(
            "La memoria flash NAND se caracteriza por",
            "tener alta densidad de celdas, lo que",
            "permite almacenar grandes cantidades de",
            "datos. Es la tecnología utilizada en",
            "tarjetas de memoria, unidades USB y SSD,",
            "debido a su bajo consumo de energía y",
            "alta capacidad de almacenamiento. Cada",
            "celda de memoria está compuesta",
            "principalmente por dos compuertas:",
            "control gate (puerta de control) y",
            "floating gate (puerta flotante).",
            alignment="left", font_size=20, color=BLACK
        ).next_to(sub_nand, DOWN, aligned_edge=LEFT, buff=0.4)

        try:
            img_nand = ImageMobject("assets/nand_diagram.png").scale(1.2)
            img_nand.to_edge(RIGHT, buff=1.0).shift(DOWN * 0.5)
        except Exception:
            img_nand = Rectangle(width=3, height=4, color=BLACK)
            img_nand.to_edge(RIGHT, buff=1.0).shift(DOWN * 0.5)

        sub_nor = Text("Memoria flash NOR", font_size=32, weight=BOLD, color=BLACK)
        sub_nor.move_to(UP * 1.5 + RIGHT * 2.5)

        txt_nor = Paragraph(
            "La memoria flash NOR está basada en",
            "transistores FGMOS (Floating Gate Metal",
            "Oxide Semiconductor), dispositivos",
            "capaces de almacenar información binaria",
            "(0 o 1). En esta tecnología, las celdas",
            "de memoria se organizan en paralelo, lo",
            "que permite mayores velocidades de",
            "lectura en comparación con otros tipos de",
            "memoria flash.",
            alignment="left", font_size=20, color=BLACK
        ).next_to(sub_nor, DOWN, aligned_edge=LEFT, buff=0.4)

        try:
            img_nor = ImageMobject("assets/nor_diagram.png").scale(1.2)
            img_nor.to_edge(LEFT, buff=1.0).shift(DOWN * 0.5)
        except Exception:
            img_nor = Rectangle(width=3, height=4, color=BLACK)
            img_nor.to_edge(LEFT, buff=1.0).shift(DOWN * 0.5)

        sub_3d = Text("Memoria flash 3D", font_size=32, weight=BOLD, color=BLACK)
        sub_3d.move_to(UP * 1.5 + LEFT * 3.5)

        txt_3d = Paragraph(
            "La memoria flash 3D es una",
            "tecnología más reciente que",
            "incrementa la densidad de celdas",
            "mediante una estructura",
            "tridimensional. Gracias a ello,",
            "puede ofrecer mayor capacidad de",
            "almacenamiento que la memoria",
            "NAND tradicional, siendo",
            "ampliamente utilizada en SSD de",
            "alta capacidad.",
            alignment="left", font_size=20, color=BLACK
        ).next_to(sub_3d, DOWN, aligned_edge=LEFT, buff=0.4)

        try:
            img_3d = ImageMobject("assets/3d_diagram.png").scale(1.2)
            img_3d.to_edge(RIGHT, buff=1.0).shift(DOWN * 0.5)
        except Exception:
            img_3d = Rectangle(width=3, height=4, color=BLACK)
            img_3d.to_edge(RIGHT, buff=1.0).shift(DOWN * 0.5)

        self.play(Write(titulo))
        
        self.play(
            FadeIn(sub_nand, shift=DOWN),
            FadeIn(txt_nand, shift=RIGHT),
            FadeIn(img_nand, shift=LEFT)
        )
        self.wait(2)
        self.next_slide()

        self.play(
            ReplacementTransform(sub_nand, sub_nor),
            ReplacementTransform(txt_nand, txt_nor),
            FadeOut(img_nand, shift=LEFT),
            FadeIn(img_nor, shift=LEFT)
        )
        self.wait(2)
        self.next_slide()

        self.play(
            ReplacementTransform(sub_nor, sub_3d),
            ReplacementTransform(txt_nor, txt_3d),
            FadeOut(img_nor, shift=RIGHT),
            FadeIn(img_3d, shift=RIGHT)
        )
        self.wait(2)
        self.next_slide()

        self.play(
            FadeOut(titulo),
            FadeOut(sub_3d),
            FadeOut(txt_3d),
            FadeOut(img_3d)
        )
        self.limpiar_pantalla()
        
    def slide_ventajas_ssd(self):
        titulo, linea = self.crear_titulo("Ventajas de las SSD", palabra_clave="Ventajas", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        txt_ren = "Son considerablemente más rápidas en el arranque,\ntransferencia de archivos y acceso a los datos."
        txt_dur = "Al carecer de partes móviles tienen menor riesgo\nde daños físicos, haciéndolas ideales para laptops."
        txt_con = "Consumen mucha menos energía, lo que contribuye\na una mayor duración de batería en portátiles."

        icon_ren = VGroup(
            Arrow(start=LEFT*0.25+DOWN*0.25, end=RIGHT*0.25+UP*0.25, color=BLACK, buff=0),
            Line(RIGHT*0.1+DOWN*0.1, RIGHT*0.3+DOWN*0.1, color=BLACK),
            Line(LEFT*0.1+UP*0.1, LEFT*0.3+UP*0.1, color=BLACK)
        )
        icon_dur = VGroup(
            Square(side_length=0.45, color=BLACK).rotate(PI/4),
            Text("✔", font_size=14, color=BLACK).move_to(ORIGIN)
        )
        icon_con = VGroup(
            RoundedRectangle(width=0.6, height=0.3, corner_radius=0.05, color=BLACK),
            Rectangle(width=0.05, height=0.1, fill_color=BLACK, fill_opacity=1).move_to(RIGHT*0.325)
        )

        datos = [
            ("Mayor rendimiento", txt_ren, icon_ren),
            ("Mayor durabilidad", txt_dur, icon_dur),
            ("Menor consumo", txt_con, icon_con)
        ]

        tarjetas_finales = VGroup()
        for i, (tit, txt, icono) in enumerate(datos):
            base = RoundedRectangle(width=8, height=1.3, corner_radius=0.1, fill_color=LIGHT_GRAY, fill_opacity=0.3, stroke_width=0)
            borde_izq = Rectangle(width=0.15, height=1.3, fill_color=BLUE_D, fill_opacity=1, stroke_width=0).align_to(base, LEFT)
            lbl_tit = Text(tit, font_size=20, weight=BOLD, color=BLACK)
            lbl_txt = Text(txt, font_size=14, color=DARK_GRAY, line_spacing=0.8)
            grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            contenido = VGroup(icono.copy(), grupo_txt).arrange(RIGHT, buff=0.4).move_to(base.get_center()).align_to(base, LEFT).shift(RIGHT*0.5)
            tarjeta = VGroup(VGroup(base, borde_izq), contenido)
            tarjetas_finales.add(tarjeta)

        tarjetas_finales.arrange(DOWN, buff=0.2).shift(DOWN*0.2)
        
        for i, tarjeta_base in enumerate(tarjetas_finales):
            tarjeta_centro = tarjeta_base.copy().scale(1.15).move_to(DOWN * 0.2)
            dir_ent = LEFT if i % 2 == 0 else RIGHT
            self.play(FadeIn(tarjeta_centro, shift=dir_ent))
            
            if i == 0: self.play(tarjeta_centro[1][0][0].animate.shift(RIGHT*0.1+UP*0.1), run_time=0.5, rate_func=there_and_back)
            elif i == 1: self.play(Flash(tarjeta_centro[1][0], color=GREEN, flash_radius=0.4))
            elif i == 2: self.play(tarjeta_centro[1][0][0].animate.set_fill(GREEN, opacity=0.4), run_time=1, rate_func=there_and_back)

            self.next_slide()
            self.play(FadeOut(tarjeta_centro, shift=dir_ent*(-0.5)))

        self.play(LaggedStart(*[FadeIn(t, shift=DOWN*0.2) for t in tarjetas_finales], lag_ratio=0.15))
        self.next_slide()
        self.limpiar_pantalla()


    def slide_desventajas_ssd(self):
        titulo, linea = self.crear_titulo("Desventajas de las SSD", palabra_clave="Desventajas", color_clave=BLACK)
        self.play(Write(titulo), Create(linea))

        txt_cos = "El costo por unidad de almacenamiento sigue\nsiendo más alto en comparación con los HDD."
        txt_cap = "A medida que aumenta la capacidad el precio\ncrece considerablemente respecto a los HDD."
        txt_cor = "Un corte repentino de energía en la escritura\npuede causar pérdida o corrupción de datos."

        icon_cos = Text("$", font_size=32, weight=BOLD, color=BLACK)
        icon_cap = VGroup(
            Line(DOWN*0.3, UP*0.3, color=BLACK), 
            Line(DOWN*0.3, RIGHT*0.4, color=BLACK),
            Arrow(start=DOWN*0.2+LEFT*0.1, end=UP*0.2+RIGHT*0.3, color=BLACK, buff=0)
        )
        
        triangulo_cor = Triangle(color=BLACK).scale(0.4)
        exclamacion = Text("!", font_size=26, weight=BOLD, color=BLACK)
        exclamacion.move_to(triangulo_cor.get_center() + DOWN * 0.08)
        
        icon_cor = VGroup(triangulo_cor, exclamacion)

        datos = [
            ("Mayor costo inicial", txt_cos, icon_cos),
            ("Capacidad más costosa", txt_cap, icon_cap),
            ("Riesgo de corrupción", txt_cor, icon_cor)
        ]

        tarjetas_finales = VGroup()
        for i, (tit, txt, icono) in enumerate(datos):
            base = RoundedRectangle(width=8, height=1.3, corner_radius=0.1, fill_color=LIGHT_GRAY, fill_opacity=0.3, stroke_width=0)
            borde_izq = Rectangle(width=0.15, height=1.3, fill_color=RED_D, fill_opacity=1, stroke_width=0).align_to(base, LEFT)
            lbl_tit = Text(tit, font_size=20, weight=BOLD, color=BLACK)
            lbl_txt = Text(txt, font_size=14, color=DARK_GRAY, line_spacing=0.8)
            grupo_txt = VGroup(lbl_tit, lbl_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            contenido = VGroup(icono.copy(), grupo_txt).arrange(RIGHT, buff=0.4).move_to(base.get_center()).align_to(base, LEFT).shift(RIGHT*0.5)
            tarjeta = VGroup(VGroup(base, borde_izq), contenido)
            tarjetas_finales.add(tarjeta)

        tarjetas_finales.arrange(DOWN, buff=0.2).shift(DOWN*0.2)

        for i, tarjeta_base in enumerate(tarjetas_finales):
            tarjeta_centro = tarjeta_base.copy().scale(1.15).move_to(DOWN * 0.2)
            dir_ent = RIGHT if i % 2 == 0 else LEFT
            self.play(FadeIn(tarjeta_centro, shift=dir_ent))
            
            if i == 0: self.play(Wiggle(tarjeta_centro[1][0]))
            elif i == 1: self.play(tarjeta_centro[1][0][2].animate.scale(1.3), run_time=0.8, rate_func=there_and_back)
            elif i == 2: self.play(Flash(tarjeta_centro[1][0], color=RED, flash_radius=0.4))

            self.next_slide()
            self.play(FadeOut(tarjeta_centro, shift=dir_ent*(-0.5)))

        self.play(LaggedStart(*[FadeIn(t, shift=DOWN*0.2) for t in tarjetas_finales], lag_ratio=0.15))
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