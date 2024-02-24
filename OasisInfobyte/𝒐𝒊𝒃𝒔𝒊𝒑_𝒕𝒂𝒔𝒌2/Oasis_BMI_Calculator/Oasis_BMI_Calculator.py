#Basic
def main():
    weight = get_input('Enter your weight in Kg: ', 'weight')
    height = get_input('Enter your height in meters: ', 'height')

    bmi = calc_bmi(weight, height)
    classification = class_bmi(bmi)

    print('BMI:', bmi)
    print('Classification:', classification)


def get_input(prompt, input_type):
    while True:
        try:
            value = float(input(prompt))
            if input_type == 'weight' and value <= 0:
                raise ValueError("Weight must be greater than 0.")
            elif input_type == 'height' and value <= 0:
                raise ValueError("Height must be greater than 0.")
            return value
        except ValueError:
            print(f"Invalid {input_type}. Please enter a valid numeric value.")


def calc_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def class_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    else:
        return "Overweight"


if __name__ == "__main__":
    main()



# Key Concepts and Challenges:

# User Input Validation: Ensure valid user inputs within reasonable ranges and handle errors gracefully.
# BMI Calculation: Accurately implement the BMI formula. 
# Categorization: Classify BMI values into health categories based on predefined ranges.