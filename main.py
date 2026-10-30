
import requests

from urllib.parse import urlparse


def check_website(url):
    # Add HTTPS if the user did not enter a scheme
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Validate the URL
    parsed_url = urlparse(url)

    if not parsed_url.hostname:
        print("Invalid URL.")
        return

    try:
        response = requests.get(url, timeout=10, stream=True)

        status_code = response.status_code
        response.close()

        print(f"\nWebsite: {url}")
        print(f"HTTP Status Code: {status_code}")

        if 200 <= status_code < 300:
            print("Result: Website responded successfully.")
        elif 300 <= status_code < 400:
            print("Result: Website responded with a redirect.")
        elif 400 <= status_code < 500:
            print("Result: Website responded with a client error.")
        else:
            print("Result: Website responded with a server error.")

    except requests.exceptions.Timeout:
        print(f"\nWebsite: {url}")
        print("Result: Request timed out.")

    except requests.exceptions.SSLError:
        print(f"\nWebsite: {url}")
        print("Result: SSL certificate verification failed.")

    except requests.exceptions.ConnectionError:
        print(f"\nWebsite: {url}")
        print("Result: Could not connect to the website.")

    except requests.exceptions.RequestException as error:
        print(f"\nWebsite: {url}")
        print(f"Result: Request failed: {error}")


def main():
    print("===== Website Status Checker =====")
    print("Enter website URLs separated by commas.")
    print("Example: example.com, python.org")

    user_input = input("\nEnter URLs: ").strip()

    if not user_input:
        print("Please enter at least one website URL.")
        return

    websites = user_input.split(",")

    for website in websites:
        website = website.strip()

        if website:
            check_website(website)


if __name__ == "__main__":
    main()
