from fasthtml.common import *
from home_components import *
from content import *

_blank = dict(target="_blank", rel="noopener noreferrer")
description = 'Modern web applications in pure Python'

def benefit(title, content):
    return Div(
        H3(title, cls=f"text-black heading-3"),
        P(content, cls=f"l-body mt-6 lg:mt-6"),
        cls="w-full p-6 bg-soft-yellow rounded-2xl xl:p-12 lg:h-[22rem] lg:w-[26rem]")

def faq_item(question, answer, id):
    return accordion(
        id=id, question=question, answer=answer,
        question_cls="text-black s-body",
        answer_cls="s-body text-black/80 col-span-full",
        container_cls=f"{col} justify-between bg-soft-blue rounded-[1.25rem] {bnset}"
    )

def hero_section():
    return (
    Header(
        Nav(
            A(
                Img(src='/assets/logo.svg', alt='FastHTML', width='105', height='24'),
                href='#'),
            A('Read docs', href='https://docs.fastht.ml', **_blank,
              cls=f'bg-black text-white py-2 px-4 s-body rounded-[62.5rem] hover:bg-black/80 transition-colors duration-300 px-4 py-1 h-10 {center} justify-center'),
            cls=f'py-2 px-4 {between} items-center rounded-full w-full max-w-[400px] bg-white/50 backdrop-blur-lg border border-white/20'),
        cls=f'fixed top-0 w-full left-0 p-4 {center} justify-center z-50'),
    Section(
        Div(
            File('assets/hero-shapes.svg'),
            cls='absolute z-0 lg:-top-[15%] top-0 left-1/2 -translate-x-1/2 grid grid-cols-1 grid-rows-1 w-[120%] aspect-square max-w-[2048px] min-w-[900px]'),
        Div(
            Div(cls='lg:flex-1 max-lg:basis-[152px]'),
            Div(
                H1(description, cls='heading-1 max-w-3xl'),
                P('Built on solid web foundations, not the latest fads - with\nFastHTML you can get started on anything from simple dashboards to\nscalable web applications in minutes.',
                    cls='m-body max-w-[40rem] text-center'),
                cls=f'flex-1 {col} items-center justify-center gap-6 text-center w-full text-black'
            ),
            Div(
                A('Learn more', href='https://about.fastht.ml', **_blank,
                    cls=f'{bnset} m-body px-4 py-1 rounded-full bg-black hover:bg-black/80 transition-colors duration-300 text-white h-[76px] w-full max-w-[350px] flex items-center justify-center'),
                video_button('Watch intro', '/assets/thumb.png', '7min 30sec', "QqZUzkPcU7A?si=lTtHuMT5HPC66-49"),
                cls=f'flex-1 {center} justify-center content-center flex-wrap lg:gap-6 gap-4 m-body'),
                video_player('Try now'),
            cls=f'{col} flex-1 relative px-4 lg:px-16'),
        cls=f'{col} relative w-full h-screen max-h-[1024px] min-h-[720px] overflow-hidden bg-grey')
    )

def code_display(file_name, code_snippet, snippet_id):
    return Div(
        Div(
            Div(
                P(file_name, cls=f"xs-mono-body {center}"),
                Button(
                    Div(
                        Img(cls="button-content w-4 h-4", src="assets/icons/copy-icon.svg", alt="Copy"),
                        Span("Copied!", cls=f"absolute bg-inherit rounded-l-[0.5rem] {center} py-2 h-full right-0 copied-text overflow-hidden w-0 peer-clicked:w-fit s-body text-white/80 transition-transform transition-all duration-600 ease-out"),
                        cls=f"relative bg-black/20 rounded-[0.5rem] {center} p-2 h-8 w-fit"),
                    cls="copy-button"),
                cls=f"w-full {between}"),
            cls="bg-black/20 text-white/80 w-full max-w-2xl lg:max-w-xl p-4 rounded-2xl"),
        Pre(
            Code(code_snippet, cls="python w-full mono-body"),
            id=snippet_id,
            cls="code-snippet relative max-h-[25rem] overflow-hidden hide-scrollbar"),
        Div(cls="absolute code-fade-out bottom-0 left-0 right-0 h-16 bg-gradient-to-b from-transparent to-[#3a2234] pointer-events-none"),
        cls=f"relative {col} gap-6 lg:max-w-[45rem] w-full overflow-hidden"
    )

def code_demo(title, file_name, code_snippet, demo_content, is_active=False):
    snippet_id = f"{title.lower().replace(' ', '-')}-code-snippet"
    demo_cls = f"{center} my-11 p-4 flex-none whitespace-normal justify-center h-96 rounded-3xl bg-soft-purple lg:p-8 w-full max-w-2xl lg:max-w-md lg:mx-28 lg:my-8 overflow-y-auto {'lg:items-start hide-scrollbar' if snippet_id == 'reusable-code-snippet' else ''}"
    return Div(
        code_display(file_name, code_snippet, snippet_id),
        Div(demo_content, cls=demo_cls),
        aria_labelledby=f"tab-{title.lower().replace(' ', '-')}", role="tabpanel",
        cls=f"code-container pt-8 lg:pt-16 tab-panel relative hide-scrollbar toggle-element {col} lg:flex-row lg:justify-between overflow-hidden w-full lg:max-w-[1440px] xl:mx-auto {'hidden' if not is_active else ''}",
        id=f"{title.lower().replace(' ', '-')}-code-demo")

def tab_button(title, is_active=False):
    classes = f"z-10 button-container flex-none relative px-8 py-2 w-[10.59375rem] h-11 rounded-full {center}"
    active = f"{classes} current active transition-all duration-300 text-white"
    inactive = f"{classes} text-white/80 hover:text-white"
    return Li(
        Button(
            Div(title, cls="m-body w-max mx-auto"),
            id=f"tab-{title.lower().replace(' ', '-')}",
            cls="toggle-button w-full cursor-pointer",
            data_target=f"{title.lower().replace(' ', '-')}-code-demo",
            tabindex="-1" if not is_active else None,
            name=f"tab-{title.lower().replace(' ', '-')}"),
        role="tab", aria_selected="true" if is_active else "false",
        cls=active if is_active else inactive)

async def component_preview_section():
    cs = await components()
    return Section(
        Div(
        Div(
            H2("This home page is a FastHTML app.", cls="text-white heading-2 pt-8"),
            P("Click the buttons below to see four small, live components in action.", cls=f"text-white pt-8 l-body {maxrem(32)}"),
            cls=f"{maxrem(50)} mx-auto {col} {center} text-center gap-6"
        ),
        *[code_demo(title, file_name, code_snippet, demo_content, i == 0) for i, (title, file_name, code_snippet, demo_content) in enumerate(cs)],
        Ul(
            *[tab_button(title, i == 0) for i, (title, _, _, _) in enumerate(cs)],
            Div(id="highlighter", cls=f"{inset} z-0 highlighter w-[10.59375rem] absolute bg-white/20 h-[2.75rem] rounded-[62.5rem] transition-transform duration-300"),
            role="tablist", id="tab-list",
            cls=f"relative mt-12 text-white/80 flex-none rounded-[62.5rem] bg-black/20 p-2 max-w-full overflow-x-auto lg:mx-auto {center} hide-scrollbar lg:max-w-[43.375rem]"),
            cls=f"{col} {center}"),
        cls="relative bg-purple px-4 lg:px-16 pb-24 -mt-8 lg:-mt-10 flex-col xl:items-center items-start gap-6 lg:gap-16 rounded-t-3xl lg:rounded-t-[2.5rem] overflow-x-hidden")

def stacked_cards_section():
    return Section(
        Div(
            Div(
                Div(
                    P("TECH STACK", cls="mono-body text-opacity-60"),
                    H2("FastHTML scales up and scales down.", cls="text-black heading-2"),
                    P("Read more about our ", 
                        A("design philosophy here", href="https://about.fastht.ml/vision", **_blank,
                          cls="border-b-2 border-b-black/30 hover:border-b-black/80"),
                        ", or click a button below:",
                        cls=f"l-body {maxrem(32)}"),
                    cls=f"{maxrem(50)} mx-auto {col} {center} text-center gap-6"),
                cls="py-8 lg:pt-16 px-4 lg:px-16 rounded-t-3xl lg:rounded-t-[2.5rem] bg-green"),
            cls="bg-yellow sticky top-0 bottom-[calc(100%-300px)] w-full"),
        Div(
            Div(
                *[stacked_card(title, description, tech_stack, "bg-soft-green") for title, description, tech_stack in stacked],
                id="stacked-cards", cls=f"{maxrem(50)} mx-auto"),
            cls="px-4 lg:px-16 w-full bg-green pt-8"),
        id="stacked-cards-section", cls="relative")

def samples_section():
    text = "FastHTML can be used for everything from collaborative games to multi-modal UI. We've selected small self-contained examples for you to learn from."
    return section_wrapper(
            (section_header("SAMPLES", "See FastHTML in action", text, max_width=40),
            Div(
                *[Div(
                    A(
                        File(f"assets/{svg}"),
                        Div(
                            P(name, cls="border-b-2 border-b-black/30 hover:border-b-black/80 regular-body"),
                            Img(src=f"{icons}/arrow-up-right.svg", alt="Arrow right icon", cls="group-hover:translate-y-[-0.1rem] transition-all ease-in-out duration-300"),
                            cls=f"{gap2} transition-transform transform relative items-center mt-4 lg:mt-6"),
                        href=url, cls=f"{col} items-center"),
                    cls="group px-2"
                ) for name, svg, url in samples],
                cls="grid max-w-5xl lg:grid-cols-4 lg:max-w-7xl lg:gap-x-12 grid-cols-2 gap-x-4 gap-y-8 w-full mx-auto"),
            A("Discover all", href=eg_url,
                cls=f"{bnset} bg-black text-white py-2 px-4 s-body rounded-full hover:bg-black/70 transition-colors duration-300")),
        bg_color="grey")

def how_it_works_section():
    msg = "With FastHTML you create good-looking modern web applications in pure Python and deploy them in minutes."
    return section_wrapper(
        (Div(
            section_header( "GET STARTED IN MINUTES", "The fastest way to create a real web application.", msg),
            cls="max-w-3xl w-full mx-auto flex-col items-center text-center gap-6 mb-8 lg:mb-8"),
            Div(*[benefit(title, content) for title, content in benefits],
                cls=f"{col} w-full lg:flex-row gap-4 items-center lg:gap-8 max-w-7xl mx-auto justify-center"),),
        bg_color="yellow", flex=False)

def faq_section():
    return section_wrapper(
        Div(
            section_header( "FAQ", "Questions? Answers.", "Your top FastHTML questions clarified.",
                max_width=21, center=False),
            Div(
                *[faq_item(question, answer, i+3) for i, (question, answer) in enumerate(faqs)],
                cls=f"{col} gap-4 {maxrem(32)} transition ease-out delay-[300ms]"),
            cls=f"{section_base} w-full mx-auto lg:flex-row items-start max-w-7xl"),
        bg_color="blue")

def testimonials_section():
    testimonial_cards = [testimonial_card(i, *args) for i, args in enumerate(testimonials)]
    return section_wrapper(
        Div(
            section_header(
                "LOVE IS IN THE AIR", "What the experts say",
                "Top web programmers tell us that they love working with FastHTML.",
                max_width=21, center=False),
            carousel(testimonial_cards),
            cls=f"{section_base} {maxrem(90)} mx-auto lg:flex-row items-start"),
        bg_color="pink")

def footer_link(text, href, **kw):
    return Li(A(
        Span(text, cls="border-b border-b-transparent border-b-white/50"),
        Img(src=f"{icons}/arrow-up-right-white.svg", alt="Arrow right icon", width="16", height="16", cls="w-4 h-4"),
        href=href, cls=f"{gap2} items-center hover:text-white border-b border-b-transparent hover:border-b-white", **kw))

def footer():
    return Section(
        Div(
            Div(
                P("© 2024 onwards AnswerDotAI. All rights reserved.", cls="mr-auto"),
                Nav(
                    Ul(
                    footer_link("Github", "https://github.com/AnswerDotAI/fasthtml", **_blank),
                    footer_link("Join Discord", "https://discord.gg/qcXvcxMhdP", **_blank),
                    footer_link("Docs", "https://docs.fastht.ml", **_blank),
                    footer_link("Site design", "https://tinloof.com/", **_blank),
                    cls="flex max-lg:flex-col max-lg:items-start gap-4 lg:gap-6 flex-wrap")),
                cls="relative z-[1] mono-s flex max-lg:flex-col gap-6 text-white/80 px-4 lg:px-16 pb-16"),
            Div(
                Div(
                    File("assets/footer-shapes.svg"),
                    cls=f"absolute z-0 lg:-top-[15%] top-0 left-1/2 -translate-x-1/2 grid grid-cols-1 grid-rows-1 lg:w-[150%] w-[200%] aspect-square max-w-none min-w-max"),
                File("assets/footer-path.svg"),
                cls=f"relative z-0 w-full px-4 lg:px-16 pb-1 {col} flex-1 justify-end"),
            cls=f"relative w-full h-[420px] lg:h-[600px] {col} pt-8 lg:pt-12 rounded-t-3xl lg:rounded-t-[2.5rem] bg-black overflow-hidden -mt-8 lg:-mt-10"))

hdrs = [
    Meta(charset='UTF-8'),
    Meta(name='viewport', content='width=device-width, initial-scale=1.0, maximum-scale=1.0'),
    Meta(name='description', content=description),
    *Favicon('favicon.ico', 'favicon-dark.ico'),
    *Socials(title='FastHTML',
        description=description,
        site_name='fastht.ml',
        twitter_site='@answerdotai',
        image=f'/assets/og-sq.png',
        url=''),
    # surrsrc,
    Script(src='https://cdn.jsdelivr.net/gh/gnat/surreal@main/surreal.js'),
    scopesrc,
    Link(href='css/main.css', rel='stylesheet'),
    Link(href='css/tailwind.css', rel='stylesheet'),
    Link(href='css/stack.css', rel='stylesheet'),
    Link(href='css/preview-stack.css', rel='stylesheet'),
    Link(href='css/highlighter-theme.css', rel='stylesheet')]

from gallery.main import ar as gallery_ar, application_routes
from about.main import app as about_app
routes = [Mount(f"/about", about_app),
          Mount('/docs', StaticFiles(directory='docs', html=True)),
          Mount('/gallery/files', StaticFiles(directory='gallery')),
          *application_routes
          ]

bodykw = {"class": "relative bg-black font-geist text-black/80 font-details-off"}
app,rt = fast_app(hdrs=hdrs, default_hdrs=False, bodykw=bodykw, on_startup=[startup], routes=routes)

gallery_ar.to_app(app)

scripts = (
    Script(src='https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js'),
    Script(src='https://cdnjs.cloudflare.com/ajax/libs/highlightjs-line-numbers.js/2.8.0/highlightjs-line-numbers.min.js'),
    # Script(src='js/videoPopup.js'),
    Script(src='js/pythonHighlighter.js'),
    Script(src='js/carouselScroll.js'),
    Script(src='js/stack.js'),
    Script(src='js/togglePreview.js'),
    Script(src='js/codeOverflow.js'),
    Script(src='js/copyCode.js'),
    )

from fastcore.xtras import timed_cache

@timed_cache(seconds=60)
async def home():
    return (Title(f"FastHTML - {description}"), 
        Main(
            hero_section(),
            await component_preview_section(),
            how_it_works_section(),
            stacked_cards_section(),
            samples_section(),
            faq_section(),
            testimonials_section(),
            footer()),
        *scripts)

@rt("/")
async def get(): return await home()



serve()