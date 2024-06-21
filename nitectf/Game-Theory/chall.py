import random

def play_round(player_input, opponent_input):
    rules = {'CC': (1, 1), 'CD': (3, 0), 'DC': (0, 5), 'DD': (-1, -1)}
    return rules[player_input + opponent_input]

def play_tournament():
    players = ['Bot1', 'Bot2', 'Bot3', 'Bot4', 'Bot5']
    cumulative_points = 0
    rounds_played = 0

    while cumulative_points < 40 and rounds_played < 10:
        opponents = random.sample(players, 3)
        player_input = input("Enter your move (C/D): ")

        for opponent in opponents:
            opponent_input = random.choice(['C', 'D'])
            player_score, opponent_score = play_round(player_input, opponent_input)
            cumulative_points += player_score

            print(f"Round {rounds_played + 1}: {player_input}/{opponent_input} - "
                  f"You: {player_score}, {opponent}: {opponent_score}, "
                  f"Cumulative Points: {cumulative_points}")

        rounds_played += 1

    if cumulative_points >= 40:
        print("Congratulations! You reached 40 points.")
    else:
        print("Game over. You did not reach 40 points in 10 rounds.")

# Example usage:
play_tournament()
