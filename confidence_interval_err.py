import numpy as np
import scipy.stats as st

def confidence_interval_err(vector: np.ndarray, alpha: float = 0.95):
    """Computes desired confidence interval error.
    
    https://en.wikipedia.org/wiki/Confidence_interval
     
    Args:
        vector: List of values over which a confidence interval will be computed.
        alpha: Confidence level.
 
    Returns:
        The confidence level error
    """

    # Validate
    if not(alpha > 0. and alpha < 1,):
        raise ValueError(':param alpha: must be between 0 and 100.')

    # Compute estimators
    mean = np.mean(vector)
    scale = st.sem(vector)  # standard error mean (how close to pop. mean)

    # Determine central limit theorem assumption
    if vector.shape[0] >= 30:
        print('Assume CLT...')
        interval = st.norm.interval(alpha=alpha, loc=mean, scale=scale)

    else:
        print('Not assuming CLT...')
        interval = st.t.interval(alpha=alpha, df=len(
            vector)-1, loc=mean, scale=scale)

    # Confidence intervals are m +- h
    # from left_bound = mean - h and right_bound = mean + h
    # From the 'Example' at https://en.wikipedia.org/wiki/Confidence_interval
    # it is clear that [mean - cs/sqrt(n), mean + cs/sqrt(n)] means that the
    # value of cs/sqrt(n), denoted err can be computed with simple rearrangement.
    left_bound, right_bound = interval
    err = right_bound - mean

    # Resulting err for errorbars
    return err
