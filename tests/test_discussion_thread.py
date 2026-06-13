from datetime import datetime
from discussion_thread import DiscussionThread, Comment

def test_post_comment():
    thread = DiscussionThread("Module 1")
    thread.post_comment("John Doe", "This is a test comment")
    assert len(thread.comments) == 1
    assert thread.comments[0].author == "John Doe"
    assert thread.comments[0].content == "This is a test comment"

def test_reply_comment():
    thread = DiscussionThread("Module 1")
    parent_comment = Comment("John Doe", "This is a test comment", datetime.now())
    thread.comments.append(parent_comment)
    thread.reply_comment(parent_comment, "Jane Doe", "This is a reply comment")
    assert len(thread.comments) == 2
    assert thread.comments[1].author == "Jane Doe"
    assert thread.comments[1].content == "This is a reply comment"

def test_upvote_comment():
    thread = DiscussionThread("Module 1")
    comment = Comment("John Doe", "This is a test comment", datetime.now())
    thread.comments.append(comment)
    thread.upvote_comment(comment)
    assert comment.upvotes == 1

def test_display_thread():
    thread = DiscussionThread("Module 1")
    thread.post_comment("John Doe", "This is a test comment")
    thread.reply_comment(thread.comments[0], "Jane Doe", "This is a reply comment")
    thread.upvote_comment(thread.comments[0])
    thread.display_thread()
