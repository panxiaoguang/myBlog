import pynecone as pc
from myBlog.components.navabar import navbar
from myBlog.basestate import state
from Bio import SeqIO
from urllib.request import urlopen
import io
import json as json_package
from myBlog.components.loop import maketd,format_output

circle_style={
    "position":"absolute",
    "width":"250px",
    "height":"250px"
}

circle1_style={
    "bgGradient":"linear(130deg,rgba(77,73,191,.8),rgba(255,255,255,.2))",
    "top":"20%",
    "left":"5%"
}

circle2_style={
    "bgGradient":"linear(130deg,rgba(5,219,242,.8),rgba(255,255,255,.2))",
    "bottom":"5%",
    "right":"5%"
}
heading_style={
    "bgGradient":"linear(to-l, #7928CA, #FF0080)",
    "bgClip":'text'
}
button_style={
    "bgGradient":"linear(to-br,rgba(251,251,254,.9),rgba(251,251,254,.2))"
}
body_style={
    "width":"80%",
    "border_style":"solid",
    "border_width":"2px",
    "padding_left":"2.5rem",
    "padding_right":"2.5rem",
    "padding_bottom":"2.5rem",
    "padding_top":"1.5%",
    "border_radius":"1.5rem",
    "bgGradient":"linear(to-br,rgba(251,251,254,.6),rgba(251,251,254,.2))",
    "backdropFilter":"auto",
    "backdropBlur":'10px',
    "zIndex":"2"
}
all_style={
    "padding":"10%",
    "background_color":"#DFE9F2",
    "fontFamily":"Open Sans"
}
seq_style={
    "border_style":"solid",
    "border_color":"#bdbdbd",
    "border_width":"medium",
    "width":"100%",
    "height":"auto",
    "minH":"100px",
    "border_radius":"md",
    "padding":"1%"
}

class Sequence(state):
    dis:bool=True
    show: bool = False
    waiting:bool = True
    input:str=""
    output:list
    blatData:list[list]

    def change(self):
        self.show = not (self.show)
    
    def nima(self):
        self.waiting = not (self.waiting)
    
    def nima2(self):
        self.input=""
        self.output=[]
        self.blatData = [[]]

    def change_dis(self,_):
        if self.input!="":
            self.dis=False
        else:
            self.dis=True
            self.waiting=True

    def complement(self):
        jieguo=[]
        for record in SeqIO.parse(io.StringIO(self.input),"fasta"):
            jieguo.append(">"+str(record.id))
            jieguo.append(str(record.seq.complement()))
        self.output = jieguo

    def rev_complement(self):
        jieguo=[]
        for record in SeqIO.parse(io.StringIO(self.input),"fasta"):
            jieguo.append(">"+str(record.id))
            jieguo.append(str(record.seq.reverse_complement()))
        self.output = jieguo

    def translate(self):
        jieguo=[]
        for record in SeqIO.parse(io.StringIO(self.input),"fasta"):
            jieguo.append(">"+str(record.id))
            jieguo.append(str(record.seq.translate()))
        self.output = jieguo

    def blat(self):
        finallyData = []
        for record in SeqIO.parse(io.StringIO(self.input),"fasta"):
            userseq = str(record.seq)
            url = f"https://genome.ucsc.edu/cgi-bin/hgBlat?userSeq={userseq}&type=DNA&db=hg38&output=json"
            r = urlopen(url)
            tmpData = json_package.load(r)['blat']
            if len(tmpData) > 0:
                for i in tmpData:
                    finallyData.append([record.id,i[13],i[15],i[16],i[8]])
        if len(finallyData) == 0:
            self.show=True
            self.blatData = [[]]
        else:
            self.waiting = True
            self.blatData = finallyData

def seuquencetools()->pc.components:
    return pc.box(
                navbar(),
                pc.center(
                pc.circle(style=[circle_style,circle1_style]),
                pc.circle(style=[circle_style,circle2_style]),
                pc.center(
                    pc.vstack(
                        pc.heading("Seq tools!",style=heading_style),
                        pc.box(pc.heading("Introduction:",size="md"),
                               pc.text("""Welcome to Seqtools! It's a Pynecone-based tool for processing genomic sequences.featuring reverse complementation and translation. Its most notable functionality
                                        includes the ability to retrieve input sequence positions on the reference genome via UCSC's BLAT interface. 
                                        Currently limited to human-genome support only, this tool accurately locates genomic data with ease.
                                        """),
                        pc.heading("Usage: ",size="md"),
                        pc.text("You should input a format like fasta files: "),
                        pc.text(">1"),
                        pc.text("TGTTCGGCAAGATCTCGGGCTGG"),
                        pc.text(">2"),
                        pc.text("AACAATGATCGCCCGAGTGGCGG"),
                              ),
                        pc.text_area(value=Sequence.input,
                                    placeholder="Input your seq...",
                                    on_change = Sequence.set_input,
                                    on_blur = Sequence.change_dis,
                                    width="100%",
                                    borderWidth="medium",
                                    borderColor="#bdbdbd"),
                        pc.hstack(pc.button("Complement!",
                                            on_click = Sequence.complement,
                                            style=button_style,
                                            is_disabled= Sequence.dis),
                                  pc.button("Reverse Comp!",
                                            on_click = Sequence.rev_complement,
                                            style=button_style,
                                            is_disabled=Sequence.dis),
                                  pc.button("Translate!",
                                            on_click = Sequence.translate,
                                            style=button_style,
                                            is_disabled=Sequence.dis),
                                ),
                        pc.hstack(pc.button("Blat!",
                                            style=button_style,
                                            on_click = [Sequence.nima,Sequence.blat],
                                            is_disabled= Sequence.dis),
                                  pc.button("Clean!",
                                            style=button_style,
                                            on_click = Sequence.nima2
                                            )
                                  
                                ),
                        pc.divider(),
                        pc.alert_dialog(
                            pc.alert_dialog_overlay(
                                pc.alert_dialog_content(
                                    pc.alert_dialog_header("Info"),
                                    pc.alert_dialog_body(
                                            "No BLAT matches were found for this sequence in genome"
                                                            ),
                                    pc.alert_dialog_footer(
                                    pc.button(
                                            "Close",
                                            on_click=Sequence.change,
                                            )
                                                            ),
                                                        )
                                                    ),
                                    is_open=Sequence.show,
                                        ),
                        pc.box(
                            pc.foreach(Sequence.output,format_output),
                            style=seq_style
                              ),
                        pc.divider(),
                        pc.cond(
                            Sequence.waiting,
                            pc.html("</hr>"),
                            pc.circular_progress(is_indeterminate=True)),
                            pc.table_container(
                                pc.table(
                                    pc.thead(
                                        pc.tr(
                                            pc.th("Name"),
                                            pc.th("Chrom"),
                                            pc.th("Start"),
                                            pc.th("End"),
                                            pc.th("Strand")
                                            )
                                            ),
                                    pc.tbody(pc.foreach(Sequence.blatData,maketd)))),
                    ),
                style = body_style),
    style=all_style,
    ),
    spacing="0em",
    )