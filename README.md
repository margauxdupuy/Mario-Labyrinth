# Mario Labyrinth

## Setup

- Check if you have Python3 installed on your computer : `python3 --version`
- If you don't have it, run : download the package on `https://www.python.org/downloads/`

- Once you get at least `3.5` as the installed version, you can proceed:

    - Clone this repository : `git clone https://github.com/MargauxDupuy/Mario-Labyrinth.git`
    - Go to the repo : `cd Mario-Labyrinth`
    - Install the requirements : `pip install -r requirements.txt`
    - Launch the game : `python3 labyrinth.py your_username` 


## Rules

The goal is obvious, you must find the peach princess who is lost in this amazing maze.
You can save your score with your name and play another time while keeping your old score.

If you pass level 1, you will get 2 points.
If you pass level 2, you will get 4 points.

Each coin will earn you 1 point.


## Troubleshooting

It's possible that you have issues with pygame (no images on the game), try to install the latest dev release instead : `pip install pygame==2.0.0.dev4`  
