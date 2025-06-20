# ...
import os
import sys
# sys.path.insert(0, os.path.abspath('.')) # Descomenta si tienes módulos Python que documentar

# -- Project information -----------------------------------------------------
project = 'Algoritmos y Estructuras de Datos'
copyright = '2023, Docentes de la Cátedra AED - UTN FRRe' # Ajusta el año y autor
author = 'Docentes de la Cátedra AED - UTN FRRe'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_rtd_theme', # Para usar el tema ReadTheDocs
    'sphinx.ext.todo',  # Para usar .. todo::
]

templates_path = ['_templates']
exclude_patterns = []
language = 'es'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme' # Asegúrate que sea este
html_static_path = ['_static']

# (Opcional) Si quieres un logo:
# html_logo = "_static/logo.png" # Asegúrate que el logo esté en docs/source/_static/

# (Opcional) Para que la barra lateral de "Table of contents" sea más profunda
html_theme_options = {
    'navigation_depth': 4, # Puedes ajustar este número
    'collapse_navigation': False,
    'sticky_navigation': True,
    'titles_only': False
}