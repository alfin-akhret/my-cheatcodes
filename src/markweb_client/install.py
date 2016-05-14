#!/usr/bin/env python
# seems I need to use PyGithub to fetch from github repo
# reference: http://sookocheff.com/post/tools/downloading-directories-of-code-from-github-using-the-github-api/

# logging to github
from github import Github, GithubException
from config import githubCredentials
import base64

def install():

    github = Github(githubCredentials['username'], githubCredentials['password'])
    user = github.get_user()

    # accessing repo
    repo_name = 'my-cheatcodes'
    repository = user.get_repo(repo_name)

    # branch to download
    branch_name = 'master'
    sha = get_sha_for_tag(repository, branch_name)

    # directory to download
    directory_to_download = 'src/markweb_skeleton'
    download_directory(repository, sha, directory_to_download)

def get_sha_for_tag(repository, tag):
    """
    Returns a commit PyGithub object for the specified repository and tag.
    """
    branches = repository.get_branches()
    matched_branches = [match for match in branches if match.name == tag]
    if matched_branches:
        return matched_branches[0].commit.sha

    tags = repository.get_tags()
    matched_tags = [match for match in tags if match.name == tag]
    if not matched_tags:
        raise ValueError('No Tag or Branch exists with that name')
    return matched_tags[0].commit.sha

def download_directory(repository, sha, server_path):
    """
    Download all contents at server_path with commit tag sha in 
    the repository.
    """
    contents = repository.get_dir_contents(server_path, ref=sha)

    for content in contents:
        print "Processing %s" % content.path
        if content.type == 'dir':
            download_directory(repository, sha, content.path)
        else:
            try:
                path = content.path
                file_content = repository.get_contents(path, ref=sha)
                file_data = base64.b64decode(file_content.content)
                file_out = open(content.name, "w")
                file_out.write(file_data)
                file_out.close()
            except (GithubException, IOError) as exc:
                logging.error('Error processing %s: %s', content.path, exc)

if __name__ == '__main__':
    install()