# Call this as rescue_code(f), or whatever your function is, and a new cell should be created with the code of you function
# Source with explanation of how it works http://blog.rtwilson.com/how-to-rescue-lost-code-from-a-jupyteripython-notebook/

def rescue_code(function):
    import inspect
    get_ipython().set_next_input("".join(inspect.getsourcelines(function)[0]))