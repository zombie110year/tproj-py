from pathlib import Path
from .utils import get_template_dir

from typing import List

def ls_main():
    """列出所有可用的模板归档"""
    for i in get_templates():
        print("{}".format(i.stem))

def get_templates() -> List[Path]:
    template_dir = get_template_dir()
    return list(template_dir.glob("*.zip"))
