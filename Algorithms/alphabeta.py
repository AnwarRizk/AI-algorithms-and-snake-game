# Alpha Beta Algorithm:

# The alpha-beta algorithm is an optimization of the minimax algorithm that reduces the number of nodes evaluated in the search tree. It maintains two values, alpha and beta, which represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of, respectively.

# The algorithm prunes branches of the search tree that are guaranteed to be worse than the current best move. This reduces the number of nodes that need to be evaluated, making the search more efficient.

def alphabeta(position, depth, alpha, beta, max_turn):
    if depth == 0 or not position[1]:  # Base case: if depth is 0 or no more child positions
        return position[0]
    
    if max_turn:
        max_eval = float('-inf')
        for child in position[1]:
            eval = alphabeta(child, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in position[1]:
            eval = alphabeta(child, depth-1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
    
position = (0, [(1, [(1, []), (2, [])]), (2, [(5, []), (4, [])])])
print('Best:', alphabeta(position, 3, float('-inf'), float('inf'), True)) # Output: 4

# Tree structure:
#           0
#         /   \
#        1     2
#       / \   / \
#      1   2 5   4