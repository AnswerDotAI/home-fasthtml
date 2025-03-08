from itertools import chain
from fasthtml.common import *
from functools import partial
from monsterui.all import *
import fasthtml.common as fh
from monsterui.foundations import *

_A = partial(A, target='_blank')
def Markdown(s, **kw): return Div(render_md(s, class_map_mods={'ul':'uk-list uk-list-bullet space-y-2 mb-6 ml-6 text-lg'}), **kw)

ghurl = 'https://github.com/AnswerDotAI/fasthtml'
fhurl = 'https://fastht.ml'
docs = 'https://fastht.ml/docs'

def NavBar(*c, # Component for right side of navbar (Often A tag links)
           brand=None, # Brand/logo component for left side
           right_items=None,
           right_cls='items-center space-x-4', # Spacing for desktop links
           mobile_cls='space-y-4', # Spacing for mobile links
           cls='p-4', # Classes for navbar
           )->FT: # Responsive NavBar
    "Creates a responsive navigation bar with mobile menu support"
    menu_id = fh.unqid()
    mobile_icon = A(UkIcon("menu", width=30, height=30), cls="md:hidden", data_uk_toggle=f"target: #{menu_id}; cls: hidden")
    return Div(
        Div(DivFullySpaced(
                DivLAligned(brand, Div(*c, cls='hidden md:flex space-x-4')), # Brand/logo component for left side
                mobile_icon, # Hamburger menu icon
                Div(*right_items,cls=(stringify(right_cls),'hidden md:flex'))), # Desktop Navbar 
            cls=('monster-navbar', stringify(cls))),
        DivCentered(*c, *right_items,
                    cls=(stringify(mobile_cls),stringify(cls),'hidden md:hidden monster-navbar'), 
                    id=menu_id))


def NavLink(*args, cls='', target='_blank', **kw):
    return fh.A(*args, cls=(cls,TextT.lg), target=target, **kw)

def BstPage(selidx, title, h2s, *c):
    navitems = [('About', '/about'), ('Vision', '/about/vision'), ('Foundations', '/about/foundation'),
                ('Technology', '/about/tech'), ('Components', '/about/components'), ('Limits', '#', {'disabled':True})]
    logo = 'assets/logo.svg'
    return (
        Title(title),
        Container(
            # NavBar
            NavBar(
                *[NavLink(k, href=v, target=None, cls=TextT.bold if selidx==i else '') for i, (k,v) in enumerate(navitems[:-1])],
                NavLink('Limits', href='javascript:void(0)', disabled=True, uk_tooltip='No limits!', cls=TextT.gray, target=None),
                brand=A(Img(src=logo), href=fhurl),
                right_items=[
                    NavLink("Theme"),  DropDownNavContainer(Div(ThemePicker(font=False, shadows=False, radii=False), cls='p-6 uk-drop-close')),
                    NavLink('Docs', href=docs),
                    NavLink(UkIcon('github'), href=ghurl),
                ],
                cls='bg-green-400/70 rounded-lg rounded-tl-3xl shadow-md p-2 px-4'
            ),

            # Main Content
            Container(
                Grid(
                    Div(NavContainer(*[Li(A(h2, href=f'#sec{i+1}')) for i,h2 in enumerate(h2s)],
                        sticky=True, uk_scrollspy_nav=True), cls='hidden md:block col-span-1'),
                    Div(H1(title, cls='mb-12'), *c, cls='col-span-12 md:col-span-5'),
                    cols=6)),
            # Footer
            DividerLine(),
            Grid(
                    P("© 2024 onwards AnswerDotAI, Inc", cls=TextPresets.muted_lg),
                    DivCentered(A(Img(src=logo, height=24), href=fhurl)),
                    DivRAligned(A("Home"), 
                                _A("Docs",href='https://fastht.ml/docs'), 
                                _A("Company", href='https://www.answer.ai/'), cls=TextPresets.muted_lg+'space-x-4'),
                ),
                cls='py-8 mb-4' + ContainerT.xl))

def Sections(h2s, texts):
    colors = 'yellow', 'pink', 'teal', 'blue'
    div_cls = 'py-2 px-3 mt-4 mb-2 bg-{}-400/70 shadow-md rounded-lg rounded-tl-3xl' #bg-{}-100
    return chain([Div(H2(h2, id=f'sec{i+1}', cls=div_cls.format(colors[i%4])), Div(txt, cls='px-2'))
                  for i,(h2,txt) in enumerate(zip(h2s, texts))])
