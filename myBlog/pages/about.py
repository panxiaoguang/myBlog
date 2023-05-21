import pynecone as pc
from myBlog.components.navabar import navbar
from myBlog.basestate import state

Style={
    "span#bold":{
        "color":"white",
        "background_color":"#689EF4",
        "font_weight":"bold"
    },
    "span#italic":{
        "font_style": "italic"
    }
}

class aboutState(state):
    pass 

def about() -> pc.component:
    return pc.box(
        navbar(),
        pc.vstack(
            pc.heading("About",size="2xl"),
            pc.divider(),
            pc.heading("个人介绍(Brief Introduction):",size="lg",width="100%"),
            pc.box(pc.span("潘晓光 (Xiaoguang Pan) , ",id="bold"),"第一批90后，已在社会上摸爬滚打了4年有余……",width="100%"),
            pc.box("本硕就读于山东省内的",pc.span("985工程，211工程",id="bold"),"的山东大学，毕业后不辍学业，于2018年7月进入",pc.span("青岛华大基因研究院",id="bold"),"，继续在生物专业领域深耕科研。主攻",pc.span("基因组编辑",id="bold"),"生物信息学分析，次要方向为",pc.span("染色体外环状DNA",id="bold"),"(eccDNA) 在癌症等多种疾病中的潜在作用及标记基因发现。",width="100%"),
            pc.box("2022年11月1日，在公司联合培养项目下继续进入丹麦",pc.span("哥本哈根大学",id="bold"),"深造，攻读博士研究生学位，方向为基因组编辑。",width="100%"),
            pc.box("I'm Xiaoguang Pan, a member of the post-90s generation, and I've been striving in society for over four years........",width="100%"),
            pc.box("I pursued my undergraduate studies at Shandong University, which is renowned for its participation in the prestigious 985 Project and 211 Project in Shandong Province. After graduation, I continued my academic pursuits by joining BGI-Qingdao in July 2018, where I've been actively engaged in scientific research in the field of biology. My primary research interests lie in bioinformatics analysis of genome editing, while my secondary focus is on exploring the potential role of extracellular circular DNA (eccDNA) in cancer and other diseases, as well as discovering marker genes.",width="100%"),
            pc.box("In pursuit of my academic goals, I recently embarked on a new journey through my company's joint training program. I was given the opportunity to pursue a PhD in genome editing at the University of Copenhagen in Denmark, which marks a significant milestone in my academic and professional journey. I'm eager to make the most of this opportunity to further deepen my knowledge and expertise in my chosen field, and I'm excited about what the future holds.",width="100%"),
            pc.heading("已发表论文 (Published Papers ) ：",size="lg",width="100%"),
            pc.unordered_list(
                pc.list_item("Corsi, G. I., Qu, K., Alkan, F., ",pc.span("Pan, X.",id="bold"),", Luo, Y., & Gorodkin, J. (2022). CRISPR/Cas9 gRNA activity depends on free energy changes and on the target PAM context. ",pc.span("Nature communications",id="italic"),", 13(1), 3006. "),
                pc.list_item("Jiang, X., ",pc.span("Pan, X.",id="bold"),", Li, W., Han, P., Yu, J., Li, J., Zhang, H., Lv, W., Zhang, Y., & He, Y. (2023). Genome-wide characterization of extrachromosomal circular DNA in gastric cancer and its potential role in carcinogenesis and cancer progression. "),
                pc.list_item("Li, C., Zhang, Y., Leng, L., ",pc.span("Pan, X.",id="bold"),", Zhao, D., Li, X., Huang, J., Bolund, L., Lin, G., & Luo, Y. (2022). The single-cell expression profile of transposable elements and transcription factors in human early biparental and uniparental embryonic development. ",pc.span("Frontiers in Cell and Developmental Biology",id="italic"),", 10. "),
                pc.list_item("Lv, W., ",pc.span("Pan, X.",id="bold"),", Han, P., Wang, Z., Feng, W., Xing, X., Wang, Q., Qu, K., Zeng, Y., & Zhang, C. (2022). Circle‐Seq reveals genomic and disease‐specific hallmarks in urinary cell‐free extrachromosomal circular DNAs. ",pc.span("Clinical and Translational Medicine",id="italic"),", 12(4), e817. "),
                pc.list_item("",pc.span("Pan, X.",id="bold"),", Qu, K., Yuan, H., Xiang, X., Anthon, C., Pashkova, L., Liang, X., Han, P., Corsi, G. I., & Xu, F. (2022). Massively targeted evaluation of therapeutic CRISPR off-targets in cells. ",pc.span("Nature communications",id="italic"),", 13(1), 4049. "),
                pc.list_item("Pang, J., ",pc.span("Pan, X.",id="bold"),", Lin, L., Li, L., Yuan, S., Han, P., Ji, X., Li, H., Wang, C., & Chu, Z. (2022). Characterization of plasma extrachromosomal circular DNA in gouty arthritis. ",pc.span("Frontiers in Genetics",id="italic"),", 13, 859513. "),
                pc.list_item("Xiang, X., Corsi, G. I., Anthon, C., Qu, K., ",pc.span("Pan, X.",id="bold"),", Liang, X., Han, P., Dong, Z., Liu, L., & Zhong, J. (2021). Enhancing CRISPR-Cas9 gRNA efficiency prediction by data integration and deep learning. ",pc.span("Nature communications",id="italic"),", 12(1), 3238. "),
                pc.list_item("Xiang, X., Luo, L., Nodzyński, M., Li, C., Han, P., Dou, H., Petersen, T. S., Liang, X., ",pc.span("Pan, X.",id="bold"),", & Qu, K. (2019). LION: a simple and rapid method to achieve CRISPR gene editing. ",pc.span("Cellular and Molecular Life Sciences",id="italic"),", 76, 2633-2645. "),
                pc.list_item("Xiang, X., Zhao, X., ",pc.span("Pan, X.",id="bold"),", Dong, Z., Yu, J., Li, S., Liang, X., Han, P., Qu, K., & Jensen, J. B. (2021). Efficient correction of Duchenne muscular dystrophy mutations by SpCas9 and dual gRNAs. ",pc.span("Molecular Therapy-Nucleic Acids",id="italic"),", 24, 403-415. "),
                pc.list_item("Yu, J., Xiang, X., Huang, J., Liang, X., ",pc.span("Pan, X.",id="bold"),", Dong, Z., Petersen, T. S., Qu, K., Yang, L., & Zhao, X. (2020). Haplotyping by CRISPR-mediated DNA circularization (CRISPR-hapC) broadens allele-specific gene editing. ",pc.span("Nucleic Acids Research",id="italic"),", 48(5), e25-e25."),
                pc.list_item("Zhang, L., Li, L., ",pc.span("Pan, X.",id="bold"),", Shi, Z., Feng, X., Gong, B., Li, J., & Wang, L. (2018). Enhanced growth and activities of the dominant functional microbiota of chicken manure composts in the presence of maize straw. ",pc.span("Frontiers in microbiology",id="italic"),", 9, 1131."),
            ),
        pt="5%",
        pl="20%",
        pr="20%",
        style=Style,
        ),
    )