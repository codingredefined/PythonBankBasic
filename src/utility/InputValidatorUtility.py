import re


class InputValidatorUtility:

    def __init__(self):
        self.alphaPattern = re.compile('[a-zA-Z]')
        self.numberPattern = re.compile('[0-9]')
        self.alphaNumericPattern = re.compile('[a-zA-Z0-9 ]')

    def mainMenuInputValidator(self, value):
        if self.alphaPattern.match(value):
            return "Error: Invalid value. Alphabets not allowed, must be Numeric."
        elif not self.numberPattern.match(value):
            return "Error: Invalid value. Special characters not allowed, must be Numeric."
        else:
            return "valid"


    def isAlpha(self, value):
        return self.alphaPattern.match(value)

    def isNum(self, value):
        return self.numberPattern.match(value)

    def isAlphaNumeric(self, value):
        return self.alphaNumericPattern.match(value)