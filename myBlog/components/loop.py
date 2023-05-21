import pynecone as pc
from myBlog.components.custom import pageList
import pandas as pd

def eachpagelist(haha:pageList):
    return pc.box(
                pc.box(pc.link(haha.title,href="/post/"+haha.path,font_size="2em",font_weight="500",),mb="1em"),
                pc.text(haha.abbre,mb="1em"),
                pc.divider(mb="1em"),
            )
def eachtocs(wocao:str):
    return pc.box(pc.unordered_list(pc.list_item(wocao,color="rgb(107,99,246)"),),width="100%")

def maketd(blat_result:list):
    return pc.tr(
            pc.td(blat_result[0]),
            pc.td(blat_result[1]),
            pc.td(blat_result[2]),
            pc.td(blat_result[3]),
            pc.td(blat_result[4]),
        )

def format_output(textOut:str):
    return pc.text(textOut)

def makenames(df:pd.DataFrame,col:str)->pd.DataFrame:
    s='_'+df.groupby(col).cumcount().add(1).astype(str)
    df.loc[:,col]+=s.mask(s=="_1","")
    return df

def makeOut(cmd:str):
    return pc.text(cmd,color="#f2ad85",white_space="nowrap")