# i have created this file --salman
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext=request.GET.get('text','default')
    #check the checked buttons
    removepunc=request.GET.get('removepuc','off')
    removenewline=request.GET.get('removenewline','off')
    removeextraspace=request.GET.get('removeextraspace','off')
    capitlize=request.GET.get('capitlize','off')
    count=request.GET.get('count','off')

    if removepunc=='on':
        punctuation='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed+char
        params={'purpose':'Remove text','analyzed_text':analyzed}
        djtext=analyzed

    if removenewline =="on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
            print("pre", analyzed)
        params = {'purpose': 'Remove New line', 'analyzed_text': analyzed}
        djtext=analyzed

    if removeextraspace =="on":
            analyzed=""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index + 1] == " "):

                    analyzed=analyzed+char
            params = {'purpose': 'Remove Extra spaces', 'analyzed_text': analyzed}
            djtext=analyzed

    if capitlize=="on":
        analyzed= ""
        for char in djtext:
            analyzed= analyzed + char.upper()
        params = {'purpose': 'Upper case letters', 'analyzed_text': analyzed}
        djtext=analyzed

    if count=="on":
        analyzed = 0
        for char in djtext:
            analyzed+=1
        params = {'purpose': 'your characters are:', 'analyzed_text': analyzed}
        djtext=analyzed
    if(removepunc!="on" and removenewline!="on" and removeextraspace!="on" and capitlize!="on" and count!="on"):
        return HttpResponse('Error')
    return render(request, 'analyze.html', params)
