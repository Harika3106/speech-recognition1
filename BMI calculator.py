def calculate_bmi(weight, height):
    try:
        # Calculate BMI
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Height cannot be zero!"
    except Exception as e:
        return f"Error occurred: {e}"

def bmi_category(bmi):
    # Determine BMI category
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Example usage:
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Your BMI is: {bmi}")
print(f"BMI Category: {category}")
