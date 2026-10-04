from pathlib import Path

import pandas as pd

from clean import drop_missing

DATA = Path(__file__).parent / "penguins.csv"


def test_drop_missing_removes_nan_rows():
    df = pd.read_csv(DATA)
    assert df["body_mass_g"].isna().sum() == 2

    cleaned = drop_missing(df, ["body_mass_g"])

    assert len(cleaned) == 6
    assert cleaned["body_mass_g"].notna().all()
    assert list(cleaned.index) == [0, 1, 2, 3, 4, 5]
