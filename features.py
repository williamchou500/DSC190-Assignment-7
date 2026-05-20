from pathlib import Path
import pandas as pd


INPUT = Path("data/transformed/events.csv")
OUTPUT = Path("data/features/events.csv")


def main():
    df = pd.read_csv(INPUT)

    df["duration_minutes"] = (
        pd.to_numeric(df["duration_seconds"])
        / 60
    )

    dates = pd.to_datetime(df["date"])

    df["weekday"] = dates.dt.day_name()

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        OUTPUT,
        index=False,
    )


if __name__ == "__main__":
    main()