"""
Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;
Lua: returns a Table;
Have fun!

for example, a tower of 3 floors looks like below

[
  "  *  ",
  " *** ",
  "*****"
]
and a tower of 6 floors looks like below

[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]
Go challenge Build Tower Advanced once you have finished this :)
"""

def tower_builder(n_floors):

    if n_floors == 0:
        return []
    else:
        tower = []
        for n in range(n_floors):
            tower.append("*"*(n+1+n))
        new_tower = []
        for el in tower:
            el_l = list(el)
            while len(el_l) != n+len(tower):
                el_l.insert(0, " ")
                el_l.append(' ')
            new_tower.append("".join(el_l))

    return new_tower


print(tower_builder(4))
print(tower_builder(3))
print(tower_builder(2))
print(tower_builder(1))
print(tower_builder(0))



"""
        tower_builder(1), ['*', ]
        tower_builder(2), [' * ', '***']
        tower_builder(3), ['  *  ', ' *** ', '*****']
"""