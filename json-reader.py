import json import os

def read_json(file_path): """Read JSON data from a file.""" with open(file_path, 'r', encoding='utf-8') as file: return json.load(file)

def extract_emails(data): """Extract emails from the JSON data.""" return [entry['Email'] for entry in data if 'Email' in entry]

def get_next_filename(base_name): """Generate the next available filename with an increment.""" if not os.path.exists(base_name): return base_name

counter = 1
while os.path.exists(f"emails-{counter}.txt"):
    counter += 1

return f"emails-{counter}.txt"

def write_emails_to_file(emails, output_file): """Write the extracted emails to a text file.""" with open(output_file, 'w', encoding='utf-8') as file: for email in emails: file.write(email + '\n')

def main(): json_file_path = input("Enter file path: ")

try:
    data = read_json(json_file_path)
except Exception as e:
    print(f"Error reading JSON file: {e}")
    return

emails = extract_emails(data)
if not emails:
    print("No emails found in the JSON file.")
    return

output_file = get_next_filename("emails.txt")
write_emails_to_file(emails, output_file)
print(f"Emails written to {output_file}.")

if name == "main": main()

