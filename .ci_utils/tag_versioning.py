"""
The versioning based on the repo tags
"""

__author__ = "Frauen-Leben-Freiheit"
__version__ = "0.0.1"

import os
import git


cwd = os.getcwd()
parent_dir = os.path.dirname(cwd)
print(f"Current working directory: {cwd}")
print(f"Parent directory: {parent_dir}")
the_repo = git.Repo(parent_dir, search_parent_directories=True).git
the_branch = os.getenv("CI_COMMIT_BRANCH")

# if the bump_type is bump_patch, it will bump the patch version
# if the bump_type is bump_minor, it will bump the minor version
# if the bump_type is bump_major, it will bump the major version
class TagBump:
    def __init__(self, latest_tag: str, bump_type: str):
        """
        Args:
            latest_tag (str): The latest tag of the repo
            bump_type (str): The type of the bump
        """
        if latest_tag[0] != "V":
            raise ValueError("The tag should start with V")
        if len(latest_tag.split('.')) != 3:
            raise ValueError("The tag should have 3 parts")
        self.latest_tag = latest_tag
        self.version = [int(val) for val in latest_tag[1:].split('.')]
        self.bump_type = bump_type
        self.updated_tag = None
    
    def _bump_minor(self):
        """Bump the minor version"""
        self.version[1] += 1
        self.version[2] = 0

    def _bump_major(self):
        """Bump the major version"""
        self.version[0] += 1
        self.version[1] = 0
        self.version[2] = 0
    
    def _bump_patch(self):
        """Bump the patch version"""
        self.version[2] += 1
    
    def bump_version(self) -> str:
        """Bump the version based on the bump_type"""
        if self.bump_type=="bump_patch":
            self._bump_patch()
        elif self.bump_type=="bump_minor":
            self._bump_minor()
        elif self.bump_type=="bump_major":
            self._bump_major()
        else:
            raise ValueError("The bump_type should be bump_patch, bump_minor or bump_major")
        self.updated_tag = f"V{'.'.join([str(val) for val in self.version])}"
        return self.updated_tag

    def apply_tag(self):
        """Apply the tag to the repo"""
        the_repo.tag(self.updated_tag,
            ref=the_branch, message=f"Version {self.updated_tag} is created")
        the_repo.push("--tags")
        # the_repo.git.push(the_branch)

if __name__ == "__main__":
    latest_tag = os.environ.get("LATEST_TAG")
    bump_type = os.environ.get("BUMP_TYPE")
    print(f"LATEST_TAG: {latest_tag}")
    print(f"BUMP_TYPE: {bump_type}")    
    tag_bump = TagBump(latest_tag, bump_type)
    UPATED_TAG = tag_bump.bump_version()
    print(f"UPATED_TAG: {UPATED_TAG}")
    os.environ["UPDATED_TAG"] = UPATED_TAG
    print(f"{os.getenv('UPDATED_TAG')}")
    tag_bump.apply_tag()

