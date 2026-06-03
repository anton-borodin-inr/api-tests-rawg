import requests
import allure

class RawgClient:
    def __init__(self, base_url, api_key):
        """Store config and create a reusable session."""
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()

    @allure.step("GET /games (search={search}, page_size={page_size})")
    def get_games(self, search=None, page_size=20, platforms=None):
        """GET /games with optional filters. Returns Response."""
        params = {"key": self.api_key, "page_size": page_size}
        if search is not None:
            params["search"] = search
        if platforms is not None:
            params["platforms"] = platforms
        return self.session.get(f"{self.base_url}/games", params=params)

    @allure.step("GET /games/{game_id}")
    def get_game_details(self, game_id):
        """GET /games/{id}. Returns Response."""
        return self.session.get(f"{self.base_url}/games/{game_id}", params={"key": self.api_key})

    @allure.step("GET /platforms")
    def get_platforms(self):
        """GET /platforms. Returns Response."""
        return self.session.get(f"{self.base_url}/platforms", params={"key": self.api_key})