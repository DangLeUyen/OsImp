import numpy as np
import random

def generate_nan(Xtrain, missing_rate):
    """
    Generate NaN values in a dataset based on a missing rate.
        
    Parameters:
        - Xtrain: The dataset where missing values will be simulated.
        - missing_rate: The ratio of missing values to be generated.
        
    Returns:
        - numpy.ndarray: Dataset with NaN values generated.
        - int: 0 if successful, -1 if input is invalid.
    """
    if missing_rate < 0 or missing_rate > 1:
        return None, -1  # Invalid missing rate

    Xshape = Xtrain.shape
    n_missing = np.count_nonzero(np.isnan(Xtrain))
    Xtr_nan = Xtrain.flatten()
    Xtr_nan_id = list(range(Xtrain.size))  # All indices of elements after flattening
    nan_input_id = np.where(np.isnan(Xtr_nan))[0].tolist()  # Find NaN indices
    choice_list = [e for e in Xtr_nan_id if e not in nan_input_id]  # Non-NaN elements
    na_id = random.sample(choice_list, round(missing_rate * (Xtrain.size - n_missing)))
    Xtr_nan[na_id] = np.nan 
    return Xtr_nan.reshape(Xshape)

def partial_equalization(N, R=0.7):
    """
        Perform partial equalization based on a target ratio R.
        
        Args:
            N (list or array): A list/array containing the number of samples for each class.
            R (float): The target ratio to balance the classes, default is 0.7.
            
        Returns:
            list: A list of the number of samples to generate.
    """
    if R < 0 or R > 1:
        return None  # Invalid ratio

    N0 = max(N)
    samples_to_generate = []

    for Ni in N:
        target_size = R * N0
        samples_needed = max(int(target_size - Ni), 0)
        samples_to_generate.append(samples_needed)

    return np.array(samples_to_generate)