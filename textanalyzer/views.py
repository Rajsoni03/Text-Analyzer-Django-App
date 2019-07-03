#I create this file - raj
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def analyze(request):

    #get the text
    analyzed = request.POST.get('text', '')

    #check box values
    removepunc = request.POST.get('removepunc', 'off')
    capfull = request.POST.get('capfull', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    #analyzing
    if (analyzed != ''):
        alartState = 'alert-success'
        alartMsg1 = 'Successfully Analyzed,'
        alartMsg2 = ' Here The Text...'

        if removepunc == 'on':
            punctations='''!()-[]{}:;'"\/,<>.?@#$%^&*_+=~'''
            finaltext = ''
            for char in analyzed:
                if char not in punctations:
                    finaltext = finaltext + char
            analyzed = finaltext

        if (spaceremove == 'on'):
            finaltext = ''
            for index, char in enumerate(analyzed):
                if not (analyzed[index] == ' ' and analyzed[index+1] == ' '):
                    finaltext = finaltext + char
            analyzed = finaltext

        if (newlineremove == 'on'):
            finaltext = ''
            for char in analyzed:
                if char !='\n' and char != '\r':
                    finaltext = finaltext + char
            analyzed = finaltext

        if capfirst == 'on':
            analyzed = analyzed.title()

        if capfull == 'on':
            analyzed = analyzed.upper()

        if charcount == 'on':
            analyzed = len(str(analyzed).split())

    else:
        alartState = "alert-danger"
        alartMsg1 = 'Empty Text!'
        alartMsg2 = 'Please Type Again'

    para = {'porpose': (('Remove Punctuation' if removepunc=='on' else '')
                        +('\nCapitilize Full' if capfull=='on' else '')
                        +('\nCapitilize First' if capfirst=='on' else '')
                        +('\nNew Line Remove' if newlineremove=='on' else '')
                        +('\nSpace Remove' if spaceremove=='on' else '')
                        +('\nChar Count' if charcount=='on' else '')),
            'analyzed_text': analyzed,
            'alartState' : alartState,
            'alartMsg1': alartMsg1,
            'alartMsg2': alartMsg2,
            }

    return render(request,'analyze.html',para)

'''
def charcount(request):
    return HttpResponse("<h1>charcount Pge</h1>")
'''