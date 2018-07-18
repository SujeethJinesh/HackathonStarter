from pygithub3 import Github
import getpass

from credentials.github_credentials import get_github_username


class GitClient:

    def __init__(self):
        self.git_client = self.initialize_git_client()
        self.repo = None

    def _initialize_git_client(self):
        password = getpass.getpass('Insert your password:')
        return Github(login=get_github_username(), password=password)

    def create_repo(self):
        user = self.git_client.get_user()
        self.repo = user.create_repo()
