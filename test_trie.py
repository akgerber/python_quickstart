from trie import Trie


def test_trie():
    my_trie = Trie[str]()
    assert my_trie.search_under_prefix("y") == []
    my_trie.upsert("yo", "yo result")
    assert my_trie.search_under_prefix("y") == ["yo result"]
    my_trie.upsert("yoo", "yoo result")
    assert sorted(my_trie.search_under_prefix("y")) == sorted(["yo result", "yoo result"])
    my_trie.upsert("yo", "new yo result")
    assert sorted(my_trie.search_under_prefix("y")) == sorted(["new yo result", "yoo result"])
    assert sorted(my_trie.search_under_prefix("yo")) == sorted(["new yo result", "yoo result"])

