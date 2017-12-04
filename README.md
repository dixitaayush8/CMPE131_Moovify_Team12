# CMPE131_Moovify_Team12

Do the following procedures in order:

If you are running this application on Windows, download and install/"repair" [Microsoft Visual C++ Compiler for Python 2.7](https://www.microsoft.com/en-us/download/details.aspx?id=44266). If you are running this application on MacOS, no need to install C++ compiler because it is built-in.

To ensure that this project works (see requirements.txt for reference): 
1. download and install [Python 2.7](https://www.python.org/downloads/release/python-2713/). If using Windows, set appropriate paths in environment variables after installing Python 2.7.

2. Install Django (pip install django after installing Python 2.7).

3. Install the [IMDBPy API](https://github.com/alberanid/imdbpy) (pip install git+https://github.com/alberanid/imdbpy).

To run the project, download or clone this project and unzip the zip file of the project. Afterwards, on Terminal/Command Prompt, navigate to the directory of the project, type in "python manage.py runserver", and copy and paste the link displayed on the console to your browser.

Completed functional requirements:
1. Users can log in or register.
2. Users can search for movies by title, alphabetical order, release date, or genre. (Login is optional for searching.)
3. User can select a movie after searching for a movie and see information displayed about the movie. Unique URL used for each movie.
4. User can comment reviews about movies.
5. User can rate movies on a scale from 0 to 10 (decimals included) while reviewing.
6. User can get search recommendations for movies based on the movies they gave positive reviews to.