import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()   # Raises an error if status code is not 200

        

        data = response.json()        # Convert response to JSON
        return data

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")

    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

    return None


# ---- MAIN PROGRAM ----
joke = get_random_joke()

if joke:
    print("Setup:", joke["setup"])
    print("Punchline:", joke["punchline"])
