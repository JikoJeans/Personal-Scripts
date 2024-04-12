# This script utilizes panda to both read the website and parse the tables so that all
# 'duplicate' (entries with the same title but different platforms) can be filtered and removed.
import pandas as pd
# Tables now contains all the tables form the url provided
tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_2K_games')
#  print(tables[1])  #  can confirm table collection with a simple print statement
# For my specific case I chose to grab the second table
selected_table = tables[1]
# game_list will contain all the game titles that have been seen and the initial entry is representative of a blank title
game_list = ['[]', ]
# For each row in the table we want to perform an operation
for index in range(len(selected_table)):
    # If the game title has not been seen yet
    if selected_table.iat[index, 0] not in game_list:
        # Output a line that can be copied from the terminal later
        print(f'{selected_table.iat[index, 0]}, {selected_table.iat[index , 1]}, {selected_table.iat[index, 2]}, {selected_table.iat[index, 3]}')
        # Add the game title to the list
        game_list.append(selected_table.iat[index, 0])

# For fun we can also output all the games seen during the filter
# print('final game list')
# print(game_list)