import requests

def test_get_games_returns_200(base_url, api_key):
    response = requests.get(f"{base_url}/games", params={"key": api_key})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

def test_get_games_returns_results(base_url, api_key):
    response = requests.get(f"{base_url}/games", params={"key": api_key})
    body = response.json()
    assert "results" in body, f"Response JSON missing 'results' key. Got keys: {list(response.json().keys())}"
    assert len(body["results"]) > 0, "No results returned"