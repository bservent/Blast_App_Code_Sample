To Run App:

git clone

cd into app

to start django server run in terminal:

brew install python@3.9 (if you don't already have it)

python3 -m venv .env

source.env/bin/activate

pip3 install -r requirements.txt

python3 manage.py runserver

The application should be running on http://localhost:8000


Technologies in play:
Python,
Django,
postgresql,
Bootstrap4,
Biopython, and 
BLAST API


<img width="1440" alt="Screen Shot 2021-07-13 at 6 56 08 PM" src="https://user-images.githubusercontent.com/69656339/125552611-156af297-a27f-40ee-a3df-7625dace649a.png">

<img width="1436" alt="Screen Shot 2021-07-13 at 6 56 46 PM" src="https://user-images.githubusercontent.com/69656339/125552889-89e8684b-ddad-415d-b0d9-3df8a85aa9bc.png">

<img width="1436" alt="Screen Shot 2021-07-13 at 6 57 11 PM" src="https://user-images.githubusercontent.com/69656339/125552994-dac52a29-3003-47dc-9e7a-120aa2f2ab22.png">



Backend: The first thing I did was acquaint myself with biopython and BLAST for a few hours and make a BLAST query in the terminal using the python shell. After feeling more comfortable with the BLAST API, I decided on my technology stack. I first made a working virtual environment for my Python/Django backend then installed all the dependencies I would need and saved the dependencies in a requirement file. Then I fired up the django server and created the postgresql database. After making sure all of my installed apps were in settings.py, I created a Model to define how the Sequence input. After I was done making my model, I did my migrations. I decided I could easily create a text file with the queryset from the terminal and render it to the browser. I then made the two sample querys in text files and made functions to render them into the browser. If I were to do this over again I would have serialized the xml data into json and used the django_rest_framework to make an internal api so I could parse the data out all pretty. Alas, I did what seemed the quick way out and render the text file into the browser with an HttpResponse.

Frontend: I decided to use server side templates with Django Templating Language. I found my bootstrap cdn and script and added that to my boilerplate. I render the templates into the browser using a specified url pattern that is associated to view functions.

Conclusion: As a junior developer, I am very happy that I got to get my hands on some technology I haven't used before and create an application that is more life science based. Attached some photos so you can see what is going on in the browser if you don't want to fire it up locally.
