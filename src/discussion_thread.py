from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Comment:
    author: str
    content: str
    timestamp: datetime
    upvotes: int = 0

@dataclass
class DiscussionThread:
    module_name: str
    comments: List[Comment] = None

    def __post_init__(self):
        if self.comments is None:
            self.comments = []

    def post_comment(self, author: str, content: str):
        comment = Comment(author, content, datetime.now())
        self.comments.append(comment)

    def reply_comment(self, parent_comment: Comment, author: str, content: str):
        reply_comment = Comment(author, content, datetime.now())
        self.comments.append(reply_comment)

    def upvote_comment(self, comment: Comment):
        comment.upvotes += 1

    def display_thread(self):
        print(f"Module: {self.module_name}")
        for comment in self.comments:
            print(f"Author: {comment.author}, Timestamp: {comment.timestamp}, Upvotes: {comment.upvotes}")
            print(f"Content: {comment.content}")
            print("------------------------")
