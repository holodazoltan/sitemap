# sitemap
generate sitemap as csv file

## Requirements ##

- git
- python 3.x (you might install it with `pyenv`) + pip
- pipenv

## Install ##

```
$ git clone https://github.com/holodazoltan/sitemap.git
$ cd sitemap
$ pipenv install
```

# usage
```
pipenv run python sitemap.py --url http://www.freshdirect.com/ --csv freshdirect_sitemap.csv
```