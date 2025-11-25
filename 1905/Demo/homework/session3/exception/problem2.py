# 2. Write a function that handles an exception and re-raises it to the caller and handle it in the caller


def process_data(data):
    try:
        # Some processing that might raise an exception
        if not isinstance(data, int):
            raise TypeError("Data must be an integer.")
        return data * 2
    except TypeError as e:
        print(f"Warning: Data type mismatch in process_data: {e}")
        raise # Re-raise the exception

try:
    process_data("abc")
except TypeError as e:
    print(f"Caught re-raised exception: {e}")



