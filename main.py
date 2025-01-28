from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# Prepare the Actor input
run_input = {
    "Keyword": "Web",
    "social_network": "linkedin.com/",
    "Country": "www",
    "Email_Type": "0",
    "proxySettings": { "useApifyProxy": False },
}

# Run the Actor and wait for it to finish
run = client.actor("1KoCTvsASIAXqkvY7").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
