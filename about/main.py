import about.vision, about.overview, about.foundations, about.tech, about.components
from fasthtml.common import *
from monsterui.all import *

hdrs = (
    *Theme.blue.headers(highlightjs=True),
    Script(src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/languages/html.min.js"),
    *Socials(title='About FastHTML', description='Learn the foundations of FastHTML', site_name='about.fastht.ml',
             twitter_site='@answerdotai', image=f'/assets/og-sq.png', url=''),
)

app,rt = fast_app(hdrs=hdrs)
app.get('/')(about.overview.page)
app.get('/components')(about.components.page)
app.get('/foundation')(about.foundations.page)
app.get('/tech')(about.tech.page)
app.get('/vision')(about.vision.page)

serve()
