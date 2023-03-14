Reading:
    var = open("name", "{r|w|a|r+}") - to open
    close(var)

    with {name} as {var}:

    {var}.
    -- read()-reads all the lines
    -- readines()-returns lines as a list
    -- readline()-returns the first line (katrs naakamais readline returno naakamo line)
    - tell() - returns the position where "the read cursor" is at (in characters)
    - seek({int}) - sets "the read cursor" at the int counting from the start of the file


    **KAA LASIIT BIG FILES?
    visu reize neevar printeet - memory issue

    1. ar for loop
    2. read({range}) -> range = 100 == 100 characters


Writing:
    open("test2.txt")
        ja test2 neeksistee, tad vins taadu uztaisiis

    writing ovverrides the file (after a new open), appending - adds

Append:
    