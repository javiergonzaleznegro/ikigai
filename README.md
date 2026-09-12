# Sistema de Mejora Personal / IKIGAI

Referencia visual para el uso diario. Version **v1.2.7** (12/09/2026): publicacion limpia y Cadena de proposito aplicada a Mentalizacion / Focalizar, con protagonismo de OBJETIVOS.

## Regla de publicacion

Por indicacion expresa de Javi, la pagina publicada no lleva etiquetas PROPUESTA, REUBICACION, bordes de revision ni sufijos de comprobacion. Estas marcas se reservan a los ficheros de prueba que se revisan en la conversacion. Publicar el programa no consolida automaticamente los textos de los apuntes o del libro.

## Fuente y generacion

- `work.html`: fuente HTML limpia.
- `construye_pages.py`: valida la version y genera `index.html`, `sw.js` y `manifest.json`.
- `index.html`: pagina publicada, identica a `work.html`.
- `sw.js`: respaldo offline; HTML network-first y cache `smp-1.2.7`.
- `icon-180-v1.png` e `icon-512-v1.png`: iconos existentes, conservados.

Ejecutar desde esta carpeta:

```sh
python3 construye_pages.py
```

El generador exige titulo, meta y sello coherentes y detiene la generacion si detecta marcas de revision en el HTML. No editar por separado los archivos generados. Versionado vX.Y.Z del proyecto; X solo por indicacion de Javi.

## Contenido de esta entrega

Focalizar muestra SENTIDO -> OBJETIVOS -> TAREAS, destacando el eslabon OBJETIVOS. El sentido orienta; las tareas se concretan en Planeamiento. La representacion general de la cadena sigue en Mirada / Preguntarse. Sin formularios nuevos ni cambios en las rutinas.

La copia de Drive es `Sistema_v1.2.7.html`. `work.html` e `index.html` coinciden con ella.
SHA-256: `527913fb46ffaf5f549f462bf54d3ff4f01ad2a86ef794529130fdfd07f440ce`.

Las preparaciones puntuales de v1.2.6 y v1.2.7 se conservan en `.github/patches/` y `.github/workflows/preparar-publicacion-v*.yml`. Cada una depende de hashes de una base concreta; no son un automatismo generico ni deben ejecutarse sobre una entrega posterior. El parche v1.2.7 es legible y verifica base y resultado antes de generar el commit.

Decisiones de fondo, capturas, estados por producto y relevos viven en la coordinacion de Drive. Las revisiones se publican por tandas o por orden expresa, no en cada retoque.
