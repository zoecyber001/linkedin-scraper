# LinkedIn Email Script


Clone this directory
```bash
git clone https://www.github.com/zoecyber001/linkedin-scraper
cd linkedin-scrapper

```

Or 
Download the Zipped file

## Setup Instructions
Create an Account on : https://console.apify.com
1. **Create a Virtual Environment**:
   ```bash
   pip3 install --user virtualenv
   python3 -m venv linkedin_env
   source linkedin_env/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install apify-client
   ```

## Running the Script

1. Run the main script:
   ```bash
   python3 main.py
   ```

2. Check the Apify dashboard to monitor the script's progress.

## Extracting Emails

1. After the script has finished running, export the data from the Apify dashboard.
2. Download the JSON file containing the extracted data.
3. Run the JSON reader to extract all the emails:
   ```bash
   python3 json-reader.py 
   ```

This README provides the necessary steps to set up and run the LinkedIn email script effectively.
