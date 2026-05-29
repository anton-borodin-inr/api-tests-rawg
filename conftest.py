import pytest
import os
from dotenv import load_dotenv

load_dotenv()
@pytest.fixture(scope="session")
def api_key():
    """Reads RAWG API key from environment. Fails fast if missing."""
    key = os.getenv("RAWG_API_KEY")
    if not key:
        pytest.fail("RAWG_API_KEY not found. Create .env with RAWG_API_KEY = your_api_key")
    return key

@pytest.fixture(scope="session")
def base_url():
    """Base URL for RAWG API."""
    return "https://api.rawg.io/api"