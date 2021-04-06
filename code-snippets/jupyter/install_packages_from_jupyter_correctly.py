# Install pip package in the current Jupyter kernel
import sys 
!{sys.executable} -m pip install <package_name>


# Install a conda package in the current Jupyter kernel
import sys
!conda install --yes --prefix {sys.prefix} numpy


