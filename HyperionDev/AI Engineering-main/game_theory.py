import itertools
import random

class Strategy:
    """Class to define a strategy with an optional memory for tit-for-tat strategies."""
    def __init__(self, name, function, memory=False):
        self.name = name
        self.function = function
        self.memory = memory  # Indicates if it needs the previous enemy choice

    def get_choice(self, previous_enemy_choice=None):
        if self.memory:
            return self.function(previous_enemy_choice)
        return self.function()

# Strategy Functions
def always_cooperate():
    return 'cooperate'

def always_undercut():
    return 'undercut'

def random_strategy():
    return random.choice(['cooperate', 'undercut'])

def tit_for_tat(previous_enemy_choice='cooperate'):
    return previous_enemy_choice

def greedy_merchant():
    """Mostly undercuts but sometimes cooperates to maintain trust."""
    return 'undercut' if random.random() < 0.8 else 'cooperate'

def cautious_investor(previous_enemy_choice='cooperate'):
    """Cooperates until betrayed, then always undercuts."""
    return 'cooperate' if previous_enemy_choice == 'cooperate' else 'undercut'

# Customer Decision Model
def customer_choice(quality_weight, price_weight, quality_score, price_score):
    """Determines if a customer prefers quality or price-based strategy."""
    total_weight = (quality_score * quality_weight) + (price_score * price_weight)
    if total_weight == 0:
        return random.choice(['cooperate', 'undercut'])
    quality_prob = (quality_score * quality_weight) / total_weight
    return 'cooperate' if random.random() < quality_prob else 'undercut'

# Game Simulation
def play_game(strategy1, strategy2, customers=100, quality_weight=0.6, price_weight=0.4, rounds=10):
    score1, score2 = 0, 0
    prev_choice1, prev_choice2 = 'cooperate', 'cooperate'

    for _ in range(rounds):
        choice1 = strategy1.get_choice(prev_choice2) if strategy1.memory else strategy1.get_choice()
        choice2 = strategy2.get_choice(prev_choice1) if strategy2.memory else strategy2.get_choice()

        # Assigning quality and price scores
        quality_score1, price_score1 = (10, 0) if choice1 == 'cooperate' else (0, 10)
        quality_score2, price_score2 = (10, 0) if choice2 == 'cooperate' else (0, 10)

        for _ in range(customers):
            customer_choice1 = customer_choice(quality_weight, price_weight, quality_score1, price_score1)
            customer_choice2 = customer_choice(quality_weight, price_weight, quality_score2, price_score2)

            if customer_choice1 == 'cooperate' and customer_choice2 == 'cooperate':
                score1 += int(customers * quality_weight / 2) + 10
                score2 += int(customers * quality_weight / 2) + 10
            elif customer_choice1 == 'cooperate' and customer_choice2 == 'undercut':
                score2 += int(customers * price_weight) + 20
            elif customer_choice1 == 'undercut' and customer_choice2 == 'cooperate':
                score1 += int(customers * price_weight) + 20
            else:
                score1 += int(customers * price_weight / 2) - 10
                score2 += int(customers * price_weight / 2) - 10

        prev_choice1, prev_choice2 = choice1, choice2

    return score1, score2

# Main Execution
def main():
    strategies = {
        'Always Cooperate': Strategy('Always Cooperate', always_cooperate),
        'Always Undercut': Strategy('Always Undercut', always_undercut),
        'Random': Strategy('Random', random_strategy),
        'Tit for Tat': Strategy('Tit for Tat', tit_for_tat, memory=True),
        'Greedy Merchant': Strategy('Greedy Merchant', greedy_merchant),
        'Cautious Investor': Strategy('Cautious Investor', cautious_investor, memory=True)
    }

    results = {name: 0 for name in strategies}

    for (name1, strategy1), (name2, strategy2) in itertools.combinations(strategies.items(), 2):
        score1, score2 = play_game(strategy1, strategy2)
        results[name1] += score1
        results[name2] += score2
        print(f"{name1} vs {name2}: {score1} - {score2}")

    ranked_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    print("\nFinal Rankings:")
    for rank, (name, score) in enumerate(ranked_results, 1):
        print(f"{rank}. {name} - {score} points")

if __name__ == "__main__":
    main()
