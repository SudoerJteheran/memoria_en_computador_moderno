# Jerarquía de Memoria en un Computador Moderno

Presentación creada con **Manim** sobre la jerarquía de memoria en computadores modernos.

El objetivo de esta presentación es explicar cómo se organizan los diferentes niveles de memoria en un computador actual.

---

## Integrantes

Jerónimo Hoyos B.  
Juan Manuel Teherán M.  
Jerónimo Restrepo R.


---

# Enunciado del Trabajo

Investigar los distintos tipos de arreglos de memoria que usa un PC de última generación en sus:

- registros
- caché
- RAM
- disco

Relacionarlo con los diseños vistos en clase e incluir en la discusión aspectos como:

- costo
- velocidad
- capacidad

---

# Ejecutar la presentación

Instalar dependencias:

```bash
pip install manim
pip install manim-slides
````

Renderizar la animación:

```bash
manim -pqh main.py Presentacion
```

Modo presentación con diapositivas:

```bash
manim_slides present Presentacion
```

Exportar a video:

```bash
manim -pqh main.py Presentacion
```

---

# Estructura de la presentación

La presentación incluye las siguientes secciones:

* Introducción a la memoria del computador
* Motivación de la jerarquía de memoria
* Tipos de memoria
* Memoria primaria
* Memoria secundaria
* Registros
* Caché
* RAM
* Escalabilidad de la RAM
* Estándares de memoria
* Características
* Ventajas
* Desventajas
* Simulación NAND2Tetris

---

# Referencias

Memory Hierarchy Design and its Characteristics
[https://www.geeksforgeeks.org/computer-organization-architecture/memory-hierarchy-design-and-its-characteristics/](https://www.geeksforgeeks.org/computer-organization-architecture/memory-hierarchy-design-and-its-characteristics/)

Difference Between HDD and SSD
[https://www.geeksforgeeks.org/computer-organization-architecture/difference-between-hard-disk-drive-hdd-and-solid-state-drive-ssd/](https://www.geeksforgeeks.org/computer-organization-architecture/difference-between-hard-disk-drive-hdd-and-solid-state-drive-ssd/)

Nand2Tetris
[https://www.nand2tetris.org](https://www.nand2tetris.org)

How Computers Actually Work (Nand2Tetris explanation)
[https://www.youtube.com/watch?v=feeQk8HNYR4](https://www.youtube.com/watch?v=feeQk8HNYR4)



---

# Herramientas utilizadas

* Python
* Manim
* Manim Slides

