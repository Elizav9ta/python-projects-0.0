"""The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates."""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) #set3 = set1 | set2
print(set3)