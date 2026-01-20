import numpy as np

directions = np.array(["Left", "Right", "Straight", "Back"])
events = ["pond", "fruit yard", "mountain", "forest"]

responses = {
    "Swim": "You swim across the pond safely and continue your journey.",
    "Walk": "You walk alongside the pond, finding a safe passage.",
    "Pick Fruit": "You pick a fruit and eat it. Delicious!",
    "Explore": "You keep exploring the area and find something interesting.",
    "Hide": "You hide safely until danger passes.",
    "Ignore": "You ignore the danger and move forward cautiously.",
    "Take Pet": "You take the abandoned pet home. Such a kind heart!",
    "Leave Pet": "You leave the pet behind and continue exploring."
}


def choose(prompt, options):
    while True:
        print("\n" + prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Select an option (number): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid number. Try again!")
        except ValueError:
            print("Please enter a valid number.")


def first_stage():
    path = choose("Which path will you take?", directions)
    
    if path == "Left":
        print(f"You see a {events[0]} ahead.")
        action = choose("Do you Swim or Walk?", ["Swim", "Walk"])
    else:
        print(f"You enter a {events[1]} ahead.")
        action = choose("Do you Pick Fruit or Explore?", ["Pick Fruit", "Explore"])
    
    print(responses[action])
    return path, action

def second_stage():
    action = choose("You hear a growl. Do you Hide or Ignore?", ["Hide", "Ignore"])
    print(responses[action])
    return action

def third_stage():
    action = choose("You find an abandoned pet. Do you Take it or Leave it?", ["Take Pet", "Leave Pet"])
    print(responses[action])
    return action

def play_game():
    print("\n--- Welcome to Adventure Game! ---")
    path1, action1 = first_stage()
    action2 = second_stage()
    action3 = third_stage()
    
    print("\n--- Game Summary ---")
    print(f"Path chosen: {path1}")
    print(f"First action: {action1}")
    print(f"Second action: {action2}")
    print(f"Third action: {action3}")

def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay == "no":
            print("Thanks for playing! Goodbye!")
            break
        elif replay != "yes":
            print("Invalid input, exiting game.")
            break

main()