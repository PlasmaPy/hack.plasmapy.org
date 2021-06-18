title: Installing Python for Plasma Hack Week
hidetitle: True

# Installing Python for Plasma Hack Week

The following sets of instructions are intended to get us set up with
Python for the Plasma Hack Week.

## Installation with Anaconda Navigator (recommended) 

1. Please follow these instructions for
   [installing Anaconda](https://docs.anaconda.com/anaconda/install/).
When this is done, you should have Anaconda Navigator installed.
2. Create a folder on your computer for the Hack Week, which we'll call `HackWeek`.
2. Download this
   [`environment.yml`](https://raw.githubusercontent.com/PlasmaPy/hack-week-2021/main/environment.yml)
   to the `HackWeek` folder.
3. [Open Anaconda
   Navigator](https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-navigator).
4. [Create an Anaconda environment](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/#importing-an-environment) 
   with the `environment.yml` file.  This should create a new environment
   called `hackweek` that has everything we need installed in it.
5. Go to the "Environments" tab on Anaconda Navigator, and find the
   `hackweek` environment.  Click on the arrow for that environment, and
   select the option to "Open with Jupyter Notebook".
6. After Jupyter Notebook opens in your web browser, click on the button
   for "New", and click on "Python 3" to open a Python notebook.
7. Test the installation by typing
   ```Python
   import plasmapy
   ```
   and then use shift-Enter to execute the cell.   
   
## Installation with `conda` from the command line

If you have a working installation of `conda` then you can install the 
`hackweek` environment with the following steps.  

1. Open a terminal.
2. Create a folder on your computer for the Hack Week, which we'll call
   `HackWeek`.
2. Download the `environment.yml` file by running
   ```shell
   wget https://raw.githubusercontent.com/PlasmaPy/hack-week-2021/main/environment.yml
3. Run the following command to create the environment.
   ```shell
   conda env create -f environment.yml
   ```
4. Activate this environment by running
   ```shell
   conda activate hackweek
   ```
5. Test the installation    

## Binder link



[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PlasmaPy/hack-week-environment-2021/HEAD)
