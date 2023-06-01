import pynecone as pc
from myBlog.pages.index import index
from myBlog.pages.bloglist import bloglist,bloglistState
from myBlog.pages.posts import post
from myBlog.pages.about import about
from myBlog.pages.sequenceTools import seuquencetools
from myBlog.pages.excel2shell import excel2shell
from myBlog.basestate import state


# Add state and page to the app.
app = pc.App(state=state)
app.add_page(index,title="Xiaoguang's Blog")
app.add_page(bloglist,title="Xiaoguang's Blog")
app.add_page(about,title="Xiaoguang's Blog")
app.add_page(seuquencetools,title="Xiaoguang's Blog")
app.add_page(excel2shell,title="Xiaoguang's Blog")
app.add_page(post,route="/post/[path]",title="Xiaoguang's Blog")
app.compile()
