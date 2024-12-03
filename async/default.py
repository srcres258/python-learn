from time import sleep, perf_counter

def fetch_url(url: str) -> str:
    print('Fetching the URL')
    sleep(1)
    print('Finished fetching')
    return 'url_content'

def read_file(filepath: str) -> str:
    print('Reading the file')
    sleep(1)
    print('Finished reading')
    return 'file_content'

def main() -> None:
    url = 'example.com'
    filepath = 'example.txt'
    fetch_result = fetch_url(url)
    read_result = read_file(filepath)

if __name__ == '__main__':
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f'Time taken: {end_time - start_time}')