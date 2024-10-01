'''
def count_ladies(names):
    # Create a dictionary to store the count of ladies for each prefix
    prefix_count = {}

    # Iterate through the names
    for name in names:
        # Initialize the count for the current prefix to 0
        prefix_count[name] = 0

        # Iterate through the characters in the name
        for i in range(len(name)):
            # Get the prefix of the current length
            prefix = name[:i+1]

            # Increment the count for the current prefix
            prefix_count[prefix] += 1

    # Return the count of ladies for each prefix
    return prefix_count

# Test the function
names = ["S", "YS", "RYS", "ERYS", "NERYS", "ENERYS", "AENERYS", "DAENERYS", "YAENERYS", "RYAENERYS"]
print(count_ladies(names))
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def prefixCount(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count

def count_ladies(names, queries):
    trie = Trie()
    for name in names:
        trie.insert(name)
    return [trie.prefixCount(query) for query in queries]

# Test the function
names = ["S", "YS", "RYS", "ERYS", "NERYS", "ENERYS", "AENERYS", "DAENERYS", "YAENERYS", "RYAENERYS"]
queries = ["RY", "E", "N", "S", "AY"]
print(count_ladies(names, queries))

