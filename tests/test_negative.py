import requests
import pytest

def test_invalid_api_key_returns_401(base_url):
    response = requests.get(f"{base_url}/games", params={"key": "invalid_xyz"})
    assert response.status_code == 401, f"Expected 401 for invalid key, got {response.status_code}"

def test_missing_api_key_returns_401(base_url): #both 401 and 403 can be correct for "Non-authorized" status
    response = requests.get(f"{base_url}/games")
    assert response.status_code in [401, 403], f"Expected 401 or 403 for missing key, got {response.status_code}"

def test_nonexistent_game_id_returns_404(base_url, api_key):
    response = requests.get(f"{base_url}/games/999999999999", params={"key": api_key})
    assert response.status_code == 404, f"Expected 404 for game id, got {response.status_code}"

def test_nonexistent_game_slug_returns_404(base_url, api_key):
    response = requests.get(f"{base_url}/games/abcdddfg", params={"key": api_key})
    assert response.status_code == 404, f"Expected 404 because id/slug is not valid, got {response.status_code}"