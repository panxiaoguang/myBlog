import pynecone as pc
from myBlog.basestate import state
from myBlog.models import Blogs

class writeState(state):
    title:str=""
    author:str=""
    path:str=""
    content:str=""

    def upload_articles(self):
        new_rows = Blogs(author=self.author,
                         title=self.title,
                         path=self.path,
                         content=self.content,
                         pagenumber=1)
        with pc.session() as session:
            session.add()

def writepage()->pc.component:
    return pc.container(
        pc.form(
            pc.text("Title: "),
            pc.input(on_change=writeState.set_title),
            pc.text("Author: "),
            pc.input(on_change=writeState.set_author),
            pc.text("path: "),
            pc.input(on_change=writeState.set_path),
            pc.text("content: "),
            pc.text_area(on_change=writeState.set_content),
            pc.button("Submit!")
        ),
        pc.divider(),
        pc.form(
            pc.text("Change page Size:"),
            pc.input(),
            pc.button()
        ),

    )