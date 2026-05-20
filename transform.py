from pathlib import Path
import pandas as pd


INPUT = Path("data/clean/events.csv")
OUTPUT = Path("data/transformed/events.csv")


def main():
    df = pd.read_csv(INPUT)

    timestamps = pd.to_datetime(df["timestamp"])

    df["timestamp"] = timestamps.dt.strftime(
        "%Y-%m-%dT%H:%M:%S"
    )

    df["date"] = timestamps.dt.strftime(
        "%Y-%m-%d"
    )

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