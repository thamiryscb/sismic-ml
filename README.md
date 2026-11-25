# Seismic ML Generalization

## About the Project

This project investigates the application of unsupervised Machine Learning algorithms to real seismic data, focusing on seismic attribute clustering and cross-basin generalization.

The study compares K-means and Gaussian Mixture Models (GMM), evaluating their ability to identify seismic patterns and transfer learned representations between different sedimentary basins.

## Objectives

- Extract and analyze seismic attributes.
- Apply unsupervised Machine Learning techniques.
- Optimize clustering hyperparameters.
- Compare K-means and GMM.
- Evaluate cross-basin generalization.
- Analyze computational efficiency and clustering uncertainty.

## Technologies

- Python
- NumPy
- Pandas
- SciPy
- Scikit-learn
- Matplotlib
- Segyio
- Jupyter Notebook

## Datasets

The initial experiments will use seismic data from the Jequitinhonha Basin, Brazil.

An additional seismic dataset will be selected for external validation and cross-basin generalization.

Raw seismic files are not included in this repository due to their size and potential data usage restrictions.

## Installation

Clone the repository, create a Python virtual environment and install the dependencies listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

Place the seismic datasets inside `data/raw/` and open the notebook located in `notebooks/`.

## Project Status

Under development.

## Academic Purpose

This project is developed as part of an academic study on Machine Learning applied to geological and geophysical data at the Federal University of Rio Grande do Norte (UFRN).