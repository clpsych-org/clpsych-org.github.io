import os
from pathlib import Path

import markdown

from staticjinja import Site

markdowner = markdown.Markdown(output_format="html5", extensions=['meta'])

def md_context(template):
    markdown_content = Path(template.filename).read_text()
    content = markdowner.convert(markdown_content)
    context = {k: v[0] for k, v in markdowner.Meta.items()}
    context['content'] = content
    return context


def render_md(site, template, **kwargs):
    # i.e. posts/post1.md -> build/posts/post1.html
    out = site.outpath / Path(template.name).with_suffix(".html")

    # Compile and stream the result
    os.makedirs(out.parent, exist_ok=True)
    site.get_template("_layout.html").stream(**kwargs).dump(str(out), encoding="utf-8")


site = Site.make_site(
    env_globals={
        'date': 'July 2–7, 2026',
        'location': 'CLPsych 2026 will be held at ACL in San Diego',
    },
    searchpath="templates",
    outpath="_build",
    contexts=[(r".*\.md", md_context)],
    rules=[(r".*\.md", render_md)],
)

site.render()
