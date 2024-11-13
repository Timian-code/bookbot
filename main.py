"""
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents) 
if __name__ == "__main__":
    main()

def count():
    with open("books/frankenstein.txt") as f:
        content = f.read()
        word_count = len(content.split())
    print(f"The file contains {word_count} words.")
count()

def count_characters():
    with open("books/frankenstein.txt") as f:
        character_count = {}
        book_text = f.read()
        for char in book_text:
            char = char.lower()
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

result = count_characters()
print(result)
    
def get_sorted_characters(character_count):
    letters = []
    for char, num in character_count.items():
        letters.append({"character": char, "num": num})
    
    letters.sort(key=sort_on, reverse=True)
    return letters

sorted_characters = get_sorted_characters(character_count)
print("--- Begin Character Frequency Report ---")
for item in sorted_characters:
    character = item["character"]
    frequency = item["num"]
    print(f"The '{character}' character was found {frequency} times")
print("--- End Character Frequency Report ---") 
"""

def sort_on(item):
    return item["num"]

def count_characters():
    with open("books/frankenstein.txt") as f:
        character_count = {}
        book_text = f.read()
        for char in book_text:
            char = char.lower()
            if char.isalpha():
                if char in character_count:
                    character_count[char] += 1
                else:
                    character_count[char] = 1
    return character_count

result = count_characters()

def get_sorted_characters(character_count):
    letters = []
    for char, num in character_count.items():
        letters.append({"character": char, "num": num})
    
    letters.sort(key=sort_on, reverse=True)
    return letters

sorted_characters = get_sorted_characters(result)

print("--- Begin Character Frequency Report ---")
for item in sorted_characters:
    character = item["character"]
    frequency = item["num"]
    print(f"The '{character}' character was found {frequency} times")
print("--- End Character Frequency Report ---")


