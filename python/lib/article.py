import os
from dataclasses import dataclass
from typing import List

class Label(str):

    def __init__(self) -> None:
        super().__init__()


class Category(str):

    def __init__(self) -> None:
        super().__init__()


@dataclass
class Article:

    labels: List[Label]
    category: Category

    def __init__(self, 
        template=None,
        ) -> None:
        if template is not None:
            pass

    def create_from_template(self, template):
        pass


@dataclass
class Template:

    pass