from ..utils import log
import os
import pandas as pd
from dataclasses import dataclass
from typing import List


@dataclass
class Post:

    post_id: int
    text: str

    def __init__(self, 
        template_id = None,
        post_id = None,
        ):
        if post_id is not None:
            pass
        elif template_id is not None:
            pass
        else:
            log.debug("creating post with default template")
            self.post_id = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
            self.text = """
---
Title: default
Tag:
---
            """
