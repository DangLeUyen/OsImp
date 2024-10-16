# OsImp - Oversampling and Imputation for imbalanced missing data
This repository contains the **OsImp** package, developed to address the dual challenges of missing and imbalanced data. The package is based on the methodology outlined in the paper **Oversampling and imputation for imbalanced missing data"**

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

# Initialize a suitable imputer for missing data. Here, we use the MICE algorithm.
mice_imputer = IterativeImputer().fit_transform

# Create an instance of the OsImp class,specifying the target ratio R for oversampling minority classes.
# If imputer and R are not provided (e.g., osimputer = OsImp()), MICE and R=0.9 are used by default.
osimputer = OsImp(mice_imputer, R=0.9)

# Apply OsImp to the imbalanced and missing dataset
Xnew, ynew = osimputer.os_and_impute(X, y)
```

For additional examples and details, please refer to the `example.ipynb` file in the repository.
### Citation
If you use this package in your research, please cite the paper:

Oversampling and imputation for imbalanced missing data.

-------------------------------
This README provides users with a clear guide on installing and using the OsImp package while also giving proper credit to the research behind it.

