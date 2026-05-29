import requests

API_KEY = "REPLACE_ME"
BASE_URL = "https://api.rawg.io/api"

def test_get_games_returns_200():
    response = requests.get(f"{BASE_URL}/games", params={"key": API_KEY})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

def test_get_games_returns_results():
    response = requests.get(f"{BASE_URL}/games", params={"key": API_KEY})
    body = response.json()
    assert "results" in body, f"Response JSON missing 'results' key. Got keys: {list(response.json().keys())}"
    assert len(body["results"]) > 0, "No results returned"