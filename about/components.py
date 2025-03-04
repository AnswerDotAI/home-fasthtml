from about.app import *

def page():
    h2s = 'Why', 'How', 'The future'
    txts = [Markdown(s1), Markdown(s2), Markdown(s3)]
    secs = Sections(h2s, txts)
    return BstPage(4, "Python HTML components", h2s, *secs)

s1 = """
FastHTML embeds HTML generation inside Python code. The idea of embedding an HTML generator inside a programming language is not new. It is a particularly popular approach in functional languages, and includes libraries like: Elm-html (Elm), hiccl (Common Lisp), hiccup (Clojure), Falco.Markup (F#), Lucid (Haskell), and dream-html (OCaml). But the idea has now gone far beyond the functional programming world--- JSX, an embedded HTML generator for React, is one of the most popular approaches for creating web apps today.

However most Python programmers are probably more familiar with template-based approaches, such as Jinja2 or Mako. Templates were originally created for web development in the 1990s, back when web design required complex browser-specific HTML. By using templates, designers were able to work in a familiar language, and programmers could "fill in the blanks" with the data they needed. Today this is not needed, since we can create simple semantic HTML, and use CSS to style it.

Templates have a number of disadvantages, for instance:

- They require a separate language to write the templates, which is an additional learning curve
- Template languages are generally less concise and powerful than Python
- Refactoring a template into sub-components is harder than refactoring Python code
- Templates generally require separate files
- Templates generally do not support the Python debugger.

By using Python as the HTML-generation language, we can avoid these disadvantages. More importantly, we can create a rich ecosystem of tools and frameworks available as pip-installable Python modules, which can be used to build web applications.
"""

s2 = """
FastHTML's underlying component data structure is called `FT` ("FastTag"). To learn how this works in detail, see the [Explaining FT Components](https://fastht.ml/docs/explains/explaining_xt_components.html) page. `FT` objects can be created with functions with the Capitalized name of each HTML tag, such as `Div`, `P`, and `Img`. The functions generally take positional and keyword arguments:

- Positional arguments represent a list of children, which can be strings (in which case they are text nodes), FT child components, or other Python objects (which are stringified).
- Keyword arguments represent a dictionary of attributes, which can be used to set the properties of the HTML tag
- Keyword arguments starting with `hx_` are used for HTMX attributes.

Some functions, such as `File`, have special syntax for their arguments. For instance, `File` takes a single filename argument, and creates a DOM subtree representing the contents of the file.

Any FastHTML handler can return a tree of `FT` components, or a tuple of FT component trees, which will be rendered as HTML partials and sent to the client for processing by HTMX. If a user goes directly to a URL rather than using HTMX, the server will automatically return a full HTML page with the partials embedded in the body.

Much of the time you'll probably be using pre-written FastHTML components that package up HTML, CSS, and JS. Often, these will in turn hand off much of the work to some general web framework; for instance the site you're reading now uses Bootstrap (and the `fh-bootstrap` FastHTML wrapper). At first, moving from HTML to FT components, can seem odd, but it soon becomes natural -- as Audrey Roy Greenfeld, a hugely experienced Python web programmer author, and educator, told us:

> "*In my head I had resistance and initial scepticism to converting all my HTML to FT. When I realised that working with the tags in Python is like the elegance of working in the frequency domain after Fourier transform vs. working with time series data in the time domain, I finally gave in, let go, started enjoying the FT tags. The first few times I thought the approach of conversion and then copy pasting was crazy. It was only when I started to understand how to organise the tags into components that it suddenly felt elegant and templates felt crazy.*"

One good approach to creating components is to find things you like on the web and convert them to FastHTML. There's a simple trick to doing this:

1. Right-click on the part of a web page that you want to use in your app, and choose 'Inspect'
1. In the elements window that pops up, right-click on the element you want, choose 'Copy', and then 'Outer HTML'
1. Now you've got HTML in your clipboard, you can automatically convert it to FastHTML: go to [h2f.answer.ai](https://h2x.answer.ai/), paste the HTML into the text area at the top, then the FastHTML code will appear at the bottom. Click the Copy icon at the top right of that code and then paste it into your Python app.

BTW, the h2f app mentioned above is written in around a dozen lines of code! You can see the [source code here](https://github.com/AnswerDotAI/fasthtml-example/blob/main/h2f/main.py).
"""

s3 = """
We want your help! FastHTML is very new, so the ecosystem at this stage is still small. We hope to see FastHTML Python versions of style libraries like Bootstrap, DaisyUI, and Shoelace, as well as versions of all the most popular JavaScript libraries. If you are a Python developer, we would love your help in creating these libraries! If you do create something for FastHTML users, let us know, so we can link to your work (or if you think it would be a useful part of the FastHTML library itself, or one of our extension libraries, feel free to send us a pull request).

We would also like to see Python modules that hook into FastHTML's and Starlette's extensibility points, such as for authentication, database access, deployment, multi-host support, and so forth. Thanks to Python's flexibility and the power of ASGI, it should be possible for a single FastHTML server to replace a whole stack of separate web servers, proxies, and other components.
"""
