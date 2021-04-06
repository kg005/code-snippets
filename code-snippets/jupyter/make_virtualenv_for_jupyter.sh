# make virtual environment in current directory
virtualenv <name>

# activate the environment
source <env_name>/bin/activate

# deactivate the environment
deactivate

# check which are we currently using
which python

# remove environment
sudo rm -rf <env_name>


# add environment to the jupyter notebook (need to first activate, and install ipykernel to for desired environment)
python -m ipykernel install --user --name=<env_name> --display-name=<name that will be displayed in the ntb>

# check it was added
# cd to the env folder and check kernel.json
# the folder path is usually printed out after kernel install like:
# 'home/kg/.local/share/jupyter/kernels/bizm_venv'


# remove virtualenv from the notebook
jupyter kernelspec uninstall <env_name>
