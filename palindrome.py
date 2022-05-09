'''def is_palindrome(input_string):

	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""

	for i in reversed(input_string[0:]):
		reverse_string+=i

	if input_string != new_string:
		new_string = input_string.replace(" ","")

		reverse_string =reverse_string.replace(" ","")

	# Compare the strings
	if new_string.lower()==reverse_string.lower():
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True'''
animal="Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])