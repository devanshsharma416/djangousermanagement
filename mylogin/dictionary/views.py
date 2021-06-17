from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def dict(request):
    return render(request, 'dictionary.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    print(meaning)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)
    context = {

        'meaning':meaning['Noun'][0],
        'synonyms':synonyms,
        'antonyms': antonyms
    }

    return render(request, 'word.html', context)