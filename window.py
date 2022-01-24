"""Windowing function for time series data."""

def window(arr, time_lag, forecast_horizon, sampling_rate=1):
    """Creates time lagged-forecast horizoned windows.
    
    TODO: Specify label column indices or name of labels.
    
    Args:
      arr: Array with the first index as time steps.
      time_lag: Time steps in the past.
      forecast_horizon: Time steps in the future.
      sampling_rate: Difference between the i^{th} element
        time step and the i+1 element time step for
        n windows.
        
    Returns:
      Windowed data of the form [(feature, target)] 
      where feature and targets are arrays whose length
      is determined by the `time_lag` and `forecast_horizon`.
      
    Example:
    ```
    >>> arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> windowed_data = window(arr=arr, time_lag=2, forecast_horizon=3, sampling_rate=1)
    >>> windowed_data
    [([0, 1], [2, 3, 4]),
    ([1, 2], [3, 4, 5]),
    ([2, 3], [4, 5, 6]),
    ([3, 4], [5, 6, 7]),
    ([4, 5], [6, 7, 8]),
    ([5, 6], [7, 8, 9]),
    ([6, 7], [8, 9, 10])]
    ```
    """

    windowed_data = []
    
    stop = len(arr)-(time_lag+forecast_horizon)+1
    for ix in range(0, stop, sampling_rate):
        feature = arr[ix:ix+time_lag]
        target = arr[ix+time_lag: ix+time_lag+forecast_horizon]
        windowed_data.append((feature, target))
        
    return windowed_data
