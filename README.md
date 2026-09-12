# Sistema de Mejora Personal / IKIGAI

Referencia visual para el uso diario. Publicacion acumulada **v1.2.6** (12/09/2026), autorizada por Javi. Conserva las marcas de propuesta de la candidata para continuar la revision visual; no implica consolidar textos de los apuntes ni del libro.

## Fuente y publicacion

- `work.html`: fuente HTML.
- `construye_pages.py`: genera `index.html`, `sw.js` y `manifest.json`.
- `index.html`: pagina publicada. Debe ser identica a `work.html`.
- `sw.js`: respaldo offline, con HTML network-first y cache `smp-1.2.6`.
- `icon-180-v1.png` e `icon-512-v1.png`: iconos existentes, conservados.

Ejecutar desde esta carpeta:

```sh
python3 construye_pages.py
```

Versionar el HTML conforme a las reglas del proyecto. El generador admite tanto una entrega normal como una de comprobacion, pero exige que titulo, meta y sello indiquen la misma version. No editar por separado los archivos generados.

## Integridad de esta entrega

La candidata de Drive es `Sistema_v1.2.6_COMPROBACION_PROPUESTAS.html` (183920 bytes). `work.html` e `index.html` coinciden exactamente con ella.

SHA-256: `7812bcfa49423b2678b43ccfcfe5509327e89515f25c5eba707fd54f41abc2d0`.

La preparacion de esta publicacion esta archivada en `.github/patches/v1.2.6` y `.github/workflows/preparar-publicacion-v1.2.6.yml`. Es una operacion puntual, ligada a hashes de la base v1.1.0, no un flujo generico para versiones posteriores. Sus comprobaciones deben detenerla si la base ya cambio. No volver a ejecutarla sobre una entrega posterior.

Las decisiones de fondo, aprobaciones y relevos se mantienen en la coordinacion del proyecto en Drive. Las revisiones se publican por tandas o por orden expresa de Javi, no en cada retoque.
