"""
file_in = open("requirements.txt", 'r')
# pracuji se souborem
file_in.close()"""

try:
    with open("new_file.txt", 'w') as f:
        f.write("Ahoj\n")
        f.write("Druhy radek\n")
        f.write("Konec zpravy")
        print("Zpráva zapsána do souboru.")
except Exception as e:
    print(e)

try:
    with open("new_file.txt", 'r') as f:
        print(f)
        header = f.__next__()
        print(header)
        for line in f:
            print(f"'{line.strip()}'")
        print("-"*40)
        f.seek(0)
        for line in f:
            print(f"'{line.strip()}'")
        with open("requirements.txt", 'r') as f_r:
            pass

except Exception as e:
    print(e)

print("-"*40)

try:
    with open("new_file.txt", 'r') as f:
        lines = f.readlines()
        print(lines)
        for line in lines:
            print(line.strip())
        print("-"*40)
        for line in lines:
            print(line.strip())
except Exception as e:
    print(e)

print("="*80)
try:
    content = ""
    with open("new_file.txt", 'r') as f:
        content = f.read().replace(" ", "_")
        print(content)
    with open("new_file.txt", 'w') as f:
        f.write(content)
except Exception as e:
    print(e)

print("Konec")
