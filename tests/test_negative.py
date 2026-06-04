import requests
import pytest
import allure

pytestmark = [allure.epic("RAWG API Tests"), allure.feature("Negative scenarios")]
# Auth negative tests use raw requests because api_client always sends a valid API key.

@pytest.mark.regression
@pytest.mark.negative
@allure.story("Valid url with invalid API key returns 401")
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_api_key_returns_401(base_url):
    response = requests.get(f"{base_url}/games", params={"key": "invalid_xyz"})
    assert response.status_code == 401, f"Expected 401 for invalid key, got {response.status_code}"

@pytest.mark.regression
@pytest.mark.negative
@allure.story("Valid url without API key returns 401 or 403")
@allure.severity(allure.severity_level.NORMAL)
def test_missing_api_key_returns_401(base_url): #both 401 and 403 can be correct for "Non-authorized" status
    response = requests.get(f"{base_url}/games")
    assert response.status_code in [401, 403], f"Expected 401 or 403 for missing key, got {response.status_code}"

@pytest.mark.regression
@pytest.mark.negative
@allure.story("Nonexistent game id returns 404")
@allure.severity(allure.severity_level.NORMAL)
def test_nonexistent_game_id_returns_404(base_url, api_key):
    response = requests.get(f"{base_url}/games/999999999999", params={"key": api_key})
    assert response.status_code == 404, f"Expected 404 for game id, got {response.status_code}"

@pytest.mark.regression
@pytest.mark.negative
@allure.story("Nonexistent game slug returns 404")
@allure.severity(allure.severity_level.NORMAL)
def test_nonexistent_game_slug_returns_404(base_url, api_key):
    response = requests.get(f"{base_url}/games/abcdddfg", params={"key": api_key})
    assert response.status_code == 404, f"Expected 404 because id/slug is not valid, got {response.status_code}"