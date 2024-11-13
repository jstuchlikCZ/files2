# Files tasky

'''
Task 1
You have a text file. Create a new file where you should write all words consisting
of at least seven letters found in the source file.


f = open("test1.txt", "w")
f.write("Hello world!")
f.close()



f2 = open("test1.txt", "r")
data = f2.read()
f2.close()


print(data)
'''
import re

source_file_p = 'C:/Users/Honza/Downloads/terms_and_conditions.txt'
output_file_p = 'C:/Users/Honza/OneDrive/Plocha/Python Kurz/Lekce 8 13.11.2024/Lekce8/7letters.txt'

with open(source_file_p, "r", encoding="utf-8") as source_file:
    text = source_file.read()

words = re.findall(r'\b\w{7,}\b', text)

with open(output_file_p, "w") as output_file:
    for word in words:
        output_file.write(word + '\n')

print(f"Slova co mají 7 a více slov jsou uloženy v souboru 7letters.txt")

'''
Task2
You have a text file. Write its lines to another file. 
The order of lines in the second file must match the order of lines in the source file.
'''


