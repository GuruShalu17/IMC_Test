name1 = input("Enter the first name: ")
name1_capitalized = name1.capitalize()
name2 = input("Enter the second name: ")
name2_capitalized = name2.capitalize()
name3 = input("Enter the third name: ")
name3_capitalized = name3.capitalize()


print(f"The names are: {name1_capitalized}, {
      name2_capitalized} and {name3_capitalized}")

# Remove spaces
name4 = input("Enter the first name: ")
name4_formatted = name4.strip().capitalize()

print(f"The name without space are: {name4_formatted}")


# remove comma in numbers

x = input("Give me a number to multiple by 10: "). replace(",", "")

print(int(x) * 10)
