import json

# Read JSON file
def read_json(file_path):
    """Read JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_emails(data):
    """Extract emails from the JSON data."""
    emails = []
    for entry in data:
        if 'Email' in entry:
            emails.append(entry['Email'])
    return emails

def write_emails_to_file(emails, output_file):
    """Write the extracted emails to a text file."""
    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')

def main():
    # Load the JSON data
    json_file_path = input("Enter file path: ")

    try:
        data = read_json(json_file_path)
    except Exception as e:
        print(f"Error: {e}")
        return

    # Extract emails
    emails = extract_emails(data)

    # Write emails to a text file
    output_file = 'emails.txt'
    write_emails_to_file(emails, output_file)
    print(f"Emails written to {output_file}.")

if __name__ == "__main__":
    main()
