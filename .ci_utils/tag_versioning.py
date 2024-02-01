import git
import os


repo = git.Repo('.')
branch = os.getenv("CI_COMMIT_BRANCH")


def get_latest_tag():
    return str(sorted(repo.tags,
                           key=lambda t: t.commit.committed_datetime)[-1]
               )

def get_current_version(latest_tag):
    if latest_tag[0] == "v" or latest_tag[0] == "V":
        version = latest_tag[1:]
        version_list = [ int(n) for n in version.split('.') if n.isnumeric()]
        if len(version_list) != 3:
                    raise ValueError(f"the tag does not have the right format {latest_tag}")
    elif latest_tag[0].isnummeric():
        version_list = [ int(n) for n in version.split('.') if n.isnumeric()]
        if len(version_list) != 3:
            raise ValueError(f"the tag does not have the right format {latest_tag}")
    else:
       raise ValueError(f"the tag does not have the right format {latest_tag}")
    return version_list

def eval_bump_type():
    commits = list(repo.iter_commits(f'{branch}', max_count=10))
    ind = 0
    if str(commits[0].message).find("Merge") or str(commits[0].message).find("merge"):
        ind = 1
    if str(commits[ind].message).find("#bump_major") > 0:
        bump_type = "major"
    elif str(commits[ind].message).find("#bump_minor") > 0:
        bump_type = "minor"
    elif str(commits[ind].message).find("#no_bump") > 0:
        bump_type= "no_bump"
    else:
        bump_type = "patch"
    return bump_type

def bump_version(version, bump_type):
    if bump_type=="patch":
        version[2] += 1
    elif bump_type=="minor":
        version[1] += 1
        version[2] = 0
    elif bump_type=="major":
        version[0] += 1
        version[1] = 0
        version[2] = 0
    version_list = [str(n) for n in version]
    return '.'.join(version_list)

def push_tag(new_tag):
    for remote in repo.remotes:
        print(f"pushing tag: {new_tag}")
        remote.push(new_tag)


if __name__ == "__main__":
    print(f"branch: {branch}")
    if branch == "main":
        latest_tag = get_latest_tag()
        version = get_current_version(latest_tag)
        head = repo.head
        repo.git.checkout(branch)
        bump_type = eval_bump_type()
        new_version = bump_version(version, bump_type)
        print(f"version: {version}, bump_type: {bump_type}")
        print(f"new_version: {new_version}")
        if bump_type != "no_bump":
            new_tag_name = f"V{new_version}"
            if not new_tag_name in repo.tags:
                print(f"creating the new tag!")
                new_tag = repo.create_tag(f"V{new_version}")
                push_tag(new_tag)
            else:
                print(f"the tag existed: V{new_version}")
            
        repo.git.checkout(head, '--detach')
    else:
        print("it seems it is not on main!")
        latest_tag = get_latest_tag()
        version = get_current_version(latest_tag)
        head = repo.head
        repo.git.checkout(branch)
        bump_type = eval_bump_type()
        new_version = bump_version(version, bump_type)
        print(f"version: {version}, bump_type: {bump_type}")
        print(f"new_version: {new_version}")
        repo.git.checkout(head, '--detach')
