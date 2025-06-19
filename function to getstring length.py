# function to getstring length

def getstringlength(string) -> int:
    counter = 0

    if string is not None:
        for character in string:
            counter = counter + 1
    return counter

# invocation code
input1 = None  # Null
print(f"string length of {input1} is {getstringlength(input1)}")

input2 = ""
print(f"string length of '{input2}' is {getstringlength(input2)}")

input3 = "v"
print(f"string length of '{input3}' is {getstringlength(input3)}")