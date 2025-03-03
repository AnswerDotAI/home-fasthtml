from about.app import *

def page():
    caption = "A minimal FastHTML app really is minimal."
    fig = Figure(DivCentered(Img(src='assets/hello.png', alt='Web dev', cls='h-60'), Caption(caption, cls=TextT.lg+'pt-2')), cls='float-right m-2')
    h2s = 'No compromise', 'Scaling down', 'Scaling up'
    txts = [Markdown(s1), Div(fig, Markdown(s2)), Markdown(s3)]
    secs = Sections(h2s, txts)
    return BstPage(1, 'The FastHTML Vision', h2s, *secs)

s1 = """FastHTML is a general-purpose full-stack web programming system, in the same vein as Django, NextJS, and Ruby on Rails. The vision is to make it the easiest way to create quick prototypes, and **also** the easiest way to create scalable, powerful, rich applications.

It is important to have a system that can scale down, as well as up. That's because the best way to create a big complex application is to first create a small simple application, and then add to it in small steps. If we don't make it easy to create small, simple applications, then fewer people get started and fewer ideas get tried.

#### Two types of tools

Most software development platforms that make it easy to get started make it hard to scale in size and complexity. As a result, the development landscape gets segmented into "domain expert tools" like Streamlit, Gradio, and Wordpress, vs "serious programmer tools" like React and Django.

This means that picking one of those domain expert tools is a compromise: if what you're building is really successful, then at some point you'll have to throw it away and start again---possibly in a whole different programming language. The domain expert tools generally use very high-level abstractions specific to a single tool, which means learning a new set of foundations too. And the serious programmer tools add unnecessary complexity, slowing down both learning and development, and making maintenance harder.
"""

s2 = """
FastHTML scales down by picking the most widely used language for "getting stuff done": Python. And then it throws away everything that makes Python web programming complicated. No templates with quirky template languages. No multi-folder multi-file project skeletons. No complex type systems. No separate JavaScript frontend. No single-framework reactive abstractions. No build step. No tree shaking. No nonsense.

A FastHTML application can start as a single Python file. In fact, it can stay as a single Python file! You only need to break things into multiple files if _you_ decide that will help you build or maintain your software.

FastHTML applications don't require learning about and installing separate CSS and JavaScript frameworks. You can pip install a complete style library, such as a UI toolkit or template, and use it entirely from Python. We're building FastHTML libraries for DaisyUI, Bootstrap, Shoelace, Flowbite, and more. You can use these, or create your own, and customise them all with Python. You can pip install additional functionality provided by JavaScript and Python libraries, both controllable entirely from Python.
"""

s3 = """
FastHTML scales up by taking advantage of the foundations of the web. Because a FastHTML application directly uses HTTP, HTML, JavaScript, and CSS, there's nothing standing between your application and the power of the web. FastHTML comes with powerful yet simple tools for function-level and handler-level caching, async, threading, HTML partials, and much more.

The most important thing is that the fundamentals you started out with when you scaled down are identical to those you will use when you scale up! Same language, same libraries, same abstractions. As you continue on your web programming journey, all your new skills become more and more powerful!
"""
