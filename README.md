# Mario Labyrinth

## Setup (macOS)

- Check if you have Python3 installed on your computer : `python3 --version`
- If you don't have it, run : use Homebrew with `brew install python3` or download the package `https://www.python.org/ftp/python/3.8.1/python-3.8.1-macosx10.9.pkg`

- Once you get at least `3.5` as the installed version, you can proceed:

    - Clone this repository
    - Install the requirements : `pip install -r requirements.txt`
    - Launch the game : `python3 labyrinth.py your_username` 


## Rules

The goal is obvious, you must find the peach princess who is lost in this amazing maze.
You can save your score with your name and play another time while keeping your old score.

If you pass level 1, you will get 2 points.
If you pass level 2, you will get 4 points.

Each coin will earn you a point.


## Troubleshooting

It's possible that you have issues with pygame (no images), try to install the latest dev release : `pip install pygame==2.0.0.dev4`  
