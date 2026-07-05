
import numpy as np

# Runs scored in 10 matches
scores = np.array([45, 60, 30, 100, 75, 82, 55, 120, 40, 90])

# Balls faced in each match
balls = np.array([35, 50, 25, 80, 60, 65, 45, 95, 30, 70])

print("CRICKET PERFORMANCE ANALYZER")
print("-" * 40)

print("Scores:", scores)

# Basic Statistics
total_runs = np.sum(scores)
average_runs = np.mean(scores)
highest_score = np.max(scores)
lowest_score = np.min(scores)

print("\nTotal Runs:", total_runs)
print("Average Runs:", round(average_runs, 2))
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)

# Half Centuries
half_centuries = scores[scores >= 50]
print("\nHalf Centuries:", len(half_centuries))

# Centuries
centuries = scores[scores >= 100]
print("Centuries:", len(centuries))

# Best Match
best_match = np.argmax(scores)
print("\nBest Match Number:", best_match + 1)

# Scores Above Average
above_average = scores[scores > average_runs]
print("Scores Above Average:", above_average)

# Strike Rate
strike_rates = (scores / balls) * 100

print("\nStrike Rates:")
for i in range(len(strike_rates)):
    print(f"Match {i+1}: {strike_rates[i]:.2f}")

overall_strike_rate = (total_runs / np.sum(balls)) * 100

print("\nOverall Strike Rate:", round(overall_strike_rate, 2))

# Consistency Analysis
std_dev = np.std(scores)

print("Performance Consistency (Standard Deviation):",
      round(std_dev, 2))

if std_dev < 25:
    print("Player is Consistent")
else:
    print("Player is Inconsistent")