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

    root_dir = pathlib.Path(ROOT_DIR)
    post_dir = root_dir / "post"
    meta_table_path = root_dir / "meta.csv"

    def __init__(self) -> None:

        for _ in [self.root_dir, self.post_dir]:
            if not os.path.exists(_):
                log.info(f"creating {_}")
                _.mkdir(parents=True, exist_ok=True)
        self.meta_table = MetaTable(self.meta_table_path)

    def save_post(self, post: Post):
        """ Save a post in database.
        """
        self.meta_table.update(ID=post.post_id, meta=post.meta)
        post_path = self.post_dir / f"{post.post_id}.md"
        log.info(f"saving post at {post_path}")
        with open(post_path, "w") as f: f.write(post.text)
    
    def read_post(self, post_id: str) -> Post:
        """ Reads a post with given id.
        """
        post_path = self.post_dir / f"{post_id}.md"
        log.info(f"reading post at {post_path}")
        with open(post_path, "w") as f: return f.read()


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
