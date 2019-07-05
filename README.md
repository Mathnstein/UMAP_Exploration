# Project Goals

Here we are taking an in-depth look at UMAP performance in real data. During DSSG 2018, Team Starbucks had discovered that UMAP had some interesting qualities to finding structure that TSNE did not have. This exploration's intention is to flesh this idea out further and perhaps generalize this. At the very least we will extend our results to the entirety of British Columbia.

# DSSG 2018 report

You may find the Arxvix paper on the Surrey study [here](https://arxiv.org/abs/1903.09639).

# Getting Started

Once you have cloned the repo, open a terminal and run:
```python setup.py install```
This will install all necessary dependencies for the code.

A simple script to run UMAP embedding on the NIST digits and iris datasets can be run through
```python exploration.py```

## Required packaged installed

```
numpy
umap-learn
sklearn
pandas
matplotlib
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)