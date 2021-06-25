from django.shortcuts import render
from django.http import HttpResponse

with open(r'C:\Users\User\PycharmProjects\GamblingSim\epiclbdata.txt', 'r') as firstmoners:
    fileread = str(firstmoners.read())
    filesplit = fileread.split('\n')
    name1 = filesplit[int(len(filesplit) - 1)]
    money1 = filesplit[0]

# Create your views here.
def index(response):
    return render(response, "Leaderboard/table.html", {"name1": name1, "money1": money1, "name2": None, "money2": None})

def home(response):
    return HttpResponse("<h1>Welcome to the official Gambling Simulator website!</h1>Developed by Ali Kaddaha 8E<br></br><br></br><a href=\"http://127.0.0.1:8000/downloads/\"><button>Download the simulator!</button></a><a href=\"http://127.0.0.1:8000/leaderboard/\"><button>Leaderboard</button></a>")

def downloads(response):
    return HttpResponse("<h1>Downloads</h1>\n<br><h3>Test releases</h3>\n•\t<a href=\"https://drive.google.com/u/0/uc?export=download&confirm=BpqJ&id=1fEcecZG271NfqWShVUE5w3Blv26bKZKn\">Release 5.4.1</a><h3>Official releases</h3>\n•\t<a href=\"https://drive.google.com/u/0/uc?export=download&confirm=9pAe&id=1y6HuEeoodGSAMiSoQC5JiBlvYHlYzFkB\">Release 5.4</a><br><br></br><a href=\"http://127.0.0.1:8000\"><button>Back to home</button></a>")
