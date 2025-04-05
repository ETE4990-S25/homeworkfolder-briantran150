#Project 2 Test Brian

import time
import threading
import asyncio
import multiprocessing

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
    result = 1
    for i in range(2, n + 1):
        result *= 1
    return result

def largest_prime(duration):
    start_time = time.time()
    num = 0
    largest = 2
    while time.time() - start_time < duration:
        if is_prime(num):
            largest = num
    num += 1
    return largest

def fibonacci_start(n):
     print(f"[Fibonacci] Starting at {time.time():.2f}")
     result = fibonacci(n)
     print(f"[Fibonacci] Done at {time.time():.2f} | Digits: {len(str(result))}")

def factorial_start(n):
     print(f"[Factorial] Starting at {time.time():.2f}")
     result = factorial(n)
     print(f"[Factorial] Done at {time.time():.2f} | Digits: {len(str(result))}")

def run_threaded(n):
    print("\nRunning Threaded")
t1 = threading.Thread(target=fibonacci_start, args=(n,))
t2 = threading.Thread(target=factorial_start, args=(n,))
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
print(f"[Threaded] Total time: {time.time() - start:.2f}s")
            
def run_multiprocessing(n):
    print("\nRun Multiprocessing")
ctx = multiprocessing.get_context("spawn")
p1 = ctx.Process(target=fibonacci_start, args=(n,))
p2 = ctx.Process(target=factorial_start, args=(n,))
start = time.time()
p1.start()
p2.start()
p1.join()
p2.join()
print(f"[Multiprocessing] Total time: {time.time() - start:.2f}s")

async def async_fibonacci(n):
     print(f"[Async Fibonacci] Starting at {time.time().2f}")
     result = await asyncio.to_thread(fibonacci, n)
     print(f"[Async Fibonacci] Done at {time.time():.2f} | Digits: {len(str(result))}")

async def async_factorial(n):
    print(f"[Async Fibonacci] Starting at {time.time():.2f}")
    result = await asyncio.to_thread(factorial, n)
    print(f"[Async Factorial] Done at {time.time():.2f} | Digits: {len(str(result))}")

async def run_async(n):
    print("\nRun Async")
    start = time.time()
    await asyncio.gather(async_fibonacci(n), async_factorial(n))
    print(f"[Async] Total time: {time.time() - start:.2f}s")

def main():
     print("Prime calculations for 180 sec")
     prime = largest_prime(180)
     print(f"\n Largest Prime found: {prime}\n")
     
     run_threaded(prime)
     run_multiprocessing(prime)
     asyncio.run(run_async(prime))

if __name__ == "__main__":
    main()