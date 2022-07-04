Google Colab Pip Helper
=======================

This is just a small utility to help installing python libraries from a private
git repository (on GitHub) in Google Colab. This requires a "Personal Access Token"
to be generated in GitHub and used as part of the package url, like this:

`!pip install git+https://Token@github.com/User/Repo`

The problem with this approach is, that the token is exposed in the Colab notebook.
This library thus allows to put the access token in a separate text file and use
that for the installation.

  1. Create a new personal access token in GitHub with "repo" authorization
  2. Save the access token to a text file in your Google Drive
  3. Install the private library in your notebook like this:

     ```python
     import gcolab_pip_helper as gcph
     github_token = gcph.read_token(("Colab Notebooks", "Tests", "github_token.txt"))
     gcph.pip_install("git+https://%s@github.com/User/Repo" % github_token)
     ```

This is basicaly a simpified version of [colab-utils](https://github.com/namiyousef/colab-utils).

Copyright
---------

This code is relased under the public domain.