class UserProfile:
    def __init__(self, name, age, gender, weight, height, activity_level, preferences=None, health_conditions=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.activity_level = activity_level
        self.preferences = preferences or []
        self.health_conditions = health_conditions or []

    def calculate_bmi(self):
        return round(self.weight / ((self.height/100) ** 2), 2)
