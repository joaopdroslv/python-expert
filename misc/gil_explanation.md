# What is GIL (Global Interpreter Lock) in Python

The GIL exists mainly because of the way Python manages memory and the **garbage collector**. The Python interpreter uses a reference counting system to manage memory allocation and deallocation. Without the GIL, multiple threads could modify an object's reference count at the same time, leading to **race conditions** and **potential memory corruption**

## How does the GIL affect thread execution?

### 🔴 Threads are not really parallel in pure Python:

If you use `threading` to create multiple threads in Python, they will not run at the same time, but rather interleaved. The interpreter switches between threads periodically to give the feeling of concurrency.

### ✅ The GIL does not affect separate processes:

The `multiprocessing` module creates independent processes, each with its own instance of the Python interpreter. As a result, the GIL does not prevent multiple processes from running simultaneously.

## Practical example of the impact of GIL

### Using `threading` with a CPU-bound operation (bad)

CPU-bound operations do not benefit from threading because of the GIL.

```python
import threading
import time

def count():
    total = 0
    for _ in range(10**7):
        total += 1

start = time.time()

# Creating 2 threads to execute the function
t1 = threading.Thread(target=count)
t2 = threading.Thread(target=count)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Time with threads: {time.time() - start:.2f} seconds")
```

🔴 **Problem:** Even with two threads, the execution time will be **almost the same** as running the function twice sequentially. This is because the GIL prevents both threads from running at the same time.

### Using `multiprocessing` to bypass the GIL (better)

```python
import multiprocessing
import time

def count():
    total = 0
    for _ in range(10**7):
        total += 1

start = time.time()

# Creating 2 separate processes
p1 = multiprocessing.Process(target=count)
p2 = multiprocessing.Process(target=count)

p1.start()
p2.start()

p1.join()
p2.join()

print(f"Time with multiprocessing: {time.time() - start:.2f} seconds")
```

✅ **Advantage:** This code actually uses **two CPU cores**, resulting in an execution time that is **practically halved**.

## Does the GIL affect everything in Python?

No! The GIL affects **CPU-bound operations** only.
For I/O-bound operations (such as network requests or file reading/writing), `threading` can still be useful, because the GIL is released when the program waits for the response from an I/O operation.

## Conclusion

📌 **GIL limits the actual execution of multiple threads in Python**, preventing them from running simultaneously in CPU-bound operations.
📌 For **heavy computational tasks**, `multiprocessing` is a better solution.
📌 For **I/O** tasks, `threading` can still be efficient, as GIL is freed during wait operations.
