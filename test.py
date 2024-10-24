print("Here is the data for the food you have been eating today")

for food in nutrition_data["foods"]:
    print(f'{food["nf_calories"]} calories')
    print(f'{food["nf_protein"]} protein')
    print(f'{food["nf_total_carbohydrate"]} carbohydrate')
    print(f'{food["nf_total_fat"]} fat')


print(json.dumps(nutrition_data, indent=4))

    total = sum(calories)
    print(total, "calories")


food_list = []

for food in nutrition_data["foods"]:
    food_list.append(food["nf_calories"])

print(sum(food_list))


exercise_data = response.json()

for exercise in exercise_data[]
