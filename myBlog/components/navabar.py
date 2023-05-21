import pynecone as pc

def navbar() -> pc.component:
    return pc.flex(
            pc.hstack(
                pc.image(src="/favicon.ico",width="15%"),
                pc.link("Xiaohanys",font_size="1.5em",font_weight="700",href="/"),
                pl="5%"),
            pc.hstack(
                pc.link("Blog",href="/bloglist",color="#666666",font_size="18px",mr="16px",_hover={"color": "#7B68EE"}),
                pc.link("About",href="/about",color="#666666",font_size="18px",mr="16px",_hover={"color": "#7B68EE"}),
                pc.menu(
                    pc.menu_button("Tools",pc.icon(tag="chevron_down"),color="#666666",font_size="18px",_hover={"color": "#7B68EE"}),
                        pc.menu_list(
                            pc.menu_item(pc.link("Sequence tools",href="/seuquencetools",color="#666666",font_size="16px")),
                            pc.menu_divider(),
                            pc.menu_item(pc.link("Excel2Shell",href="/excel2shell",color="#666666",font_size="16px")),),
                        ),
                pc.link(pc.span(pc.image(src="/github.png",height="1.25em",ml="14px")),href="https://github.com/panxiaoguang"),
                pr="5%"),
            position="fixed",
            width="100%",
            justify="space-between",
            border_bottom="0.05em solid #AAAAAA",
            background=" rgba(255,255,255, 0.9)",
            padding="0.5%"
            )