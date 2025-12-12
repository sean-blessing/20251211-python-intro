# Advanced Lists
print('Welcome to More Lists')
# doc string - for documentation
"""Basic sorting example"""

# list comprehension w/ 'if' statement
# get list of numbers between 1 and 100 that are evenly divisible by 7
# nbrs_evenly_divisible_by_seven = [x for x in range(1,101) if x % 7 == 0]
# print(f"nbrs_evenly_divisible_by_seven = {nbrs_evenly_divisible_by_seven}")


fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

# print(f"fruits unsorted:", fruits)
# print(f"basic sort fruits:", sorted(fruits))

# print("="*20)
# # sort alphabetically, ignoring case
# sorted_fruits_1 = sorted(fruits, key=str.lower)
# print(f"sorted_fruits_1:", sorted_fruits_1)

# print("="*20)
# print("Custom Sort - using a method we define")
# def ignore_case(item):
#     return item.lower()

# print(f'ignore_case(HeLlo):', ignore_case('HeLlo'))

# sorted_fruits_2 = sorted(fruits, key=ignore_case)
# print(f"sorted_fruits_2:", sorted_fruits_2)

# use lambda to sort fruits
# sorted_fruits_3 = sorted(fruits, key=lambda fruit: fruit.lower())
# print(f"sorted_fruits_3:", sorted_fruits_3)

# books = [
#     "A Study in Scarlet",
#     "The Sign of the Four",
#     "The Hound of the Baskervilles",
#     "The Valley of Fear",
#     "The Adventures of Sherlock Holmes",
#     "The Memoirs of Sherlock Holmes",
#     "The Return of Sherlock Holmes",
#     "His Last Bow",
#     "The Case-Book of Sherlock Holmes",
# ]

# def print_books(book_list):
#     print("--- book list ---")
#     for book in book_list:
#         print(book)

# print("books unsorted:")
# print_books(books)
# print("-"*30)
# sorted_books_1 = sorted(books)
# print("sorted_books_1")
# print_books(sorted_books_1)
# print("-"*30)

# # custom function for book sorting
# def strip_article(title):
#     # convert to lower case
#     title = title.lower()
#     # strip a, an, the
#     for article in 'a ', 'an ', 'the ':
#         if title.startswith(article):
#             title = title.removeprefix(article)
#             break
#     return title

# sorted_books_2 = sorted(books, key=strip_article)
# print("sorted_books_2")
# print_books(sorted_books_2)


computer_people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

print("unsorted computer people:")
print(computer_people)
print("=== sort computer people ===")
sorted_cp_1 = sorted(computer_people)
print(sorted_cp_1)

# sort by last name (2nd field in tuple)
print("="*20)
sorted_cp_2 = sorted(computer_people, key=lambda cp: cp[1])
print("sorted_cp_2", sorted_cp_2)

# sort by the company name (3rd field in tuple)
print("="*20)
sorted_cp_3 = sorted(computer_people, key=lambda cp: cp[2])
print("sorted_cp_3", sorted_cp_3)

# sort by last, first names - built in function
print("="*20)
def by_last_first(item):
    return item[1], item[0]

sorted_cp_4 = sorted(computer_people, key=by_last_first)
print("sorted_cp_4", sorted_cp_4)



print('Bye')