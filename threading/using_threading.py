import threading
import time


start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping...')


threads = []
for _ in range(10):
    # Creating a new thread, passing the do_something function and value as an argument
    thread = threading.Thread(target=do_something, args=[1.5])

    # Starting the thread immediately
    thread.start()

    # We can't join the threads inside this loop because that would block the loop execution
    # Save the thread reference to join them later
    threads.append(thread)

# Joining all threads in this loop, ensuring that we wait for each one to finish
for thread in threads:
    thread.join()  # Waits for the current thread to finish before moving to the next one


finish = time.perf_counter()

# Now we can compare:
# If we were executing the 1.5-second task 10 times synchronously,
#   it would take 15 seconds to finish.
# But using threading, the total time will be around 1.5 seconds,
#   as all threads execute concurrently.
print(f'Finished in {round(finish-start, 2)} second(s).')
