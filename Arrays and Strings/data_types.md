**Data types != Data structures**

Let's say you have a box and put a label on it, that label is called a data type. 
Inside this box you can store anything you want, numbers, letters etc. 
How you arrange these boxes is data structures. 

Here are some common data types in Python: 

text type: str 
numeric type: int, float, complex
sequence type: list, tuple, range
mapping type: dict
set types: set, frozenset
boolean type: bool
binary type: bytes
none type: NoneType

*New ones*:

Complex is simply ```x = 1j```
Range is ```y = range(6)```
Frozenset is just a set that is immutable (cannot be changed) ```z = frozenset({1,2,3})```

**Dictionary methods**:

- clear() -> removes all the elements 
- copy() -> returns a copy of the dict 
- fromkeys(keys, value) -> assigns the value to the key

```
d = {"a": 1, "b": 2, "c": 3, "d":4, "e": 5}
d.fromkeys("a", 5)
{"a": 5}
#This returns a new new dictionary but doesnt modify the og. 

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
{'key1': 0, 'key2': 0, 'key3': 0}
```

- get(key) -> returns the value of the key 
- pop(key) -> removes the element with this key 
- popitem() -> removes the last inserted key value pair and returns it 
- setdefault(key) -> returns the value of the key, if it doesnt exist, it will create it
- keys() -> returns a list containing all the keys of the dict 
- values() -> returns a list of all values in a dict 
- update(key_val_pair) -> update the dict with this key value pair  

**String operations**

- string[position] -> index at a str
- s += -> concatenation 
- len(s) -> find the length 
- s =><! ->  lexicographical comparisons based on alphabetical order.

