import os, sys
from setuptools import setup, find_packages

scriptPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, scriptPath)

# Install wheels first
whlPath = os.path.join(scriptPath, 'wheels')
depend_links = os.listdir(whlPath)

install_requires = [
    'numpy >= 1.20, < 1.21',
    'umap-learn >= 0.5, < 0.6',
    'scikit-learn >= 0.24, < 0.25',
    'pandas >= 1.2, < 1.3',
    'matplotlib >= 3.3, < 3.4',
    'seaborn >= 0.11, < 0.12',
    'ipywidgets >= 7.6, < 7.7',
    'openpyxl >= 3.0.7, < 3.0.8',
    'geopandas >= 0.9, < 1.0',
    'bokeh >= 2.3, <2.3.1'
] 

setup(
    name="UMAP_Exploration",
    version ='0.0.1',
    package_dir= {"" : os.path.relpath(scriptPath, start=os.getcwd())}, # using a relative path is required to make the develop command work
    install_requires=install_requires,
    dependency_links = depend_links
)