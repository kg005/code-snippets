from IPython.display import Markdown as md

def mdd(text: str, h: int = None, bold=False):
    """
    Shortucut function for displaying markdown
    :param text: text to display as MD
    :param h: optional header level
    """
    display(
        md(
            f'{"#" * h + " " if h is not None else ""}{"__" if bold else ""}{text}{"__" if bold else ""}'
        )
    )

