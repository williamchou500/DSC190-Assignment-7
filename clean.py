from pathlib import Path
import pandas as pd


INPUT = Path("data/raw/events.csv")
OUTPUT = Path("data/clean/events.csv")

VALID_EVENT_TYPES = {
    "click",
    "view",
    "purchase",
}


def main():
    df = pd.read_csv(INPUT)

    df = df.dropna()

    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    df["duration_seconds"] = pd.to_numeric(
        df["duration_seconds"],
        errors="coerce",
    )

    df = df[df["duration_seconds"] > 0]

    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce",
    )

    df = df.dropna(subset=["timestamp"])

    df["timestamp"] = (
        df["timestamp"]
        .dt.strftime("%Y-%m-%dT%H:%M:%S")
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        OUTPUT,
        index=False,
    )


if __name__ == "__main__":
    main()