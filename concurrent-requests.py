import requests
import concurrent.futures

def send_request(url):
    response = requests.get(url)
    print(f"Request to {url} - Status Code: {response.status_code}")

if __name__ == "__main__":
    # Specify the URL you want to send requests to
    target_url = "http://localhost:8080/concurrent_requests_from_python"

    # Number of requests to send
    num_requests = 10000

    # Create a list of the same URL for concurrent requests
    urls = [target_url] * num_requests

    # Using ThreadPoolExecutor for concurrent requests
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_requests) as executor:
        # Submit the requests concurrently
        executor.map(send_request, urls)
