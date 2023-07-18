# GitVisualizer

A simple tool to visualize the git history of a repository. 

## Design 

### main.py

This module is responsible for executing the visualization construction and opening the visualization in the browser.

### server.py

This module is responsible for starting up the server to display the visualization on a thread
and passing the endpoint to main.py which can open it in the browser.

