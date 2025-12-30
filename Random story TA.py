import random

# --- USER INPUT ---
name = input("Enter a character name: ")
age = input("Enter the character's age: ")
place = input("Enter a place: ")
goal = input("What is the character trying to do?: ")

# --- RANDOM LISTS ---
obstacles = [
    "a giant storm blocked the path",
    "a mysterious stranger appeared",
    "they found a locked gate",
    "a wild animal started following them",
    "the ground started shaking",
    "they suddenly forgot where they were"
]

helpers = [
    "an old wizard offered help",
    "a friendly robot joined them",
    "a talking cat guided them",
    "a brave warrior teamed up with them",
    "a floating spirit protected them"
]

twists = [
    "but it turned out to be a trap",
    "but it was all part of a prophecy",
    "and they discovered a hidden power",
    "and they realized the real danger was behind them",
    "but time suddenly froze",
]

endings = [
    "In the end, they succeeded and became a legend.",
    "They failed… but learned an important lesson.",
    "They saved the world without even knowing it.",
    "Everything changed, and a new adventure began.",
    "They returned home, stronger than ever."
]

# --- RANDOM CHOICES ---
obstacle = random.choice(obstacles)
helper = random.choice(helpers)
twist = random.choice(twists)
ending = random.choice(endings)

# --- STORY ---
story = f"""
Once upon a time, {name}, who was {age} years old, lived in {place}.
One day, {name} decided they wanted to {goal}.

On their journey, {obstacle}.
Just when things looked bad, {helper} appeared.

Together they continued, {twist}.
{ending}
"""

print(story)
