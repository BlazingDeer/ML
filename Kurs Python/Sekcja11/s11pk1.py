class HtmlCM:
    def __init__(self):
        pass

    def __enter__(self):
        html="""
        <TABLE>
        <TR>
            <TH>Number</TH> <TH>Description</TH>
        </TR>"""
        print(html)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("</TABLE>")

with HtmlCM() as htmlcm:
    html="""
    <TR>
        <TD>1</TD> <TD>Say hello!</TD>
    </TR>
    <TR>
        <TD>2</TD> <TD>Say good bye!</TD>
    </TR>"""
    print(html)