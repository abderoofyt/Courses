import random

# Step 1: Get user input for their own joke
setup = input("Enter the setup for your joke: ")
misdirection = input("Enter the misdirection: ")
punchline = input("Enter the punchline: ")

# List of joke formats using dynamic inputs
jokes = [
    # Knock-Knock Joke Variations
    f"Knock, knock.\n- Who's there?\n{setup}.\n- {setup} who?\n{setup}! {misdirection}! But wait, {punchline}! 😭💻",
    f"Knock, knock.\n- Who's there?\nIt's {setup}.\n- {setup} who?\nJust wait for it… {misdirection}, and the punchline? {punchline}! 😆",
    f"Knock, knock.\n- Who's there?\nIt's your worst nightmare: {setup}.\n- {setup} who?\nWell, you thought you knew... but {misdirection}. Here comes {punchline}! 🎉",
    
    # Observation Joke Variations
    f"{setup}? You might think {misdirection}, but nope—here's the plot twist: {punchline}! 📡📉",
    f"Why does {setup} always lead to {misdirection}? Well, not really, because {punchline}! 🤯",
    f"Ever noticed how {setup} always gets {misdirection}? But you don't expect {punchline} coming! 😜",
    f"{setup}… You'd expect {misdirection}, but actually the punchline is: {punchline}! 🚀",
    
    # Wordplay (Pun) Joke Variations
    f"Do you get {setup}? {misdirection}… you probably don't, but {punchline}! 🤓👓",
    f"{setup}, huh? Well, {misdirection}… but the real zinger is: {punchline}! 💻",
    f"Here's a pun for you: {setup}? You'll think {misdirection}, but here's the real punchline: {punchline}! 💥",
    
    # Dad Joke Variations
    f"Why did the programmer bring a ladder to work?\nBecause {misdirection}, and here's the punchline: {punchline}! 🌩️",
    f"I've got a UDP joke, but {misdirection}. Wait, wait—here's the punchline: {punchline}! 😆",
    f"Why don't skeletons fight each other?\nBecause {misdirection}, and the punchline is: {punchline}! 🦴",
    
    # Dark Humor Variations
    f"Here's a little dark humor: {setup}, but you'll think {misdirection}. But nope, the punchline is: {punchline}! 🖤",
    f"I told my friend a joke about {setup}... {misdirection}—and the punchline is: {punchline}! 😈",
    f"Ever heard of {setup}? You thought {misdirection}, but the truth is, the punchline is: {punchline}! 💀",
    
    # Story Joke Variations
    f"Once upon a time, {setup} went into a bar.\nThe bartender asked, 'What can I get you?'\n{misdirection}, but the punchline is: {punchline}! 🍻💻",
    f"A developer walks into a bar… {misdirection}, but wait for the twist: {punchline}! 🍸💻",
    f"Imagine a world where {setup} happens, and everyone is like {misdirection}, but the punchline is: {punchline}! 😜",
    f"So, {setup} enters a coffee shop, and the barista says: ‘You won't believe this, but {misdirection}—and the punchline is: {punchline}! ☕💻",
    
    # Absurd / Nonsense Jokes
    f"Here's the thing: {setup} went {misdirection}, but the only explanation I have is: {punchline}! 🤪",
    f"Why do {setup} keep trying {misdirection}? I don't know, but the punchline is: {punchline}! 😂",
]
# Add the user's own joke version based on inputs
user_jokes = [
    f"{setup}... You might think {misdirection}, but the punchline is: {punchline}! 😜",
    f"Ever wondered {setup}? You'd think {misdirection}, but nope, here's {punchline}! 🎉",
    f"What's the deal with {setup}? You'd expect {misdirection}, but the punchline is: {punchline}! 🤣",
]

jokes.extend(user_jokes)

while True:
    #Use Random.Choice()
    random_joke = random.choice(jokes)  # Select a random joke
    print("\nHere's a randomly selected joke for you:\n")
    print(random_joke)

    # Ask if they want to regenerate
    choice = input("\nNot happy with the joke? (yes to regenerate, no to stop): ").strip().lower()
    if choice == "no":
        print("\nGreat! Enjoy your joke. 😆")
        break  # Exit loop if they are happy
