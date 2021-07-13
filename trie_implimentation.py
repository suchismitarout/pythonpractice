class TrieNode():
    def __init__(self, char):
        self.char = char
        self.children = []
        self.counter = 1
        self.endOfWord = False


def add_to_trie(root, word):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                node.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.endOfWord = True


def find_prefix(root, prefix):
    node = root
    if not node.children:
        return
    for char in prefix:
        found_in_child = True
        for child in node.children:
            if child.char == char:
                found_in_child = False
                node = child
                break
        if found_in_child:
            return False, 0
    return True, node.counter


def delete_word(root, word):
    node = root
    found_word = find_prefix(root, word)
    if list(found_word)[0]:
        for char in word:
            for child in node.children:
                if child.char == char:
                    if node.counter > 1:
                        node = child
                        node.counter -= 1
                        break
                    else:
                        node.children.remove(child)
                        return "element removed"
    else:
        return "word is not present"

def check_word_break(strr, root):
    n = len(strr)
    if (n == 0):
        return True
    for i in range(1, n + 1):
        if (find_prefix(root, strr[:i]) and check_word_break(strr[i:], root)):
            return True
    return False



if __name__ == '__main__':
    t = TrieNode('')
    # list1 = ["the", "a", "there", "anaswe", "any",
    #          "by", "their"]
    # for i in list1:
    #     add_to_trie(t, i)
    # print(find_prefix(t, 'their'))
    # print(delete_word(t, 'their'))
    # print(find_prefix(t, 'their'))
    # print(delete_word(t, 'sun'))
    wordDict = ["the", "quick", "fox", "brown"]
    for w in wordDict:
        add_to_trie(t, w)
    print(check_word_break("thequickbrownfox", t))



