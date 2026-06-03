import pytest
import allure

pytestmark = [allure.epic("RAWG API Tests"), allure.feature("Search")]

@pytest.mark.smoke
@pytest.mark.regression
@allure.story("Search by game name returning results")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_returns_relevant_results(api_client):
    response = api_client.get_games(search="witcher")
    results = response.json()["results"]
    assert any("witcher" in game["name"].lower() for game in results), f"Expected 'witcher' to return, but no returned game contains this name"

@pytest.mark.regression
@allure.story("Search by incorrect game name returning no results")
@allure.severity(allure.severity_level.NORMAL)
def test_search_empty_returns_no_results(api_client):
    response = api_client.get_games(search="xqzjvwkbmrtp")
    assert response.json()["count"] == 0, f"Expected 'count' to return 0, but it returned count={response.json()['count']}"

@pytest.mark.regression
@allure.story("Search with pagination by page size")
@allure.severity(allure.severity_level.NORMAL)
def test_search_pagination(api_client):
    response = api_client.get_games(page_size=5)
    results = response.json()["results"]
    assert len(results) == 5, f"Expected 5 results per page, but it returned {len(results)}"