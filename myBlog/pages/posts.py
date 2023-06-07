import pynecone as pc
from myBlog.components.navabar import navbar
from myBlog.basestate import state
from myBlog.components.custom import inputText
from myBlog.models import Blogs
from sqlmodel import select
from myBlog.components.loop import eachtocs
import re

Style={
    "pre": {
    "background":" white !important",
    "color":" rgb(56, 58, 66) !important",
    "font-family": "'Fira Code', 'Fira Mono', Menlo, Consolas, 'DejaVu Sans Mono', monospace",
    "direction": "ltr",
    "text-align": "left",
    "white-space": "pre",
    "word-spacing": "normal",
    "word-break": "normal",
    "line-height": "1.5",
    "tab-size": "2",
    "hyphens": "none",
    "padding": "1em",
    "margin": "0.5em 0px",
    "overflow": "scroll",
    "border-radius": "1em",
},
   "background":" rgb(250, 250, 250)",
   ".chakra-heading":{
       "pt":"0.5em",
       "pb":"0.5em",
   },
   ".chakra-code":{
       "display": "inline-block",
       "font-family": "var(--chakra-fonts-mono)",
       "font-size": "var(--chakra-fontSizes-sm)",
       "padding-inline": "0.2em",
       "border-radius": "var(--chakra-radii-sm)",
       "background": "var(--badge-bg)",
       "box-shadow": "var(--badge-shadow)",
       "--badge-bg": "var(--chakra-colors-gray-100)",
       "--badge-color": "var(--chakra-colors-gray-800)"
   }
}

def get_header(contents:str)->list[str]:
    pattern = r'^(#+)\s+(.*)$'
    matches = re.findall(pattern, contents, re.MULTILINE)
    headings = []
    in_code_block = False
    for match in matches:
        text = match[1]
        if text.startswith('```'):
            in_code_block = not in_code_block
        if not in_code_block or '```' not in text:
            headings.append(text)
    return headings

class postState(state):
    @pc.var
    def get_contents(self) -> inputText:
        need_path = self.get_query_params().get("path","no path")
        with pc.session() as session:
            tmp = session.exec(select(Blogs).where(Blogs.path==need_path))
            tmp2 = [inputText(title=x.title,author=x.author,content=x.content,header=get_header(x.content)) for x in tmp]
            if len(tmp2)>0:
                return tmp2[0]
            else:
                return inputText(title="none",author="none",content="none",header=["none"])


def post()->pc.component:
    return pc.box(
            navbar(),
            pc.vstack(pc.box(pc.heading(postState.get_contents.title,size="lg"),
                    pc.divider(),
                    pc.box(pc.text("author: "+postState.get_contents.author,color="grey",font_size="1.1em"),mb="1em"),
                    pc.markdown(postState.get_contents.content),
                    padding="10%",
                    line_height="2em",
                    width="80%",
                    style=Style,
                 ),),
            
    )