"""Parche puntual v1.2.6 -> v1.2.7; ejecutar desde la raiz del repositorio."""
from pathlib import Path
import re, hashlib
ROOT = Path.cwd()
def git_hash(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
def change_once(text, old, new):
    assert text.count(old) == 1, 'Fragmento ambiguo o ausente: ' + old[:80]
    return text.replace(old, new, 1)
html_file = ROOT / 'work.html'
builder_file = ROOT / 'construye_pages.py'
assert git_hash(html_file.read_bytes()) == '15b429a9b69eacefb0d5171cbc10f6fa3109a338'
assert git_hash(builder_file.read_bytes()) == '78ae487e987bb00ff18719901e30af87002cbbda'
html = html_file.read_text(encoding='utf-8')
html = change_once(html, '<title>Sistema de Mejora Personal — v1.2.6 · Comprobación</title>', '<title>Sistema de Mejora Personal — v1.2.7</title>')
html = change_once(html, '<meta name="version" content="1.2.6">', '<meta name="version" content="1.2.7">')
html = change_once(html, '<p class="sello">v1.2.6 — comprobación</p>', '<p class="sello">v1.2.7</p>')
html, badges = re.subn(r'<span class="revision-etiqueta">PROPUESTA</span>', '', html)
assert badges == 12, badges
def clean_classes(match):
    classes = [c for c in match[1].split() if c not in {'propuesta-chatgpt','propuesta-chatgpt--dark','arq-reorganizado'}]
    return 'class="' + ' '.join(classes) + '"'
html = re.sub(r'class="([^"]*)"', clean_classes, html)
html = re.sub(r'^/\* =+ marcas de propuesta .*?\*/\n', '', html, flags=re.M)
html = re.sub(r'^\.propuesta-chatgpt[^\n]*\n', '', html, flags=re.M)
html = re.sub(r'^\.personas-actitud::after\{[^\n]*\n', '', html, flags=re.M)
html = re.sub(r'^\.arq-apartado\.arq-reorganizado\{[^\n]*\n', '', html, flags=re.M)
html = re.sub(r'(?m)^\s*[^{}\n]*\.revision-etiqueta[^{}\n]*\{[^{}]*\}', '', html)
html = html.replace('.revision-concepto', '.proposito-referencia')
html = html.replace(' revision-concepto"', ' proposito-referencia"')
html = change_once(html, '.proposito-referencia>summary .mas{margin-left:0}', '.proposito-referencia>summary .mas{margin-left:auto}')
html = html.replace('border:1px dashed var(--mirada)', 'border:1px solid rgba(34,64,111,.22)')
html = html.replace('border-bottom:1px dashed var(--mirada)', 'border-bottom:1px solid rgba(34,64,111,.22)')
html = change_once(html, '.op-apoyo{border:1px dashed rgba(34,64,111,.3);', '.op-apoyo{border:1px solid rgba(34,64,111,.3);')
html = change_once(html, '.op-apoyo>summary .mas{flex:none;', '.op-apoyo>summary .mas{margin-left:auto;flex:none;')
html = change_once(html, '⟦elementos propuestos por mí: fuego empuja · aire aligera · agua cuida · tierra sostiene⟧', 'fuego empuja — aire aligera — agua cuida — tierra sostiene')
html = change_once(html, '<p class="margen-nota"><span class="pend">⟦emparejamiento propuesto: sale de los elementos⟧</span></p>', '<!-- Relación de Enfoque y Tomar acción sugerida durante la revisión; autoría y estado conservados en Drive. -->')
start = html.index('<details class="arq-apartado" id="mental-focalizar">')
end = html.index('<details class="arq-apartado" id="mental-grabar">', start)
block = html[start:end]
block = change_once(block, '<span class="arq-glosa">qué objetivos me marco</span>', '<span class="arq-glosa">qué quiero conseguir y para qué</span>')
block = change_once(block, '<div class="arq-contenido">', '''<div class="arq-contenido">
            <div class="foco-cadena" role="group" aria-label="Cadena de propósito. En Focalizar, el centro son los objetivos.">
              <p class="fc-titulo">Cadena de propósito</p>
              <div class="fc-fila">
                <div class="fc-nodo"><b>SENTIDO</b><span>para qué</span></div>
                <span class="fc-flecha" aria-hidden="true">→</span>
                <div class="fc-nodo fc-objetivos"><b>OBJETIVOS</b><span>qué quiero conseguir</span></div>
                <span class="fc-flecha" aria-hidden="true">→</span>
                <div class="fc-nodo"><b>TAREAS</b><span>qué hago</span></div>
              </div>
              <p class="fc-lectura">El sentido orienta. Las tareas se concretan en Planeamiento.</p>
            </div>''')
block = change_once(block, '<p class="margen-nota">las preguntas del <b>sentido de la vida</b> ya no viven aquí: están en Mirada · Preguntarse</p>', '')
html = html[:start] + block + html[end:]
css = '''
/* v1.2.7 — Cadena de proposito aplicada a Focalizar; OBJETIVOS en primer plano. */
.foco-cadena{max-width:500px;margin:5px auto 13px;text-align:center}
.fc-titulo{margin-bottom:9px;font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--tinta-suave)}
.fc-fila{display:grid;grid-template-columns:minmax(0,1fr) 14px minmax(0,1.65fr) 14px minmax(0,1fr);gap:4px;align-items:center}
.fc-nodo{min-width:0;padding:8px 4px;border:1px solid rgba(34,64,111,.2);border-radius:5px;color:var(--tinta-suave);line-height:1.25}
.fc-nodo b{display:block;font-size:10px;letter-spacing:.035em}
.fc-nodo span{display:block;margin-top:4px;font-size:12px;line-height:1.3}
.fc-objetivos{padding:12px 5px;border:1.5px solid var(--tinta);background:rgba(155,221,144,.3);color:var(--tinta)}
.fc-objetivos b{font-size:14px;letter-spacing:.04em}
.fc-objetivos span{font-size:13px}
.fc-flecha{font-size:16px;color:var(--tinta-suave)}
.fc-lectura{margin:10px 4px 0;font-size:12px;color:var(--grafito);line-height:1.4}
@media(max-width:430px){.fc-nodo b{font-size:9px;letter-spacing:0}.fc-nodo span{font-size:11px}.fc-objetivos b{font-size:12px}.fc-objetivos span{font-size:12px}}
'''
html = change_once(html, '</style>', css + '\n</style>')
assert hashlib.sha256(html.encode('utf-8')).hexdigest() == '527913fb46ffaf5f549f462bf54d3ff4f01ad2a86ef794529130fdfd07f440ce'
html_file.write_text(html, encoding='utf-8')
builder = builder_file.read_text(encoding='utf-8')
a = builder.index('    # Publicar una candidata no obliga')
b = builder.index('    for f in (', a)
builder = builder[:a] + '''    # Solo versiones limpias: las marcas de revision se quedan fuera de Pages.
    if ('<title>%s — v%s</title>' % (NOMBRE, ver)) not in html:
        fallos.append('title: usar version limpia')
    if ('<p class="sello">v%s</p>' % ver) not in html:
        fallos.append('sello visible: usar version limpia')
    from html.parser import HTMLParser
    class RevisionDetector(HTMLParser):
        def handle_starttag(self, tag, attrs):
            classes = dict(attrs).get('class', '').split()
            if set(classes) & {'propuesta-chatgpt', 'revision-etiqueta', 'arq-reorganizado', 'revision-concepto'}:
                fallos.append('marcas de revision en HTML')
        def handle_data(self, data):
            if data.strip().upper() in {'PROPUESTA', 'REUBICACIÓN', 'COMPROBACIÓN'}:
                fallos.append('etiqueta de revision en HTML')
    RevisionDetector().feed(html)
''' + builder[b:]
assert hashlib.sha256(builder.encode('utf-8')).hexdigest() == '732305c8986c36ec681efe9c6d0bc5f3a00922a712e90c8cf1bdba761204cb3b'
builder_file.write_text(builder, encoding='utf-8')
print('Parche verificado. Etiquetas retiradas:', badges)
