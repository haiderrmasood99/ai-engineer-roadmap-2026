from scripts.validate_roadmap import validate


def test_roadmap_has_required_pages_and_repo_index() -> None:
    assert validate() == []
