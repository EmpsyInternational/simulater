# -*- coding: utf-8 -*-
"""Genera index.html (archivo autonomo) a partir de artifact.html.

artifact.html no puede llevar <html>/<head>/<body> porque ese es el formato que
exige la publicacion del link. Este script lo envuelve y ademas sube las
etiquetas de favicon al <head>, que es donde el navegador las aplica de forma
fiable: dentro del <body> muchas veces las ignora.
"""
import io
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FAVICON_SVG = (
    "data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20"
    "viewBox='0%200%2064%2064'%3E%3Crect%20width='64'%20height='64'%20rx='14.08'%20"
    "fill='%23d81b60'/%3E%3Cpath%20d='M42.65%2047.2%20A18.56%2018.56%200%201%201%20"
    "42.65%2016.8'%20fill='none'%20stroke='%23ffffff'%20stroke-width='8'%20"
    "stroke-linecap='round'/%3E%3C/svg%3E"
)

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Simulador Credix</title>
<link rel="icon" href="favicon.ico" sizes="16x16 32x32 48x48">
<link rel="icon" type="image/svg+xml" href="%s">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>
  html{color-scheme:light}
  body{margin:0;font-family:system-ui,-apple-system,sans-serif;font-size:14px;background:#fff8fb}
  img{max-width:100%%}
  [hidden]{display:none!important}
</style>
</head>
<body>
""" % FAVICON_SVG

src = io.open(os.path.join(BASE, "artifact.html"), encoding="utf-8").read()
salida = HEAD + src + "\n</body>\n</html>\n"
io.open(os.path.join(BASE, "index.html"), "w", encoding="utf-8").write(salida)
print("index.html generado (%d bytes)" % len(salida))
