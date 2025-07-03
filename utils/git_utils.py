import os
import git
import streamlit as st
from file_methods.csv_file_methods import find_csv_file_location
from file_methods.md_file_methods import find_md_file_location

def setup_git_repo():
    try:
        GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
        repo = git.Repo(".")
        username = "rakshita-vijay"
        repo_url = f"https://{username}:{GITHUB_TOKEN}@github.com/{username}/finance-tracker-streamlit.git"
        repo.remote().set_url(repo_url)
        return repo
    except git.exc.InvalidGitRepositoryError:
        st.error("Not in a Git repository. Make sure you're running from your repo directory.")
        return None

def git_push_csv(csv_relative_path=find_csv_file_location(), commit_message="Update transactions via Streamlit"):
    repo = setup_git_repo()
    if repo is None:
        return False, "Git repo not found."
    try:
        repo.git.add(csv_relative_path)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
        return True, "CSV pushed to GitHub successfully."
    except Exception as e:
        return False, f"Git push failed: {e}"

def git_push_md(md_relative_path=find_md_file_location(), commit_message="Update markdown report via Streamlit"):
    repo = setup_git_repo()
    if repo is None:
        return False, "Git repo not found."
    try:
        repo.git.add(md_relative_path)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
        return True, f"Markdown report pushed to GitHub successfully."
    except Exception as e:
        return False, f"Git push failed: {e}"
