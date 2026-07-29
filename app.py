"""Application entry point for the Career Intelligence Platform."""

from src.config import RAW_DATA

from src.extract.csv_loader import load_data
from src.profile.reports import generate_profile
from src.clean.clean import clean_data
from src.transform.mapper import build_documents
from src.validation.validator import (
    validate_documents,
    get_valid_documents,
)
from src.database.repository import (
    insert_documents,
    count_documents,
)


def main() -> None:
    """Application entry point."""

    print("\n" + "=" * 60)
    print("CAREER INTELLIGENCE PLATFORM")
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


    #test to see if the columns are being read in correctly
    #print(df.columns.tolist())

    print("\nMapping Career Intelligence documents...")
    documents = build_documents(df)

    print(f"✓ Created {len(documents)} documents.")

    print("\nValidating documents...")
    validation_results = validate_documents(documents)

    valid_documents = get_valid_documents(documents)

    print(f"✓ Valid documents : {len(valid_documents)}")
    print(f"✗ Invalid documents: {len(documents) - len(valid_documents)}")

    invalid = [
    result
    for result in validation_results
    if not result["valid"]
    ]

    if invalid:

        print("\nValidation errors:\n")

        for result in invalid[:5]:

            print(f"Document {result['index']}")

            for error in result["errors"]:
                print(f"  - {error}")


    if valid_documents:

        print("\nImporting validated documents into MongoDB...")

        inserted, duplicates = insert_documents(valid_documents)

        print(f"✓ Inserted {inserted} new documents.")
        print(f"✓ Skipped {duplicates} duplicate documents.")
        print(f"✓ Total documents in MongoDB: {count_documents()}")

    else:

        print("\nNo valid documents available for import.")
    
    print("\nProcess complete.")

if __name__ == "__main__":
    main()