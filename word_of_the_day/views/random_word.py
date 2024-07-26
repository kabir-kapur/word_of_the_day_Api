import nltk
import random
import ssl

from django.http import JsonResponse
from nltk.corpus import words

def main(request):
	download_nltk_corpus()
	word = random_word()
	print(word)
	response = JsonResponse({"word": word})
	return response

def random_word():
	"""Generate a random word from the words.words() default corpus."""
	corpus = words.words()

	return random.choice(corpus)

def download_nltk_corpus():
	"""Create an ssl context and then download the nltk corpus."""
	try:
		_create_unverified_https_context = ssl._create_unverified_context
	except AttributeError:
		pass
	else:
		ssl._create_default_https_context = _create_unverified_https_context

	nltk.download('words')