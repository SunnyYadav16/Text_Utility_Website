from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'Index Bootstrap.html')


def analyze(request):
    # Getting the text from the textbox
    text_output = request.POST.get('textbox', 'default')

    # Checking the checkbox value
    removepunc_output = request.POST.get('removepunc', 'off')
    fullcaps_output = request.POST.get('fullcaps', 'off')
    newlineremove_output = request.POST.get('newlineremover', 'off')
    spaceremove_output = request.POST.get('spaceremover', 'off')
    charcount_output = request.POST.get('charcount', 'off')

    # Checking which checkbox is ON
    if removepunc_output == 'on':
        punctuation_list = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        analyzed = ""
        for char in text_output:
            if char not in punctuation_list:
                analyzed += char

        params = {'purpose': "Removed Punctuations", 'analyzed_text': analyzed}
        text_output = analyzed

    if fullcaps_output == 'on':
        analyzed = ''
        for char in text_output:
            analyzed += char.upper()

        params = {'purpose': "Changed to Uppercase", 'analyzed_text': analyzed}
        text_output = analyzed

    if newlineremove_output == 'on':
        analyzed = ''
        for char in text_output:
            if char != '\n' and char != '\r':
                analyzed += char

        params = {'purpose': "Removed Newline", 'analyzed_text': analyzed}
        text_output = analyzed

    if spaceremove_output == 'on':
        analyzed = ''
        for index, char in enumerate(text_output):
            if not (text_output[index] == " " and text_output[index + 1] == " "):
                analyzed += char

        params = {'purpose': "Removed Extra Space", 'analyzed_text': analyzed}
        text_output = analyzed

    if charcount_output == 'on':
        analyzed = "The length of your Text is: {}".format(len(text_output))

        params = {'purpose': "Counting Characters", 'analyzed_text': analyzed}

    if removepunc_output == 'off' and spaceremove_output == 'off' and newlineremove_output == 'off' and \
            charcount_output == 'off' and fullcaps_output == 'off':
        return HttpResponse("Error")

    return render(request, "Analyze Bootstrap.html", params)
