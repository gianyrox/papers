import os
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_DIR = os.path.join(ROOT_DIR, "book")

CHAPTERS = [
    ("prologue", "Prologue", "prologue.md"),
    ("ch1", "Chapter 1", "ch1.md"),
    ("ch2", "Chapter 2", "ch2.md"),
    ("ch3a", "Chapter 3 · Part A", "ch3a.md"),
    ("ch3b", "Chapter 3 · Part B", "ch3b.md"),
    ("ch3c", "Chapter 3 · Part C", "ch3c.md"),
    ("ch4a", "Chapter 4 · Part A", "ch4a.md"),
    ("ch4b", "Chapter 4 · Part B", "ch4b.md"),
    ("ch4c", "Chapter 4 · Part C", "ch4c.md"),
    ("ch4d", "Chapter 4 · Part D", "ch4d.md"),
    ("ch5a", "Chapter 5 · Part A", "ch5a.md"),
    ("ch5b", "Chapter 5 · Part B", "ch5b.md"),
    ("ch5c", "Chapter 5 · Part C", "ch5c.md"),
    ("ch5d", "Chapter 5 · Part D", "ch5d.md"),
    ("ch5e", "Chapter 5 · Part E", "ch5e.md"),
    ("ch6", "Chapter 6", "ch6.md"),
    ("appendices", "Appendices", "appendices.md"),
]

TOC_SECTIONS = [
    ("Front Matter", ["prologue"]),
    ("The Dream & The Problem", ["ch1", "ch2"]),
    ("The Bridge", ["ch3a", "ch3b", "ch3c"]),
    ("Fast Money", ["ch4a", "ch4b", "ch4c", "ch4d"]),
    ("The Reckoning", ["ch5a", "ch5b", "ch5c", "ch5d", "ch5e"]),
    ("The Return", ["ch6"]),
    ("Back Matter", ["appendices"]),
]

TOC_LABELS = {
    "prologue": "I Wrote This for My Dad",
    "ch1": "Ch 1 · A Stablecoin Utopia",
    "ch2": "Ch 2 · Slow Money",
    "ch3a": "Ch 3A · The Core Innovation",
    "ch3b": "Ch 3B · The Applications",
    "ch3c": "Ch 3C · What Changes for You",
    "ch4a": "Ch 4A · Architecture & Frontier",
    "ch4b": "Ch 4B · The Convergence",
    "ch4c": "Ch 4C · The Dollar Question",
    "ch4d": "Ch 4D · The Messy Middle",
    "ch5a": "Ch 5A · What\u2019s Already Broken",
    "ch5b": "Ch 5B · The Case Against",
    "ch5c": "Ch 5C · What If Tether Fails?",
    "ch5d": "Ch 5D · Who Loses",
    "ch5e": "Ch 5E · What Gets Better",
    "ch6": "Ch 6 · The Return",
    "appendices": "Appendices",
}

def read_md(filename):
    path = os.path.join(BOOK_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def build_toc_html():
    lines = []
    for section_name, ids in TOC_SECTIONS:
        lines.append(f'    <li class="sec"><span>{section_name}</span></li>')
        for cid in ids:
            lines.append(f'    <li><a href="#{cid}">{TOC_LABELS[cid]}</a></li>')
    return "\n".join(lines)

def build_chapter_data():
    data = []
    for cid, label, filename in CHAPTERS:
        md = read_md(filename)
        data.append({"id": cid, "label": label, "md": md})
    return data

def main():
    toc_html = build_toc_html()
    chapter_data = build_chapter_data()
    chapter_json = json.dumps(chapter_data, ensure_ascii=False)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Your Money Is Broken — Stablecoin Book</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700&family=Source+Sans+3:ital,wght@0,300;0,400;0,600;0,700;1,400;1,600&display=swap');
:root {{
  --bg:#faf8f5;--sidebar:#f0ede8;--text:#2c2c2c;--muted:#6b6b6b;
  --accent:#b8860b;--border:#e0dcd4;--heading:#1a1a1a;--link:#8b6914;
  --sw:280px;--cw:680px;--nw:320px;
  --note-bg:#f7f5f0;--note-border:#e8e4db;--note-accent:#6b8e4e;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{font-size:18px;scroll-behavior:smooth;-webkit-font-smoothing:antialiased}}
body{{font-family:'Merriweather',Georgia,serif;background:var(--bg);color:var(--text);line-height:1.8;display:flex;min-height:100vh}}

.sb{{position:fixed;top:0;left:0;width:var(--sw);height:100vh;background:var(--sidebar);border-right:1px solid var(--border);overflow-y:auto;z-index:100;transition:transform .3s;display:flex;flex-direction:column}}
.sb-h{{padding:1.5rem 1.2rem .8rem;border-bottom:1px solid var(--border);flex-shrink:0}}
.sb-h h1{{font-family:'Source Sans 3',sans-serif;font-size:.8rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin-bottom:.2rem}}
.sb-h p{{font-size:.65rem;color:var(--muted);line-height:1.4}}
.toc{{list-style:none;padding:.8rem 0;flex:1;overflow-y:auto}}
.toc li{{border-left:3px solid transparent;transition:all .2s}}
.toc li.active{{border-left-color:var(--accent);background:rgba(184,134,11,.06)}}
.toc li a{{display:block;padding:.4rem 1.2rem;font-family:'Source Sans 3',sans-serif;font-size:.75rem;color:var(--muted);text-decoration:none;line-height:1.4;transition:color .15s}}
.toc li a:hover,.toc li.active a{{color:var(--heading)}}
.toc li.active a{{font-weight:600}}
.toc li.sec{{border-left-color:transparent!important;background:none!important}}
.toc li.sec span{{display:block;padding:.8rem 1.2rem .2rem;font-family:'Source Sans 3',sans-serif;font-size:.58rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}}
.sb-f{{padding:1rem 1.5rem;border-top:1px solid var(--border);flex-shrink:0}}
.bp{{display:flex;align-items:center;justify-content:center;gap:.5rem;width:100%;padding:.65rem 1rem;font-family:'Source Sans 3',sans-serif;font-size:.8rem;font-weight:600;color:#fff;background:var(--accent);border:none;border-radius:6px;cursor:pointer;transition:background .2s}}
.bp:hover{{background:#9a7209}}.bp:disabled{{background:#ccc;cursor:wait}}
.bp svg{{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}}

.mn{{margin-left:var(--sw);margin-right:var(--nw);flex:1;min-height:100vh;transition:margin-right .3s}}
.mn.np-closed{{margin-right:0}}
.ct{{max-width:var(--cw);margin:0 auto;padding:3rem 2rem 6rem}}
.ch{{margin-bottom:4rem;padding-bottom:4rem;border-bottom:1px solid var(--border)}}
.ch:last-child{{border-bottom:none}}
.cl{{font-family:'Source Sans 3',sans-serif;font-size:.65rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin-bottom:.5rem}}
.ch h1{{font-family:'Source Sans 3',sans-serif;font-size:2rem;font-weight:900;line-height:1.2;color:var(--heading);margin-bottom:1.8rem;letter-spacing:-.02em}}
.ch h2{{font-family:'Source Sans 3',sans-serif;font-size:1.3rem;font-weight:700;line-height:1.3;color:var(--heading);margin-top:2.5rem;margin-bottom:1rem}}
.ch h3{{font-family:'Source Sans 3',sans-serif;font-size:1rem;font-weight:700;color:var(--heading);margin-top:2rem;margin-bottom:.8rem}}
.ch p{{margin-bottom:1.2rem}}.ch strong{{font-weight:700;color:var(--heading)}}
.ch hr{{border:none;border-top:1px solid var(--border);margin:2.5rem auto;width:40%}}
.ch blockquote{{border-left:3px solid var(--accent);padding:.8rem 1.2rem;margin:1.5rem 0;background:rgba(184,134,11,.04);font-style:italic;color:var(--muted)}}
.ch blockquote p:last-child{{margin-bottom:0}}
.ch ul,.ch ol{{margin:1rem 0 1.5rem 1.5rem}}.ch li{{margin-bottom:.5rem}}
.ch a{{color:var(--link);text-decoration:underline;text-decoration-color:rgba(139,105,20,.3);text-underline-offset:2px}}
.ch a:hover{{text-decoration-color:var(--link)}}
mark.hl{{background:rgba(184,134,11,.18);border-bottom:2px solid rgba(184,134,11,.4);padding:0 1px;border-radius:2px;cursor:pointer;transition:background .15s}}
mark.hl:hover{{background:rgba(184,134,11,.3)}}

.np{{position:fixed;top:0;right:0;width:var(--nw);height:100vh;background:var(--note-bg);border-left:1px solid var(--note-border);display:flex;flex-direction:column;z-index:100;transition:transform .3s}}
.np.closed{{transform:translateX(100%)}}
.np-head{{padding:1rem 1.2rem .8rem;border-bottom:1px solid var(--note-border);display:flex;align-items:center;justify-content:space-between;flex-shrink:0}}
.np-head h2{{font-family:'Source Sans 3',sans-serif;font-size:.8rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--note-accent)}}
.np-actions{{display:flex;gap:.4rem}}
.np-btn{{width:30px;height:30px;border-radius:6px;border:1px solid var(--note-border);background:transparent;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .15s}}
.np-btn:hover{{background:var(--border)}}
.np-btn svg{{width:15px;height:15px;stroke:var(--muted);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}}
.np-count{{font-family:'Source Sans 3',sans-serif;font-size:.65rem;color:var(--muted);padding:0 1.2rem .4rem;flex-shrink:0}}
.np-list{{flex:1;overflow-y:auto;padding:.5rem}}
.np-empty{{text-align:center;padding:3rem 1.5rem;color:var(--muted);font-family:'Source Sans 3',sans-serif;font-size:.8rem;line-height:1.6}}
.np-empty b{{display:block;margin-bottom:.5rem;font-size:.85rem;color:var(--text)}}

.note-card{{background:#fff;border:1px solid var(--note-border);border-radius:8px;padding:.8rem 1rem;margin-bottom:.6rem;position:relative;transition:box-shadow .15s}}
.note-card:hover{{box-shadow:0 2px 8px rgba(0,0,0,.06)}}
.note-ref{{font-family:'Source Sans 3',sans-serif;font-size:.6rem;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--accent);margin-bottom:.3rem;cursor:pointer}}
.note-ref:hover{{text-decoration:underline}}
.note-quote{{font-size:.75rem;font-style:italic;color:var(--muted);line-height:1.5;padding:.5rem .7rem;background:rgba(184,134,11,.04);border-left:2px solid var(--accent);border-radius:0 4px 4px 0;margin-bottom:.5rem;max-height:4rem;overflow:hidden;cursor:pointer;transition:max-height .3s}}
.note-quote.expanded{{max-height:none}}
.note-text{{width:100%;min-height:50px;border:1px solid var(--note-border);border-radius:4px;padding:.5rem .6rem;font-family:'Source Sans 3',sans-serif;font-size:.78rem;color:var(--text);background:var(--note-bg);resize:vertical;line-height:1.5;outline:none;transition:border-color .15s}}
.note-text:focus{{border-color:var(--note-accent)}}
.note-del{{position:absolute;top:.6rem;right:.6rem;width:22px;height:22px;border-radius:4px;border:none;background:transparent;cursor:pointer;display:flex;align-items:center;justify-content:center;opacity:0;transition:opacity .15s}}
.note-card:hover .note-del{{opacity:1}}
.note-del:hover{{background:#f5e6e6}}
.note-del svg{{width:13px;height:13px;stroke:#c44;fill:none;stroke-width:2;stroke-linecap:round}}
.note-time{{font-family:'Source Sans 3',sans-serif;font-size:.55rem;color:#aaa;margin-top:.3rem}}

.np-toggle{{position:fixed;top:50%;right:0;transform:translateY(-50%);z-index:101;width:24px;height:60px;background:var(--note-bg);border:1px solid var(--note-border);border-right:none;border-radius:6px 0 0 6px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:right .3s}}
.np-toggle.shifted{{right:var(--nw)}}
.np-toggle svg{{width:14px;height:14px;stroke:var(--muted);fill:none;stroke-width:2;stroke-linecap:round;transition:transform .3s}}
.np-toggle.shifted svg{{transform:rotate(180deg)}}

.sel-popup{{position:absolute;z-index:200;background:#333;color:#fff;font-family:'Source Sans 3',sans-serif;font-size:.72rem;font-weight:600;padding:.4rem .8rem;border-radius:6px;cursor:pointer;box-shadow:0 4px 12px rgba(0,0,0,.2);white-space:nowrap;display:none;transform:translateX(-50%)}}
.sel-popup:hover{{background:#555}}
.sel-popup::after{{content:'';position:absolute;top:100%;left:50%;transform:translateX(-50%);border:5px solid transparent;border-top-color:#333}}

.toast{{position:fixed;bottom:2rem;left:50%;transform:translateX(-50%) translateY(20px);background:#333;color:#fff;font-family:'Source Sans 3',sans-serif;font-size:.8rem;padding:.7rem 1.4rem;border-radius:8px;opacity:0;transition:opacity .3s,transform .3s;z-index:300;pointer-events:none}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}

.hb{{display:none;position:fixed;top:1rem;left:1rem;z-index:200;width:44px;height:44px;border-radius:8px;background:var(--sidebar);border:1px solid var(--border);cursor:pointer;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,.06)}}
.hb svg{{width:20px;height:20px;stroke:var(--text);fill:none;stroke-width:2;stroke-linecap:round}}
.ov{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.3);z-index:90}}
.pb{{position:fixed;top:0;left:var(--sw);right:var(--nw);height:3px;z-index:50;transition:right .3s}}
.pb.np-closed{{right:0}}
.st{{position:fixed;bottom:2rem;right:calc(var(--nw) + 1.5rem);width:44px;height:44px;border-radius:50%;background:var(--accent);color:#fff;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 12px rgba(0,0,0,.15);opacity:0;transform:translateY(10px);transition:opacity .3s,transform .3s,right .3s;z-index:50}}
.st.np-closed{{right:2rem}}
.st.v{{opacity:1;transform:translateY(0)}}
.st svg{{width:20px;height:20px;fill:none;stroke:#fff;stroke-width:2.5;stroke-linecap:round}}

@media(max-width:1200px){{
  :root{{--nw:280px}}
}}
@media(max-width:900px){{
  .sb{{transform:translateX(-100%)}}.sb.open{{transform:translateX(0)}}
  .ov.open{{display:block}}.hb{{display:flex}}.mn{{margin-left:0}}
  .pb{{left:0}}.ct{{padding:4rem 1.5rem 6rem}}.ch h1{{font-size:1.8rem}}
  .np{{width:100%;max-width:360px}}.np-toggle{{display:none}}
  .mn{{margin-right:0!important}}.pb{{right:0!important}}.st{{right:2rem!important}}
}}
@media print{{
  .sb,.hb,.ov,.pb,.st,.np,.np-toggle,.sel-popup,.toast{{display:none!important}}
  .mn{{margin-left:0!important;margin-right:0!important}}
  .ct{{max-width:100%;padding:1cm}}
  .ch{{border-bottom:none;margin-bottom:1rem;padding-bottom:0}}
  .cl{{color:#b8860b}}
  body{{font-size:11pt;line-height:1.6;display:block}}
  h1{{page-break-before:always;page-break-after:avoid}}
  .ch:first-child h1{{page-break-before:avoid}}
  h2,h3{{page-break-after:avoid}}
  p,blockquote,ul,ol{{orphans:3;widows:3}}
  img{{max-width:100%}}
}}
</style>
</head>
<body>

<button class="hb" onclick="T()" aria-label="Menu">
<svg viewBox="0 0 24 24"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
</button>
<div class="ov" onclick="T()"></div>

<nav class="sb" id="sb">
  <div class="sb-h">
    <h1>Your Money Is Broken</h1>
    <p>How Stablecoins Bridge Slow Money to Fast Money</p>
  </div>
  <ul class="toc" id="toc">
{toc_html}
  </ul>
  <div class="sb-f">
    <button class="bp" onclick="P()">
      <svg viewBox="0 0 24 24"><path d="M12 3v12m0 0l-4-4m4 4l4-4M4 17v2a2 2 0 002 2h12a2 2 0 002-2v-2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      Save as PDF
    </button>
  </div>
</nav>

<div class="pb" id="pbar"><div class="fl" id="fl"></div></div>
<button class="st" id="st" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">
<svg viewBox="0 0 24 24"><polyline points="18 15 12 9 6 15"/></svg>
</button>

<main class="mn" id="mn"><div class="ct" id="bc"></div></main>

<div class="np" id="np">
  <div class="np-head">
    <h2>Notes</h2>
    <div class="np-actions">
      <button class="np-btn" title="New note" onclick="addBlankNote()"><svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
      <button class="np-btn" title="Copy all notes" onclick="exportNotes()"><svg viewBox="0 0 24 24"><path d="M16 4h2a2 2 0 012 2v14a2 2 0 01-2 2H6a2 2 0 01-2-2V6a2 2 0 012-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg></button>
      <button class="np-btn" title="Clear all notes" onclick="clearNotes()"><svg viewBox="0 0 24 24"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14a2 2 0 01-2 2H8a2 2 0 01-2-2L5 6"/><path d="M10 11v6"/><path d="M14 11v6"/></svg></button>
    </div>
  </div>
  <div class="np-count" id="np-count">0 notes</div>
  <div class="np-list" id="np-list"></div>
</div>

<button class="np-toggle shifted" id="np-toggle" onclick="toggleNotes()" title="Toggle notes panel">
<svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>
</button>

<div class="sel-popup" id="sel-popup" onmousedown="addNoteFromSelection(event)">+ Add Note</div>
<div class="toast" id="toast"></div>

<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
var D={chapter_json};
var notes=JSON.parse(localStorage.getItem("book_notes")||"[]");
var notesOpen=localStorage.getItem("notes_open")!=="false";

function T(){{document.getElementById("sb").classList.toggle("open");document.querySelector(".ov").classList.toggle("open")}}
document.querySelectorAll(".toc a").forEach(function(a){{a.addEventListener("click",function(){{if(window.innerWidth<=900)T()}});}});

function R(){{
  var c=document.getElementById("bc"),h="";
  D.forEach(function(d){{
    var r=marked.parse(d.md,{{breaks:false,gfm:true}});
    h+='<section class="ch" id="'+d.id+'"><div class="cl">'+d.label+'</div>'+r+'</section>';
  }});
  c.innerHTML=h;
  S();
  renderNotes();
  applyHighlights();
  applyNotesState();
}}

function S(){{
  var ss=document.querySelectorAll(".ch"),ti=document.querySelectorAll(".toc li:not(.sec)"),fl=document.getElementById("fl"),st=document.getElementById("st");
  function O(){{
    var s=window.scrollY,dh=document.documentElement.scrollHeight-window.innerHeight;
    fl.style.width=(dh>0?(s/dh)*100:0)+"%";
    st.classList.toggle("v",s>400);
    var cur="";ss.forEach(function(e){{if(e.getBoundingClientRect().top<=120)cur=e.id}});
    ti.forEach(function(li){{var a=li.querySelector("a");if(!a)return;li.classList.toggle("active",a.getAttribute("href").slice(1)===cur)}});
  }}
  window.addEventListener("scroll",O,{{passive:true}});O();
}}

function getChapterForNode(node){{
  var el=node.nodeType===3?node.parentElement:node;
  while(el&&!el.classList.contains("ch"))el=el.parentElement;
  return el;
}}

function getChapterLabel(chEl){{
  if(!chEl)return"Unknown";
  var cl=chEl.querySelector(".cl");
  return cl?cl.textContent:chEl.id;
}}

var selText="",selChapter="",selChapterId="";
document.addEventListener("mouseup",function(e){{
  var popup=document.getElementById("sel-popup");
  var sel=window.getSelection();
  if(!sel||sel.isCollapsed||sel.toString().trim().length===0){{popup.style.display="none";return;}}
  var range=sel.getRangeAt(0);
  var ch=getChapterForNode(range.startContainer);
  if(!ch){{popup.style.display="none";return;}}
  selText=sel.toString().trim();
  selChapter=getChapterLabel(ch);
  selChapterId=ch.id;
  var rect=range.getBoundingClientRect();
  popup.style.display="block";
  popup.style.left=(rect.left+rect.width/2+window.scrollX)+"px";
  popup.style.top=(rect.top+window.scrollY-40)+"px";
}});

document.addEventListener("mousedown",function(e){{
  if(!e.target.closest(".sel-popup")){{
    document.getElementById("sel-popup").style.display="none";
  }}
}});

function addNoteFromSelection(e){{
  e.preventDefault();
  e.stopPropagation();
  if(!selText)return;
  var note={{
    id:Date.now()+"_"+Math.random().toString(36).substr(2,5),
    chapter:selChapter,
    chapterId:selChapterId,
    quote:selText.substring(0,500),
    text:"",
    ts:Date.now()
  }};
  notes.push(note);
  saveNotes();
  renderNotes();
  applyHighlights();
  document.getElementById("sel-popup").style.display="none";
  window.getSelection().removeAllRanges();
  if(!notesOpen)toggleNotes();
  setTimeout(function(){{
    var ta=document.querySelector('.note-card[data-id="'+note.id+'"] .note-text');
    if(ta)ta.focus();
  }},100);
  toast("Note added");
}}

function addBlankNote(){{
  var note={{
    id:Date.now()+"_"+Math.random().toString(36).substr(2,5),
    chapter:"General",
    chapterId:"",
    quote:"",
    text:"",
    ts:Date.now()
  }};
  notes.push(note);
  saveNotes();
  renderNotes();
  if(!notesOpen)toggleNotes();
  var list=document.getElementById("np-list");
  list.scrollTop=list.scrollHeight;
  setTimeout(function(){{
    var ta=document.querySelector('.note-card[data-id="'+note.id+'"] .note-text');
    if(ta)ta.focus();
  }},100);
  toast("Note added");
}}

function saveNotes(){{
  localStorage.setItem("book_notes",JSON.stringify(notes));
}}

function renderNotes(){{
  var list=document.getElementById("np-list");
  var count=document.getElementById("np-count");
  count.textContent=notes.length+" note"+(notes.length!==1?"s":"");
  if(notes.length===0){{
    list.innerHTML='<div class="np-empty"><b>No notes yet</b>Select any text in the book and click "Add Note" to annotate it.</div>';
    return;
  }}
  var h="";
  notes.forEach(function(n){{
    var d=new Date(n.ts);
    var ts=d.toLocaleDateString()+" "+d.toLocaleTimeString([],{{hour:"2-digit",minute:"2-digit"}});
    h+='<div class="note-card" data-id="'+n.id+'">';
    h+='<div class="note-ref" onclick="scrollToQuote(\\''+n.id+'\\')">'+escHtml(n.chapter)+'</div>';
    if(n.quote)h+='<div class="note-quote" onclick="scrollToQuote(\\''+n.id+'\\')">'+escHtml(n.quote)+'</div>';
    h+='<textarea class="note-text" placeholder="Write your note..." oninput="updateNote(\\''+n.id+'\\',this.value)">'+escHtml(n.text)+'</textarea>';
    h+='<div class="note-time">'+ts+'</div>';
    h+='<button class="note-del" onclick="deleteNote(\\''+n.id+'\\')" title="Delete note"><svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>';
    h+='</div>';
  }});
  list.innerHTML=h;
}}

function escHtml(s){{
  var d=document.createElement("div");
  d.textContent=s;
  return d.innerHTML;
}}

function updateNote(id,val){{
  for(var i=0;i<notes.length;i++){{
    if(notes[i].id===id){{notes[i].text=val;break;}}
  }}
  saveNotes();
}}

function deleteNote(id){{
  notes=notes.filter(function(n){{return n.id!==id}});
  saveNotes();
  renderNotes();
  applyHighlights();
  toast("Note deleted");
}}

function clearNotes(){{
  if(!confirm("Delete all notes? This cannot be undone."))return;
  notes=[];
  saveNotes();
  renderNotes();
  applyHighlights();
  toast("All notes cleared");
}}

function applyHighlights(){{
  document.querySelectorAll("mark.hl").forEach(function(m){{
    var p=m.parentNode;
    while(m.firstChild)p.insertBefore(m.firstChild,m);
    p.removeChild(m);
    p.normalize();
  }});
  notes.forEach(function(n){{
    if(!n.quote||!n.chapterId)return;
    var ch=document.getElementById(n.chapterId);
    if(!ch)return;
    var snippet=n.quote.substring(0,120);
    var walker=document.createTreeWalker(ch,NodeFilter.SHOW_TEXT,null,false);
    while(walker.nextNode()){{
      var tnode=walker.currentNode;
      var idx=tnode.textContent.indexOf(snippet);
      if(idx===-1)continue;
      var range=document.createRange();
      range.setStart(tnode,idx);
      range.setEnd(tnode,Math.min(idx+n.quote.length,tnode.textContent.length));
      var mark=document.createElement("mark");
      mark.className="hl";
      mark.dataset.noteId=n.id;
      mark.title="Click to view note";
      mark.onclick=function(){{
        var card=document.querySelector('.note-card[data-id="'+n.id+'"]');
        if(card){{card.scrollIntoView({{behavior:"smooth",block:"center"}});card.style.transition="box-shadow .3s";card.style.boxShadow="0 0 0 3px rgba(184,134,11,.4)";setTimeout(function(){{card.style.boxShadow=""}},2000);}}
      }};
      range.surroundContents(mark);
      break;
    }}
  }});
}}

function scrollToQuote(noteId){{
  var note=null;
  for(var i=0;i<notes.length;i++){{if(notes[i].id===noteId){{note=notes[i];break;}}}}
  if(!note)return;
  var ch=document.getElementById(note.chapterId);
  if(!ch)return;
  if(note.quote){{
    var snippet=note.quote.substring(0,80);
    var walker=document.createTreeWalker(ch,NodeFilter.SHOW_TEXT,null,false);
    var found=null;
    while(walker.nextNode()){{
      if(walker.currentNode.textContent.indexOf(snippet)!==-1){{
        found=walker.currentNode.parentElement;
        break;
      }}
    }}
    if(!found){{
      var words=snippet.split(/\\s+/).slice(0,6).join(" ");
      walker=document.createTreeWalker(ch,NodeFilter.SHOW_TEXT,null,false);
      while(walker.nextNode()){{
        if(walker.currentNode.textContent.indexOf(words)!==-1){{
          found=walker.currentNode.parentElement;
          break;
        }}
      }}
    }}
    if(found){{
      found.scrollIntoView({{behavior:"smooth",block:"center"}});
      found.style.transition="background .3s";
      found.style.background="rgba(184,134,11,.15)";
      setTimeout(function(){{found.style.background=""}},2000);
      return;
    }}
  }}
  ch.scrollIntoView({{behavior:"smooth",block:"start"}});
}}

function toggleNotes(){{
  notesOpen=!notesOpen;
  localStorage.setItem("notes_open",notesOpen);
  applyNotesState();
}}

function applyNotesState(){{
  var np=document.getElementById("np");
  var mn=document.getElementById("mn");
  var pb=document.getElementById("pbar");
  var st=document.getElementById("st");
  var tog=document.getElementById("np-toggle");
  if(notesOpen){{
    np.classList.remove("closed");
    mn.classList.remove("np-closed");
    pb.classList.remove("np-closed");
    st.classList.remove("np-closed");
    tog.classList.add("shifted");
  }}else{{
    np.classList.add("closed");
    mn.classList.add("np-closed");
    pb.classList.add("np-closed");
    st.classList.add("np-closed");
    tog.classList.remove("shifted");
  }}
}}

function exportNotes(){{
  if(notes.length===0){{toast("No notes to copy");return;}}
  var nl="\\n";
  var out="# Book Review Notes"+nl+"# Your Money Is Broken"+nl+"# Exported: "+new Date().toLocaleString()+nl+nl;
  out+="---"+nl+nl;
  var byChapter={{}};
  notes.forEach(function(n){{
    var key=n.chapter||"General";
    if(!byChapter[key])byChapter[key]=[];
    byChapter[key].push(n);
  }});
  Object.keys(byChapter).forEach(function(ch){{
    out+="## "+ch+nl+nl;
    byChapter[ch].forEach(function(n){{
      if(n.quote)out+="> "+n.quote.replace(/\\n/g,nl+"> ")+nl+nl;
      if(n.text)out+=n.text+nl+nl;
      else out+="_(no annotation)_"+nl+nl;
      out+="---"+nl+nl;
    }});
  }});
  navigator.clipboard.writeText(out).then(function(){{
    toast("All notes copied to clipboard");
  }}).catch(function(){{
    var ta=document.createElement("textarea");
    ta.value=out;ta.style.position="fixed";ta.style.left="-9999px";
    document.body.appendChild(ta);ta.select();document.execCommand("copy");
    document.body.removeChild(ta);
    toast("All notes copied to clipboard");
  }});
}}

function toast(msg){{
  var t=document.getElementById("toast");
  t.textContent=msg;t.classList.add("show");
  setTimeout(function(){{t.classList.remove("show")}},2000);
}}

function P(){{
  toast("In the print dialog, set Destination to 'Save as PDF'");
  setTimeout(function(){{window.print()}},400);
}}

R();
</script>
</body>
</html>'''

    out_path = os.path.join(ROOT_DIR, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built {out_path} ({os.path.getsize(out_path):,} bytes)")

if __name__ == "__main__":
    main()
