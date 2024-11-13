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


Druhý způsob řešení

source_file_p = 'C:/Users/Honza/Downloads/terms_and_conditions.txt'
output_file_p = 'C:/Users/Honza/OneDrive/Plocha/Python Kurz/Lekce 8 13.11.2024/Lekce8/7letters.txt'

def threshold_filter(source_file_p, output_file_p, threshold):
    f = open(source_file_p, "r")
    data = f.read()
    f.close()

    output_date = ""
    for line in data.split("\n"):
        for word in line.split():
            if len(word) > threshold:
                output_data += f"{word}\n"

    for open(output_file_p, "w")
    f.write(output_data)
    f.close()

SOURCE_PATH = "data.txt"
FILE_PATH = "filtered.txt"

threshold_filter(SOURCE_PATh, FILE_PATH, threshold:7)




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
source_file_p2 = 'C:/Users/Honza/Downloads/pes.txt'
output_file_p2 = 'C:/Users/Honza/OneDrive/Plocha/Python Kurz/Lekce 8 13.11.2024/Lekce8/klon_psa.txt'

with open(source_file_p2, "r", encoding="utf-8") as source_file2:
    with open(output_file_p2, "w") as pes_klon:
        for line in source_file2:
            pes_klon.write(line)

print(f"Řádky ze souboru {source_file_p2} byly naklonováno do {output_file_p2} ve stejném pořadí")


'''
Task3
You have a text file. Write its lines to another file. 
The order of lines in the second file must be inverse.
'''
source_file_p3 = 'C:/Users/Honza/Downloads/pes.txt'
output_file_p3 = 'C:/Users/Honza/OneDrive/Plocha/Python Kurz/Lekce 8 13.11.2024/Lekce8/klon_psa_reversed.txt'

with open(source_file_p3, "r", encoding="utf-8") as source_file3:
    lines = source_file3.readlines()

lines.reverse()

with open (output_file_p3, "w") as output_file:
    for line in lines:
        output_file.write(line)

print(f"Řádky ze souboru {source_file_p3} byly naklonováno do {output_file_p3} ve opačném pořadí")


'''
Task 5
You have a text file. Calculate the number of words that begin with a character set by the user.
'''
source_file_task5 = 'C:/Users/Honza/Downloads/pes.txt'
char = input("Vložte písmeno, kterým mají začínat slova v textu: ").lower()
count = 0
count2 = 0
words_with_char = []

with open(source_file_task5, "r", encoding="utf-8") as source_file:
    for line in source_file:
        words = line.split()
        count += sum(1 for word in words if word.lower().startswith(char))
        for word in words:
            if word.lower().startswith(char):
                words_with_char.append(word)
                count2 += 1
print(f"Počet slov začínajících na {char} je {count}")
print(f"Jsou to tato slova: {words_with_char}")

'''
Task 6
You have a text file. Write all its lines to another file while replacing * with & and vice versa.
'''
source_file_task6 = 'C:/Users/Honza/Downloads/pes.txt'
output_file_task6 = 'C:/Users/Honza/OneDrive/Plocha/Python Kurz/Lekce 8 13.11.2024/Lekce8/klon_psa2.txt'


with open(source_file_task6, "r", encoding="utf-8") as source_file6:
    with open(output_file_task6, "w") as pes_klon2:
        for line in source_file6:
            modified_line = line.replace("*", "#TEMP#").replace("&", "*").replace("#TEMP#", "&")
            pes_klon2.write(modified_line)

'''
Task 7
You have an array of strings. 
Write them to a file while placing each array element on a separate line and preserving the order.
'''
source_file_task7 = 'C:/Users/Honza/Downloads/pes_composed.txt'
output_file_task7 = 'C:/Users/Honza/OneDrive/Plocha/Python Kurz/Lekce 8 13.11.2024/Lekce8/pes_decomposed.txt'

with open(source_file_task7, "r", encoding="utf-8") as source_file7:
    with open(output_file_task7, "w") as pes_decomposed:
        for line in source_file7:
            pes_decomposed.write(line + "\n")

print(f"Řádky ze souboru {source_file_task7} byly naklonováno do {output_file_task7} ale rozdělen na řádky")
'''
Task 8
You have an array of strings. 
Write them to a file while placing each array element on a separate line and reversing the order.
'''

'''
Task 9
You have a text file. Calculate the number of characters in it.
'''

'''
Task 10
You have a text file. Calculate the number of lines in it.
'''


















