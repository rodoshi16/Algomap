class Tree:
    """

    A recursive tree data structure. 

    Representation invariants:

    _root: The item stored at this tree's root
    _subtrees: list of subtrees of this tree 
    
    
    """

    _root: Optional[Any]
    _subtrees: list[Tree]

    def _-init__(self, root: Optional[Any], subtrees: list[Tree]):
        self._root = root
        self._subtrees = subtrees
    
    def is_empty(self) -> bool:
        return self._root is None 