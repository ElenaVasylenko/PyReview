####Hashable
Most of Python’s immutable built-in objects are hashable;  
mutable containers (such as lists or dictionaries) are not;  
immutable containers (such as tuples and frozensets) are only hashable if their   
elements are hashable. Objects which are instances of user-defined classes are   
hashable by default. They all compare unequal (except with themselves), and their  
hash value is derived from their id().

####Frozenset
In Python, frozenset is same as set except its elements are immutable.  
**Mutable** - list, dict, set