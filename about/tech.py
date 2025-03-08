from about.app import *

def page():
    h2s = 'Python', 'HTMX', 'Uvicorn', 'Starlette', 'SQLite'
    txts = [Markdown(s1), Markdown(s2), Markdown(s3), Markdown(s4), Markdown(s5)]
    secs = Sections(h2s, txts)
    return BstPage(3, "FastHTML's tech stack", h2s, *secs)

s1 = """
Many of the largest software systems in the world are built using Python, such as much of the code for YouTube, Instagram, Dropbox, and many others. In 2019, Dropbox announced that python was their "most widely used language both for backend services and the desktop client app", with 4 million lines of code.

If you're already a Python programmer, then you'll know how easy it is to turn your ideas into code using this language. As well as being used for large-scale systems, Python is also popular for the day-to-day work of scientists, engineers, data analysts, and so forth.

One particular challenge for Python programmers has been that to create a modern web application, they have had to also learn JavaScript, along with a framework like React, Angular, or Vue. Even after learning all this, they still have to deal with the complexity of writing, debugging, and maintaining a multi-language system with complex interactions between the two languages and across the client-server boundary.

With FastHTML, you'll often find you never have to write any JavaScript at all. Not only does development and debugging become much easier, but many features suddenly become easier to implement. For instance, when we wanted to add caching to speed up our [home page](https://fastht.ml), we simply added a standard decorator to the function that creates it. No need for special infrastructure, because the implementation is all in one place. ASGI makes this particularly powerful---it can handle caching, sessions, authentication, host-based redirects, sub-routing, and more, all in one place. All of this is directly accessible from FastHTML.
"""

s2 = """
Nowadays most web applications are built using backend systems that return a combination of JSON and HTML data over HTTP. Javascript, normally using frameworks such as React, Angular, or Vue, is used to combine the JSON and HTML together for display in the browser. This is an *"API based"* approach to web development.

An alternative "hypermedia-based" approach, used by [HTMX](https://htmx.org/), simplifies things greatly by just returning HTML. FastHTML is designed to create hypermedia applications. Nearly all of the complexity of client-server programming vanishes when using this approach. When going to a page directly, the server will respond with a standard HTML web page:

```html
<html>
  <head><title>FastHTML Page</title></head>
  <body>
    <p id="greet" hx-get="/change">Hello World!</p>
  </body>
</html>
```

This can be generated using this FastHTML code:

```python
@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")
```

When clicking on this link, the server will respond with an "*HTML partial*"---that is, just a snippet of HTML which will be inserted into the existing page:

```html
<p>Nice to be here!</p>
```

In this case, the returned element will replace the original `P` element (since that's the default behavior of HTMX). Our code to create this `/change` handler is:

```python
@rt('/change')
def get(): return P('Nice to be here!')
```

As we discussed in the [HTMX foundations](/foundation#sec2) section, HTMX removes four critical constraints of HTML. It allows any event on any DOM element to call any HTTP method on any path and place the response anywhere in the DOM. If you haven't written a hypermedia-based application before, then we strongly recommend reading the [Hypermedia Systems book](https://hypermedia.systems/). It explains how to build hypermedia applications using HTMX; the techniques you learn there will be directly applicable to FastHTML.
"""

s3 = """
[Uvicorn](https://www.uvicorn.org/) is, according to its website, "an ASGI web server". What does that even mean? As [we've discussed](/foundation#sec1), ASGI is a Python API that converts HTTP requests and responses into Python function calls. Uvicorn is a web server which a web browser can talk to, and it in turn talks to an ASGI application, returning its results back to the browser.

Most of the time you'll run your FastHTML application by simply adding one line of code to the end of your `main.py` file: `serve()`. When you do, a message will be printed letting you know that you now have a web server running on your computer, and if you click on the provided link you'll see your application running. If you look at the source code for `main.py`, you'll see that the line of code that actually runs the server is calling Uvicorn to do the work:

```python
uvicorn.run(f"{fname}:{app}", host=host, port=port, reload=reload)
```

When you deploy your application, you'll often use a service provider like Railway or Vercel. The one-click deployment we provide simply calls `python main.py` for you, and the provider is responsible for connecting the port that Uvicorn is running on to a public IP address. You can also run your application on a server such as a VPS, and either set the `PORT` environment variable to `80` to make it available directly, or add a frontend server like nginx or caddy to forward requests to the port that Uvicorn is running on.
"""

s4 = """
Because ASGI is such a simple API (it's literally a single Python function that takes three arguments), counter-intuively that actually makes it quite complex to use. It doesn't do that much for you, so there's quite a lot of boilerplate to write in order to create an ASGI application directly to use with Uvicorn.

[Starlette](https://www.starlette.io/) makes it much easier to create ASGI applications. It removes a lot of the boilerplate by providing a few simple abstractions, such as `Request`, `Response`, and `Route`. Reading the source code to Starlette is very informative, because you realise how little code is actually involved; it's just converting the minimal ASGI API into a more convenient set of classes and functions.

Starlette isn't at all opinionated about how you create your web application. Therefore, other libraries have stepped in to provide more specific functionality. For instance, [FastAPI](https://fastapi.tiangolo.com/) provides a framework built on top of Starlette that adds a lot of functionality for creating JSON APIs.

When Jeremy Howard decided he wanted to create a library to make it easier to build hypermedia applications, he used FastAPI as a role model. In fact, he went through each page of the FastAPI tutorial and attempted to replicate as much as he could, but for hypermedia applications instead of JSON APIs. The creator of FastAPI, Sebastián Ramírez, was extremely generous with his time and advice to Jeremy and helped to explain the thinking behind FastAPI's design.

The main `FastHTML` class is actually implemented as a subclass of Starlette's `Application` class. That means that you can use any middleware, routing, and other features that are compatible with Starlette. (However, you'll often find that FastHTML provides a more convenient way to do things.)

Although FastAPI and FastHTML are both built on top of Starlette, and FastHTML is inspired by FastAPI, there are plenty of differences, since they have different purposes. So if you've used FastAPI before, don't assume that everything will be identical!
"""

s5 = """
Out of the box, FastHTML provides support for SQLite, via the [Fastlite](https://answerdotai.github.io/fastlite/) library. SQLite is built in to Python, so you don't need to install anything extra. Because it uses a file to store and access the database directly from Python, it's extremely fast to access, and it's very easy to use. Fastlite provides an extremely simple API for database access, and lets you use standard Python builtin functionality such as dataclasses and dicts to read and write data.

Older versions of SQLite were not scalable, because they didn't support concurrent reads with writes. That limitation however was resolved some years ago through the addition of [write-ahead logging](https://www.sqlite.org/wal.html) (WAL), which FastHTML uses by default. With WAL and a modern multi-core computer and fast SSD, SQLite can support large and popular websites. Systems such as [Litestream](https://litestream.io/) can be used to replicate the database to a remote server.

Instead of Fastlite and SQLite, you can also use SQLModel, SQLAlchemy, Redis, or any other database server or data storage system. We (and the FastHTML community) will be continually adding more data storage options to FastHTML.
"""
