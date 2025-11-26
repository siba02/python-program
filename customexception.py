import requests

# -------- CUSTOM EXCEPTION --------
class JokeAPIError(Exception):
    """Custom exception for joke API errors."""
    def __init__(self, message, status_code=None):
        self.status_code = status_code
        super().__init__(message)


def get_random_joke():
    url = "https://official-joke-api.appspot./random_joke"

    try:
        response = requests.get(url, timeout=5)

        # Raise exception for HTTP errors (non-200 responses)
        if response.status_code != 200:
            raise JokeAPIError("Failed to fetch joke", status_code=response.status_code)

        return response.json()

    except requests.exceptions.Timeout:
        raise JokeAPIError("Request to Joke API timed out")

    except requests.exceptions.HTTPError as http_err:
        raise JokeAPIError(f"HTTP error occurred: {http_err}")

    except requests.exceptions.RequestException as err:
        raise JokeAPIError(f"General network error: {err}")


# ---- MAIN PROGRAM ----
try:
    joke = get_random_joke()
    print("Setup:", joke["setup"])
    print("Punchline:", joke["punchline"])

except JokeAPIError as e:
    print(f"Custom Error -> {e}")
