from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
    return HttpResponse('<h1>This is my home page</h1>')      

def aboutus(requests):
    return HttpResponse('<h1>I am a third-year BE student from Vasavi College of Engineering</h1>')

def hobbies(requests):
    return HttpResponse('<h1>My Hobbies are:</h1> <ul><li>I watch TV shows.</li><li> I am an avid online consumer. So, I read many articles, watch documentaries on the Internet.</li><li>I play Football in my backyard everyday.</li><li>I spend a considerable amount of time in learning a new course. Currrently, I am onto Machine Learning.</li></ul>')




