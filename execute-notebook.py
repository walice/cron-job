import papermill as pm
import os

cwd = os.getcwd()

pm.execute_notebook(cwd + "/cron-job/index.ipynb",
                    cwd + "/cron-job/index.ipynb")
