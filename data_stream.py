#Data Stream simulation
import numpy as np
import time

def data_stream_simulation(stream_length=100, noise_level=0.2):
    """
    Simulates a real-time data stream of random numbers with added Gaussian noise.

    Parameters:
    -----------
    stream_length : int, optional (default=100)
        The number of data points to generate in the simulated stream. Must be a positive integer.
    
    noise_level : float, optional (default=0.2)
        The standard deviation of the Gaussian noise added to each data point. Must be a non-negative float or int.

    Yields:
    -------
    value : float
        A randomly generated data point with added noise.

    Raises:
    -------
    ValueError : If `stream_length` is not a positive integer, or if `noise_level` is not a non-negative float or int.
    
    Example:
    --------
    >>> stream = data_stream_simulation(stream_length=10, noise_level=0.3)
    >>> for i, value in enumerate(stream):
    >>>     print(f"Value {i+1}: {value}")
    """

    # Input validation for stream_length
    if not isinstance(stream_length, int) or stream_length <= 0:
        raise ValueError(f"Invalid stream_length: {stream_length}. It must be a positive integer.")
    
    # Input validation for noise_level
    if not isinstance(noise_level, (int, float)) or noise_level < 0:
        raise ValueError(f"Invalid noise_level: {noise_level}. It must be a non-negative float or integer.")

    # Stream data generation with error handling
    try:
        for i in range(stream_length):
            value = np.random.random() + noise_level * np.random.randn()  # Adding noise
            yield value  # Yield the generated value
            time.sleep(0.1)  # Simulate real-time streaming with a delay
    except Exception as e:
        print(f"An error occurred during data stream simulation: {e}")

# Testing the function
if __name__ == "__main__":
    try:
        # You can adjust the values for testing different scenarios
        stream_generator = data_stream_simulation(stream_length=100, noise_level=0.2)

        for i, value in enumerate(stream_generator):
            print(f"Generated value {i+1}: {value}")
            if i >= 99:  # Stop after 100 values
                break
    except ValueError as ve:
        print(f"Input Error: {ve}")

        
  

