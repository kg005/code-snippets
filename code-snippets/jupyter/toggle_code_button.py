from IPython.display import display
from IPython.display import HTML
import IPython.core.display as di

# This line will add a button to toggle visibility of code blocks, for use with the HTML export version
di.display_html('''<button onclick="jQuery('.input_area').toggle(); jQuery('.prompt').toggle();">Show/Hide Code Cells</button>''', raw=True)

# This line will hide code by default when the notebook is exported as HTML
# di.display_html('<script>jQuery(function() {if (jQuery("body.notebook_app").length == 0) { jQuery(".input_area").toggle(); jQuery(".prompt").toggle();}});</script>', raw=True)

# this makes the notebook wider
display(HTML("<style>.container { width:90% !important; }</style>"))