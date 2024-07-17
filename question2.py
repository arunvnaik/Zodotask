import requests
from time import sleep

def download_urls(urls):
    results = {}

    for url in urls:
        attempts = 0
        success = False
        while attempts < 3 and not success:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raises HTTPError for bad responses
                results[url] = response.text
                success = True
            except requests.exceptions.HTTPError as e:
                print(f"HTTPError for {url}: {e}")
            except requests.exceptions.ConnectionError as e:
                print(f"ConnectionError for {url}: {e}")
            except requests.exceptions.Timeout as e:
                print(f"Timeout for {url}: {e}")
            except requests.exceptions.RequestException as e:
                print(f"RequestException for {url}: {e}")
            attempts += 1
            if not success:
                sleep(1)  # Wait for 1 second before retrying

        if not success:
            results[url] = None

    return results

# Example usage:
urls = [
    "https://www.google.com/",
    "https://www.youtube.com/watch?v=TZBvriSSA50",  # This will fail
    "https://www.youtube.com/"       # This will fail with an HTTP error
]

content = download_urls(urls)
for url, data in content.items():
    if data is not None:
        print(f"Content of {url}: {data[:100]}...")  # Print first 100 characters
    else:
        print(f"Failed to download {url} after 3 attempts.")
