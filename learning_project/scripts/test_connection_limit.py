import aiohttp
import asyncio
import time

async def send_request(session, url, i):
    try:
        start_time = time.time()
        async with session.get(url) as response:
            status = response.status
            text = await response.text()
            print(f"Req: {i}, Total Time: {time.time() - start_time}")
            return status
    except Exception as ex:
        print(f"Request failed with error: {ex}")
        return None

async def main():
    url = "http://127.0.0.1:8000/api/ping/"
    limit = 10000

    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, url, i) for i in range(limit)]
        responses = await asyncio.gather(*tasks)

    successful_reqs = sum(1 for r in responses if r == 200)
    failed_reqs = sum(1 for r in responses if r is None)

    print(f"Success: {successful_reqs}, failed: {failed_reqs}")

if __name__ == "__main__":
    asyncio.run(main())


###########
import asyncio
import aiohttp
import time

async def send_request(session, url, request_id):
    start_time = time.time()
    try:
        async with session.get(url) as response:
            status = response.status
            duration = time.time() - start_time
            print(f"Request {request_id}: Status {status}, Time: {duration:.2f}s")
            return status
    except Exception as e:
        duration = time.time() - start_time
        print(f"Request {request_id} failed: {str(e)}, Time: {duration:.2f}s")
        return None

async def main():
    url = "http://127.0.0.1:8000/api/ping/"
    limit = 10000

    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        tasks = [send_request(session, url, i) for i in range(limit)]
        responses = await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time

    successful_reqs = sum(1 for r in responses if r == 200)
    failed_reqs = sum(1 for r in responses if r is None)

    print(f"\nTotal requests: {limit}")
    print(f"Successful requests: {successful_reqs}")
    print(f"Failed requests: {failed_reqs}")
    print(f"Time taken: {total_time:.2f} seconds")
    print(f"Requests per second: {limit / total_time:.2f}")

if __name__ == "__main__":
    asyncio.run(main())