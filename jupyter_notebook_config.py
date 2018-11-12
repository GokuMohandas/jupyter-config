# Configuration file for Jupyter Notebooks
# __author__: Goku Mohandas
#

import os
from IPython.lib import passwd

c = get_config()

# Don't open browser at launch
c.NotebookApp.open_browser = True

# Port to open Jupyter Notebook
c.NotebookApp.port = 8888

# # Notebook directory
# c.NotebookApp.notebook_dir = "%s/notebooks"%(os.environ['CODE_PATH'])

# c.NotebookApp.password = passwd('password')
c.NotebookApp.token = ''