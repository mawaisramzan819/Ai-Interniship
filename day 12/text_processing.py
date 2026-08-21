sentence = input("Enter your name and email: ")


def count_words(text):
	"""Count the number of words in the text."""
	return len(text.split())


print(f"Total words in the sentence are: {count_words(sentence)}")


def extract_email(text):
	"""Find and return an email address from the text."""
	for email in text.split():
		if "@" in email and "gmail.com" in email:
			return email


def remove_punctuation(text):
	"""Remove punctuation marks from the text."""
	result = ""
	for char in text:
		if char not in ".,!?":
			result += char
	return result


def title_case(text):
	"""Change the first letter of each word to uppercase."""
	title = text.title()
	return title


def process_text(text, remove_puc=True, title=True):
	"""Remove punctuation and change the text to title case."""
	if remove_puc:
		text = remove_punctuation(text)
	if title:
		text = title_case(text)
	return text


print(process_text(sentence, remove_puc=True, title=True))


def analyze_text(text):
	"""Return the word count, character count, and unique words."""
	clean_text = remove_punctuation(text)
	words_count = len(clean_text.split())
	char_count = len(clean_text)
	unique_words = set(clean_text.lower().split())
	return words_count, char_count, unique_words


words_count, char_count, unique_words = analyze_text(sentence)

print("Words:", words_count)
print("Characters:", char_count)
print("Unique words:", unique_words)
