from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d = {
        'name': 'john Doe',
        'age': 30,
        'birthday': datetime.datetime.now(),
        'hobbies': "",
        'languages': ['English', 'Spanish', 'French'],
        'friends':  [
            {
                'name': 'Jane Doe',
                'age' : 28
            },
            {
                'name': 'Alice Johnson',
                'age' : 29

            },
            {
                'name': 'Bob Smith',
                'age' : 25
            }  
        ],
        'occupation': "I'm working as a Software Developer",
        'education': {
            'high_school': 'ABC High School',
            'university': 'XYZ University',
            'degree': 'Bachelor of Science in Applied Mathematics',
        },
    }
    return render(request, 'app/home.html', d)
