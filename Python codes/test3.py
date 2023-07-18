
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def distributeCoins(root):
    moves = [0]  # Number of moves required to distribute coins

    def dfs(node):
        if not node:
            return 0

        left_excess = dfs(node.left)   # Excess coins from the left subtree
        right_excess = dfs(node.right)  # Excess coins from the right subtree

        total_excess = left_excess + right_excess + node.val - 1  # Total excess coins at the current node
        moves[0] += abs(total_excess)  # Accumulate the number of moves required

        return total_excess

    dfs(root)
    return moves[0]

root = [3,0,0]








