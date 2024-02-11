"""
The versioning based on the repo tags
"""

__author__ = "Frauen-Leben-Freiheit"
__version__ = "0.0.1"

import os

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
        if latest_tag.split('.').count != 3:
            raise ValueError("The tag should have 3 parts")
        self.latest_tag = latest_tag
        self.version = latest_tag[1:].split('.')
        self.bump_type = bump_type
    
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
        return f"V{'.'.join(self.version)}"


if __name__ == "__main__":
    latest_tag = os.environ.get("LATEST_TAG")
    bump_type = os.environ.get("BUMP_TYPE")
    tag_bump = TagBump(latest_tag, bump_type)
    os.environ["UPDATED_TAG"] = tag_bump.bump_version()
