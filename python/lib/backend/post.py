from ..utils import log
import os
import pandas as pd
from dataclasses import dataclass
from typing import List
import yaml


@dataclass
class Post:

    ID: str = ""
    meta: dict = None
    text: str = ""

    def __init__(self, ID=None, text=None) -> None:
        if ID is None:
            self.gen_id()
        if text is None:
            self.update("---\ntitle: None\n---\n")
        else:
            self.update(text)

    def extract_meta(self):
        _ = self.text.split("---")
        assert len(_) >= 3
        _, meta_str, *_ = _
        self.meta = yaml.safe_load(meta_str)

    def update(self, raw_text):
        self.text = raw_text
        self.extract_meta()
        print(f"{self.meta=}, {self.text=}")
    
    def gen_id(self):
        self.post_id = pd.Timestamp.now().strftime("%Y%m%d%H%M%S")
        log.info(f"generated new {self.post_id=}")