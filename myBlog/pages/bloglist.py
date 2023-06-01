import pynecone as pc
import re
from myBlog.components.navabar import navbar
from myBlog.basestate import state
from myBlog.components.loop import eachpagelist
from myBlog.components.custom import pageList
from sqlmodel import select
from myBlog.models import Blogs
from myBlog.components.pagnation import Pagination

pls = Pagination.create

def get_abbre(contents:str)->str:
    # 使用正则表达式匹配 `<!-- more -->` 并获取之前的内容
    match = re.search(r'(.*)<!--\s*more\s*-->', contents, re.DOTALL)

    if match:
        summary = match.group(1).strip()  # 去除前后空白字符
        return summary
    else:
        return "none"
    
class bloglistState(state):
    current: int = 1
    total:int = 4
    pageSize:int = 2

    @pc.var
    def get_titles(self) -> list[pageList]:
        with pc.session() as session:
            result=[]
            tmp = session.exec(select(Blogs))
            for x in tmp:
                if x.pagenumber==self.current:
                    result.append(pageList(title=x.title,abbre=get_abbre(x.content),path=x.path))
            return result
   
        
    
def bloglist()->pc.component :
    return pc.box(
        navbar(),
        pc.vstack(
            pc.foreach(bloglistState.get_titles,eachpagelist),
            pls(total=bloglistState.total,
                current=bloglistState.current,
                pageSize=bloglistState.pageSize,
                on_change=bloglistState.set_current),
        pt="10%",
        pl="20%",
        pr="20%",
        ),
    )