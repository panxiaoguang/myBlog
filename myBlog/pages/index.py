import pynecone as pc
from myBlog.components.navabar import navbar
from myBlog.basestate import state

class IndexState(state):
    pass

def index() -> pc.component :
    return pc.box(
        navbar(),
        pc.vstack(
            pc.box(pc.text("BioInfor.  eccDNA.CRISPR.",font_size="4em",font_weight="700",lineHeight="1.2em"),
                   pc.text("Learning Road.",font_size="4em",lineHeight="1.2em",font_weight="700",bgGradient='linear(to-l, #EE756A 25%, #756AEE 50%)',bgClip='text'),
                   ),
            pc.box(pc.text("Share my Knoweledge and experience with Bio. As a diary",color="grey",font_size="1.1em",),
                   ),
            pc.hstack(
                pc.input(placeholder="Having any questions..."),
                pc.button("Send me email", bg="black", color="white",width="70%"),
    ),
            pl="25%",
            pr="25%",
            pt="15%",
            pb="15%",
            width="100%",
            spacing="2em",
            bgImage="grid.png",
            text_align="center"),
    )