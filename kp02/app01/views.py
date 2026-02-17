from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def response(request):
    return HttpResponse('Hello world')

def response_text(request):
    # with open('./temp.html', 'r') as f:
    #     html_text = f.readlines()
    html_text = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text</title>
    <style>
        h1 {text-align: center;}
        p {text-align: center;}
        div {text-align: center;}
    </style>
</head>
<body>
    <h1>Static Web Page</h1>
    <p>Crated by <br> Oleh Kozyr</p>    
</body>
</html>
'''

    return HttpResponse(html_text)