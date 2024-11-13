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



