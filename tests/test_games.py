import json
import os
import pytest
from jsonschema import validate


def _load_known_games():
    """Reads known games list from test_data/test_games.json at module level."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "test_data", "test_games.json")
    with open(path) as f:
        return json.load(f)["known_games"]

KNOWN_GAMES = _load_known_games()

def test_get_games_returns_200(api_client):
    response = api_client.get_games()
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

def test_get_games_returns_results(api_client):
    response = api_client.get_games()
    body = response.json()
    assert "results" in body, f"Response JSON missing 'results' key. Got keys: {list(body.keys())}"
    assert len(body["results"]) > 0, "No  results returned"

def test_game_details_match_schema(api_client):
    schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "helpers", "schemas",
                               "game_schema.json")
    with open(schema_path) as f:
        schema = json.load(f)
    response = api_client.get_game_details(3498)
    validate(instance=response.json(), schema=schema)

def test_games_list_matches_schema(api_client):
    schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "helpers", "schemas", "games_list_schema.json")
    with open(schema_path) as f:
        schema = json.load(f)
    response = api_client.get_games()
    validate(instance=response.json(), schema=schema)

@pytest.mark.parametrize("game", KNOWN_GAMES, ids=[g["name"] for g in KNOWN_GAMES])
def test_game_id_returns_correct_name(api_client, game):
    response = api_client.get_game_details(game["id"])
    actual_name = response.json()["name"]
    assert actual_name == game["name"], f"For id={game['id']}: expected '{game['name']}', got '{actual_name}'"
