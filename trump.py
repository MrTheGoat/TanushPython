import csv
import random
import pyfiglet

# ---------- Load Cards ----------

with open("Top Trumps - Harry Potter and the Deathly Hallows Part 2.csv", "r") as file:
    all_cards = list(csv.DictReader(file))

# Ignore the first column (character name)
relevant_keys = list(all_cards[0].keys())[1:]

# Create shortcut dictionary
mapping_dict = {}

for key in relevant_keys:
    mapping_dict[key[0].upper()] = key

# Shuffle cards
random.shuffle(all_cards)

# Split between player and computer
player_cards = all_cards[1::2]
comput_cards = all_cards[0::2]

table_cards = []

chance = "player"
game_over = False


# ---------- Functions ----------

def display_card(card):

    print("\nCharacter:", card["Individual"])
    print("-" * 35)

    for key in relevant_keys:
        print(f"{key:10} : {card[key]}")


def determine_winner(player_value, comput_value, order=1):

    if player_value == comput_value:
        return "draw"

    if order == 1:

        if player_value > comput_value:
            return "player"
        else:
            return "computer"

    else:

        if player_value < comput_value:
            return "player"
        else:
            return "computer"
def categoryrank(tcard,category):
    metric= [float(card[mapping_dict[category]]) for card in all_cards]
    if category in ['M',"C","W"]:
        metricsorted=sorted(metric, reverse=True)
    else:
        metricsorted=sorted(metric )
    rank=metricsorted.index(float(tcard[mapping_dict[category]])) +1
    return rank



# ---------- Main Game ----------

while not game_over:

    print("\n--------------------------------------")
    print("Player Cards :", len(player_cards))
    print("Computer Cards:", len(comput_cards))
    print("--------------------------------------")

    player = player_cards.pop(0)
    comput = comput_cards.pop(0)

    table_cards.append(player)
    table_cards.append(comput)

    display_card(player)

    if chance == "player":

        print("\nChoose a category")

        for key in mapping_dict:
            print(key, "-", mapping_dict[key])

        choice = input("Choice: ").upper()

        key_requested = mapping_dict[choice]
        print('the rank of your card in that category is ', categoryrank(player,choice))

        chance = "computer"

    else:

        key_requested = random.choice(relevant_keys)

        print("\nComputer chose:", key_requested)

        chance = "player"

    metric_player = float(player[key_requested])
    metric_comput = float(comput[key_requested])

    # Temper → lower wins
    if key_requested == "Temper":
        winner =pyfiglet.figlet_format( determine_winner(metric_player, metric_comput, 0),font='digital')

    else:
        winner = pyfiglet.figlet_format(determine_winner(metric_player, metric_comput),font='digital' )


    print()
    print("Player", key_requested, "=", metric_player)
    print("Computer", key_requested, "=", metric_comput)
    print("Winner:", winner)

    if winner == "player":
        player_cards.extend(table_cards)
        table_cards.clear()

    elif winner == "computer":
        comput_cards.extend(table_cards)
        table_cards.clear()

    if len(player_cards) == 0:
        print("\nComputer Wins the Game!")
        game_over = True

    elif len(comput_cards) == 0:
        print("\nPlayer Wins the Game!")
        game_over = True