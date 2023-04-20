"""Windowing function for time series data."""

def window(arr, time_lag, forecast_horizon, sampling_rate=1):
    """Creates time lagged-forecast horizoned windows.
    
    TODO: Specify label column indices or name of labels.
    
    
    Example:
    ```
    >>> # Create time series windows with 2 time steps
    >>> # in the past (`time_lag`) used to predict 
    >>> # 3 time steps in future (`forecast_horizon`).
    >>> # Note that with `sampling_rate=1`, the 
    >>> # difference between the elements of rows 
    >>> # is 1. If the sampling rate is increased,
    >>> # it essentially decreases the number rows
    >>> # and increases the difference between elements
    >>> # of rows.
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
    """

    windowed_data = []
    
    stop = len(arr)-(time_lag+forecast_horizon)+1
    for ix in range(0, stop, sampling_rate):
        feature = arr[ix:ix+time_lag]
        target = arr[ix+time_lag: ix+time_lag+forecast_horizon]
        windowed_data.append((feature, target))
        
    return windowed_data


def np_window(x, y, lag, horizon: int = 1):
    """Sliding window over x and y data.
    
    Sampling rate is 1 and sequence stride is 1.
    """
    x_windowed = sliding_window_view(
        x[:-lag], window_shape=lag)
    y_windowed = sliding_window_view(
        y[lag:], window_shape=horizon,)
    
    if len(x_windowed) < len(y_windowed):
        y_windowed = y_windowed[:len(x_windowed), :]
    else:
        x_windowed = x_windowed[:len(y_windowed), :]
    
    if horizon == 1:
        y_windowed = np.squeeze(y_windowed)
    
    return x_windowed, y_windowed
