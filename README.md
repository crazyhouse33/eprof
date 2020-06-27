# Eprofiler 0.0
Block profiler.

# Function and motivation

Eprofiler is a tool designed to easely and precisaly time events duration (bloc of code duration)rather than a function of a line. This is also done to work across many process. It's composed a small C library  providing a really basic interface that product primitives outputs. This outputs are processed by eprof executable to produce kvhf files(https://github.com/crazyhouse33/kvhf). This design allow for the lib code to be the most simple, precise and efficient as possible. This allow to code the same 4/5 functions interfaces in your language if you ever need it. Then you can reuse eprof executable and even the generic library tests suits to see how your implementation compete in term of precision and overhead.


# Install

```bash
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

