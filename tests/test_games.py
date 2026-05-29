import requests

def test_get_games_returns_200(api_client):
    response = api_client.get_games()
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

def test_get_games_returns_results(api_client):
    response = api_client.get_games()
    body = response.json()
    assert "results" in body, f"Response JSON missing 'results' key. Got keys: {list(body.keys())}"
    assert len(body["results"]) > 0, "No results returned"