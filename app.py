"""Application entry point for the Career Intelligence Platform."""

from config import RAW_DATA

from src.extract.csv_loader import load_data
from src.profile.reports import generate_profile
from clean.clean import clean_data


def main() -> None:
    """Application entry point."""

    print("\n" + "=" * 60)
    print("NHS CAREER INTELLIGENCE PLATFORM")
    print("=" * 60)

    print("\nLoading dataset...")
    df = load_data(RAW_DATA)

    print("✓ Dataset loaded successfully.")

    print("\nGenerating data profile...")
    generate_profile(df)

    choice = input("\nApply cleaning suggestions? (Y/N): ").strip().lower()

    if choice == "y":
        print("\nCleaning dataset...")
        df = clean_data(df)

        print("✓ Cleaning complete.")

        print("\nUpdated data profile...")
        generate_profile(df)

    print("\nProcess complete.")


if __name__ == "__main__":
    main()