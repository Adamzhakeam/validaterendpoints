'''
this module checks for validity of a phone number 
'''

def _isString(number:str) -> bool:
    '''
    function Checks if the input is a string
    '''
    return isinstance(number, str)

def _isLengthValid(number: str) -> bool:
    """
    function Check if the number has the correct length
    """
    return len(number) in [12]

def _areAllDigits(number: str) -> bool:
    '''
    function checks if all the numbers in a phoneNumber string are digits
    '''
    return number.isdigit()

def _firstDigitsValid(number: str) -> bool:
    '''
    function Checks if the first 4 characters in the phone number start with "2567"
    '''
    return number[:4] in ["2567"]

def isValid(number: str) -> bool:
    '''
    function checks the given number for type of the number(str), 
    length of the number(12), and te first four characters in the number(2567)
    '''
    return _isString(number) and _isLengthValid(number) and \
            _areAllDigits(number) and _firstDigitsValid(number)

if __name__ == "__main__":
    for testCase, TestResponse in [
        ("2567504408  ", False), ("2567504409,,", False),
        ("750440821", False),    ("+256750440832", False),
        ('+256750440821', False),  ("256750440821", True), 
        ('750440821', False),      ("256950440821", False), 
        ("056750440821", False),  ("2567087", False), 
        ("07568__", False),        ("2567745", False), ("750645", False), 
        ("25675034576", False),("1234567890", False),
        ("+12345678901", False),  ("001234567890", False),
        ("123-456-7890", False),  ("(123) 456-7890", False),
        ("12-345-6789", False),   ("12345678901", False),
        ("+123(456)7890", False), ("123 456 7890", False),
        ("1234", False), ("+123456", False),
        ("", False), ("0000000000", False),
        ("2567089456", False),  ("+2567089456", False),
        ("+256-708-9456", False), ("256-708-9456", False),
        ("(256) 708-9456", False), ("256 708 9456", False),
        ("0708945678", False), ("256 708 945 687", False)
    ]:
        response = isValid(testCase)
        assert response==TestResponse, f"{testCase} returned {response} instead of {TestResponse}"

    print("All test cases passed!")


