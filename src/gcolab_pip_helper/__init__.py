import os, subprocess, sys

def read_token(path_parts):
    """
    Read GitHub access token from a text file on Google Drive.

    Parameters:
      path: Filename path, e.g. "/drive/Colab Notebooks/Tests/github_token.txt"
  
    Returns:
      Token read from the text file
    """
    path = path.replace("/", os.sep)
    token = ""
  
    with open(path, "r", encoding="utf-8") as token_file:
      token = token_file.read().strip()
  
    return token

def pip_install(pkg_name):
    """
    Install a package with pip, akin to `!pip install ...` but use
    the Python kernel. This allos to replace a placeholder in the
    package URL with the GitHub access token like so:

    >>> from google.colab import drive
    >>> drive.mount("/drive")

    >>> import gcolab_pip_helper as gcph
    >>> github_token = gcph.read_token("/drive/Colab Notebooks/Tests/github_token.txt")
    >>> gcph.pip_install("git+https://%s@github.com/User/Repo" % github_token)
    """
    output = subprocess.run([sys.executable, "-m", "pip", "install", pkg_name], capture_output=True)
  
    if output.returncode == 0:
      print("Success!")
    else:
      print("Error! Return code %s" % output.returncode)
      print()
      print("Standard Output:\n  %s\n\n" % output.stdout)
      print("Standard Error:\n  %s\n" % output.stderr)
