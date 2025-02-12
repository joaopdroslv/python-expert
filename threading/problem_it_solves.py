import time


start = time.perf_counter()


def do_something():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done sleeping...')


# Calling the function once
do_something()  

# Each additional call to do_something() will add 1 second to the total execution time
# do_something()  # +1 second
# do_something()  # +1 second
# do_something()  # +1 second

# The CPU is idle while waiting for time.sleep(1) to complete
#   because this script is running synchronously, meaning tasks are executed one after another


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s).')
