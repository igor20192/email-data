# Script to work with email data

## Mounting
> Installing pipenv

Ubuntu you can install pipenv

    sudo apt install software-properties-common python-software-properties
    sudo add-apt-repository ppa:pypa/ppa
    sudo apt update
    sudo apt install pipenv

In all other cases, in particular on Windows, the easiest way is to install in the user's home directory

    pip install --user pipenv

Now let's check the installation:

    pipenv --version

    pipenv, version 2018.11.26

If you get a similar output, then everything is in order.

Clone the repository

    git clone https://github.com/igor20192/bc387adcbde0d0bacbd547dba57ca857.git

    cd bc387adcbde0d0bacbd547dba57ca857

To create a virtual environment and install dependencies into it, run the following command:

    pipenv sync --dev

If you don't need dev dependencies

    pipenv sync

To "enter" inside the virtual environment, you need to run:

    pipenv shell

## Script Functions

### 1. Show wrong emails

Use commands

    python emailoperations.py --incorrect-emails

or

    python emailoperations.py -ic

### 2. Search for letters by text

Use commands

    python emailoperations.py --search str

    python emailoperations.py -s str

String argument instead of str

### 3. Group emails by domain

Group emails by one domain and arrange domains and emails alphabetically.

Use commands

    python emailoperations.py --group-by-domain

    python emailoperations.py --gbd



     



    





