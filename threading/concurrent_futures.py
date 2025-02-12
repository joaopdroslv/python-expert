import concurrent.futures
import time


start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping {seconds} second(s)...'


# Using ThreadPoolExecutor to manage threads more easily
# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:  # Limiting to 3 concurrent threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]

    # Using executor.map:
    # This method applies the function to each item in the iterable (seconds)
    #   and returns results in the order of the input list.
    print("\nUsing executor.map:")
    results = executor.map(do_something, seconds)
    for result in results:
        print(result)  # Prints the result for each thread in the order they were called


    # Alternative approach using executor.submit:
    # This method schedules the function to be executed by a thread and returns a Future object.
    # It allows more fine-grained control over the execution of tasks.
    print("\nUsing executor.submit and as_completed:")
    results = [executor.submit(do_something, sec) for sec in seconds]


    # Using as_completed to process the results as threads complete:
    for future in concurrent.futures.as_completed(results):
        print(future.result())  # Prints the result once the thread is finished


    # Timeout example with .result(timeout=3):
    print("\nDemonstrating timeout with result():")
    future = executor.submit(do_something, 5)  # Task that takes 5 seconds
    try:
        # Wait at most 3 seconds for the result, which will raise TimeoutError
        result = future.result(timeout=3)
    except concurrent.futures.TimeoutError:
        print("The thread execution exceeded the timeout!")


    # Using shutdown to explicitly shut down the executor after all tasks are done
    print("\nShutting down the executor:")
    executor.shutdown(wait=True)  # Ensure all threads finish before shutting down


    # Demonstrating handling exceptions inside threads
    def do_something_with_exception(seconds):
        """A function that raises an exception for a specific case."""
        if seconds == 3:
            raise ValueError("An error occurred!")
        time.sleep(seconds)
        return f"Done sleeping {seconds} seconds"

    print("\nDemonstrating exception handling inside threads:")
    futures_with_exception = [executor.submit(do_something_with_exception, sec) for sec in seconds]
    for future in concurrent.futures.as_completed(futures_with_exception):
        try:
            print(future.result())  # This will raise the ValueError for the thread that sleeps 3 seconds
        except Exception as e:
            print(f"Error occurred: {e}")


# Stop measuring execution time
finish = time.perf_counter()

# Compare:
# If we were executing the tasks sequentially (one at a time), it would take 15 seconds to finish.
# But using threading with ThreadPoolExecutor, the total time will be around the time it takes
#   for the longest task (which is 5 seconds in this case), as all threads execute concurrently.
print(f'\nFinished in {round(finish-start, 2)} second(s).')
