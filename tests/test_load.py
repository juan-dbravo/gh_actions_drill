from pathlib import Path

def test_load_output_exists():
    path = Path("data/final/final_output.csv")
    assert path.exists(), "❌ Final output file not found"

def test_load_output_has_content():
    lines = Path("data/final/final_output.csv").read_text().splitlines()
    assert len(lines) >= 1, "❌ Final output file is empty"