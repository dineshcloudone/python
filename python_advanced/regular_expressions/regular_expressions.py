import re

# git url : https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Regular-Expressions

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# raw strings
#print(r'\tTab')

#pattern = re.compile(r'abc')

# '.' is a special character in reg exp
#pattern = re.compile(r'\.') #exact dot matches
#pattern = re.compile(r'coreyms\.com')

# matching telephone numbers
#pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d')

# parsing phone numbers from text file
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d')


# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

## [character set] reading mohile numbers from data.txt file and printing the matches
#pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d') # to match 800-555-1234 , 900-555-1234
pattern = re.compile(r'[a-z]') #matches only lower case letters
pattern = re.compile(r'[A-Z]') #matches only Upper case letters
pattern = re.compile(r'[a-zA-Z]') #matches upper case and lower case letters
pattern = re.compile(r'[^A-Z]') #matches everything except Upper case letters
pattern = re.compile(r'[^b]at') #matches words ending with at but not starting with b


## using quantifiers
pattern = re.compile(r'\d{3}.\d{3}.\d{\3}') # to match 800-555-1234 , 900-555-1234
pattern = re.compile(r'Mr\.?\s[A-Z]') # prints some matches of names
pattern = re.compile(r'Mr\.?\s[A-Z]\w*') # prints some matches of names

# using groups
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') #matches all naming convensitons

# using groups except putting M in grouping
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') #matches all naming convensitons


# printing emails
pattern = re.compile(r'[a-zA-z]+@[a-zA-Z]+\.com') #matches CoreyMSchafer@gmail.com

pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)') #matches corey.schafer@university.edu

pattern = re.compile(r'[a-zA-Z0-0.-]+@[a-zA-Z]+\.(com|edu|net)') #matches corey-321-schafer@my-work.net

#printing urls
urls='''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = pattern.finditer(urls)
for match in matches:
        print(match)

# reading from files
with open('data.txt','r',encoding='utf-8') as f:
    contents = f.read()
    pattern =pattern.finditer(contents)
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
        
    # groups
    for match in matches:
        print(match.group(0))
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))

    #substituted urls    
    subbed_urls = pattern.sub(r'\2\3',urls)
    print(subbed_urls)


# other methods
  #pattern.findall() - prints all the matched data storing in List
  #pattern.match() - searches only at the beginning of the string, if doesn't match anything it will return None
  #pattern.search() - searches through out the string, if doesn't match anything it will return None
  
# Flags in regular expressions
pattern = re.compile(r'start',re.IGNORECASE) # instead of r'[Ss][Tt][Aa][Rr][Tt]
matches = pattern.search(sentence)
print(matches)

'''Flags explanation from chatgpt

In Python's `re` module, you can use flags to modify how regular expressions are interpreted and applied. Flags are optional parameters that you can pass to the `re.compile()` function or as the second argument to many `re` module functions. Here are some commonly used flags in regular expressions:

1. **re.IGNORECASE (or re.I):**
   - This flag makes the regular expression pattern case-insensitive, so it will match both uppercase and lowercase letters.

   ```python
   import re

   pattern = re.compile(r'apple', re.IGNORECASE)
   result = pattern.match('Apple')  # This will match
   ```

2. **re.MULTILINE (or re.M):**
   - This flag allows the `^` and `$` anchors to match the start and end of each line within a multi-line string, not just the start and end of the entire string.

   ```python
   import re

   pattern = re.compile(r'^line', re.MULTILINE)
   text = 'line 1\nline 2\nline 3'
   result = pattern.findall(text)  # This will find all occurrences of 'line' at the start of lines
   ```

3. **re.DOTALL (or re.S):**
   - This flag makes the `.` in your pattern match any character, including newline characters (`\n`).

   ```python
   import re

   pattern = re.compile(r'pattern.*end', re.DOTALL)
   text = 'pattern\nsome text\nend'
   result = pattern.match(text)  # This will match the entire text
   ```

4. **re.VERBOSE (or re.X):**
   - This flag allows you to write more readable regular expressions by ignoring whitespace and allowing comments within the pattern.

   ```python
   import re

   pattern = re.compile(r''' '''
      \d{3}   # Match three digits
      -       # Match a hyphen
      \d{2}   # Match two more digits
       ''' ''', re.VERBOSE) 

   text = '123-45'
   result = pattern.match(text)  # This will match
   ```

5. **re.ASCII (or re.A):**
   - This flag makes the `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s`, and `\S` character classes match only ASCII characters.

   ```python
   import re

   pattern = re.compile(r'\w+', re.ASCII)
   text = 'café'
   result = pattern.findall(text)  # This will match 'caf' only
   ```

6. **re.UNICODE (or re.U):**
   - This flag makes the `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s`, and `\S` character classes match Unicode characters (the default behavior).

   ```python
   import re

   pattern = re.compile(r'\w+', re.UNICODE)
   text = 'café'
   result = pattern.findall(text)  # This will match 'café'
   ```

These are some of the commonly used flags in Python's regular expressions. You can use them to modify the behavior of your regular expressions to suit your specific needs when matching patterns in strings.

'''
  

