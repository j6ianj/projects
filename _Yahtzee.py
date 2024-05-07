print('Yahtzee Game')
import random

def roll_die():
    return random.randint(1, 6)

def draw_die(number):
    dice_faces = [
        "+-------+\n|       |\n|   ●   |\n|       |\n+-------+",  # Face 1
        "+-------+\n| ●     |\n|       |\n|     ● |\n+-------+",  # Face 2
        "+-------+\n| ●     |\n|   ●   |\n|     ● |\n+-------+",  # Face 3
        "+-------+\n| ●   ● |\n|       |\n| ●   ● |\n+-------+",  # Face 4
        "+-------+\n| ●   ● |\n|   ●   |\n| ●   ● |\n+-------+",  # Face 5
        "+-------+\n| ●   ● |\n| ●   ● |\n| ●   ● |\n+-------+"   # Face 6
    ]
    return dice_faces[number - 1]

def choose_score(option, rolls):
    score = 0
    if option in ["ones", "twos", "threes", "fours", "fives", "sixes"]:
        for num in rolls:
            if option == "ones" and num == 1:
                score += 1
            elif option == "twos" and num == 2:
                score += 2
            elif option == "threes" and num == 3:
                score += 3
            elif option == "fours" and num == 4:
                score += 4
            elif option == "fives" and num == 5:
                score += 5
            elif option == "sixes" and num == 6:
                score += 6
    elif option == "three_of_a_kind":
        if any(rolls.count(x) >= 3 for x in rolls):
            score += sum(rolls)
    elif option == "four_of_a_kind":
        if any(rolls.count(x) >= 4 for x in rolls):
            score += sum(rolls)
    elif option == "full_house":
        if sorted(set(rolls), key=lambda x: rolls.count(x), reverse=True) == [2, 3]:
            score += 25
    elif option == "small_straight":
        if sorted(set(rolls)) in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]:
            score += 30
    elif option == "large_straight":
        if sorted(set(rolls)) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]:
            score += 40
    elif option == "yahtzee":
        if len(set(rolls)) == 1:
            score += 50
    elif option == "chance":
        score += sum(rolls)
    return score

def main():
    scoring_options = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes', 'three_of_a_kind', 'four_of_a_kind', 'full_house', 'small_straight', 'large_straight', 'chance', 'yahtzee']
    total_score = 0
    while len(scoring_options) > 0:
        rolls = []
        turns = 0
        while turns < 3:
            print("Roll " + str(turns+1) + ":")
            i = len(rolls)  # Start index for new rolls
            while i < 5:
                roll = roll_die()
                rolls.append(roll)
                i += 1
            for x in rolls:  # Display all rolls
                print(draw_die(x), end=" ")
            print()
            turns += 1
            if turns < 3:
                while True:  # Loop until valid reroll option is provided
                    reroll_option = input("Would you like to reroll any dice? (y/n): ")
                    if reroll_option.lower() in ['y', 'n']:
                        break
                    else:
                        print("Invalid option. Please enter 'y' or 'n'.")
                if reroll_option.lower() == 'n':
                    break
                elif reroll_option.lower() == 'y':
                    while True:  # Loop until valid reroll indices are provided
                        reroll_indices = input("Enter the indices of dice you want to reroll (space-separated): ")
                        reroll_indices = reroll_indices.split()
                        reroll_indices = [int(index) for index in reroll_indices]
                        if all(index >= 0 and index < 5 for index in reroll_indices):
                            break
                        else:
                            print("Invalid indices. Please enter valid indices.")
                    for index in reroll_indices:
                        rolls[index] = roll_die()  # Replace only the specified indices
                    print("Rerolled dice:")
                    for x in rolls:  # Display all rolls after rerolls
                        print(draw_die(x), end=" ")
                    print()

        print("Choose a scoring option:")
        for option in scoring_options:
            print(option)
        chosen_option = input("Enter your choice: ")
        while chosen_option not in scoring_options:  # Check if input is valid
            print("Invalid option. Please choose a valid scoring option.")
            chosen_option = input("Enter your choice: ")
        score = choose_score(chosen_option, rolls)
        total_score += score
        print("Score for " + chosen_option + ": " + str(score))
        print("Total Score: " + str(total_score))
        scoring_options.remove(chosen_option)

if __name__ == "__main__":
    main()
