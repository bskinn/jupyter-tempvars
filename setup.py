import re
from pathlib import Path

from setuptools import setup

NAME = "jupyter-tempvars"

exec_vars = {}
exec(
    Path("src", "jupyter_tempvars", "version.py").read_text(encoding="utf-8"), exec_vars
)
__version__ = exec_vars["__version__"]


doc_version_override = None
media_ref_override = None

media_url_prefix_template = f"https://github.com/bskinn/{NAME}/raw/{{ref}}/media"


def readme():
    content = Path("README.md").read_text(encoding="utf-8")

    new_doc_ver = doc_version_override or "v" + __version__

    new_media_ref = media_ref_override or "v" + __version__
    new_media_url_prefix = media_url_prefix_template.format(ref=new_media_ref)

    def content_update(content, pattern, sub):
        """Perform a case-insensitive regex sub on the given content."""
        return re.sub(pattern, sub, content, flags=re.M | re.I)

    # Docs reference updates to current release version, for PyPI
    # This one gets the badge image
    content = content_update(
        content, r"(?<=/readthedocs/{0}/)\S+?(?=\.svg$)".format(NAME), new_doc_ver
    )

    # This one gets the RtD links
    content = content_update(
        content,
        r"(?<={0}\.readthedocs\.io/en/)\S+?(?=/)".format(NAME),
        new_doc_ver,
    )

    # This replaces all of the href= links to the full-size GIFs in <a> tags
    content = content_update(content, rf'(?<=<a href=")media', new_media_url_prefix)

    # This replaces all of the src= source links for the GIFs in <a> tags
    content = content_update(content, rf'(?<=<img src=")media', new_media_url_prefix)

    return content


setup(
    version=__version__,
    long_description=readme(),
    long_description_content_type="text/markdown",
)
