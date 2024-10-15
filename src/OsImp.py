import numpy as np
from funcs import partial_equalization, generate_nan

class OsImp:
    def __init__(self, imputer, R=0.9, missing_range=np.arange(0, 0.6, 0.1)):
        """
        Initialize the OsImp object.
        
        Parameters:
        - imputer: The imputation function to handle missing data.
        - R: Target ratio to generate new samples for each class.
        - missing_range: Range of missing values to simulate in the data.
        """
        self.imputer = imputer
        self.R = R
        self.missing_range = missing_range

    def os_and_impute(self, X, y):
        """
        Perform oversampling and imputation as per the algorithm.
        
        Returns:
        - Xnew: The new dataset with imputed values.
        - ynew: The new target labels including the oversampled data.
        """
        y = y.flatten()
        # Get unique classes and their counts
        G, class_counts = np.unique(y, return_counts=True)

        # Determine the number of samples to generate based on the target ratio R
        n = partial_equalization(class_counts, self.R)
            
        # Get the positive index of the classes that need oversampling
        posId = np.where(n > 0)[0]

        # Generate new samples for the classes to be oversampled
        idz = np.array([np.random.choice(range(sum(y == g)), n[g]) for g in G], dtype = object)
        Zover = [X[y == g][idz[g]] for g in posId]
        Zover = np.vstack((Zover))
            
        # Imputation process over different missing ranges
        Xlist = []
        for mr in self.missing_range:
            Zover_with_nan = generate_nan(Zover, mr)
            T = np.vstack((Zover_with_nan, X))
            Xlist.append(self.imputer(T))

        # Average the results across all missing ranges
        Xnew = np.mean(Xlist, axis=0)

        # Create new target labels with the oversampled data
        # Check if there are any arrays to concatenate
        arrays = [np.repeat(g, n[g]) for g in posId]
        if len(arrays) > 0:
            ynew = np.hstack((np.concatenate(arrays), y))
        else:
            ynew = y

        return Xnew, ynew