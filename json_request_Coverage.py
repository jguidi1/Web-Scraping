import requests
import json
# API URL
url = "https://orchestrator.pgatour.com/graphql"

# GraphQL Query
query = """
query Coverage($tournamentId: ID!) {
  coverage(tournamentId: $tournamentId) {
    id
    tournamentName
    coverageType {
      ... on BroadcastAudioStream {
        streamTitle
        roundNumber
        channelTitle
        roundDisplay
        startTime
        endTime
        liveStatus
      }
    }
  }
}
"""

# Variables
variables = {
    "tournamentId": "R2025475"
}

# Headers (add your API key)
headers = {
    "Content-Type": "application/json",
    "x-api-key": "da2-gsrx5bibzbb4njvhl7t37wqyl4"  # This is the key you found
}

# Send the POST request
response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)

# Print the response data
if response.status_code == 200:
    print("Success! Here's the data:")
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")

print(json.dumps(response.json(), indent=4))

from datetime import datetime

# Extract data
tournament_name = response.json()['data']['coverage']['tournamentName']
coverage_data = response.json()['data']['coverage']['coverageType']

print(f"Tournament: {tournament_name}")

# Loop through and display non-empty coverage info
for coverage in coverage_data:
    if coverage:
        start_time = datetime.fromtimestamp(coverage['startTime'] / 1000)
        end_time = datetime.fromtimestamp(coverage['endTime'] / 1000)
        
        print(f"\nStream Title: {coverage['streamTitle']}")
        print(f"Round: {coverage['roundDisplay']} (Round {coverage['roundNumber']})")
        print(f"Channel: {coverage['channelTitle']}")
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print(f"Live Status: {coverage['liveStatus']}")
