from time import sleep, perf_counter
import asyncio

async def fetch_url(url):
    print('Fetching the url')
    await asyncio.sleep(1)
    print('Finished fetching')
    return 'url_content'

async def read_file(filepath):
    print('Reading the file')
    await asyncio.sleep(1)
    print('Finished reading')
    return 'file_content'

async def main():
    url = 'example.com'
    filepath = 'example.txt'
    tasks = [asyncio.create_task(coro) for coro in [fetch_url(url), read_file(filepath)]]
    fetch_result = await tasks[0]
    read_result = await tasks[1]

if __name__ == '__main__':
    start_time = perf_counter()
    asyncio.run(main())
    end_time = perf_counter()
    print(f'Time taken: {end_time - start_time}')