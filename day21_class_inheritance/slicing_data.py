"""
Concepts: Slicing
 -- slicing a specific segment of a data structure for its values
 -- slicing based of the position of a data structure
 -- Syntax:
    -- data_structure[position1, position2]
        --Note: position2 is NOT inclusive of the returned value
    -- data_structure[position1:] <-- used getting the specified position value plus the rest of the values in the data structure
    -- data_structure[:position2] <-- works in the reverse; get all values upto specified position
    -- data_structure[position1:position2:skipByNumber]  <-- not skipByNumber is referred to as "increment"
    -- data-structure[::-1] <-- is a trick (or shortcut) that will reverse the data structure  <-- returning last to first
"""


# Slicing example
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5]) # will return a "slice" of the piano_key list - "c, d, e"

print(piano_keys[2:]) # will return all values from specified index position (2) onward - "c, d, e, f, g"

print(piano_keys[:5]) # will return all values up to specified position (0 up to 5) = "a, b, c, d, e"

print(piano_keys[2:5:2]) #will return every value starting at position1 and up to position2, incrementing by 2 (skipping every other index position) - "c, e"

print(piano_keys[::2]) # will return every value, incrementing by 2 - "a, c, e, g,";

print(piano_keys[::-1]) # will return every value in reverse order - "g, f, e, d, c, b, a"