from fasthtml.common import *
from inspect import getsource
from home_components import accordion,col,inset,bnset

eg_url = 'https://github.com/AnswerDotAI/fasthtml-example/tree/main'
samples = [
    ("Game of life", "game-of-life.svg", f"{eg_url}/00_game_of_life"),
    ("To-do", "todo.svg", f"{eg_url}/01_todo_app"),
    ("Chat bot", "chat-bot.svg", f"{eg_url}/02_chatbot"),
    ("Pictionary AI", "pictionary-ai.svg", f"{eg_url}/03_pictionary")
]

from weather import all_weather

async def weather_table():
    """Dynamically generated python content
    directly incorporated into the HTML"""
    # These are actual real-time weather.gov observations
    try: results = await all_weather()
    except: return P('Weather not available')
    rows = [Tr(Td(city), *map(Td, d.values()), cls="even:bg-purple/5")
            for city,d in results.items()]
    flds = 'City', 'Temp (C)', 'Wind (kmh)', 'Humidity'
    head = Thead(*map(Th, flds), cls="bg-purple/10")
    return Table(head, *rows, cls="w-full")

bgurl = "https://ucarecdn.com/35a0e8a7-fcc5-48af-8a3f-70bb96ff5c48/-/preview/750x1000/"
cardcss = "font-family: 'Arial Black', 'Arial Bold', Gadget, sans-serif; perspective: 1500px;"
def card_3d_demo():
    """This is a standalone isolated Python component.
    Behavior and styling is scoped to the component."""
    def card_3d(text, background, amt, left_align):
        # JS and CSS can be defined inline or in a file
        scr = ScriptX('card3d.js', amt=amt)
        align='left' if left_align else 'right'
        sty = StyleX('card3d.css', background=f'url({background})', align=align)
        return Div(text, Div(), sty, scr)
    # Design credit: https://codepen.io/markmiro/pen/wbqMPa
    card = card_3d("Mouseover me", bgurl, amt=1.5, left_align=True)
    return Div(card, style=cardcss)

a_cls="s-body text-black/80 col-span-full",
c_cls=f"{col} justify-between bg-purple/10 rounded-[1.25rem] {inset}",
acc_cls=f"{col} gap-4 transition ease-out delay-[300ms]"
qas = [
    ("What is this?", "This is a little demo of a reusable accordion component."),
    ("What is FastHTML?", "FastHTML is a Python library for building web apps."),
    ("What is HTMX?", "HTMX is a JavaScript library that extends browser interaction behavior.")]
def accordion_demo():
    """UI components can be styled and reused.
    UI libraries can be installed using `pip`."""
    accs = [accordion(id=id, question=q, answer=a,
        question_cls="text-black s-body", answer_cls=a_cls, container_cls=c_cls)
        for id,(q,a) in enumerate(qas)]
    return Div(*accs, cls=acc_cls)

list_class = "m-body text-black list-disc pl-5"
db = database('data/todos.db')
class Todo:
    "Use any database system you like"
    id:int; title:str; done:bool
    def __ft__(self):
        "`__ft__` defines how FastHTML renders an object"
        return Li("✅ " if self.done else "", self.title)

todos = db.create(Todo)
def todos_table():
    "This example uses the `fastlite` DB lib"
    return Ul(*todos(), cls=list_class)

def startup():
    if not todos():
        todos.insert(title="Create sample todos", done=True)
        todos.insert(title="Create a sample FastHTML app", done=True)
        todos.insert(title="Read this todo list")

async def components():
    return [
        ("Components", "card3d.py", getsource(card_3d_demo), card_3d_demo()),
        ("Dynamic", "weather.py", getsource(weather_table), await weather_table()),
        ("Reusable", "accordion.py", getsource(accordion_demo), accordion_demo()),
        ("Databases", "todos.py", f"{getsource(Todo)}\ntodos = db.create(Todo)\n{getsource(todos_table)}",
         Div(H2("DB-generated todo list", cls="text-2xl font-bold mb-4"), todos_table()))
    ]

stacked = [
    ("Build on solid foundations", "FastHTML stands on the shoulders of giants:", [
        ("ASGI", "asgi_logo-color.svg", "https://fastht.ml/about/foundation#sec1"),
        ("HTMX", "htmx.svg", "https://fastht.ml/about/foundation#sec1"),
        ("HTTP", "http-domain-svgrepo-com.svg", "https://fastht.ml/about/foundation#sec3"),
        ("HTML", "html-1.svg", "https://fastht.ml/about/components"),
    ]),
    ("Use tools you already know", "FastHTML embraces the familiar:", [
        ("Python", "python.svg", "https://fastht.ml/about/tech#sec1"),
        ("Uvicorn", "uvicorn.png", "https://fastht.ml/about/tech#sec3"),
        ("Starlette", "starlette.svg", "https://fastht.ml/about/tech#sec4"),
        ("SQLite", "sqlite370_banner.gif", "https://fastht.ml/about/tech#sec5"),
    ]),
    ("Deploy anywhere", "FastHTML runs anywhere Python does, including 1-click deploy to:", [
        ("Railway", "railway.svg", "https://railway.app/"),
        ("Vercel", "vercel.svg", "https://vercel.com/templates/python/fasthtml-python-boilerplate"),
        ("Hugging Face", "hugging-face.svg", "https://huggingface.co/"),
        ("PythonAnywhere", "python-anywhere.svg", "https://www.pythonanywhere.com/"),
    ]),
]

benefits = [
    ("Get started fast", "A single Python file is all that's needed to create any app you can think of. Or bring in any Python or JS library you like."),
    ("Flexibility", "FastHTML provides full access to HTTP, HTML, JS, and CSS, bringing the foundations of the web to you. There's no limits to what you can build."),
    ("Speed & scale", "FastHTML applications are fast and scalable. They're also easy to deploy, since you can use any hosting service that supports Python.")
]

faqs = [
    ("What kinds of applications can be written with this?",
     "It's good for: general purpose web applications (i.e anything you'd build with React, Django, Next.js, etc); quick dashboards, prototypes, and in-company apps (e.g. like what you might use gradio/streamlit/etc for); Analytics/models/dashboards interactive reports; Custom blogs and content-heavy sites where you also want some interactive/dynamic content."),
    ("Where can I deploy my FastHTML to? What's needed?",
     "You can deploy a FastHTML app to any service or server that supports Python. We have guides and helpers for Railway.app, Vercel, Hugging Face Spaces, Replit, and PythonAnywhere. You can also use any VPS or server, or any on-premise machine with Python installed. All major operating systems are supported."),
    ("How does FastHTML relate to FastAPI?",
     "FastAPI is one of the inspirations for FastHTML. We are fans of its developer experience and tried to make FastHTML extremely familiar for FastAPI users. FastAPI is designed for creating APIs, whereas FastHTML is designed for creating HTML (i.e \"Hypermedia applications\"). Anything you could create with FastAPI (plus a JS frontend), you could also create with FastHTML, and vice versa -- if you prefer mainly writing JS, you might prefer FastAPI, since you can move a lot of client-side logic into the JS. If you prefer mainly writing Python, you'll probably want to use FastHTML, since you can often avoid using JS entirely."),
    ("Is this only for multi-page \"old style\" web apps, or can FastHTML be used for modern SPA apps too?",
     "FastHTML is specifically designed to make writing modern SPA apps as fast and easy as possible, whilst also ensuring the apps you write are scalable and performant. By default, FastHTML routes return lightweight \"partials\" that update the DOM directly, rather than doing a full page refresh."),
    ("What is HTMX, and what's it go to do with FastHTML?",
     "HTMX is best thought of as filling in the missing bits of a web browser -- in fact, web browser manufacturers are considering incorporating similar features directly into future browsers. It is a small javascript library that with a single line of HTML lets you respond to any event from any part of a web page by modifying the DOM in any way you like, all directly from Python. Whilst you don't have to use it with FastHTML, it will dramatically increase the amount of stuff you can do!"),
    ("Do I need to know JS? Can I use it if I want, with FastHTML?",
     "No, and yes! You can write nearly any standard web app with just Python. However, using a bit of JS can be helpful -- for instance, nearly any existing JS lib can be incorporated into a FastHTML app, and you can sprinkle bits of JS into your pages anywhere you like."),
    ("Are FastHTML apps slower than React, Next.js, etc?",
     "It depends. Apps using FastHTML and HTMX are often faster than JS-based approaches using big libraries, since they can be very lightweight.")
]

# Create images with:
#  `magick input.jpg -alpha set -background none -vignette 0x0+0+0 -crop 100%x100%+0+0 +repage -resize 112x112 output.png`
gr_test = Div(Ul(Li('ergonomic af'), Li('fast af'), Li('slick af'), Li('SSR af'),
                 style="list-style-type: square;", cls="m-body text-black"),
             P(A('(From twitter)', href='https://x.com/rauchg/status/1807965785585078773', cls="border-b-2 border-b-black/30 hover:border-b-black/80")))
testimonials = [
    ("FastHTML is as intuitive as FastAPI, lends itself to clean architecture, and its HTML+HTMX structure makes it a good competitor to Django for building webapps. Most importantly, it's fun to use.",
        "Daniel Roy Greenfeld", "Co-author", "Two Scoops of Django", "assets/testimonials/daniel-roy.png"),
    ("Python has always been a wonderful tool for creating web applications; with FastHTML, it's even better!",
        "Giles Thomas", "Founder", "PythonAnywhere", "assets/testimonials/giles-thomas.png"),
    ("With FastHTML and Railway, Pythonistas can now have a real web application running in minutes, and can scale it all the way up to sophisticated production deployments.",
        "Jake Cooper", "CEO", "Railway.app", "assets/testimonials/jake-cooper.png"),
    (gr_test, "Guillermo Rauch", "CEO", "Vercel", "assets/testimonials/guillermo-rauch.jpg"),
    # ("FastHTML is a breath of fresh air. It's simple, it's fast, and it's fun to use.",
    #     "Jake Cooper", "CEO", "Railway.app", "assets/testimonials/jake-cooper.png"),
]
