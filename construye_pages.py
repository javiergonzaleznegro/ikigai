#!/usr/bin/env python3
"""construye_pages.py — de work.html a los cinco ficheros que se suben a Pages.

    work.html  ->  index.html + sw.js + manifest.json
                   (+ icon-180-vN.png e icon-512-vN.png, que ya existen)

Lo generado NO se edita a mano: se toca work.html y se vuelve a ejecutar esto.
"""
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
FUENTE = os.path.join(AQUI, 'work.html')
NOMBRE = 'Sistema de Mejora Personal'
CORTO = 'Sistema'
FONDO = '#131C30'
ICONO_V = 'v1'          # sube cuando cambie el dibujo del icono


def leer_version(html):
    m = re.search(r'<meta name="version" content="([\d.]+)">', html)
    if not m:
        sys.exit('!! work.html no lleva <meta name="version">')
    return m.group(1)


def comprobar(html, ver):
    """La versión debe decir lo mismo en los tres sitios donde vive."""
    fallos = []
    if html.count('<meta name="version" content="%s">' % ver) != 1:
        fallos.append('meta')
    if ('<title>%s — v%s</title>' % (NOMBRE, ver)) not in html:
        fallos.append('title')
    if ('<p class="sello">v%s</p>' % ver) not in html:
        fallos.append('sello visible')
    for f in ('icon-180-%s.png' % ICONO_V, 'icon-512-%s.png' % ICONO_V):
        if not os.path.exists(os.path.join(AQUI, f)):
            fallos.append('falta ' + f)
    if fallos:
        sys.exit('!! desincronizado: ' + ' · '.join(fallos))


SW = """/* generado por construye_pages.py — no editar a mano */
const CACHE = 'smp-%(ver)s';
const BASE = ['./', './index.html', './manifest.json',
              './icon-180-%(iv)s.png', './icon-512-%(iv)s.png'];

self.addEventListener('install', e => {
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(BASE)).catch(() => {}));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  /* EL HTML VA A RED PRIMERO: si no, la app se queda clavada en una version vieja */
  if (req.mode === 'navigate' || req.destination === 'document') {
    e.respondWith(
      fetch(req)
        .then(r => {
          const copia = r.clone();
          caches.open(CACHE).then(c => c.put('./index.html', copia));
          return r;
        })
        .catch(() => caches.match('./index.html').then(r => r || caches.match('./')))
    );
    return;
  }

  /* iconos y manifiesto: cache primero */
  e.respondWith(
    caches.match(req).then(r => r || fetch(req).then(res => {
      const copia = res.clone();
      caches.open(CACHE).then(c => c.put(req, copia));
      return res;
    }))
  );
});
"""


def main():
    if not os.path.exists(FUENTE):
        sys.exit('!! no encuentro work.html')
    html = open(FUENTE, encoding='utf-8').read()
    ver = leer_version(html)
    comprobar(html, ver)

    open(os.path.join(AQUI, 'index.html'), 'w', encoding='utf-8').write(html)

    open(os.path.join(AQUI, 'sw.js'), 'w', encoding='utf-8').write(
        SW % {'ver': ver, 'iv': ICONO_V})

    manifest = {
        "name": NOMBRE,
        "short_name": CORTO,
        "description": "Arquitectura Interior y Proceso Diario",
        "lang": "es",
        "start_url": "./index.html",
        "scope": "./",
        "display": "standalone",
        "orientation": "portrait",
        "background_color": FONDO,
        "theme_color": FONDO,
        "icons": [
            {"src": "./icon-180-%s.png" % ICONO_V, "sizes": "180x180", "type": "image/png"},
            {"src": "./icon-512-%s.png" % ICONO_V, "sizes": "512x512",
             "type": "image/png", "purpose": "any"},
            {"src": "./icon-512-%s.png" % ICONO_V, "sizes": "512x512",
             "type": "image/png", "purpose": "maskable"}
        ]
    }
    open(os.path.join(AQUI, 'manifest.json'), 'w', encoding='utf-8').write(
        json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')

    print('v%s · generados: index.html · sw.js · manifest.json' % ver)
    print('   caché del sw: smp-%s' % ver)
    print('   a subir: index.html · sw.js · manifest.json · icon-180-%s.png · icon-512-%s.png'
          % (ICONO_V, ICONO_V))


if __name__ == '__main__':
    main()
