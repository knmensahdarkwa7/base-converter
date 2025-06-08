class BaseConverter:
    def __init__(self, number, base):
        self.number = number
        self.base = base

    def validate_number(self):
        """Ensure the number is valid for its given base."""
        valid_chars = {
            2: '01',
            5: '01234',
            8: '01234567',
            16: '0123456789ABCDEF'
        }

        return all(char in valid_chars.get(self.base, '') for char in self.number)

    def convert_to_decimal(self):
        """Convert the number from its given base to decimal."""
        if not self.validate_number():
            return f"Error: {self.number} is not a valid base-{self.base} number."

        decimal_value = sum(int(char, self.base) * (self.base ** i) for i, char in enumerate(reversed(self.number)))
        return f"{self.number} in base {self.base} is {decimal_value} in decimal."


class DecimalConverter:
    def __init__(self, number, target_base):
        self.number = number
        self.target_base = target_base

    def convert_from_decimal(self):
        """Convert a decimal number to the target base."""
        if self.target_base not in [2, 5, 8, 16]:
            return "Error: Unsupported target base."

        digits = "0123456789ABCDEF"
        result = ""

        num = self.number
        while num > 0:
            result = digits[num % self.target_base] + result
            num //= self.target_base

        return f"{self.number} in decimal is {result} in base {self.target_base}."



# Main function to run the program
def main():
    print("Welcome to my Base Converter!")

    while True:
        choice = input("Choose 1 to convert from other bases to decimal\n"
                       "Choose 2 to convert from decimal to other bases\n"
                       "Press 'q' to quit\n: ")

        if choice == '1':
            num = input("Enter the number: ").upper()
            base = int(input("Enter its base (2, 5, 8, 16): "))
            converter = BaseConverter(num, base)
            print(converter.convert_to_decimal())

        elif choice == '2':
            num = int(input("Enter the decimal number: "))
            target_base = int(input("Enter the base to convert into (2, 5, 8, 16): "))
            converter = DecimalConverter(num, target_base)
            print(converter.convert_from_decimal())

        elif choice.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
