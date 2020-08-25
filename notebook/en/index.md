
# Jupyter Notebooks

Next we'll do a very brief introduction on [Jupyter notebook](http://jupyter.org/),
which you will need for the machine learning assignment this week. These
notebooks allow a mixture of nicely formatted text and *Python* code.

First, you should install *Jupyter* using *Anaconda*.

    conda install -c conda-forge jupyterlab

Next, downloading the assignment file below.

[Right-click and save the assignment notebook file here](../data/notebook.ipynb)

## Starting a Notebook server

Open you terminal in the directory where you downloaded the file and run the
command

    jupyter notebook

This will print some information about the *Notebook* server in the terminal,
and open a web browser to the URL of the web application. By default this is
[http://127.0.0.1:8888](http://127.0.0.1:8888). Note that *127.0.0.1* is the
home ip-adress, so this is now a webpage running on your own computer!

This first page shows the dashboard, which lists the notebooks available in the
current directory. You can create new notebooks from the dashboard with the
`New` button (select *Python 3* notebook), or open existing ones. Creating a
new notebook will create a new file `Untitled1.ipynb`, where the extension
`.ipynb` indicates it is a notebook file.

## Running the notebook assignment

Now, using the dashboard in the your webbrowser, open the file you saved,
which was called `notebook.ipynb`. The rest of the assignment instructions are
written in that notebook.

You do not need to hand in your notebook form this short assignment, as it just
an introduction for the machine learning assignment this week.
