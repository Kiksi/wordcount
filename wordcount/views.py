from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import operator
from django.urls import reverse


def home (request):
     return render(request, 'home.html')

def count(request):
     if not 'fulltext' in request.GET:
         return HttpResponseRedirect(reverse('home'))
     fulltext = request.GET['fulltext']
     wordlist = fulltext.split()
     worddictionary = {}
     for word in wordlist:
         if word in worddictionary:
             #Increase
             worddictionary[word] += 1
         else:
             #add to the dictionary
             worddictionary[word] = 1
         sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)
     return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':worddictionary.items()})
def about(request):
    return render(request, 'about.html')
