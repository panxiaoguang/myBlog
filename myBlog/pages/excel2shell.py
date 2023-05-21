import pynecone as pc
from myBlog.components.navabar import navbar
from myBlog.basestate import state
import pandas as pd
import os
from myBlog.components.loop import makenames,makeOut


excel_body_style={
    "borderWidth":"0.1px",
    "boxShadow":'base',
    "rounded":'md',
    "width":"35%",
    "align_items":"left",
    "bgGradient":"linear(to-br,rgba(251,251,254,.6),rgba(251,251,254,.2))",
    "padding":"1.5%",
    "spacing":"0.5em",
    "backdropFilter":'auto',
    "backdropBlur":'8px',
    "font_size":"0.9em"
}

excel_textOut_style={
    "width":"64%",
    "borderWidth":"0.1px",
    "boxShadow":'base',
    "rounded":'md',
    "align_items":"left",
    "padding":"1.5%",
    "bgGradient":"linear(to-br,rgba(251,251,254,.6),rgba(251,251,254,.2))",
    "backdropFilter":'auto',
    "backdropBlur":'8px'
}

class Excel2shell(state):
    modalData:pd.DataFrame = pd.DataFrame({"sampleName":["na"],"barcode":[0],"chip":["na"],"lane":["na"],"dataPath":["na"]})
    sampleNameIndex: int = 4
    barcodeIndex: int = 23
    chipIndex: int = 27
    laneIndex: int = 28
    datapathIndex: int = 48
    remotePath: str = "10.2.100.1:/pakpox/pob8d1"
    cmd1: list[str]
    cmd2: list[str]
    show2: bool = False
    excel_file: str
    barcode_file: str
    _outfile:str
    _outfile2:str
    
    async def handle_upload(self, file: pc.UploadFile):
        upload_data = await file.read()
        outfile = f".web/public/{file.filename}"
        with open(outfile, "wb") as f:
            f.write(upload_data)
        self.excel_file = file.filename
        self._outfile = outfile
    
    async def handle_upload2(self, file: pc.UploadFile):
        upload_data = await file.read()
        outfile2 = f".web/public/{file.filename}"
        with open(outfile2, "wb") as f:
            f.write(upload_data)
        self.barcode_file = file.filename
        self._outfile2 = outfile2
    def getCmd(self):
        df = pd.read_excel(self._outfile)
        os.remove(self._outfile)
        df = df.iloc[:,[self.sampleNameIndex-1,self.barcodeIndex-1,self.chipIndex-1,self.laneIndex-1,self.datapathIndex-1]]
        ## change names
        df.columns = ["sampleName", "barcode", "chip", "lane", "dataPath"]
        ## if sampleName is duplicated, fix the name
        self.modalData = df
        df = makenames(df,"sampleName")
        ## make cmd
        df = df.assign(filename1=df.apply(lambda row : "_".join([row['chip'],row['lane'],str(row['barcode']),"1.fq.gz"]),axis=1))
        df = df.assign(filename2=df.apply(lambda row : "_".join([row['chip'],row['lane'],str(row['barcode']),"2.fq.gz"]),axis=1))
        self.cmd1 = df.apply(lambda row: "scp " + os.path.join(row['dataPath'],row['filename1']) + " " + os.path.join(self.remotePath,row['sampleName'] + "_R1.fastq.gz"),axis=1).tolist()
        self.cmd2 = df.apply(lambda row: "scp " + os.path.join(row['dataPath'],row['filename2']) + " " + os.path.join(self.remotePath,row['sampleName'] + "_R2.fastq.gz"),axis=1).tolist()
    
    def removename(self):
        df2 = self.modalData
        df = pd.read_excel(self._outfile2)
        os.remove(self._outfile2)
        df.columns = ["sampleName","trueName"]
        df2 = df2.merge(df,how="left",on="sampleName")
        df2 =df2.drop(columns=["sampleName"])
        df2 = df2.rename(columns={"trueName":"sampleName"})
        #remove Nan
        df2 = df2[~df2["sampleName"].isna()]
        self.modalData = df2
        df2 = makenames(df2,"sampleName")
        df2 = df2.assign(filename1=df2.apply(lambda row : "_".join([row['chip'],row['lane'],str(row['barcode']),"1.fq.gz"]),axis=1))
        df2 = df2.assign(filename2=df2.apply(lambda row : "_".join([row['chip'],row['lane'],str(row['barcode']),"2.fq.gz"]),axis=1))
        self.cmd1 = df2.apply(lambda row: "scp " + os.path.join(row['dataPath'],row['filename1']) + " " + os.path.join(self.remotePath,row['sampleName'] + "_R1.fastq.gz"),axis=1).tolist()
        self.cmd2 = df2.apply(lambda row: "scp " + os.path.join(row['dataPath'],row['filename2']) + " " + os.path.join(self.remotePath,row['sampleName'] + "_R2.fastq.gz"),axis=1).tolist()

    def change(self):
        self.show2 = not (self.show2)

def excel2shell() -> pc.Component:
    return pc.box(
        navbar(),
        pc.vstack(
            pc.heading("Excel2Shell",font_family="Open Sans",padding_top="5%"),
            pc.flex(
                pc.vstack(
                    pc.text("Excel from Glims..."),
                    pc.hstack(
                            pc.button(
                                pc.icon(tag="attachment"),
                                "Attach..",
                                width="23%",
                                bgColor="#BBD1EA",
                                on_click = lambda: Excel2shell.handle_upload(pc.upload_files())
                    ),
                    pc.upload(
                            pc.box(
                                pc.text(Excel2shell.excel_file),
                                borderWidth="0.1px",
                                height="40px",
                                rounded="md",
                                spacing="0em",
                                borderColor="#f2ad85"
                        
                    ),
                        width="77%"), 
                    spacing="0em"
                    ),
                    pc.text("Index for sampleName:"),
                    pc.number_input(default_value=4,on_change=Excel2shell.set_sampleNameIndex,borderColor="#f2ad85"),
                    pc.text("Index for barcode:"),
                    pc.number_input(default_value=23,on_change=Excel2shell.set_barcodeIndex,borderColor="#f2ad85"),
                    pc.text("Index for chip:"),
                    pc.number_input(default_value=27,on_change=Excel2shell.set_chipIndex,borderColor="#f2ad85"),
                    pc.text("Index for lane:"),
                    pc.number_input(default_value=28,on_change=Excel2shell.set_laneIndex,borderColor="#f2ad85"),
                    pc.text("Index for dataPath:"),
                    pc.number_input(default_value=48,on_change=Excel2shell.set_datapathIndex,borderColor="#f2ad85"),
                    pc.text("Remote path:"),
                    pc.input(default_value="10.2.100.1:/pakpox/pob8d1",on_change=Excel2shell.set_remotePath,borderColor="#f2ad85"),
                    pc.hstack(
                        pc.button(
                            pc.icon(tag="search"),
                            "Submit!",
                            on_click=Excel2shell.getCmd,
                            bgColor="#F7CAC9",
                            width="23%",
                                ),
                        pc.button(
                            "View data",
                            width="23%",
                            bgColor="#92DCE5",
                            on_click=Excel2shell.change,),
                        pc.modal(
                            pc.modal_overlay(
                            pc.modal_content(
                                pc.modal_header("Confirm"),
                                    pc.modal_body(
                                        pc.data_table(data=Excel2shell.modalData,pagination=True,
                                                      search=True,
                                                      sort=True,),
                                        ),
                            pc.modal_footer(
                                    pc.button(
                                        "Close", on_click=Excel2shell.change
                                        )
                                            ),
                                                )
                                                ),
                            is_open=Excel2shell.show2,
                            size="6xl",
                            return_focus_on_close=True
                            ),
                    ),
                    pc.divider(
                        borderWidth="0.5px",
                        borderColor="black"
                    ),
                    pc.text("Input Barcode with sampleName:"),
                    pc.hstack(
                            pc.button(
                                pc.icon(tag="attachment"),
                                "Attach..",
                                width="23%",
                                #height="40px",
                                bgColor="#BBD1EA",
                                on_click = lambda: Excel2shell.handle_upload2(pc.upload_files())
                    ),
                    pc.upload(
                            pc.box(
                                pc.text(Excel2shell.barcode_file),
                                borderWidth="0.1px",
                                height="40px",
                                rounded="md",
                                spacing="0em",
                                borderColor="#f2ad85"
                        
                    ),
                        width="77%"), 
                    spacing="0em"
                    ),
                    pc.button(pc.icon(tag="repeat"),
                            "Update!",
                            on_click=Excel2shell.removename,
                            bgColor="#F7CAC9",
                            width="23%",),
                    style=excel_body_style,),
                pc.spacer(),
                pc.vstack(
                    pc.heading("Shell Script",size="md",font_family="Open Sans",),
                    pc.divider(borderWidth="0.5px",),
                    pc.tabs(
                        items=[
                            ("Script 1", pc.box(pc.foreach(Excel2shell.cmd1,makeOut),
                                                            overflow="scroll",
                                                            maxH="600px",
                                                            minH="600px")),
                            ("Script 2", pc.box(pc.foreach(Excel2shell.cmd2,makeOut),
                                                            overflow="scroll",
                                                            maxH="600px",
                                                            minH="600px")),
                                ],
                        ),
                    style=excel_textOut_style,
            ),
            width="80%",
            
       ),
            bgColor="#DFE9F2",
            padding="1.5%",
            font_family="Open Sans",
        ),
        )