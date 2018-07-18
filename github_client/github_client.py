from pygithub3 import Github
import getpass

from credentials.github_credentials import get_github_username


class GitClient:

    def __init__(self):
        self.git_client = self._initialize_git_client()
        self.repo = None

    def _initialize_git_client(self):
        password = getpass.getpass('Insert your password: ')
        return Github(login_or_token=get_github_username(), password=password)

    def create_repo(self):
        user = self.git_client.get_user()
        repo_name = input("What is the name of your hackathon project? ")
        # need 2fa at this point
        # http://pygithub3.readthedocs.io/en/latest/repos.html#pygithub3.services.repos.Repo.create
        self.repo = user.create_repo(repo_name)
