import os
import pandas as pd
from dataclasses import dataclass
from typing import List


@dataclass
class Post:

    title: str
    post_id: int
    labels: List[str]
    body: str

    def __init__(self) -> None:
        self.post_id = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
        self.labels = []
        self.body = ""
        self.title = "untitled"

    def create_from_template(self, template):
        pass
