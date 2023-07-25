
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar('T')

@dataclass
class TrieNode:
    children: dict[str, 'TrieNode']
    # Non-null value indicates this word exists
    word_val: T | None = None

class Trie(Generic[T]):
    trie_root: TrieNode

    def __init__(self):
        # Empty root value for ""
        self.trie_root = TrieNode(word_val=None, children={})

    def upsert(self, word: str, word_val: T) -> None:
        """
        Upsert word_val into the trie for the specified word
        """
        itr = self.trie_root
        for c in word:
            if c not in itr.children:
                itr.children[c] = TrieNode(word_val=None, children={})
            itr = itr.children[c]
        itr.word_val = word_val

    def search_under_prefix(self, prefix: str) -> list[T]:
        """
        Find a list of all values stored in the trie under any children of the prefix
        """
        found = []

        if prefix is None or prefix is "":
            return found

        itr = self.trie_root
        for c in prefix:
            if c not in itr.children:
                return found
            else:
                itr = itr.children[c]
        to_search = [itr]

        # DFS all children of the prefix
        while len(to_search) > 0:
            curr = to_search.pop()
            if curr.word_val is not None:
                found.append(curr.word_val)
            to_search.extend(curr.children.values())

        return found