#Pretty table module is used to print in proper ASCII format
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Pokemon Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.add_row(["Balbusar","Grass"])
print(table)