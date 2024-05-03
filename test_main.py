import pytest

from main import BST

@pytest.fixture
def tree():
    tree = BST()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    return tree

def test_insert_one_item(tree):
    assert tree.root.value == 5

def test_insert_many(tree):
    assert tree.search(2)
    assert tree.search(4)
    assert tree.search(6)
    assert tree.search(8)
    

def test_search_not_empty(tree):
    assert tree.search(5)
    assert tree.search(3)
    assert tree.search(7)


def test_in_order_traversal(tree):
    assert tree.in_order_traversal() == [2, 3, 4, 5, 6, 7, 8]

def test_find_min(tree):
    assert tree.find_min() == 2

def test_find_max(tree):
    assert tree.find_max() == 8
    
def test_height(tree):
    assert tree.height() == 3

def test_count_leaves(tree):
    assert tree.count_leaves() == 4

def test_serialize_deserialize(tree):
    serialized_tree = tree.serialize()
    new_tree = BST()
    new_tree.deserialize(serialized_tree)
    assert new_tree.in_order_traversal() == [2, 3, 4, 5, 6, 7, 8]


    




