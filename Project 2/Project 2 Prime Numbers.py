#Prime Number Test Brian

import time
import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i ==0:
            return False
    return True

def find_primes_in_range(start, end):
    highest_prime = 0
    for num in range(start, end):
        if is_prime(num):
            highest_prime = num
    return highest_prime

def run_parallel(executor, max_time=180, chunk_size=100_000):
    start_time = time.time()
    highest_prime = 0
    current = 0

    while time.time() - start_time < max_time:
        ranges = [(current + i * chunk_size, current + (i + 1) * chunk_size) for i in range(executor._max_workers)]
        with executor as pool:
            results = list(pool.map(lambda r: find_primes_in_range(*r), ranges))
            highest_prime = max(highest_prime, max(results))
            current += len(ranges) * chunk_size
        
        return highest_prime, time.time() - start_time
    
    def find_highest_prime_multiprocessing():
        with ProcessPoolExecutor() as executor:
            return run_parallel(executor)
    
    def find_highest_prime_threaded(thread_count=4):
        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            return run_parallel(executor)
        
    async def find_highest_prime_async():
        start_time = time.time()
        highest_prime = 0
        current = 0
        chunk_size = 100_000
        max_time = 180

        async def run_task():
            nonlocal highest_prime, current
            loop = asyncio.get_running_loop()
            while time.time() - start_time < max_time:
                ranges = [current + i * chunk_size, current + (i + 1) * chunk_size for i in range(10)]
                tasks = [loop.run_in_executor(None, find_primes_in_range, *r) for r in ranges]
                results = await asyncio.gather(*tasks)
                highest_prime = max(highest_prime, max(results))
                current += len(ranges) * chunk_size
        
        await run_task()
        return highest_prime, time.time() - start_time

    def main():
    print("Starting multiprocessing...")
    mp_prime, mp_time = find_highest_prime_multiprocessing()
    print(f"Multiprocessing: Highest prime: {mp_prime}, Time: {mp_time:.2f}s")

    print("\nStarting threading...")
    threaded_prime, th_time = find_highest_prime_threaded(thread_count=4)
    print(f"Threading: Highest prime: {threaded_prime}, Time: {th_time:.2f}s")

    print("\nStarting asynchronous...")
    loop = asyncio.get_event_loop()
    async_prime, async_time = loop.run_until_complete(find_highest_prime_async())
    print(f"Asynchronous: Highest prime: {threaded_prime}, Time: {th_time:.2f}s")

    print("\n--- Performance Comparison ---")
    print(f"Multiprocessing: {mp_prime} in {mp_time:.2f}s")
    print(f":Threading: {threaded_prime} in {th-time:.2f}s")
    print(f"Asynchronous: {async_prime} in {async_time.2f}s")

if __name__ == '__main__':
    main()
    
