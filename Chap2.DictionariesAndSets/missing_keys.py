
# Sometimes it is convenient to have mappings that return some made-up value
# when a missing key is searched. There are two main approaches to this: one is
# to use a defaultdict instead of a plain dict. The other is to subclass dict
# or any other mapping type and add a __missing__ method.

# -=-=-=-=-=-=- defaultdict -=-=-=-=-=-=-=- #
