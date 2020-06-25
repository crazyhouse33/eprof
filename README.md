# Eprofiler 0.0
Easely exstensible bloc profiler.

# Function and motivation

Eprofiler is a tool designed to easely and precisaly time events duration (bloc of code duration)rather than a function of a line. This is also done to work across many process. It's had been done in C for my needs, but you can easely create modules for your prefered languages that mimic the C lib (~50 lines)

# Install

```bash
git clone https://github.com/crazyhouse33/authbreak
cd authbreak/build
cmake ..
make authbreak
```

The binary ends up in the bin directory.

# Usage

authbreak -h for a complete explanation of how this version works.

# Coming

1. Automatic timing attack
2. Big and small performance improvement (use a thread to categorize the previous output and prepare the next while the current one is running, collect only metrics useful to the used classifiers, cache the loading (idk how yet) of the targeted process)
3. User interface improvement (press key to print state, pause and continue later at any interruption, use a more powerful front for classfiers --NOT --success time<5 --success out=="tata" --OR --sucess time=<4, Others classifiers (regexp match, return status))
4. Various furtive control options (hidden cartesian product, waiting in between actions with automatic adjustement in function of previous responses)
5. More control over what's done (pass some attacks )
6. For the file template, filter the guesses to match given charset and len
7. Make it cross platform 

# Repo

Each version of authbreak is a commit in the master branch. The version changelog is the git log of master branch. 

The dev branch contains additional continuous integration files, and has a usual git messy history :)

