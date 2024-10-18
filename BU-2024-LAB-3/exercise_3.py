import random

choices = ["Heads", "Tails"]
results = random.choices(choices, k=100)

winning_results = {
    "random": 0,
    "heads": 0,
    "tails": 0    
}

for i in range(100):
    result = random.choice(choices)
    random_value = random.random()

    if random.choice(choices) == result:
        winning_results["random"] += 1

    if result == "Heads" and random_value < 0.5:
        winning_results["heads"] += 1

    if result == "Tails" and random_value >= 0.5:
        winning_results["tails"] += 1

print(f"random={winning_results["random"]}, heads={winning_results["heads"]}, tails={winning_results["tails"]}")

best_strategy = "N/A"

for key, value in winning_results.items():
    if value > winning_results.get(best_strategy, 0):
        best_strategy = key

print(f"The best strategy was {best_strategy}")
