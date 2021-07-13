class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.end_of_word = False
        self.counter = 1

def add(root, word):
    node = root
    for char in word:
        char_found = False
        for child in node.children:
            if child.char == char:
                node.counter += 1
                node = child
                char_found = True
                break
        if not char_found:
            new_node = TrieNode(char)
            node.children.append(char)
            node = new_node
    node.end_of_word = True

def find_prefix(root, word):
    node = root
    for char in word:
        found_char = True
        for child in node.children:
            if child.char == char:
                node = child
                found_char = False
                break
        if found_char:
            return False, 0
    return True, node.counter

