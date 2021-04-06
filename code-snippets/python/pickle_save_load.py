import pickle 

def save_obj(obj, name ):
    with open('./obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        print(f"'{name}' saved successfully, you can load it by calling:\n{name} = load_obj('{name}')")

def load_obj(name ):
    with open('./obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


# more advanced, outputting cell with load command, using timestamp
def save_obj(obj, name, use_timestamp=True):
    from datetime import datetime as dt
    
    suffix =  f"_{dt.now().strftime('%Y%m%d_%H%M%S')}" if use_timestamp else ""
    
    if not os.path.exists("./obj/"):
        print("Folder './obj/' does not exist, it will be created.")
        os.mkdir("./obj/")
        
    with open(f"./obj/{name}{suffix}.pkl", "wb") as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        print(
            f"File '{name}' saved successfully, load it by uncommenting and calling following cell:"
        )
        get_ipython().set_next_input(f"# {name} = load_obj('{name}{suffix}')")


def load_obj(name):
    with open("./obj/" + name + ".pkl", "rb") as f:
        return pickle.load(f)


# with folder as global variable option
import pickle 
storage_folder = './pickled_objects/'
def save_obj(obj, name ):
    global storage_folder
    with open(storage_folder + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        print(f"'{name}' saved successfully, you can load it by calling:\n{name} = load_obj('{name}')")

def load_obj(name ):
    global storage_folder
    with open(storage_folder + name + '.pkl', 'rb') as f:
        return pickle.load(f)


# more advanced, outputting cell with load command, using timestamp
def save_obj(obj, name, use_timestamp=True):
    global storage_folder
    from datetime import datetime as dt
    
    suffix =  f"_{dt.now().strftime('%Y%m%d_%H%M%S')}" if use_timestamp else ""
    
    if not os.path.exists(storage_folder):
        print(f"Folder '{storage_folder}' does not exist, it will be created.")
        os.mkdir(storage_folder)
        
    with open(f"{storage_folder}{name}{suffix}.pkl", "wb") as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        print(
            f"File '{name}' saved successfully, load it by uncommenting and calling following cell:"
        )
        get_ipython().set_next_input(f"# {name} = load_obj('{name}{suffix}')")


def load_obj(name):
    global storage_folder
    with open(storage_folder + name + ".pkl", "rb") as f:
        return pickle.load(f)
