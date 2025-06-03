import requests
import hashlib
import base64
import argparse

def generate_sri_hash(url):
    """Fetches content from a URL, calculates SHA384 hash, and base64 encodes it for SRI."""
    try:
        response = requests.get(url)
        response.raise_for_status()  
        content = response.content

        #  SHA384 hash
        sha384_hash = hashlib.sha384(content).digest()

        # Base64 encode the hash
        base64_hash = base64.b64encode(sha384_hash).decode('utf-8')

        # SRI integrity string
        return f"sha384-{base64_hash}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching {url}: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# argument parser
parser = argparse.ArgumentParser(description="Generate SRI hashes for given URLs.")
# allow multiple URLs, each with an optional name
parser.add_argument("urls", nargs='+', help="URLs to generate SRI hashes for. Can be provided as 'name=url' or just 'url'.")


args = parser.parse_args()

print("Generating SRI Hashes:")
print("-" * 30)

for item in args.urls:
    if '=' in item:
        name, url = item.split('=', 1)
    else:
        name = url = item # If no name is provided, use the URL as the name for display

    sri_hash = generate_sri_hash(url)
    print(f"{name} SRI: {sri_hash}")

print("-" * 30)
print("Copy these values and paste them into your index.html file.")