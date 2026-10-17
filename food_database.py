import pandas as pd

# Load dataset (CSV with food items and nutrients)
food_data = pd.read_csv("nutritional_dataset.csv")

# Example columns: ['Food', 'Calories', 'Protein', 'Carbs', 'Fat', 'Fiber', 'Category']
print(food_data.head())
