# Topic Group: Advanced API Automation & Workflows
# Question: Your team is prototyping a small automation client that talks to a mock API represented entirely by local functions and data. The scenario involves walking through multiple 'pages' of a long result set that can only be read in chunks while keeping everything offline. The client should detect basic error conditions represented by return codes or flags, apply simple retry or pagination rules, and collect successful results into a single combined structure. In particular, it should keep requesting the next page until a marker tells you there is no more data. Every important step, including failures and final summaries, should be appended to an in‑memory log so that the overall flow can be inspected afterwards.
# Input: No input required
# Hint: Represent the remote API as normal functions, then add wrapper logic that handles retries, backoff or pagination while building a single results list.

import random
import time     
log = []
def mock_api_call(page_token=None):
    """Simulates an API call that returns paginated data."""
    if random.random() < 0.2:  # 20% chance to simulate an error
        return {"error": "Temporary error, please retry."}
    
    data = [f"item_{i}" for i in range(random.randint(1, 5))]
    next_page_token = None if random.random() < 0.3 else f"token_{random.randint(1000,9999)}"
    
    return {
        "data": data,
        "next_page_token": next_page_token
    }
def fetch_all_data():
    all_data = []
    page_token = None
    retries = 3

    while True:
        attempt = 0
        while attempt < retries:
            response = mock_api_call(page_token)
            log.append(f"API call with token {page_token}: {response}")
            
            if "error" in response:
                log.append(f"Error encountered: {response['error']}. Retrying...")
                attempt += 1
                time.sleep(1)  # Simple backoff
            else:
                all_data.extend(response["data"])
                page_token = response["next_page_token"]
                break
        else:
            log.append("Max retries reached. Stopping.")
            break
        
        if not page_token:
            log.append("No more pages to fetch.")
            break

    return all_data
