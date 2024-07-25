# A sorted array to a height balanced BST
# Height balanced BST is where the height of left subtree and right subtree never differs by two

def sortedArrayToBst(nums):
    if not nums:
            return None
        
    # Function to recursively build the tree
    def build_tree(left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = Node(nums[mid])
        node.left = build_tree(left, mid - 1)
        node.right = build_tree(mid + 1, right)
        return node
    
    return build_tree(0, len(nums) - 1)