import pandas as pd
import matplotlib.pyplot as plt
path = '/content/Pokemon.csv' # update if needed
pokemon_df = pd.read_csv(path) 

# team work
# How many Pokémons are with 'Type 1' == Water as a % of total
water_pokemon = pokemon_df[pokemon_df['Type 1'] =="Water"]
water_pokemon_percentage = (len(water_pokemon)/len(pokemon_df))*100
print(f'number of water pokemons {len(water_pokemon)}, is {water_pokemon_percentage:.2f} %')

#What is the maximum 'Speed' value? What is the minimum 'Speed' value? What is the difference between max and min 'Speed'?  
max_speed = pokemon_df['Speed'].max()
min_speed = pokemon_df['Speed'].min()
speed_difference = max_speed - min_speed
print(f"Maximum Speed: {max_speed}")
print(f"Minimum Speed: {min_speed}")
print(f"Difference between Max and Min Speed: {speed_difference}")

#Filter the DataFrame to include only the Pokémon with 'Speed' >= 80. How many Pokémon meet this criterion? 
#Display this DataFrame using your preferred visualization method.
high_speed_pokemon = pokemon_df[pokemon_df['Speed'] >= 80]
num_high_speed_pokemon = len(high_speed_pokemon)
print(f"Number of Pokémon with Speed >= 80: {num_high_speed_pokemon}")
plt.figure(figsize=(10, 6)) 
plt.hist(high_speed_pokemon['Speed'], bins=10, color='pink', edgecolor='magenta') 
plt.title('Number of Pokemon with Speed more than 80') 
plt.xlabel('Speed')  
plt.ylabel('Number of Pokemon') 
plt.grid(linestyle='--', alpha=0.7)  
plt.show()

#(DIFFICULT) Find Pokémon with the longest name (excluding spaces)? What is this pokemons name?
# remove spaces
pokemon_df['Name_only_symbols'] = pokemon_df['Name'].str.replace(" ", "")
# find index of the longest word
max_length_index = pokemon_df['Name_only_symbols'].str.len().idxmax()
# find the longest name
longest_name = pokemon_df['Name'].loc[max_length_index]

print(f"The Pokémon with the longest name (excluding spaces) is {longest_name}.")
