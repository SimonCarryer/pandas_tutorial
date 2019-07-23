# An Opinionated Pandas Tutorial

Welcome! Pandas is by far the most popular way of manipulating and visualising data in Python, and this is a tutorial about how to use it for that purpose. But it's not just any tutorial! It's an *opinionated* tutorial! What do I mean by "opinionated"? I'm glad you asked. Pandas, like many things in programming, gives you approximately a hundred different ways of achieving any given outcome. For any goal you can name, there's probably several perfectly valid ways of doing it, and a host of people who would make strong arguments for one way over another. Furthermore, Pandas is a bit of an odd-ball. Some of the ways that you write Pandas code looks quite odd to experienced Python developers. That's a legacy of the background and experience of some of the first people to work on Pandas. It's not bad or wrong, but it is a bit strange. The consequences of both those things are that working with Pandas, and especially reading other people's code (and your own code from six months ago) is often extremely confusing. It's very easy to get to a point where you know *how* to do a lot of things in Pandas, but can't necessarily explain *why* it works.

This tutorial aims to identify a *single*, *best* approach for achieving several common operations in Pandas. It won't delve into every part of the library, but rather give you tools for solving particular common problems. What I *will* delve into is some of the working behind these methods and objects. A little bit of extra time spent understanding the core processes that make these methods work will pay off in a better understanding of how to use and extend these methods. Even if you already know and use Pandas, I hope that you'll benefit from a deeper understanding of these methods.

## Where am I?
You're reading a "readme" file in a Github repository. Github is hosting this file, and several others that make up this Pandas tutorial. There are a couple of options for running this code. The easiest is to run it in Google Colab - everything runs online, in your browser. The trickier way is to download this repository, install Python, and run it on your own machine.

## Run in Google Colab

Google Colab is a neat tool that lets you run code in your browser, using Google's servers. You can open each of the tutorials from this page.

#### Part One

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SimonCarryer/pandas_tutorial/blob/master/Part%20One%20-%20Rows%20and%20Columns.ipynb)

#### Part Five

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SimonCarryer/pandas_tutorial/blob/master/Part%20Five%20-%20Dates%20and%20Times.ipynb)


## Run Locally

You can download this code and run it on your own machine, but there are a few steps you'll have to complete first. These steps are *much* more difficult than anything in this tutorial, so don't get discouraged. Take a bit of time to read through the instructions linked below, and get a sense of what you're going to do, and how it works.

### Step One: Github

Github is a version management tool, and an essential skill for any developer, analyst, or data scientist. It's worth investing a little time in understanding the basics of Git.

* Install Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
* Create a (free) Github account: https://github.com/join
* Clone this repository: https://help.github.com/en/articles/cloning-a-repository

### Step Two: Get Pandas and Jupyter Notebook

Pandas is a "library" in the Python programming language - an extra set of commands you can use. "Jupyter Notebook" is a tool for helping you write and run Python commands, and in particular it's helpful for visualising and manipulating data with Pandas. The best way to get all three of Python, Pandas, and Jupyter Notebook is by downloading and installing something called "Anaconda" - a Python "Distribution".

There are two ways of doing this: The right way, and the easy way. If you're pretty new to software development and writing code, I suggest you go with the easy way. If you're an experienced developer and the words "versioning issues" make you shudder, go with the right way.

#### The Easy Way

*For Windows*: 
Follow this guide https://www.datacamp.com/community/tutorials/installing-anaconda-windows, but note that:
- you should choose Python 3
- you DO want to add Anaconda to your PATH variable

*For Mac*:
Follow this guide: https://www.datacamp.com/community/tutorials/installing-anaconda-mac-os-x, and
- make sure you choose Python 3

#### The Right Way

Actually I don't even know. Something to do with PyEnv? Or is it better to use conda? Nobody seems to have an answer.

### Step Three: Open the Tutorials

You'll want to open a terminal window (on a mac) or Command Prompt (on Windows) and navigate to the "pandas_tutorial" folder. Then you can type `jupyter notebook` to start up the notebook kernal. Then in your browser, you'll be able to open and run the tutorials.

