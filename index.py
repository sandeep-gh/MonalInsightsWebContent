import justpy as jp
import webapp_framework as wf
from tailwind_tags import mr, sl, sr, st
def no_action(dbref, msg):
    pass

def launcher(request):
    wp = jp.QuasarPage()
    wp.tailwind = True
    wp.head_html = """
    <link rel="stylesheet" href="https://unpkg.com/tailwindcss@^1.5/dist/base.min.css" />
    <link rel="stylesheet" href="https://unpkg.com/tailwindcss@^1.5/dist/components.min.css" />
    <link
    rel="stylesheet"
    href="https://unpkg.com/@tailwindcss/typography@0.2.x/dist/typography.min.css"
    />
    <link rel="stylesheet" href="https://unpkg.com/tailwindcss@^1.5/dist/utilities.min.css" />
    """
    tlc = jp.Div(a=wp, classes="container mx-auto bg/gray/1")
    title_ = wf.dur.title_banner_("title", "Monal Insights: An advanced Imaging Solutions Company")
    title_(tlc, "")

    intro_text = """
    MonalInsights specializes in solutions and technologies for satellite and microCT images. 
    We provide end-to-end solution for ingestion, cleaning, registration, and advanced analysis of 
    images captured in industrial (oil and gas exploration, biomedical) and institutional domains (climate change, agricultural, forest). 
    """

    wf.dur.prose_("intro", intro_text, pcp=[])(tlc, "")

    key_technology_topics = ["Massive Scale Image Storage and Processing Framework", "SemiSupervised based clustering and classification"]
    #wf.fc.StackV_()
    wf.fc.StackV_("keytechpanel", [
        wf.dur.heading_("heading", "Key technologies", pcp=[mr/st/6]),
        wf.fc.StackH_("keytechbuttons", map(lambda l: wf.dur.divbutton_(l, l, l, no_action), key_technology_topics))
        ]
               )(tlc, "")
    return wp



    
app=jp.app
jp.justpy(launcher, start_server=False)
