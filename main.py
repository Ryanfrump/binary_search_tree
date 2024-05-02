class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                return

    def search(self, value: int) -> bool:
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def in_order_traversal(self) -> list[int]:
        result = []
        stack = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    def find_min(self) -> int:
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def find_max(self) -> int:
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def height(self) -> int:
        if not self.root:
            return 0
        queue = [self.root]
        height = 0
        while queue:
            height += 1
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return height

    def count_leaves(self) -> int:
        if not self.root:
            return 0
        count = 0
        stack = [self.root]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                count += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return count
    
    def serialize(self) -> str:
        pass

    def deserialize(self, tree: str) -> None:
        pass