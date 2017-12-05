#! python3

# Get text off the clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
(\d{3}|\)\(d{3}\))?         # areacode
(\s|-|\.)?                  # separator
(\d{3})                     # first 3 digits
(\s|-|\.)                   # separator
(\d{4})                     # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

text = str(pyperclip.paste())

extractedPhone = phoneRegex.findall(text)

allPhoneNumbers = []

for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)

results = '\n'.join(allPhoneNumbers)

print(results)


# Find all phone number matches and store that into a variable

# Find all email address matches and store into a variable

# Output phone numbers

# Output email addresses

# Display message if no matches were found
