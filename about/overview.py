from about.app import *

def page():
    caption = "'Real' web development shouldn't be this hard..."
    fig = Figure(DivCentered(Img(src='/assets/webdev.jpg', alt='Web dev'), Caption(caption, cls=TextT.lg+'pt-4')), cls='float-right w-1/2 m-4')
    h2s = 'Getting started', 'Background', 'Current Status'
    txts = [Markdown(s1), Div(fig, Markdown(s2)), Markdown(s3)]
    secs = Sections(h2s, txts)
    return BstPage(0, 'About FastHTML', h2s, *secs)

s1 = """
FastHTML is a new way to create modern interactive web apps. It scales down to a 6-line python file, and scales up to complex production apps.  Auth, DBs, caching, styling, etc are all built-in, and replaceable and extensible. 1-click deploy is available to Railway, Vercel, Huggingface, and more---or deploy to any Python server or VPS, including Azure, GCP, and AWS.

You're using a FastHTML app right now. We didn't create a separate blog system for this site, because building apps with FastHTML is so easy there's no need for it! Here is the [source code](https://github.com/AnswerDotAI/fh-about/blob/main/overview.py) for the current page, for instance. You'll see that the code is very simple, relying on Python components like `Markdown` to build the page. The components are simple Python functions---here is the [source code for `Markdown`](https://github.com/AnswerDotAI/fh-about/blob/main/app.py#L6), taking just one line of code! Out of the box FastHTML provides authentication, [database](/tech#sec5) access, styles (via [PicoCSS](https://picocss.com/)), and more. Every part of the system is extensible and replacable using pip-installable Python modules.

The site you're reading right now provides background information about the key concepts and ideas behind FastHTML. The [documentation](https://docs.fastht.ml/) focuses on the code. Because FastHTML brings together many different web technologies, it's worth investing some time to understand how it all fits together. Have a look through the five sections in the green navbar (or hamburger menu if you're on mobile) above to deepen your understanding. As legendary Python coder and "Two Scoops of Django" co-author Audrey Roy Greenfeld told us:

> "*I think the fact that an experienced web dev can get productive in 1 hour accidentally undersells FastHTML a bit. For me it is like a fractal where the more I explore, the more interesting is and the more I learn. I'm about 40 hours in, enough to realise I know nothing compared with what I can learn.*"

If you're an experienced web dev, then you can use all your knowledge of CSS, HTML, JS, etc. to build web applications with FastHTML right away. We've heard from expert coders that they have successfully built complete web apps within an hour of getting started with FastHTML. We've got a [Quickstart for Web Developers](https://docs.fastht.ml/tutorials/quickstart_for_web_devs.html) tutorial that will get you up and running quickly. (Read the rest of the docs while you're there!) Next, read through the heavily-commented source of this [idiomatic fasthtml app](https://github.com/AnswerDotAI/fasthtml/blob/main/examples/adv_app.py). Then study some of the [fasthtml-example applications](https://github.com/AnswerDotAI/fasthtml-example), particularly the first four listed.

If you haven't done much (or any) web development, try following through each step of the [FastHTML By Example](https://docs.fastht.ml/tutorials/by_example.html) tutorial. We don't yet have a self-contained guide explaining all the web foundations you'll need to know (HTML, HTTP, CSS, etc.), so you'll probably need to do some self-learning through other resources. But watch this space---we're planning a complete web programming from scratch course soon! In the meantime, here's a 1-hour video lesson to help you get going:

<div class="embed-responsive embed-responsive-16by9">
    <iframe width="560" height="315" class="embed-responsive-item" src="https://www.youtube.com/embed/Auqrm7WFc0I?si=3B1ZgtH27yJ3u7d0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
"""

s2 = """
FastHTML is a system for writing web applications in Python. It is designed to be simple, powerful, and flexible. It is also designed to be easy to learn and use. The project is inspired by technologies such as React JSX, Hotwire, Astro, FastAPI, and Phoenix LiveView. FastHTML is small and simple---at the time of writing, it's under 1000 lines of code. That's because it's built on top of powerful and flexible foundations: Python, Starlette, Uvicorn, and HTMX. If you're a FastAPI user, much of FastHTML will look very familar; FastAPI was a major inspiration.

FastHTML was originally started by Jeremy Howard at Answer.AI for a number of reasons:

- Over 25 years of web development, Jeremy realized that web programming could be easier and more powerful. He was particularly concerned that recent trends had moved away from the power of the web's foundations, resulting in a fractured ecosystem of over-complex frameworks and tools
- He saw that two small but ingenious developments had made the web's foundations more powerful and more accessible: **ASGI** and **HTMX**. But the tools available for using them were still too complex, and the barriers to entry were still too high
- Jeremy and his wife Rachel had spent the last 8 years working to make artificial intelligence accessible to more people. They saw that the most widely used web development tools were too complex for people who aren't full time coders. This meant that Jeremy and Rachel's students struggled to turn their AI project ideas into working applications.
- Jeremy's goal for Answer.AI is to help society benefit from AI, which means creating lots of useful products and services that use AI effectively---so creating those products and services needs to be made as fast and easy as possible.

FastHTML is a framework that deals with all these issues: it returns to the roots of the web, leveraging ASGI and HTMX, and is usable by both experienced developers and new coders.

#### A new generation of coders

Coding is the key to turning the ideas in your head into products and services that can help people. AI has recently made it easier to get started with coding, which means there are more people than ever before who can create useful stuff.

But this new generation of coders do not generally have the same background as full-time software engineers. They may have been trained in a different field, or they may have learned to code on their own. We hope that FastHTML will make it easier for this new generation of coders to turn their ideas into reality. To create maintainable and scalable solutions.
"""

s3 = """
FastHTML works well right now, but it is still young. We are using it for nearly every part of the FastHTML project itself ("almost" because the docs are using [Quarto](https://quarto.org/) for now; we plan to port them to a FastHTML-based documentation system soon). For instance, we worked with a design team to create the [fastht.ml home page](https://www.fastht.ml/), which is implemented in FastHTML---here is the [home page source](https://github.com/AnswerDotAI/home-fasthtml/blob/main/main.py).

We're working on a number of things to make FastHTML even better. Not everything is ready "out of the box" yet. If you see something missing that you need, please let us know by [creating an issue](https://github.com/AnswerDotAI/fasthtml/issues). Or feel free to add it yourself and send in a pull request!

The plan is for FastHTML to do just about everything that frameworks like Django, NextJS, and Ruby on Rails do, but it'll take a while to get there! For experienced developers, adding bindings to CSS frameworks, pypi Python modules, and JS libraries is straightforward---if you add one, please put your binding module on pypi so that the community can use it, and let us know so we can link to your project. We invite you to use the "`fh-`" prefix on PyPI to make it easy to identify FastHTML packages there.

Here's a few of the things on our short to medium term agenda:

- OAuth support
- Support for more databases
- Support for more CSS frameworks, including DaisyUI, Bootstrap, Shoelace, and Flowbite (we've already made a start at all of these).
"""
