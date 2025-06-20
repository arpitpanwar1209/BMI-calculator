def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (meters)."""
    if height <= 0:
        return "Invalid height. Must be greater than zero."
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def interpret_bmi(bmi):
    """Return interpretation based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        bmi = calculate_bmi(weight, height)
        if isinstance(bmi, str):
            print(bmi)
        else:
            print(f"Your BMI is: {bmi}")
            print(f"Category: {interpret_bmi(bmi)}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the BMI calculator
if __name__ == "__main__":
    main()
