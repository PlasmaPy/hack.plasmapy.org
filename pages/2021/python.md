title: Prequel Python Tutorials
hidetitle: True

# Prequel Python Tutorials

In the week before the Hack Week, we are hosting two tutorials to
introduce [Python](https://www.python.org/) to students and scientists
who are new to Python.  These tutorials will be held on Monday, June 21
and Tuesday, June 22 at 15 UTC (4 pm CET / 11 am EDT / 8 am PDT).  Each
tutorial will last about an hour.  This tutorial will be adapted from
Software Carpentry's [Programming with Python
tutorial](https://swcarpentry.github.io/python-novice-inflammation/).

## Tentative schedule

Monday, June 21 at 15 UTC

 * Python fundamentals
 * Reading in data
 * [NumPy](https://numpy.org/) arrays
 * Plotting with [matplotlib](https://matplotlib.org/)  
  
Tuesday, June 22 at 15 UTC

 * Loops
 * Lists
 * Conditionals
 * Functions

## Setup

To follow along with these tutorials, you can either install Python on
your own computer, or access a Binder link that will create an environment
automatically.  

### Getting set up on your own computer

If you would like to follow along with the tutorial on your own computer,
please follow these instructions.

1. Please follow these instructions for
   [installing Anaconda](https://docs.anaconda.com/anaconda/install/).
   When this is done, you should have Anaconda Navigator installed.
2. Create a folder called `python-intro` on your computer.
3. Download [python-novice-inflammation-data.zip](https://swcarpentry.github.io/python-novice-inflammation/data/python-novice-inflammation-data.zip),
   and move the file to `python-intro`.
4. Unzip `python-novice-inflammation-data.zip` into the `python-intro`
   folder.
5. [Open Anaconda Navigator](https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-navigator).
5. Under the "Home" tab on Anaconda Navigator, search for and install
   "Jupyter Notebook".
6. Under the "Environments" tab on Anaconda Navigator, click on the
   arrow for the `base` environment.  Select "Open terminal".
7. Type `pip install numpy matplotlib` to install the necessary packages
   and press enter.   
8. Click on the arrow for the `base` environment again. Select the
   option to "Open with Jupyter Notebook".
9. Navigate to the `python-intro` directory, and enter the `data`
   sub-directory.
10. Under the "New" button (probably near the upper right corner),
    select "Python 3" to open a notebook.   
11. Test the installing by running
   ```Python
   import numpy
   import matplotlib
   data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
   matplotlib.pyplot.plot(data)
   plt.show() 
   ``` 
   Press shift-enter to run the cell.  If you get a fancy plot, you're
   all set!  If you run into any errors, please ask on the 
   [Discord channel for the Hack Week](https://discord.gg/HdsZkp9M35)
   in the `#tutorial-python` channel.

### Binder (no installation required)

Alternatively, you can click on the following binder link to create an
online Python environment that you can run from your web browser.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PlasmaPy/hack-week-python-intro/HEAD)

After the environment initializes, go to the "New" button and select 
"Python 3" to create a new notebook to use for the tutorial.
