# Project Goals

Here we are taking an in-depth look at UMAP performance in real data. During DSSG 2018, Team Starbucks had discovered that UMAP had some interesting qualities to finding structure that TSNE did not have. This exploration's intention is to flesh this idea out further and perhaps generalize this. At the very least we will extend our results to the entirety of British Columbia.

# DSSG 2018 report

You may find the Arxvix paper on the Surrey study [here](https://arxiv.org/abs/1903.09639).

# Getting Started
This project uses *python 3.7.4* and it is recommended to use a virtual environment.
Once you have cloned the repo, open a terminal and run:

```
python -m venv .venv
.venv\Scripts\Activate.ps1
python pre-setup.py
```
This will create and activate the virtual enviornment *.venv* and install all necessary dependencies for the code.

A simple script to run UMAP embedding on the NIST digits and iris datasets can be run through
```python exploration.py```

## Required packaged installed

```
    'numpy >= 1.20, < 1.21',
    'umap-learn >= 0.5, < 0.6',
    'scikit-learn >= 0.24, < 0.25',
    'pandas >= 1.2, < 1.3',
    'matplotlib >= 3.3, < 3.4',
    'seaborn >= 0.11, < 0.12',
    'pyshp >= 2.1, < 2.2',
    'xlrd >= 2.0, < 2.1',
    'descartes >= 1.1, < 1.2',
    'ipywidgets >= 7.6, < 7.7',
    'geopandas >= 0.9, < 1.0'
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)