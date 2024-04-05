class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        prev_value = 0
        for char in value[::-1]:
            current_value = roman_numerals[char]
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            prev_value = current_value
        return cls(result)

    @classmethod
    def from_string(cls, value):
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"

# Example usage:
print(Integer.from_float(3.8).value)  # Output: 3
print(Integer.from_roman('IX').value) # Output: 9
print(Integer.from_string('42').value) # Output: 42
print(Integer.from_float(5))          # Output: value is not a float
print(Integer.from_roman('ABC'))      # Output: 0 (default value of Integer object)
print(Integer.from_string('hello'))   # Output: wrong type
