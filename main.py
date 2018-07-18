from github_client.github_client import GitClient
# from gui.gui import Gui


def main():
    # gui = Gui()
    git_client = GitClient()

    git_client.create_repo()


if __name__ == '__main__':
    main()
