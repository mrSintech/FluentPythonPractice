# The set and frozenset types are both implemented with a hash table. This has
# these effects:

# • Set elements must be hashable objects. They must implement proper __hash__
# and __eq__ methods

# • Membership testing is very efficient. A set may have millions of elements,
# but an element can be located directly by computing its hash code and
# deriving an index offset, with the possible overhead of a small number of
# tries to find a matching element or exhaust the search.

# • Sets have a significant memory overhead, compared to a low-level array
# pointers to its elements—which would be more compact but also much slower to
# search beyond a handful of elements.

# • Element ordering depends on insertion order, but not in a useful or reliable
# way.If two elements are different but have the same hash code, their position
# depends on which element is added first.

# • Adding elements to a set may change the order of existing elements. That’s
# because the algorithm becomes less efficient if the hash table is more than
# two- thirds full,so Python may need to move and resize the table as it grows.
# When this happens, elements are reinserted and their relative ordering may
# change.
