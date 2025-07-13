def get_letter_grade(average):
    if average > 90:
        return "A"
    elif 80 <= average <= 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    else:
        return "D"

def main():
    print("=== Grade Average & Letter Grade Calculator ===")
    grades_input = input("Enter grades separated by spaces (e.g., 95 87 73 60): ")

    try:
        grades = [float(g) for g in grades_input.split()]

        if not grades:
            print("No grades entered.")
            return

        average = sum(grades) / len(grades)
        letter = get_letter_grade(average)

        print(f"\nYou entered {len(grades)} grades.")
        print(f"Average grade: {average:.2f}")
        print(f"Letter grade: {letter}")

    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")

if __name__ == "__main__":
    main()
