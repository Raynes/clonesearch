from getpass import getpass
import github3
from sh import git


def two_factor():
    """Two factor auth callback."""
    return input('Enter two factor authentication code: ')


def login(user):
    """Login to the Github API."""
    password = getpass('Password for {}: '.format(user))
    return github3.login(user, password, two_factor_callback=two_factor)


def clone_repo(repo, to=None):
    """Use sh to clone a git repository on Github."""
    if not to:
        to = repo.name
    print(git.clone(repo.clone_url, to, _err_to_out=True))


def search_repos(g, query):
    """Return a list of repositories matching the search query."""
    results = g.search_repositories(query)
    return [result.repository for result in results]


def main(args):
    """Entry point."""
    g = github3
    user = args['--user']
    if user:
        g = login(user)
    for repo in search_repos(g, args['<query>']):
        if args['--dry-run']:
            print(repo)
        else:
            clone_repo(repo)
