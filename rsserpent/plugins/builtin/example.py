from typing import Any, Dict


path = "/_/example/basic/"


def provider() -> Dict[str, Any]:
    """Define a basic example data provider function."""
    return {
        "title": "Example",
        "link": "https://example.com",
        "description": "An example rsserpent plugin.",
    }
