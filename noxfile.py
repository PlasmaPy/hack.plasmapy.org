"""
Contains configurations for the nox test runner.

To execute the `codespell` session (for example), run:

  pip install nox
  nox -s codespell
"""

import nox

nox.options.sessions = ["codespell"]


@nox.session
def codespell(session):
    session.install("codespell")
    session.run("codespell", "pages", "README.md", "noxfile.py")
