import string

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            return self.root
        else:
            self.root = self._insert(self.root, key, value)
            return self.root

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.balance_factor(node)

        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def search(self, key):
        node = self._search(self.root, key)
        if node is None:
            return None
        return node.value

    def _search(self, node, key):
        if node is None:
            return None
        elif key == node.key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)


def replace_abbreviations_optimized(tweets, abbreviations_dict):
    results = []
    avl_tree = AVLTree()
    for key, value in abbreviations_dict.items():
        avl_tree.insert(key, value)

    for sentence in tweets:
        words = sentence.split()
        for i, word in enumerate(words):
            stripped_word = word.strip(string.punctuation)
            make_lower = stripped_word.lower()
            node = avl_tree.search(make_lower)
            if node is not None:
                if i > 0 and words[i-1][-1] == '.':
                    words[i] = node.capitalize() + word[len(stripped_word):]
                else:
                    words[i] = node + word[len(stripped_word):]
        results.append(" ".join(words))
    return results
