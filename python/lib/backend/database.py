from ..utils import log
import pathlib
import pandas as pd
import os
from .post import Post
ROOT_DIR = os.path.expandvars("$HOME/mini_mini_blog")
USER = os.path.expandvars("${USER}")


class DataBase:

    root_dir = pathlib.Path(ROOT_DIR)
    post_dir = root_dir / "post"
    info_path = root_dir / "info.csv"

    def __init__(self) -> None:

        for _ in [self.root_dir, self.post_dir]:
            if not os.path.exists(_):
                log.info(f"creating {_}")
                _.mkdir(parents=True, exist_ok=True)

        if not os.path.exists(self.info_path):
            log.info(f"creating {self.info_path}")
            self.info = pd.DataFrame([], columns=["user", "post_id"]).set_index("post_id")
            self.info.to_csv(self.info_path, index=False)
        else:
            log.info(f"fetching info from {self.info_path}")
            self.info = pd.read_csv(self.info_path)
            log.info(f"{self.info}")

    def save_post(self, post: Post):
        """ Save a post in database.
        """

        # update/insert post info
        post_info = pd.Series({
                "user": USER,
            }, name=post.post_id)
        if post.post_id not in self.info.index: 
            self.info = self.info.append(post_info)
        else:
            self.info.loc[post.post_id] = post_info
        log.debug(self.info)
        
        # save post body
        post_path = self.post_dir / f"{post.post_id}.md"
        log.info(f"saving post at {post_path}")
        with open(self.post_dir / f"{post.post_id}.md", "w") as f:
            f.write(post.text)
    
    def read_post(self, post_id: str) -> Post:
        """ Reads a post with given id.
        """
        if post_id in self.info.index:
            post_path = self.post_dir / f"{post.post_id}.md"
            log.info(f"reading post at {post_path}")
            with open(post_path, "w") as f:
                f.read(post.text)
        else:
            log.info(f"post with post_id={post_id} not found!")
            