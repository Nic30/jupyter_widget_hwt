
# this is meant to be used from jupyter
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from IPython.display import display, HTML

def jupyter_code_format(code, lang):
    lexer = get_lexer_by_name(lang, stripall=True)
    formatter = HtmlFormatter()

    display(HTML("<style>{pygments_css}</style>".format(
        pygments_css=formatter.get_style_defs('.highlight'))))
    display(HTML(data=highlight(code, lexer, formatter)))

