from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def hello(request):
    sentence = request.GET['sentence']
    wordList = sentence.split(",")
    return render(request, 'hello.html',{'fulltext' : sentence, 'count' : len(wordList) , 'wordList': wordList })



 