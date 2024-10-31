from tweety import Twitter
import csv

# Initialize the Twitter session
app = Twitter("session")

# Attempt to sign in with the provided credentials
try:
    app.sign_in("username", "password")
except Exception as e:
    if "Check your email" in str(e):
        # Handle the case where additional verification is needed
        print("Additional verification required. Check your email.")

        # Assume you have received the confirmation code via email and stored it in a variable
        confirmation_code = input("Enter the confirmation code: ")

        try:
            # Try signing in again with the confirmation code
            app.sign_in("Username", "Password", confirmation_code)
        except Exception as e:
            # If there's an issue with the confirmation code or sign-in process, handle it appropriately
            print("Error: Unable to sign in. Please check your credentials and try again.")
            exit()
    else:
        # Handle other exceptions that may occur during sign-in
        print("Error:", e)
        exit()

# Continue with fetching tweets and writing to CSV
target_username = "IntDiabetesFed"
user = app.get_user_info(target_username)
all_tweets = app.get_tweets(user)

# Define the filename for the CSV file
csv_filename = "my_tweets.csv"

# Open the CSV file in write mode
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header row
    csv_writer.writerow(['Tweet ID', 'Author ID', 'Author Username', 'Author Name', 'Verified', 'Created On'])

    # Write each tweet's details into the CSV file row by row
    for tweet in all_tweets:
        csv_writer.writerow([tweet.id, tweet.author.id, tweet.author.username, tweet.author.name, tweet.author.verified, tweet.created_on])

print("CSV file created successfully.")

