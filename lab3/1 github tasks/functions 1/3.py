"""Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):"""

def solve(numheads, numlegs):
    # Let chickens be x and rabbits be y
    # We have the equations:
    # x + y = numheads  (1) - total heads
    # 2x + 4y = numlegs  (2) - total legs

    # From (1), we can express y in terms of x:
    # y = numheads - x

    # Substitute y in (2):
    # 2x + 4(numheads - x) = numlegs
    # 2x + 4numheads - 4x = numlegs
    # -2x + 4numheads = numlegs
    # 2x = 4numheads - numlegs
    # x = (4numheads - numlegs) / 2

    chickens = (4 * numheads - numlegs) // 2
    rabbits = numheads - chickens

    return chickens, rabbits

# Example usage:
heads = 35
legs = 94
chickens, rabbits = solve(heads, legs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")
