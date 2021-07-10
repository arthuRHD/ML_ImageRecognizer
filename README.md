# ATA Project

![Python application](https://github.com/arthuRHD/projet-ata/workflows/Python%20application/badge.svg)

A Django application that classify sended pictures with TensorFlow and store them with MongoDB
The frontend is made with a sexy design, UX/UI 2020 friendly

## Classnames

- Humans
- Cars
- Plants
- Fictional characters
- Animals

## Install

```sh
cd projet-ata
pip install -r requirements.txt
```

## Config

Create a mongodb database nammed `ata`

```sh
mongo
> use ata
```

Migrate django models to the database

```sh
python3 manage.py migrate
```

## Usage

Launch the django app

```sh
cd projet-ata
python3 manage.py runserver 0.0.0.0:8000
```

Go to [this page](http://localhost:8000/upload)

## Only test model

Launch the python file in terminal and specify the path of the tested picture

```sh
python3 frontend/ml/test.py /home/arthur/bmw.jpeg
```

Appreciate the results

![demo_img](templates/demo_img.png)

## Contributors

RICHARD Arthur, HAVARD Antoine, ROYANT Tom
