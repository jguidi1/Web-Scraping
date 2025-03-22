import requests
import json

# Define the GraphQL query
query = """
query LeaderboardLegend($tournamentId: ID!, $odds: Boolean!) {
  leaderboardLegend(tournamentId: $tournamentId, odds: $odds) {
    tournamentId
    odds
    informationSections {
      title
      sponsorImages {
        logo
        logoDark
        accessibilityText
        link
      }
      items {
        ... on Abbreviations {
          __typename
          key
          title
          description
        }
        ... on Legend {
          __typename
          title
          icon
          text
          subText
          iconUrl
        }
      }
    }
  }
}
"""

# Define the variables for the query
variables = {
    "tournamentId": "R2025475",  # Replace with actual tournament ID
    "odds": False
}

# Set the GraphQL endpoint
url = "https://your-graphql-endpoint.com/graphql"  # Replace with the actual endpoint

# Send the POST request to the GraphQL server
response = requests.post(url, json={'query': query, 'variables': variables})

# Check for a successful response
if response.status_code == 200:
    data = response.json()
    
    # Extract leaderboard information
    leaderboard = data.get("data", {}).get("leaderboardLegend", {})
    tournament_id = leaderboard.get("tournamentId")
    odds = leaderboard.get("odds")
    information_sections = leaderboard.get("informationSections", [])
    
    print(f"Tournament ID: {tournament_id}")
    print(f"Odds: {odds}")
    for section in information_sections:
        print(f"Section Title: {section['title']}")
        for item in section.get("items", []):
            if item.get("__typename") == "Abbreviations":
                print(f"Abbreviation Key: {item['key']}, Title: {item['title']}, Description: {item['description']}")
            elif item.get("__typename") == "Legend":
                print(f"Legend Title: {item['title']}, Icon: {item['icon']}, Text: {item['text']}, SubText: {item['subText']}, Icon URL: {item['iconUrl']}")
else:
    print(f"Error: {response.status_code}")
