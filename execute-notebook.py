import papermill as pm
import os

cwd = os.getcwd()

pm.execute_notebook(cwd + "/index.ipynb",
                    cwd + "/index.ipynb")
