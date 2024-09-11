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
