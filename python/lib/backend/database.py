from pandas.io.pytables import Table
from ..utils import log
import pathlib
import pandas as pd
from typing import Union
import os
from .post import Post
ROOT_DIR = os.path.expandvars("$HOME/mini_mini_blog")
USER = os.path.expandvars("${USER}")


class DataBase:

    _root_dir = pathlib.Path(ROOT_DIR)
    _post_dir = _root_dir / "post"
    _meta_table_path = _root_dir / "meta.csv"

    def __init__(self) -> None:

        for _ in [self._root_dir, self._post_dir]:
            if not os.path.exists(_):
                log.info(f"creating {_}")
                _.mkdir(parents=True, exist_ok=True)
        self.meta_table = MetaTable(self._meta_table_path)

    def save_post(self, post: Post):
        """ Save a post in database.
        """
        self.meta_table.update(ID=post.ID, meta=post.meta)
        path = self.ID2path(post.ID)
        log.info(f"saving post at {path}")
        with open(path, "w") as f: 
            f.write(post.text)
    
    def read_post(self, ID: str=None, path: str=None) -> Post:
        """ Reads a post with given id.
        """
        if ID is not None:
            path = self.ID2path(ID)
        log.info(f"reading post at {path}")
        with open(path, "r") as f: 
            text = f.read()
        return text

    def path2ID(self, path):
        return path.split("/")[-1].removesuffix(".md")

    def ID2path(self, ID):
        return str(self._post_dir / f"{ID}.md")

    @property
    def post_dir(self): return str(self._post_dir)


class MetaTable:

    table: pd.DataFrame
    path: Union[str, pathlib.Path] 

    def __init__(self, path):
        self.path = path
        if not os.path.exists(path):
            self.table = pd.DataFrame()
            self.save()
        else:
            self.read()

    def __repr__(self) -> str:
        return str(self.table)

    def read(self):
        log.debug(f"reading meta table from {self.path}")
        self.table = pd.read_csv(self.path)

    def save(self):
        log.debug(f"saving meta table to {self.path}")
        self.table.to_csv(self.path)

    def update(self, *,
            ID: str=None,
            meta: dict=None):
        if ID not in self.table.index:
            log.debug(f"{ID} not found; appending")
            self.table = self.table.append(pd.Series(meta, name=ID))
        else:
            self.table.loc[ID] = meta

    def delete(self, *, ID: str=None):
        self.table.drop(ID)

    def find(self):
        pass
