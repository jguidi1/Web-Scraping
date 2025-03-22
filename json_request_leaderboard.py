import requests
import json

# API URL
url = "https://orchestrator.pgatour.com/graphql"

# GraphQL Query
query = """
query LeaderboardCompressedV3($leaderboardCompressedV3Id: ID!) {
  leaderboardCompressedV3(id: $leaderboardCompressedV3Id) {
    id
    payload
  }
}
"""

# Variables
variables = {
    "leaderboardCompressedV3Id": "R2025475"
}

# Headers with API key
headers = {
    "Content-Type": "application/json",
    "x-api-key": "da2-gsrx5bibzbb4njvhl7t37wqyl4"  # Keep using the same API key
}

# Send the POST request
response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)


# Commenting out the code through line 40
# Print response
if response.status_code == 200:
    print("Success! Here's the data:")
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Error {response.status_code}: {response.text}")


