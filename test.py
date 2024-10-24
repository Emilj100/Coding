print("Here is the data for the food you have been eating today")

for food in nutrition_data["foods"]:
    print(f'{food["nf_calories"]} calories')
    print(f'{food["nf_protein"]} protein')
    print(f'{food["nf_total_carbohydrate"]} carbohydrate')
    print(f'{food["nf_total_fat"]} fat')

