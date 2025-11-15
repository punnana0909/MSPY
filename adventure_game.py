# This is a game where the player explores a mysterious adventure world.
# The player either can choose to explore different locations either a forest, a cave.
# Each location has its own unique challenges.
# The player has to find and reach the treasure to win the game.

# The Challenges are as follows:
# Forest: The player has to solve a riddle to find the hidden path.
# Cave: The player has to fight a monster to get the treasure.

# The player starts with 3 health points. If the player loses all health points, the game is over.

# Print a big welcome banner for the game
def print_welcome_banner(player_name):
    banner = """
    *************************************
    *                                   *
    *      WELCOME TO ADVENTURE GAME    *
    *                                   *
    *************************************
    """
    print(banner)
    print(f"Hello, {player_name}! You find yourself in a mysterious world filled with adventure and danger to discover the treasure.")

# Print a big end game banner for the game
def print_end_game_banner():
    banner = """
    *************************************
    *                                   *
    *          CONGRATULATIONS!         *
    *       YOU HAVE FOUND THE TREASURE!*
    *                                   *
    *************************************
    """
    print(banner)


# start the game by calling this function.
# This function collects user name.
def start_game():
    health = 3

    # Asks the name of the player
    player_name = input("Enter your name, brave adventurer: ")
    print_welcome_banner(player_name)

    # Prompt the player to choose (explore a forest or enter a cave)
    choice = input("Do you want to explore the Forest or enter the Cave? (Type 'forest' or 'cave'): ").lower()

    # starting the chosen adeventure
    if choice == 'forest':
        print("\n")
        print("You have chosen to explore the Forest.")
        print("To find the hidden path, you must solve this riddle:")
        print("\n")
        forest_path(player_name)
    elif choice == 'cave':
        print("\n")
        print("You have chosen to enter the Cave.")
        print("A monster appears! You must fight it.")
        print("\n")
        cave_path(player_name)
    else:
        print("Invalid choice. Please choose 'forest' or 'cave'.")
        return

# Forest path game implemetation is here.
# This function produces the user with forest path challenges.
# This method should provide options to the user to follow a river or climb a tree.
def forest_path(player_name):

    # Prompt the player to choose (explore a forest or enter a cave)
    forestChallenge = input(f"{player_name}, do you want to follow the River or climb a Tree? (Type 'river' or 'tree'): ").lower()

    # starting the chosen adeventure
    if forestChallenge == 'river':
        # For the river adventure, the playerr has to answer 4 riddles correctly as he follows the river.
        # Once all the answers are correct, the player reaches the treasure.
        print(f"{player_name}, you chose to follow the River. After a long walk, you find the hidden path and reach the treasure. You win!")
        print("\n")
        
        total = 4
        solved = 0

        def print_progress(solved_count):
            bar = '[' + '#' * solved_count + '-' * (total - solved_count) + ']'
            print("\n" + "-" * 40)
            print(f"{player_name}'s Progress: {bar} {solved_count}/{total} riddles solved")
            print("-" * 40 + "\n")

        # Riddle 1
        print(f"Riddle 1 for {player_name}: What has to be broken before you can use it?")
        answer1 = input("Your answer: ").lower()
        if answer1 == 'egg':
            solved += 1
            print(f"Correct, {player_name}! You move further along the river.")
            print_progress(solved)
        else:
            print(f"Wrong answer, {player_name}! You lost 1 health point.")
            return

        # Riddle 2
        print(f"Riddle 2 for {player_name}: I’m tall when I’m young, and I’m short when I’m old. What am I?")
        answer2 = input("Your answer: ").lower()
        if answer2 == 'candle':
            solved += 1
            print(f"Correct, {player_name}! You move further along the river.")
            print_progress(solved)
        else:
            print(f"Wrong answer, {player_name}! You lost 1 health point.")
            return

        # Riddle 3
        print(f"Riddle 3 for {player_name}: What month of the year has 28 days?")
        answer3 = input("Your answer: ").lower()
        if answer3 == 'all':
            solved += 1
            print(f"Correct, {player_name}! You move further along the river.")
            print_progress(solved)
        else:
            print(f"Wrong answer, {player_name}! You lost 1 health point.")
            return

        # Riddle 4
        print(f"Riddle 4 for {player_name}: What is full of holes but still holds water?")
        answer4 = input("Your answer: ").lower()
        if answer4 == 'sponge':
            solved += 1
            print(f"Correct, {player_name}! You have answered all riddles correctly and reached the treasure. You win!")
            print_progress(solved)
        else:
            print(f"Wrong answer, {player_name}! You lost 1 health point.")
            return
        
        # Check the End of river adventure
        # Print the End Game banner
        print_end_game_banner()


    elif forestChallenge == 'tree':
        # For the tree adventure, the player has to reach the tree top before losing all health points.
        # The player has to answer 5 questions correctly to reach the top of the tree.
        # For every correct answer, the player moves up one level.
        # For every wrong answer, the player loses 1 health point. The player starts with 3 health points.
        print(f"{player_name}, you chose to climb the Tree. Unfortunately, you slipped and fell, losing all your health points. Game Over!")

        # Start of tree climbing adventure
        health = 3
        level = 0
        total_levels = 5

        #Questions to be asked while climbing the tree are in a list here.
        questions = ['What is 5 + 3?','What is the capital of France?','What color do you get when you mix red and white?','What is the largest planet in our solar system?','What is the boiling point of water in Celsius?']
        answers = ['8', 'paris', 'pink', 'jupiter', '100']
        
        def print_tree_progress(current_level):
            bar = '[' + '#' * current_level + '-' * (total_levels - current_level) + ']'
            print("\n" + "-" * 40)
            print(f"{player_name}'s Tree Climbing Progress: {bar} Level {current_level}/{total_levels}")
            print("-" * 40 + "\n")
        while health > 0 and level < total_levels:
            print_tree_progress(level)
            print(f"Question for {player_name}: {questions[level]}")
            answer = input("Your answer: ").lower()
            if answer == answers[level]:
                level += 1
                print(f"Correct, {player_name}! You climb higher up the tree.")
            else:
                health -= 1
                print(f"Wrong answer, {player_name}! You lost 1 health point. Remaining health: {health}")
        if level == total_levels:
            print(f"Congratulations, {player_name}! You have reached the top of the tree and found the treasure. You win!")
            print_end_game_banner()
    else:
        print("Invalid choice. Please choose 'river' or 'tree'.")
        return
    

# Cave path game implemetation is here.
# This function produces the user with cave path challenges.
# This method provide player with options to light a torch or sneak past the monster in the dark.
def cave_path(player_name):

    # Prompt the player to choose to light a torch or sneak past the monster
    caveChallenge = input(f"{player_name}, do you want to light a Torch or sneak past the Monster? (Type 'torch' or 'sneak'): ").lower()

    # starting the chosen adeventure
    if caveChallenge == 'torch':
        print(f"{player_name}, you chose to light a Torch. The light scares the monster away, and you find the treasure. You win!")

        # The player chose to light a torch and found the treasure.
        # In the process, the player needs to fight a monster.
        # The player is provided with 3 health points.
        # For every wrong anser, the player loses 1 health point.
        # To defeat the monster, the player has to answer 5 questions correctly.
        # Once the player defeats the monster, he reaches the treasure.

        # Question and answers for fighting the monster are in a dictionary here.
        questions = {
            'What is 2 + 2?': '4',
            'What is the capital of Italy?': 'rome',
            'What color do you get when you mix blue and yellow?': 'green',
            'What is the smallest prime number?': '2',
            'What planet is known as the Red Planet?': 'mars'
        } 
        health = 3
        correct_answers = 0
        total = len(questions)
        def print_progress(correct):
            bar = '[' + '#' * correct + '-' * (total - correct) + ']'
            print("\n" + "-" * 40)
            print(f"{player_name}'s Progress: {bar} {correct}/{total} riddles solved")
            print("-" * 40 + "\n")

        for question, answer in questions.items():
            if health <= 0:
                print(f"Sorry, {player_name}, you have lost all your health points. Game Over!")
                return
            # show progress separator before each riddle
            print_progress(correct_answers)
            print(f"Question for {player_name}: {question}")
            player_answer = input("Your answer: ").lower()
            if player_answer == answer:
                correct_answers += 1
                print(f"Correct, {player_name}! You hit the monster.")
            else:
                health -= 1
                print(f"Wrong answer, {player_name}! You lost 1 health point. Remaining health: {health}")
            # show progress separator after each riddle
            print_progress(correct_answers)
        
        if correct_answers == len(questions):
            print(f"Congratulations, {player_name}! You have defeated the monster and found the treasure. You win!")
    elif caveChallenge == 'sneak':
        print(f"{player_name}, you chose to sneak past the Monster.")

        # The player chose to sneak past the monster.
        # The player has to answer 5 questions correctly to sneak past the monster.
        # For every wrong answer, the player loses 1 health point. The player starts with 3 health points.
        health = 3
        questions = ['What is 10 - 4?','What is the capital of Germany?','What color do you get when you mix red and blue?','What is 7 multiplied by 6?','What is the freezing point of water in Celsius?']
        answers = ['6', 'berlin', 'purple', '42', '0']
        total = len(questions)
        correct = 0

        def print_progress(correct_count):
            bar = '[' + '#' * correct_count + '-' * (total - correct_count) + ']'
            print("\n" + "-" * 40)
            print(f"{player_name}'s Sneak Progress: {bar} {correct_count}/{total} riddles solved")
            print("-" * 40 + "\n")

        for i in range(total):
            if health <= 0:
                print(f"Sorry, {player_name}, you have lost all your health points. Game Over!")
                return

            print_progress(correct)
            print(f"Question for {player_name}: {questions[i]}")
            answer = input("Your answer: ").lower()
            if answer == answers[i]:
                correct += 1
                print(f"Correct, {player_name}! You sneak past the monster.")
            else:
                health -= 1
                print(f"Wrong answer, {player_name}! You lost 1 health point. Remaining health: {health}")
            print_progress(correct)

        if correct == total:
            print(f"Congratulations, {player_name}! You have successfully snuck past the monster and found the treasure. You win!")
    else:
        print("Invalid choice. Please choose 'torch' or 'sneak'.")
        return
    
    # Print the End Game banner
    print_end_game_banner()

# Main loop to allow restarting the game after completion
def main():
    while True:
        start_game()
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again in ('y', 'yes'):
            print("\nRestarting game...\n")
            continue
        else:
            print("Thanks for playing! Goodbye.")
            break

# Start the adventure game loop
if __name__ == "__main__":
    main()