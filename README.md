# OsImp - Oversampling and imputation for imbalanced missing data
This repository contains the **OsImp** package, designed for tackling missing and imbalance data simutanously. The package is based on the methodology outlined in the paper **Oversampling and imputation for imbalanced missing data"**

### Installation of package
To install the OsImp package, you can easily do so via GitHub. Run the following command in your environment:

`!pip install git+https://github.com/DangLeUyen/OsImp.git`

After installation, you can import the **OsImp** class as follows:

`from OsImp import OsImp`

### Usage Guide

#### For a training dataset X with Labels y

```
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from OsImp import OsImp

# Initiate a suitable imputer to impute missing data. Here, we use the MICE algorithm
mice_imputer = IterativeImputer().fit_transform

# Create an instance of the OsImp class with a target ratio R for oversampling minority classes is 0.9;
# If imputer is not provided, it defaults to MICE method;
# If R is not provided, it defaults to 0.9.
osimputer = OsImp(mice_imputer, R=0.9)

# Apply OsImp to the imbalanced missing dataset
Xnew, ynew = osimputer.os_and_impute(X, y)
```

For additional examples and details, please refer to the `example.ipynb` file in the repository.
### Citation
If you use this package in your research, please cite the paper:

Oversampling and imputation for imbalanced missing data.

-------------------------------
This README provides users with a clear guide on installing and using the OsImp package while also giving proper credit to the research behind it.

