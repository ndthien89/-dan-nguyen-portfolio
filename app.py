"""Dan Thien Nguyen - portfolio. Run: streamlit run app.py"""
import base64
import json
from html import escape
from pathlib import Path

import streamlit as st

import content as C

ALL_PUBS = json.loads((Path(__file__).parent / "publications.json").read_text())

HERE = Path(__file__).parent
st.set_page_config(page_title="Dan Thien Nguyen, Ph.D.", page_icon="🔋", layout="wide")


def img_b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


CSS = """
<style>
:root {
  --ink: #1d1d1f; --ink2: #6e6e73; --ink3: #86868b; --line: rgba(0,0,0,.08);
  --bg: #fbfbfd; --panel: #ffffff; --soft: #f5f5f7; --blue: #0071e3; --blue-h: #0077ed;
  --font: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", Helvetica, Arial, sans-serif;
}
html, body, .stApp, [data-testid="stAppViewContainer"] { background: var(--bg) !important; }
.stApp, .stApp * { font-family: var(--font); -webkit-font-smoothing: antialiased; }
#MainMenu, header[data-testid="stHeader"], footer, [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
.block-container { max-width: 1120px !important; padding: 0 28px 40px !important; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }
a { color: var(--blue); text-decoration: none; }
a:hover { text-decoration: underline; }

/* nav */
.nav { position: fixed; top: 0; left: 0; right: 0; z-index: 999; height: 52px;
  background: rgba(251,251,253,.72); backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px); border-bottom: 1px solid var(--line); }
.nav-in { max-width: 1120px; margin: 0 auto; height: 100%; padding: 0 28px;
  display: flex; align-items: center; justify-content: space-between; }
.nav-name { font-weight: 600; font-size: 15px; color: var(--ink); letter-spacing: -.01em; }
.nav-links a { color: var(--ink); opacity: .8; font-size: 12.5px; margin-left: 26px; }
.nav-links a:hover { opacity: 1; text-decoration: none; }

/* sections */
section { padding: 96px 0 0; scroll-margin-top: 60px; }
.eyebrow { color: var(--ink3); font-size: 15px; font-weight: 600; letter-spacing: .01em; margin: 0 0 10px; }
h2.sec { font-size: 48px; line-height: 1.08; font-weight: 700; letter-spacing: -.025em; color: var(--ink); margin: 0 0 36px; }
p.lead { font-size: 21px; line-height: 1.45; color: var(--ink2); letter-spacing: -.01em; margin: 0; }

/* hero */
.hero { display: grid; grid-template-columns: 1.25fr .9fr; gap: 64px; align-items: center; padding-top: 104px; }
.hero h1 { font-size: 68px; line-height: 1.04; font-weight: 700; letter-spacing: -.035em; color: var(--ink); margin: 0 0 24px; }
.hero .grad { background: linear-gradient(90deg, #0071e3, #7d3cf0 55%, #e0457b); -webkit-background-clip: text;
  background-clip: text; color: transparent; }
.portrait { width: 100%; aspect-ratio: 1; border-radius: 36px; object-fit: cover;
  box-shadow: 0 30px 60px -20px rgba(0,0,0,.25), 0 0 0 1px var(--line); }
.meta { margin-top: 26px; color: var(--ink2); font-size: 15px; }
.meta span + span::before { content: "·"; margin: 0 10px; color: var(--ink3); }
.btns { margin-top: 30px; display: flex; gap: 14px; flex-wrap: wrap; }
.btn { display: inline-block; padding: 12px 24px; border-radius: 980px; font-size: 17px; font-weight: 500; }
.btn.primary { background: var(--blue); color: #fff !important; }
.btn.primary:hover { background: var(--blue-h); text-decoration: none; }
.btn.ghost { color: var(--blue) !important; border: 1px solid var(--blue); }
.btn.ghost:hover { background: rgba(0,113,227,.06); text-decoration: none; }

/* stats */
.stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin-top: 96px; }
.stat { background: var(--panel); border-radius: 22px; padding: 28px 24px; box-shadow: 0 0 0 1px var(--line); }
.stat b { display: block; font-size: 44px; font-weight: 700; letter-spacing: -.03em; color: var(--ink); line-height: 1; }
.stat span { display: block; margin-top: 12px; color: var(--ink2); font-size: 14px; line-height: 1.4; }

/* experience */
.org { background: var(--panel); border-radius: 28px; padding: 40px; margin-bottom: 22px; box-shadow: 0 0 0 1px var(--line); }
.org-head { display: flex; justify-content: space-between; align-items: baseline; gap: 16px; flex-wrap: wrap; }
.org h3 { font-size: 28px; font-weight: 700; letter-spacing: -.02em; margin: 0; color: var(--ink); }
.org .place { color: var(--ink3); font-size: 15px; }
.roles { margin: 14px 0 26px; display: flex; gap: 10px; flex-wrap: wrap; }
.role { background: var(--soft); border-radius: 980px; padding: 7px 14px; font-size: 13.5px; color: var(--ink); }
.role i { font-style: normal; color: var(--ink2); margin-left: 6px; }
.projects { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.proj { background: var(--soft); border-radius: 18px; padding: 24px; }
.proj h4 { font-size: 17px; font-weight: 600; letter-spacing: -.01em; margin: 0 0 6px; color: var(--ink); line-height: 1.3; }
.proj .tag { font-size: 12.5px; color: var(--blue); font-weight: 500; margin-bottom: 12px; }
.proj ul { margin: 0; padding-left: 18px; }
.proj li { color: var(--ink2); font-size: 14.5px; line-height: 1.5; margin: 6px 0; }

/* skills */
.skills { display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; }
.skill { background: var(--panel); border-radius: 22px; padding: 28px; box-shadow: 0 0 0 1px var(--line); }
.skill h4 { margin: 0 0 16px; font-size: 19px; font-weight: 600; color: var(--ink); letter-spacing: -.01em; }
.chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chip { background: var(--soft); border-radius: 980px; padding: 7px 14px; font-size: 13.5px; color: var(--ink); }

/* featured + highlights */
.feat { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-bottom: 18px; }
.tile { border-radius: 28px; padding: 36px; min-height: 230px; display: flex; flex-direction: column; justify-content: space-between; }
.tile.dark { background: #1d1d1f; color: #f5f5f7; }
.tile.light { background: var(--panel); box-shadow: 0 0 0 1px var(--line); }
.tile .k { font-size: 13px; font-weight: 600; letter-spacing: .02em; text-transform: uppercase; opacity: .65; }
.tile h4 { font-size: 24px; line-height: 1.22; font-weight: 600; letter-spacing: -.02em; margin: 14px 0 18px; }
.tile.dark h4 { color: #f5f5f7; } .tile.light h4 { color: var(--ink); }
.tile .d { font-size: 14px; opacity: .75; }
.tile.dark a { color: #2997ff; }
.hl { display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; }
.hl-link { color: inherit !important; transition: transform .25s ease, box-shadow .25s ease; }
.hl-link:hover { text-decoration: none; transform: translateY(-3px); box-shadow: 0 18px 40px -18px rgba(0,0,0,.25), 0 0 0 1px var(--line); }
.hl-link .d { color: var(--blue); opacity: 1; }
.hl-in { display: flex; gap: 20px; align-items: stretch; height: 100%; }
.hl-text { display: flex; flex-direction: column; justify-content: space-between; flex: 1; min-width: 0; }
.hl-thumb { width: 150px; height: 112px; flex: none; object-fit: cover; border-radius: 14px; box-shadow: 0 0 0 1px var(--line); }
.hl-link:hover .hl-thumb { filter: brightness(1.04); }
@media (max-width: 820px) { .hl-thumb { width: 104px; height: 78px; border-radius: 10px; } }
.hl .tile { min-height: 190px; padding: 30px; }
.hl .tile h4 { font-size: 19px; }

/* publications */
.list { background: var(--panel); border-radius: 22px; box-shadow: 0 0 0 1px var(--line); overflow: hidden; }
.row { padding: 22px 28px; border-top: 1px solid var(--line); display: grid; grid-template-columns: 1fr auto; gap: 20px; align-items: baseline; }
.row:first-child { border-top: 0; }
.row .t { font-size: 16px; font-weight: 500; color: var(--ink); line-height: 1.4; letter-spacing: -.005em; }
.row .a { font-size: 13.5px; color: var(--ink2); margin-top: 6px; }
.row .v { font-size: 13.5px; color: var(--ink3); white-space: nowrap; }
.row .v em { color: var(--ink); font-style: italic; }
.sub-row { display: flex; justify-content: space-between; align-items: baseline; gap: 16px; flex-wrap: wrap; margin: 44px 0 16px; }
.sub-row .sub { margin: 0; }
.sub-links a { font-size: 15px; margin-left: 22px; }
.all { margin-top: 18px; }
.all summary { list-style: none; cursor: pointer; display: inline-block; color: var(--blue); font-size: 17px; font-weight: 500;
  padding: 11px 22px; border: 1px solid var(--blue); border-radius: 980px; }
.all summary::-webkit-details-marker { display: none; }
.all summary:hover { background: rgba(0,113,227,.06); }
.all summary .more::after { content: " ↓"; } .all summary .less::after { content: " ↑"; }
.all summary .less, .all[open] summary .more { display: none; } .all[open] summary .less { display: inline; }
.all-body { margin-top: 8px; }
.yr { font-size: 15px; font-weight: 600; color: var(--ink3); margin: 26px 0 10px 4px; }
.row .a b { color: var(--ink); font-weight: 600; }
.pl { margin-top: 8px; display: flex; gap: 8px; justify-content: flex-end; }
.pl a { font-size: 12.5px; font-weight: 500; padding: 4px 11px; border-radius: 980px; background: rgba(0,113,227,.08); }
.pl a:hover { background: rgba(0,113,227,.16); text-decoration: none; }
.row .v { text-align: right; }
@media (max-width: 820px) { .pl { justify-content: flex-start; } .row .v { text-align: left; } }
.note { color: var(--ink3); font-size: 13px; margin: 18px 4px 0; }
.sub { font-size: 24px; font-weight: 600; letter-spacing: -.015em; margin: 44px 0 16px; color: var(--ink); }

/* education + contact */
.edu { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
.contact { text-align: center; padding: 120px 0 40px; }
.contact h2 { font-size: 56px; font-weight: 700; letter-spacing: -.03em; margin: 0 0 16px; color: var(--ink); }
.contact .links { margin-top: 26px; font-size: 15px; }
.contact .links a { margin: 0 12px; }
.foot { border-top: 1px solid var(--line); margin-top: 70px; padding: 22px 0; color: var(--ink3); font-size: 12px; text-align: center; }

@media (max-width: 820px) {
  .hero, .projects, .skills, .feat, .hl, .edu { grid-template-columns: 1fr; }
  .stats { grid-template-columns: 1fr 1fr; }
  .hero { padding-top: 100px; gap: 36px; } .hero h1 { font-size: 46px; }
  h2.sec { font-size: 36px; } .contact h2 { font-size: 40px; }
  .org { padding: 26px; } .nav-links a:not(:last-child) { display: none; }
  .row { grid-template-columns: 1fr; }
}
</style>
"""


def nav() -> str:
    items = [("About", "#about"), ("Experience", "#experience"), ("Skills", "#skills"),
             ("Research", "#research"), ("Contact", "#contact")]
    links = "".join(f'<a href="{h}">{t}</a>' for t, h in items)
    return f'<div class="nav"><div class="nav-in"><div class="nav-name">Dan Thien Nguyen</div><div class="nav-links">{links}</div></div></div>'


def hero() -> str:
    photo = img_b64(HERE / "assets" / "portrait.jpg")
    return f"""
<section id="about" class="hero">
  <div>
    <p class="eyebrow">{escape(C.ROLE)}</p>
    <h1><span class="grad">{C.HEADLINE}</span></h1>
    <p class="lead">{escape(C.INTRO)}</p>
    <div class="meta"><span>{escape(C.LOCATION)}</span></div>
    <div class="btns">
      <a class="btn primary" href="mailto:{C.EMAIL}">Get in touch</a>
      <a class="btn ghost" href="#experience">See my work</a>
    </div>
  </div>
  <img class="portrait" src="data:image/jpeg;base64,{photo}" alt="Portrait of Dan Thien Nguyen"/>
</section>
<div class="stats">{''.join(f'<div class="stat"><b>{escape(n)}</b><span>{escape(t)}</span></div>' for n, t in C.STATS)}</div>
"""


def experience() -> str:
    orgs = []
    for o in C.EXPERIENCE:
        roles = "".join(f'<div class="role">{escape(r)}<i>{escape(d)}</i></div>' for r, d in o["roles"])
        projs = "".join(
            f'<div class="proj"><h4>{escape(p["title"])}</h4>'
            + (f'<div class="tag">{escape(p["tag"])}</div>' if p["tag"] else "")
            + "<ul>" + "".join(f"<li>{escape(x)}</li>" for x in p["points"]) + "</ul></div>"
            for p in o["projects"])
        orgs.append(f'<div class="org"><div class="org-head"><h3>{escape(o["org"])}</h3>'
                    f'<span class="place">{escape(o["place"])}</span></div>'
                    f'<div class="roles">{roles}</div><div class="projects">{projs}</div></div>')
    return ('<section id="experience"><p class="eyebrow">Experience</p>'
            '<h2 class="sec">Ten years in the lab.<br>Programs led end to end.</h2>' + "".join(orgs) + "</section>")


def skills() -> str:
    cards = "".join(
        f'<div class="skill"><h4>{escape(k)}</h4><div class="chips">'
        + "".join(f'<span class="chip">{escape(s)}</span>' for s in v) + "</div></div>"
        for k, v in C.SKILLS.items())
    return f'<section id="skills"><p class="eyebrow">Skills</p><h2 class="sec">From synthesis<br>to full-cell data.</h2><div class="skills">{cards}</div></section>'


def paper_links(p) -> str:
    """Journal page + PDF (the paper's own Drive file if set, else the shared folder)."""
    pdf = p.get("pdf") or C.PDF_FOLDER_URL
    j = f'<a href="{p["url"]}" target="_blank">Journal ↗</a>' if p.get("url") else ""
    return f'<div class="pl">{j}<a href="{pdf}" target="_blank">PDF ↗</a></div>'


def research() -> str:
    pub = next(p for p in C.PUBLICATIONS if p["featured"])
    pat = next(p for p in C.PATENTS if p["featured"])
    feat = f"""
<div class="feat">
  <div class="tile dark"><div><div class="k">Latest paper · {escape(pub["venue"])} {pub["year"]}</div>
    <h4>{escape(pub["title"])}</h4></div><div class="d">{escape(pub["authors"])} · <a href="{pub["url"]}" target="_blank">Journal →</a> · <a href="{pub.get("pdf") or C.PDF_FOLDER_URL}" target="_blank">PDF →</a></div></div>
  <div class="tile light"><div><div class="k">Patent · with Microsoft</div>
    <h4>{escape(pat["title"])}</h4></div><div class="d">{escape(pat["detail"])} · <a href="{pat["url"]}" target="_blank">View →</a></div></div>
</div>"""
    def hl_tile(src, title, date, url, img):
        meta = f'<div class="d">{escape(date)}{" · " if date and url else ""}{"Read →" if url else ""}</div>' if (date or url) else ""
        text = f'<div class="hl-text"><div><div class="k">{escape(src)}</div><h4>{escape(title)}</h4></div>{meta}</div>'
        thumb = (f'<img class="hl-thumb" src="data:image/jpeg;base64,{img_b64(HERE / "assets" / img)}" alt="{escape(src)} story image"/>'
                 if img else "")
        inner = f'<div class="hl-in">{thumb}{text}</div>'
        return (f'<a class="tile light hl-link" href="{url}" target="_blank">{inner}</a>' if url
                else f'<div class="tile light">{inner}</div>')

    hl = '<div class="hl">' + "".join(hl_tile(*h) for h in C.HIGHLIGHTS) + "</div>"

    def pub_row(p):
        title = f'<a href="{p["url"]}" target="_blank">{escape(p["title"])}</a>' if p["url"] else escape(p["title"])
        return (f'<div class="row"><div><div class="t">{title}</div><div class="a">{escape(p["authors"])}</div></div>'
                f'<div class="v"><em>{escape(p["venue"])}</em> · {p["year"]}{paper_links(p)}</div></div>')

    def pat_row(p):
        title = f'<a href="{p["url"]}" target="_blank">{escape(p["title"])}</a>' if p["url"] else escape(p["title"])
        return f'<div class="row"><div><div class="t">{title}</div><div class="a">{escape(p["detail"])}</div></div><div></div></div>'

    pubs = '<div class="list">' + "".join(pub_row(p) for p in C.PUBLICATIONS) + "</div>"

    def full_row(p):
        au = p["authors"] if len(p["authors"]) <= 8 else p["authors"][:7] + ["et al."]
        au = ", ".join(f"<b>{escape(a)}</b>" if a == "D.T. Nguyen" else escape(a) for a in au)
        ref = ", ".join(x for x in (p["volume"], f'({p["issue"]})' if p["issue"] else "", p["pages"]) if x).replace(", (", " (")
        return (f'<div class="row"><div><div class="t"><a href="{p["url"]}" target="_blank">{escape(p["title"])}</a></div>'
                f'<div class="a">{au}</div></div><div class="v"><em>{escape(p["venue"])}</em>{" " + escape(ref) if ref else ""}{paper_links(p)}</div></div>')

    years = sorted({p["year"] for p in ALL_PUBS}, reverse=True)
    groups = "".join(f'<div class="yr">{y}</div><div class="list">' + "".join(full_row(p) for p in ALL_PUBS if p["year"] == y) + "</div>"
                     for y in years)
    full = (f'<details class="all"><summary><span class="more">Show all {len(ALL_PUBS)} publications</span>'
            f'<span class="less">Hide full list</span></summary><div class="all-body">{groups}'
            f'<p class="note">Journal articles, newest first. Titles link to the publisher. '
            f'<a href="{C.SCHOLAR_URL}" target="_blank">Google Scholar</a> also lists conference abstracts and preprints.</p></div></details>')
    pats = '<div class="list">' + "".join(pat_row(p) for p in C.PATENTS) + "</div>"
    return (f'<section id="research"><p class="eyebrow">Research</p><h2 class="sec">Published, patented,<br>and in the news.</h2>'
            f'{feat}{hl}<div class="sub-row"><div class="sub">Selected publications</div><div class="sub-links"><a href="{C.SCHOLAR_URL}" target="_blank">All papers on Google Scholar →</a><a href="{C.PDF_FOLDER_URL}" target="_blank">Paper PDFs →</a></div></div>{pubs}{full}<div class="sub">Patents</div>{pats}</section>')


def education() -> str:
    cards = "".join(
        f'<div class="tile light" style="min-height:0"><div class="k">{y}</div><h4 style="margin:10px 0 6px">{escape(d)}</h4>'
        f'<div class="d">{escape(f + " · " if f else "")}{escape(s)}</div></div>'
        for d, f, s, y in C.EDUCATION)
    return f'<section id="education"><p class="eyebrow">Education</p><div class="edu">{cards}</div></section>'


def contact() -> str:
    links = "".join(f'<a href="{u}" target="_blank">{escape(n)}</a>' for n, u in C.LINKS.items() if u)
    return f"""
<section id="contact" class="contact">
  <h2>Let's build better batteries.</h2>
  <p class="lead">Open to materials, cell, and research leadership roles.</p>
  <div class="btns" style="justify-content:center"><a class="btn primary" href="mailto:{C.EMAIL}">{C.EMAIL}</a></div>
  <div class="links">{links}</div>
</section>
<div class="foot">© {escape(C.NAME)} · {escape(C.LOCATION)}</div>
"""


st.html(CSS)
st.html(nav() + hero() + experience() + skills() + research() + education() + contact())
