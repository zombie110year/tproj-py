"""创建模板归档
"""

import zipfile
from pathlib import Path

from typing import Union
from typing import List

from .utils import parse_cfg

__all__ = (
    "create_main",
)


def create_main(name: Union[str, NoneType], src: str, force: bool):
    """根据当前工作目录的内容创建模板归档

    :param str name: 命令行传入的模板归档的命名
    :param str src: 要打包的目录
    :param bool force: 是否强制覆写已存在的同名归档
    """
    src_path = Path(src)
    cfg_path = Path(src_path / "tproj.yml")
    if cfg_path.exists():
        cfg = parse_cfg(cfg_path.read_text())
    else:
        cfg = parse_cfg(None)
    if cfg.get("name") == "":
        name = input("Template Name: ").strip()

    files = read_src_dir(src_path, cfg.get("include"))

def read_src_dir(src: Path, include: List[str], exclude: List[str]) -> List[Path]:
    """递归地读取源目录中所有文件

    :param src: 源目录
    """
    include_files = sum([list(filter(lambda x: x.is_file(), src.glob(pat))) for pat in include], [])
