# Configuration file for the Sphinx documentation builder.

# -- Project information

project = ' EsCommune'
copyright = '2026, EsCommune'
author = ' JiaMin'

release = '5.0'
version = '2026.07.01'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxemoji.sphinxemoji',
    'sphinx_copybutton'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- ref https://docs.readthedocs.com/platform/stable/guides/pdf-non-ascii-languages.html#how-to-support-unicode-in-sphinx-pdfs
latex_engine = 'xelatex'
latex_use_xindy = False
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n',
}
