# Minimax algorithm:

# The minimax algorithm is a decision rule used in two-player games to minimize the possible loss for a worst-case scenario. It is used to find the best move for the computer player in games such as chess, checkers, tic-tac-toe, and others.

# The algorithm evaluates the game tree by recursively exploring the possible moves of the players. It assumes that the opponent will make the best move possible, and the player will make the best move for themselves.

def minmax(position, depth, max_turn):
    if depth == 0 or not position[1]:  # Base case: if depth is 0 or no more child positions
        return position[0]
    
    if max_turn:
        max_eval = float('-inf')
        for child in position[1]:
            eval = minmax(child, depth-1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for child in position[1]:
            eval = minmax(child, depth-1, True)
            min_eval = min(min_eval, eval)
        return min_eval
    
position = (0, [(1, [(1, []), (2, [])]), (2, [(5, []), (4, [])])])
print('Best:', minmax(position, 3, True)) # Output: 4

# Tree structure:
#           0 max
#         /   \
#        1     4  min
#       / \   / \
#      1   2 5   4
