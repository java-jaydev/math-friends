"""10 만들기 대작전 학습지 생성기.

사용: python3 build.py [seed]
seed 가 다르면 술술 도전 문제 순서가 바뀐다. 결과: out/10making_<seed>.html, .pdf
"""
import os
import random
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "out"
CHARS = "../../assets/chars"
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

COLORS = {0: "#c9ccd3", 1: "#f04a4a", 2: "#f5832a", 3: "#f6c823", 4: "#4cc13b", 5: "#59dcb0",
          6: "#2fa6ec", 7: "#3f74e6", 8: "#a54fd8", 9: "#f56b9c", 10: "#f3a91b"}

ADD_FACTS = [(a, b) for a in range(2, 10) for b in range(2, 10) if a + b >= 11]
SUB_FACTS = [(c, d) for c in range(11, 19) for d in range(2, 10) if d > c - 10 and c - d <= 9]


def box(cls=""):
    return f'<span class="box {cls}"></span>'


def tf(*groups):
    """10칸 상자. groups = [(개수, 색) 또는 (개수, 색, "x")] 앞에서부터 채운다. "x" 는 빼서 지운 점."""
    cells = []
    for n, color, *mark in groups:
        cls = "d x" if mark else "d"
        cells += [f'<i style="--c:{color}" class="{cls}"></i>'] * n
    cells += ["<i></i>"] * (10 - len(cells))
    return f'<span class="tf">{"".join(cells)}</span>'


def char(n, h=17):
    return f'<img class="ch" style="height:{h}mm" src="{CHARS}/n{n:02d}.png">'


def header(no, title, sub, captain=10):
    return f'''
  <div class="head">
    {char(captain, 21)}
    <h1><small>점박이 숫자 친구들과 함께 · {sub}</small>{no} {title}</h1>
    <div class="who">이름 <span></span><br>날짜 <span></span></div>
  </div>'''


def sec(no, title, tip, extra=""):
    return f'<div class="sec-title"><span class="no">{no}</span>{title} <span class="tip">{tip}</span>{extra}</div>'




def split(a, op, b):
    """가르기 가지: 뒤의 수 아래에 두 칸."""
    return f'''<div class="split"><table><tr><td>{a}</td><td>{op}</td><td class="b">{b}</td><td>=</td><td>{box()}</td></tr>
      <tr><td></td><td></td><td class="br"><svg viewBox="0 0 20 8"><path d="M10 0 L3 8 M10 0 L17 8"/></svg>
      <div class="parts">{box("sm")}{box("sm")}</div></td><td></td><td></td></tr></table></div>'''


def bridge(a, op, b):
    """가르기 칸 없이 중간 단계만: 8 + 7 = 10 + □ = □ / 13 - 5 = 10 - □ = □"""
    return f'<div class="bridge">{a} {op} {b} = 10 {op} {box("sm")} = {box()}</div>'


def drill(items, cols):
    cells = "".join(f'<div><b>{a} {op} {b}</b> = {box()}</div>' for a, op, b in items)
    return f'<div class="drill" style="grid-template-columns:repeat({cols},1fr)">{cells}</div>'


def footer(stamp=True):
    friends = "".join(f'<img src="{CHARS}/n{i:02d}.png">' for i in range(10))
    st = '<div class="stamp">다 했으면<br>여기에<br>도장 쾅!</div>' if stamp else ""
    return f'<div class="foot"><div class="friends">{friends}</div>{st}</div>'


def page_add_concept():
    chips = "".join(f'<div class="chip">{a} + {box()} = 10</div>' for a in [9, 7, 8, 6, 3, 5, 2, 4])
    splits = "".join(bridge(a, "+", b) for a, b in [(8, 6), (9, 4), (6, 7), (7, 5), (8, 7), (9, 8), (5, 6), (7, 6), (9, 5), (6, 9), (8, 5), (7, 9)])
    c7, c8, c10 = COLORS[7], COLORS[8], COLORS[10]
    return f'''<div class="page">{header("①", "10 만들기 대작전! 덧셈", "개념")}
  <div class="sec">{sec(1, "10 친구 찾기", "더해서 10이 되는 짝꿍을 찾아요")}
    <div class="chips">{chips}</div></div>
  <div class="sec">{sec(2, "점을 건네서 10 만들기", "7 + 8 을 풀어 봐요")}
    <div class="story">
      <div class="step"><span class="tag">처음</span>{char(7)}{tf((7, c7))}<span class="op">+</span>{char(8)}{tf((8, c8))}</div>
      <div class="move">⬇ 8이 7에게 점 <b>3개</b>를 건네줘요. 7은 꽉 찬 10이 되고, 8은 5가 남아요.</div>
      <div class="step"><span class="tag">건넨 뒤</span>{char(10)}{tf((7, c7), (3, c8))}<span class="op">+</span>{char(5)}{tf((5, c8))}</div>
      <div class="eq">7 + 8 = 10 + 5 = {box()}</div>
    </div></div>
  <div class="sec">{sec(3, "머릿속으로 가르기", "가르기 그림 없이 10을 먼저 만들어요")}
    <div class="splits">{splits}</div></div>
  {footer()}
</div>'''


def page_sub_concept():
    chips = "".join(f'<div class="chip">10 - {b} = {box()}</div>' for b in [3, 7, 1, 6, 4, 8, 2, 5])
    splits = "".join(bridge(a, "-", b) for a, b in [(13, 5), (11, 3), (14, 6), (12, 5), (15, 7), (11, 4), (16, 8), (13, 6), (12, 7)])
    c10, c2, c4, c4b = COLORS[10], COLORS[2], COLORS[4], "#9be08f"
    return f'''<div class="page">{header("③", "10 만들기 대작전! 뺄셈", "개념")}
  <div class="sec">{sec(1, "10에서 빼기", "10 친구를 떠올리면 바로 보여요")}
    <div class="chips">{chips}</div></div>
  <div class="sec">{sec(2, "10까지 먼저 빼기", "12 - 4 를 풀어 봐요. 4를 2와 2로 갈라요")}
    <div class="story">
      <div class="step"><span class="tag">처음</span><span class="grp"><b>12</b>{char(10)}{tf((10, c10))}{char(2)}{tf((2, c2))}</span></div>
      <div class="step"><span class="tag">빼는 수</span><span class="op">-</span>{char(4)}{tf((2, c4), (2, c4b))}<span class="note">4를 2와 2로 갈라요</span></div>
      <div class="move">⬇ 4 중에서 먼저 2를 빼요. 2 친구는 0이 되고, 10이 남아요. (12 - 2 = 10)</div>
      <div class="step"><span class="tag">2 빼기</span><span class="grp"><b>10</b>{char(10)}{tf((10, c10))}{char(0)}{tf((2, c2, "x"))}</span></div>
      <div class="move">⬇ 아직 2를 더 빼야 해요. 텐텐에게서 2를 빼요. (10 - 2 = 8)</div>
      <div class="step"><span class="tag">2 더 빼기</span><span class="grp">{char(8)}{tf((8, c10), (2, c10, "x"))}</span></div>
      <div class="eq">12 - 4 = 10 - 2 = {box()}</div>
    </div></div>
  <div class="sec">{sec(3, "머릿속으로 가르기", "먼저 10까지 빼고, 남은 수를 더 빼요")}
    <div class="splits">{splits}</div></div>
  {footer()}
</div>'''


def page_drill(no, title, items, cols, captain):
    return f'''<div class="page">{header(no, title, "술술 도전", captain)}
  <div class="sec">{sec("!", f"{len(items)}문제 술술 도전", "머릿속으로 10을 만들어요")}
    {drill(items, cols)}</div>
  {footer()}
</div>'''


def answer(a, op, b):
    return a + b if op == "+" else a - b


def page_answers(pages):
    blocks = []
    for name, items in pages:
        cells = "".join(f'<span>{a}{op}{b}={answer(a, op, b)}</span>' for a, op, b in items)
        blocks.append(f'<h3>{name}</h3><div class="ans">{cells}</div>')
    return f'''<div class="page answers"><h2>정답지 (부모님용)</h2>
  <p class="hint">① 10 친구: 1·3·2·4·7·5·8·6 &nbsp; ① 머릿속 가르기: 4/14·3/13·3/13·2/12·5/15·7/17·1/11·3/13·4/14·5/15·3/13·6/16 &nbsp; ① 예시 15<br>
  ③ 10에서 빼기: 7·3·9·4·6·2·8·5 &nbsp; ③ 머릿속 가르기: 2/8·2/8·2/8·3/7·2/8·3/7·2/8·3/7·5/5 &nbsp; ③ 예시 8</p>
  {"".join(blocks)}</div>'''


def main():
    seed = sys.argv[1] if len(sys.argv) > 1 else "1"
    rng = random.Random(seed)
    add = [(a, "+", b) for a, b in ADD_FACTS]
    sub = [(c, "-", d) for c, d in SUB_FACTS]
    rng.shuffle(add)
    rng.shuffle(sub)
    mixed = rng.sample(add, 20) + rng.sample(sub, 20)
    rng.shuffle(mixed)

    pages = [
        page_add_concept(),
        page_drill("②", "덧셈 36문제", add, 3, 10),
        page_sub_concept(),
        page_drill("④", "뺄셈 36문제", sub, 3, 10),
        page_drill("⑤", "섞어서 40문제", mixed, 4, 10),
        page_answers([("② 덧셈", add), ("④ 뺄셈", sub), ("⑤ 섞어서", mixed)]),
    ]
    css = (HERE / "style.css").read_text()
    html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>10 만들기 대작전</title><style>{css}</style></head><body>{"".join(pages)}</body></html>'
    OUT.mkdir(exist_ok=True)
    src = OUT / f"10making_{seed}.html"
    src.write_text(html)
    pdf = OUT / f"10making_{seed}.pdf"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--allow-file-access-from-files",
                    "--no-pdf-header-footer", "--virtual-time-budget=10000", f"--print-to-pdf={pdf}", src.as_uri()],
                   check=True, capture_output=True)
    print(pdf)


if __name__ == "__main__":
    main()
