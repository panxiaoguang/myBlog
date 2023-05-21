import pynecone as pc
import re
from myBlog.components.navabar import navbar
from myBlog.basestate import state
from myBlog.components.loop import eachpagelist
from myBlog.components.custom import pageList
from sqlmodel import select
from myBlog.models import Blogs


def get_abbre(contents:str)->str:
    # 使用正则表达式匹配 `<!-- more -->` 并获取之前的内容
    match = re.search(r'(.*)<!--\s*more\s*-->', contents, re.DOTALL)

    if match:
        summary = match.group(1).strip()  # 去除前后空白字符
        return summary
    else:
        return "none"
    
class bloglistState(state):
    initial_page:int=1
    min:int=1
    max:int=1

    def define_min_max(self):
        with pc.session() as session:
            tmp = session.exec(select(Blogs))
            for x in tmp:
                if x.pagenumber < self.min:
                    self.min = x.pagenumber
                if x.pagenumber > self.max:
                    self.max = x.pagenumber
    @pc.var
    def get_titles(self) -> list[pageList]:
        with pc.session() as session:
            result=[]
            tmp = session.exec(select(Blogs))
            for x in tmp:
                if x.pagenumber==self.initial_page:
                    result.append(pageList(title=x.title,abbre=get_abbre(x.content),path=x.path))
            return result
    @pc.var
    def detect_min(self) -> bool:
        if self.initial_page ==self.min:
            return True
        else:
            return False
    @pc.var
    def detect_max(self) -> bool:
        if self.initial_page ==self.max:
            return True
        else:
            return False
          
    def get_next(self):
        self.initial_page+=1
    
    def get_prev(self):
        self.initial_page-=1
    
def bloglist()->pc.component :
    return pc.box(
        navbar(),
        pc.vstack(
            pc.foreach(bloglistState.get_titles,eachpagelist),
            pc.button_group(
                pc.button(pc.icon(tag="arrow_back"), color_scheme="blackAlpha",on_click=bloglistState.get_prev,is_disabled=bloglistState.detect_min),
                pc.button(pc.icon(tag="arrow_forward"), color_scheme="blackAlpha",on_click=bloglistState.get_next,is_disabled=bloglistState.detect_max),
                is_attached=True,
                width="200px",
                    ),
        pt="10%",
        pl="20%",
        pr="20%",
        ),
    )