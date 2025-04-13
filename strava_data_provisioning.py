import pandas as pd
import requests

# Step 1: Set Strava API credentials
CLIENT_ID = "******"
CLIENT_SECRET = "*********************************"
AUTH_CODE = "********************************"

# Step 2: Exchange authorization code for an access token
token_url = f"https://www.strava.com/oauth/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&code={AUTH_CODE}&grant_type=authorization_code"

response = requests.post(token_url)
token_data = response.json()

ACCESS_TOKEN = token_data["access_token"]

print(f"Access Token: {ACCESS_TOKEN}")

# Step 3: Get all activities using the access token
activities_url = f"https://www.strava.com/api/v3/athlete/activities?access_token={ACCESS_TOKEN}"

response = requests.get(activities_url)
activities = response.json()

print(f"Retrieved {len(activities)} activities.")

df = pd.DataFrame(activities)
df.to_csv("data/strava_activities.csv", index=False)

print("Data saved to strava_activities.csv")
print(df.head())