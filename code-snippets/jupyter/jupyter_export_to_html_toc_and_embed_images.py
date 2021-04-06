# Create a nbconvert_config.py file with the following content:
c = get_config()

c.NbConvertApp.notebooks = ['v6_product_pillar_evaluation.ipynb']
c.NbConvertApp.export_format = 'html_toc'
c.Exporter.preprocessors = [
    'nbconvert.preprocessors.TagRemovePreprocessor',
    'nbconvert.preprocessors.RegexRemovePreprocessor',
    'nbconvert.preprocessors.coalesce_streams',
    'nbconvert.preprocessors.CSSHTMLHeaderPreprocessor',
    'nbconvert.preprocessors.HighlightMagicsPreprocessor',
    # 'nbconvert.preprocessors.ExtractOutputPreprocessor',
]

# and call jupyter nbconvert --config nbconvert_config.py. The key is the last entry in the list which must be commented.(! for me uncommented worked only)
#  from https://stackoverflow.com/questions/58545989/export-to-html-of-jupyter-notebook-with-table-of-contents-does-not-embed-plots