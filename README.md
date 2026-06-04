# API test for RAWG
![Tests](https://github.com/anton-borodin-inr/api-tests-rawg/actions/workflows/tests.yml/badge.svg)

Automated API tests for RAWG using RawgClient + requests. Demonstrates api requests testing, work with auth, marker-based test selection and Allure reporting.

## Tech stack

- Language & Test Framework: Python 3.14, pytest, Allure, requests
- API under test: RAWG Games API

## Test coverage

- Games - basic positive test to be sure auth is working and server returns games, ids, response matches schema
- Negatives - checking wrong api key, url address, game id and slug
- Search - search with correct and incorrect game name, search with pagination by page size

## Project structure
```
├── .github
│   └── workflows
│       └── tests.yml           - settings for CI on GitHUB
├── helpers/
│   ├── schemas
│       ├── game_schema.json    - what schema should be in response
│       └── games_list_schema.json    - what schema should be in response about concrete game
│   └── api_client.py           - how to send and process requests
├── postman/
│   └── RAWG API.postman_collection.json      - collection with all requests from api_client, can be reproduced manually via Postman app
├── test_data
│   └── test_games.json          - data to use in parametrize test (test_games.py)
├── tests/                       - files with test
│   ├── test_games.py
│   ├── test_negative.py
│   └── test_search.py
├── conftest.py                  - file with fixtures
├── pytest.ini                   - pytest configuration (markers, addopts)
├── requirements.txt             - Python dependencies
└── README.md
```

## Prerequisites
- Created API key on rawg.io
- Python 3.14+

## Setup
```bash
git clone https://github.com/anton-borodin-inr/api-tests-rawg
cd api-tests-rawg
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to run tests
1. Put API key to the .env
2. Run tests:
```bash
# run all tests
pytest -v

# all except negative tests
pytest -m "not negative"

# smoke and negative tests
pytest -m "smoke or negative"

# run tests with Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

## Architecture Highlights
- API client pattern - request logic is centralized in `RawgClient`
  (an API analog of Page Object Model). Tests call client methods instead of
  building URLs and sending raw requests, so changing an endpoint touches one place.
- Negative tests - since the client only sends valid data, negative cases
  use raw `requests.get()` with deliberately bad input (wrong key, bad id,
  malformed slug) to exercise failure paths.
- JSON Schema validation - responses are validated against JSON schemas,
  so a backend change to a field's name, type or presence fails the test
  immediately instead of passing silently
- Session-scoped fixtures - the `api_client` fixture (and its underlying
  `requests.Session`) is created once per test run rather than per test,
  reusing the TCP connection and speeding up the suite


## CI/CD

Tests run automatically on every push and pull request via GitHub Actions
(`.github/workflows/tests.yml`).

The pipeline:
- sets up Python 3.14 on Ubuntu
- installs dependencies from `requirements.txt`
- runs the full pytest suite
- uploads Allure results as a build artifact (kept even if tests fail)

The RAWG API key is stored as a GitHub repository secret (`RAWG_API_KEY`),
never committed to the repo.