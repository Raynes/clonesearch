# clonesearch

Clonesearch is a little tool written in Python that lets you run a search query
on Github repositories and then clone those repositories.

## Usage

clonesearch is targeted at Python 3 and no effort is being put forth to be
compatible with Python 2. If it is, it is purely coincidental.

```
sudo pip install clonesearch
```

This will get you a program called `clones`.

```
$ clones -h
A tool for cloning repos matching a search query.

Usage:
  clones <query> [-u <user> | --user <user>] [-d | --dry-run]

Options:
  -u <user>, --user <user>   Specify the user to authenticate with.
  -d, --dry-run              Only print repositories that would be cloned.
```

Here is an example run:

```
$ clones 'user:Raynes language:Python' -d
Raynes/pygments-tomorrow-night-bright
Raynes/pyheap
Raynes/accessall
Raynes/pydiff
```

We passed the -d option to tell clonesearch that we wanted to do a dry run and
not clone any repositories. Instead, the repositories are listed so we can make
sure our search query gets us only the repos we want.

Now let's do the real thing:

```
$ clones 'user:Raynes language:Python'
Cloning into 'pygments-tomorrow-night-bright'...
remote: Reusing existing pack: 14, done.
remote: Total 14 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (14/14), done.
Checking connectivity... done.

Cloning into 'pyheap'...
remote: Reusing existing pack: 37, done.
remote: Total 37 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (37/37), done.
Checking connectivity... done.

Cloning into 'accessall'...
remote: Counting objects: 56, done.
remote: Compressing objects: 100% (36/36), done.
remote: Total 56 (delta 26), reused 46 (delta 16)
Unpacking objects: 100% (56/56), done.
Checking connectivity... done.

Cloning into 'pydiff'...
remote: Reusing existing pack: 65, done.
remote: Total 65 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (65/65), done.
Checking connectivity... done.
```

Simple enough, right? If you need to work with private repositories you can pass
the `-u` option to authenticate. It even supports two factor authentication
thanks to the awesome [github3.py](https://github.com/sigmavirus24/github3.py)
library:

```
$ clones 'user:Raynes language:Python' -u Raynes
Password for Raynes:
Enter two factor authentication code:
...
```

That about covers it! Happy cloning!
