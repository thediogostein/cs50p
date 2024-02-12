def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if max length is 6 and min of 2
    if len(s) < 2 or len(s) > 6:
         return False
    # Check if first two characters are letters, if not, then return false
    if not s[0:2].isalpha():
         return False

    # No periods, spaces, or punctuation marks are allowed"
    for c in s:
        if c in ".,!? ":
            return False

    # Numbers cannot be used in the middle; they must come at the end
        # Not acceptable: AAA22A, AA22AA
    # The first number used cannot be a 0
    # Acceptable: AAA222
    # Not acceptable: AA05

    # Find first number
        # If first number is 0, then return False
        # else
            # Check if remaining chars are numbers, if not return false

    found_digit = False
    substring = " "
    for i in range(len(s)):
        if s[i].isnumeric():
            substring = s[i:len(s)]
            found_digit = True
            break
    if substring.startswith("0"):
        return False
    if found_digit and not substring.isnumeric():
        return False


    return True


main()
