
import pandas as pd

def test_filtering():
    df = pd.DataFrame({
        "A": [1, 2, 3, 4],
        "B": [10, 20, 30, 40]
    })

    result = df[df["A"] > 2]

    assert len(result) == 2


def test_groupby():
    df = pd.DataFrame({
        "group": ["A", "A", "B", "B"],
        "value": [1, 3, 2, 4]
    })

    result = df.groupby("group")["value"].mean()

    assert result["A"] == 2
    assert result["B"] == 3


def test_sorting():
    df = pd.DataFrame({
        "A": [3, 1, 2]
    })

    result = df.sort_values("A")

    assert list(result["A"]) == [1, 2, 3]
