from pathlib import Path

def test_transform_output_exists():
    path = Path("data/transformed/data_transformed.csv")
    assert path.exists(), "❌ Transformed file not found"

def test_transform_output_has_content():
    lines = Path("data/transformed/data_transformed.csv").read_text().splitlines()
    assert len(lines) >= 1, "❌ Transformed file is empty"