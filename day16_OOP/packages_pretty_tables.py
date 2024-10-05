"""
Concept: Classes, Packages - Object Orient Programming (OOP)
 -- Packages:
    -- Packages: a lot of code from other developers bundled together for a specific purpose
    -- Packages are installed FIRST before they can be imported (used) in your code:
        -- source for packages --> pypi.org
        -- In PyCharm navigate to:
            -- PyCharm > settings > Project > Project Interpreter > + (to add a package) > Search Package & Select a Package > Install Package
        -- To view source code of a package; right-click on package name; select GoTo, and the source code will launch in the editor window
"""

from prettytable import PrettyTable

table = PrettyTable()

# .add_column method takes in the columnName (fieldName), then a LIST of data for that column
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"


print(table)

