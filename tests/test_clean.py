from pathlib import Path

def test_clean_output_exists():
    path = Path("data/clean/data_cleaned.csv")
    assert path.exists(), "❌ Cleaned data file not found"
    

def test_clean_output_has_content():
    lines = Path("data/clean/data_cleaned.csv").read_text().splitlines()
    assert len(lines) >= 1, "❌ Cleaned file is empty"
    
