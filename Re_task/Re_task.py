import re


# Tasks:
# 1. Write a regular expression to search for the HTML color specified as #ABCDEF,
# that is, # and then contains 6 hexadecimal characters.
def check_color(color):
    pattern = r"^#[a-fA-F0-9]{6}$"
    return re.match(pattern, color)


color_hex = '#0000FF'
result = check_color(color_hex)
print(result)
if result:
    print("Color matched")
else:
    print("Color not found")


# 2. Create a query to identify numbers in the text that are not followed by a + sign.
# (Examples of expressions “2-6*9*5 ” or (3+5)-9*4)
def check_numbers_not_followed_by_plus_sign(sign):
    pattern = r"\d(?!\+)"
    return re.findall(pattern, sign)


# '2+-6+*9+*5+', (3+5)-9*4)
query = '3+4+5+7+8o9jkhgfd+1+2+4+'
result = check_numbers_not_followed_by_plus_sign(query)
print(result)


# 3. Create a query to output only correctly written expressions with brackets
# (The number of open and closed brackets should be the same)
def find_expressions_in_brackets(brackets):
    pattern = r"\([\s\S]*?\)"  # r"\([^()]*?\)"
    return re.findall(pattern, brackets)


string_with_brackets = '+-,/[](), 123(***), a*(b+[c+d])*e/f+g-(find), or ('
result = find_expressions_in_brackets(string_with_brackets)
print(result)


# 4. Find the time in the text. The time has the clock format:minutes. Both hours and minutes consist
# of two digits, for example: 09:00. Write a regular expression to find the time
# in the line: "Breakfast at 09:00". Note that "37:98" is an incorrect time.
def find_time(time):
    pattern = r"\b(0\d|1\d|2[0-3]):(0\d|[1-5]\d)\b"
    return re.findall(pattern, time)


string_with_time = 'Breakfast at 08:00 or at 09:00'
result = find_time(string_with_time)
print(result)
if result:
    print("Time found")
else:
    print("No time in the text")


# 5. Create a query to select fractional numbers from the text with a decimal separator
# in the form of a dot. The digits of the whole part may not be highlighted or separated by a space
# or comma.

def find_numbers_with_comma_separator(number):
    pattern = r"\d{1,3}(?:[ ,]\d{3})*\.\d+"
    return re.findall(pattern, number)


string_with_number = ("text 1,678.99 contains 489.6001 numbers 1 984 675.890 with decimal separator 4 44,5 and 1 123,"
                      "4 and 2,123,3 and 1 and 45,67")
result = find_numbers_with_comma_separator(string_with_number)
print(result)


# 6. Create a query to highlight the text enclosed in quotation marks.
# When solving the problem, take into account that the text can be located on several lines).
def find_words_in_quotes(quotes):
    pattern = r"\"[\s\S]*?\""
    return re.findall(pattern, quotes)


string_in_quotes = ('Create a query to highlight the text enclosed in quotation marks. When "solving the prob'
                    'lem", "take" into account that the text can be "lo-'
                    'cated" on several lines).')
result = find_words_in_quotes(string_in_quotes)
print(result)
