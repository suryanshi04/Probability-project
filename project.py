import pandas as pd

# Load the datasets
matches_df = pd.read_csv('C:/Users/SURYANSHI/OneDrive/Desktop/matches.csv')
deliveries_df = pd.read_csv('C:/Users/SURYANSHI/OneDrive/Desktop/deliveries.csv')

# Merge the datasets on the 'match_id' column
merged_df = pd.merge(deliveries_df, matches_df, left_on='match_id', right_on='id')

# Function to calculate win, lose, tie, bat, and ball probabilities
def calculate_probabilities(data):
    total_matches = len(data['id'].unique())
    
    win_probability = len(data[data['winner'] == data['batting_team']]) / total_matches
    lose_probability = len(data[data['winner'] == data['bowling_team']]) / total_matches
    tie_probability = len(data[data['result'] == 'tie']) / total_matches
    
    bat_probability = len(data[data['toss_decision'] == 'bat']) / total_matches
    ball_probability = len(data[data['toss_decision'] == 'field']) / total_matches
    
    return win_probability, lose_probability, tie_probability, bat_probability, ball_probability

# Get user input for the option
print("Choose an option:")
print("1. Win Probability")
print("2. Lose Probability")
print("3. Tie Probability")
print("4. Bat Probability")
print("5. Ball Probability")

option = int(input("Enter the option number: "))

# Calculate probabilities based on user input
win_prob, lose_prob, tie_prob, bat_prob, ball_prob = calculate_probabilities(merged_df)

# Display the selected probability
if option == 1:
    print(f"Win Probability: {win_prob:.2%}")
elif option == 2:
    print(f"Lose Probability: {lose_prob:.2%}")
elif option == 3:
    print(f"Tie Probability: {tie_prob:.2%}")
elif option == 4:
    print(f"Bat Probability: {bat_prob:.2%}")
elif option == 5:
    print(f"Ball Probability: {ball_prob:.2%}")
else:
    print("Invalid option. Please choose a number between 1 and 5.")
