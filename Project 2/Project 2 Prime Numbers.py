#Project 2 Test Brian

import time
import math
import threading
import asyncio
from multiprocessing import Process, set_start_method

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % 1 == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
            a, b = b, a + b
    return a

def factorial(n):
    return math.factorial(n)

def largest_prime(duration_sec=180):
    print(f"\nSearching for largest prime number in {duration_sec} seconds")
    start_time = time.time()
    num = 0
    largest = 0
    while time.time() - start_time < duration_sec:
        if is_prime(num):
            largest = num
    num += 1
    print(f"Largest prime found: {largest}")
    return largest

def fibonacci_task(n):
     result = fibonacci(n)
     print(f"\n Fibonacci({n}) = {result}")

def factorial_task(n):
     result = factorial(n)
     print(f"\n Factorial({n}) = {result}")

def run_threaded(n):
     print("\nRunning Threaded")
     start = time.time()
t1 = threading.Thread(target=fibonacci_task, args=(n,))
t2 = threading.Thread(target=factorial_task, args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"\nThreaded time: {time.time() - start:.2f} seconds")
            
def run_multiprocessing(n):
    print("\nRun Multiprocessing")
    start = time.time()
p1 = Process(target=fibonacci_task, args=(n,))
p2 = Process(target=factorial_task, args=(n,))
p1.start()
p2.start()
p1.join()
p2.join()
print(f" Multiprocessing time: {time.time() - start:.2f} seconds")

async def run_async(n):
     print("\nRunning Async")
     start = time.time()

     async def async_fibonacci(n):
          fibonacci_task(n)

     async def async_factorial(n):
          factorial_task(n)
          await asyncio.gather(
        async_fibonacci(n),
        async_factorial(n)
        )
print(f"Async time: {time.time() - start:.2f} seconds")
  
def main():
     duration = 180
     prime = largest_prime(duration_sec=duration)
     run_threaded(prime)
     run_multiprocessing(prime)
     asyncio.run(run_async(prime))

if __name__ == "__main__":
    try:
         set_start_method("spawn")
    except RuntimeError:
         pass
    main()