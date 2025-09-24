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
    
    def __len__(self) -> int:
        """

        The length is the same as the size of a tree. 

        Base case: just root
        recursive: we sum the size of each subtree + add one for the root 

        >>> t = Tree(7, [Tree(1, [Tree(2), Tree(3)]), Tree(9, [Tree(4), Tree(5)])])
        >>> t.__len__()
        7 
        
        
        
        """
        length = 0 
        if self.is_empty:
            return 0 
        elif self._subtrees == []:
            return 1 
        else:
            for subtree in self._subtrees:
                length += subtree.__len__()
        return length + 1

    
    def str_indented(self, depth: int) -> str:
        """

        Return an indented represenation of the tree. 

        The indentation is decided by the depth of the tree. 
    
        
        """

        if self.is_empty():
            return ''
        
        else:
            str_so_far = '  ' * depth + f'{self._root}\n'
            for subtree in self._subtrees:
                subtree.str_indented(depth+1):
            return str_so_far
            
            

