title: Software Installation for Plasma Hack Week
hidetitle: True

# Software Installation for Plasma Hack Week

This page contains instructions for installing software to be used
during Plasma Hack Week. In addition, here are installation links for

- [BOUT++](https://bout-dev.readthedocs.io/en/latest/user_docs/installing.html)
- [Gkeyll](https://gkeyll.readthedocs.io/en/latest/install.html)
- [OMFIT](https://omfit.io/install.html)

## `git`

There are several ways to obtain `git` for your specific operating systems.
`git` provides a great download page, <https://git-scm.com/downloads>, that
outlines these methods, or provides a direct download when applicable.

We also recommend that you [create a free GitHub account](https://github.com/join)
in order to follow along with many of the tutorials.

## Python

### Installation with Anaconda Navigator (recommended)

The following instructions are designed to help us set up a Python
environment with several of the packages to be discussed during the Hack
Week.

1. Please follow these instructions for
   [installing Anaconda](https://docs.anaconda.com/anaconda/install/).
   When this is done, you should have Anaconda Navigator installed.

1. Create a folder on your computer for the Hack Week, which we'll call
   `hackweek`.

1. Download this
   [`environment.yml`](https://raw.githubusercontent.com/PlasmaPy/hack-week-2021/main/environment.yml)
   file to the `hackweek` folder. You might need to use the "save page
   as" option from your web browser menu.

1. [Open Anaconda
   Navigator](https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-navigator).

1. Under the "Home" tab on Anaconda Navigator, search for and install
   "Jupyter Notebook".

1. [Create an Anaconda environment](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/#importing-an-environment)
   for the Hack Week.

   - Select the "Environment" tab.
   - Below the list of environments, click "Import".
   - Click the file folder icon.
   - Navigate to and select the `environment.yml` (possibly in your
     `Downloads` folder).
   - Click "Import".

1. Under the "Environments" tab on Anaconda Navigator, find the
   `hackweek` environment. Click on the arrow for that environment, and
   select the option to "Open with Jupyter Notebook".

1. After Jupyter Notebook opens in your web browser, click on the button
   for "New", and click on "Python 3" to open a Python notebook.

1. Test the installation by typing

   ```
    import plasmapy
   ```

   and then press shift-Enter to execute the cell. This should run
   without giving any errors.

### Installation with `conda` from the command line

If you have a working installation of `conda` then you can install the
`hackweek` environment with the following steps.

1. Open a terminal.

1. Create a folder on your computer for the Hack Week, which we'll call
   `hackweek`. Enter that folder.

1. Download the `environment.yml` file by running

   <pre class="code literal-block">
    wget https://raw.githubusercontent.com/PlasmaPy/hack-week-2021/main/environment.yml
    </pre>

1. Run the following command to create the environment.

   <pre class="code literal-block">
    conda env create -f environment.yml
    </pre>

1. Activate this environment by running

   <pre class="code literal-block">
    conda activate hackweek
    </pre>

1. Test the environment by running

   <pre class="code literal-block">
    jupyter notebook
    </pre>

   In the Jupyter notebook, run

   ```
    import plasmapy
   ```

### Binder link

If you run into any problems with installation, you can also create a
Binder environment to access a Python environment from your web browser.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PlasmaPy/hack-week-environment-2021/HEAD)

## Integrated development environments

An integrated development environment (IDE) is software used for code
development. IDEs typically include a source code editor as well as
built-in tools for refactoring, version control, running tests, and
debugging.

- [PyCharm](https://www.jetbrains.com/pycharm/download)
  - Community version is free and open source
  - To be used during git & GitHub and clean coding tutorials
- [Visual Studio Code](https://code.visualstudio.com/)
  - Community version is free and open source
- [Atom](https://atom.io/)
  - Full version is open source

## Unix shell

Python and `git` are often used from the Unix shell, which is one of the
most commonly used command line interfaces. Here are instructions on
[installing and/or accessing the bash
shell](https://carpentries.github.io/workshop-template/#shell), which is
one of the most commonly used Unix shells.
