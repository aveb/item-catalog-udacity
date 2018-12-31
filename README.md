# Catalog App

An app that displays 9 common sports along with items related to each.  Users may create, edit and delete items in the Catalog.  Users may not edit or delete items that they have not created.

## Prerequisites

You will need have the following installed on your machine before running ```app.py```: 

- You must have Python 2 installed.  You can find detailed instalation instructions and a link to the download [HERE](https://www.python.org/downloads/)
- ```app.py``` runs on a linux-based virtual machine called ```VirtualBox```.  You can download it for free [HERE](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
- After installing ```VirtualBox```, you will need to download an additional tool: ```Vagrant```.  This software allows you to share files between your host and virtual machine.  You can read more and download ```Vagrant``` [HERE](https://www.vagrantup.com/downloads.html)

## Configuring the Database

The ```Catalog App``` requires you to first create and configure the database.  Inside your VM, run from the terminal:

        $ python db_setup.py

Next, populate the database with the 9 sports categories and a few common items.  From the terminal inside your VM run: 

       $ python add_categories.py
       
## Starting ```Catalog App``` Server

The ```Catalog App``` runs on your local machine on ```Port 5000```.  To start the server, run from the terminal:

       $ python app.py

## Opening ```Catalog App```

Open your favorite browser and go to [http://localhost:5000/](http://localhost:5000/)

## Accessing ```Catalog App API```

Two API endpoints are available for developers:

1. Access JSON file of ```All Categories```.  Use this link: [http://localhost:5000/catalog/JSON/](http://localhost:5000/catalog/JSON/)
2. Access JSON file of ```All Items```.  Use this link: [http://localhost:5000/catalog/items/JSON/](http://localhost:5000/catalog/items/JSON/)
