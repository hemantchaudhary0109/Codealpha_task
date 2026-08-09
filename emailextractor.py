import re


def extract_emails(input_file, output_file):
    """
    Extract email addresses from a text file
    and save them to another file.
    """

    try:
        # Read input file
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Regular expression for email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        # Find all emails
        emails = re.findall(email_pattern, text)

        # Remove duplicate emails
        emails = sorted(set(emails))

        # Save emails
        with open(output_file, "w", encoding="utf-8") as file:

            for email in emails:
                file.write(email + "\n")

        print("=" * 45)
        print("       EMAIL EXTRACTION COMPLETE")
        print("=" * 45)

        print(f"\nEmails found: {len(emails)}")
        print(f"Output saved to: {output_file}")

        if emails:
            print("\nExtracted Emails:")

            for email in emails:
                print("-", email)

        else:
            print("No email addresses were found.")

    except FileNotFoundError:
        print(f"Error: {input_file} was not found.")

    except Exception as error:
        print("An unexpected error occurred:", error)


def main():

    print("=" * 45)
    print("         EMAIL EXTRACTOR")
    print("=" * 45)

    input_file = input(
        "\nEnter input filename "
        "(press Enter for input.txt): "
    ).strip()

    if input_file == "":
        input_file = "input.txt"

    output_file = input(
        "Enter output filename "
        "(press Enter for emails.txt): "
    ).strip()

    if output_file == "":
        output_file = "emails.txt"

    extract_emails(input_file, output_file)


if __name__ == "__main__":
    main()