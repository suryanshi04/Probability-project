import pandas as pd

# Assuming the files are uploaded to the default Colab directory
matches_file_path = 'C:/Users/SURYANSHI/OneDrive/Desktop/matches.csv'
deliveries_file_path = 'C:/Users/SURYANSHI/OneDrive/Desktop/deliveries.csv'

# Read the CSV files into DataFrames
matches_df = pd.read_csv(matches_file_path)
deliveries_df = pd.read_csv(deliveries_file_path)

# Get unique teams from 'matches' DataFrame
all_teams = pd.concat([matches_df['team1'], matches_df['team2']]).unique()

# Display all team names
print("All Teams:")
for i, team in enumerate(all_teams, start=1):
    print(f"{i}. {team}")

# Ask the user to choose two teams
team1_index = int(input("Enter the number corresponding to the first team: "))
team2_index = int(input("Enter the number corresponding to the second team: "))

selected_team1 = all_teams[team1_index - 1]
selected_team2 = all_teams[team2_index - 1]

print(f"\nSelected Teams: {selected_team1} vs {selected_team2}\n")

# Filter DataFrames for the selected teams
selected_matches_df = matches_df[((matches_df['team1'] == selected_team1) & (matches_df['team2'] == selected_team2)) |
                                  ((matches_df['team1'] == selected_team2) & (matches_df['team2'] == selected_team1))]

selected_deliveries_df = deliveries_df[((deliveries_df['batting_team'] == selected_team1) & (deliveries_df['bowling_team'] == selected_team2)) |
                                       ((deliveries_df['batting_team'] == selected_team2) & (deliveries_df['bowling_team'] == selected_team1))]

# Function to calculate win, lose, bat, and ball probabilities
def calculate_probabilities(data):
    total_matches = len(data['match_id'].unique()) if 'match_id' in data else len(data['id'].unique())
    
    win_probability = len(data[data['winner'] == selected_team1]) / total_matches
    lose_probability = len(data[data['winner'] == selected_team2]) / total_matches
    
    bat_probability = len(data[data['toss_decision'] == 'bat']) / total_matches
    ball_probability = len(data[data['toss_decision'] == 'field']) / total_matches
    
    return win_probability, lose_probability, bat_probability, ball_probability

# Calculate probabilities for matches and deliveries
win_prob_matches, lose_prob_matches, bat_prob_matches, ball_prob_matches = calculate_probabilities(selected_matches_df)
win_prob_deliveries, lose_prob_deliveries, bat_prob_deliveries, ball_prob_deliveries = calculate_probabilities(selected_deliveries_df)

# Display the results
print("Probabilities for Matches:")
print(f"Win Probability: {win_prob_matches:.2%}")
print(f"Lose Probability: {lose_prob_matches:.2%}")
print(f"Bat Probability: {bat_prob_matches:.2%}")
print(f"Ball Probability: {ball_prob_matches:.2%}")

print("\nProbabilities for Deliveries:")
print(f"Win Probability: {win_prob_deliveries:.2%}")
print(f"Lose Probability: {lose_prob_deliveries:.2%}")
print(f"Bat Probability: {bat_prob_deliveries:.2%}")
print(f"Ball Probability: {ball_prob_deliveries:.2%}")
