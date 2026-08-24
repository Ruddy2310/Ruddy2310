import json, math
from pathlib import Path

data = json.loads(Path("assets/skills.json").read_text())
axes = data["axes"]
W, H = 700, 520
cx, cy, radius = 350, 260, 170

def pt(i, r):
    a = -math.pi/2 + 2*math.pi*i/len(axes)
    return cx + r*math.cos(a), cy + r*math.sin(a)

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
svg.append('<rect width="100%" height="100%" rx="20" fill="#0d1117"/>')
svg.append(f'<text x="{cx}" y="35" text-anchor="middle" fill="#39d353" font-size="22" font-family="sans-serif">{data["title"]}</text>')

for ring in [25, 50, 75, 100]:
    pts = " ".join(f"{x:.1f},{y:.1f}" for x,y in [pt(i, radius*ring/100) for i in range(len(axes))])
    svg.append(f'<polygon points="{pts}" fill="none" stroke="#30363d" stroke-width="1"/>')

for i, a in enumerate(axes):
    x,y = pt(i, radius)
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#30363d"/>')
    lx,ly = pt(i, radius+35)
    svg.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" fill="#c9d1d9" font-size="14" font-family="sans-serif">{a["label"]}</text>')

points = " ".join(f"{x:.1f},{y:.1f}" for i,a in enumerate(axes) for x,y in [pt(i, radius*a["value"]/100)])
svg.append(f'<polygon points="{points}" fill="#39d353" fill-opacity=".18" stroke="#39d353" stroke-width="3"/>')

for i,a in enumerate(axes):
    x,y = pt(i, radius*a["value"]/100)
    svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#39d353"/>')
    svg.append(f'<text x="{x:.1f}" y="{y-10:.1f}" text-anchor="middle" fill="#fff" font-size="12" font-family="sans-serif">{a["value"]}</text>')

svg.append("</svg>")
Path("assets/radar.svg").write_text("\n".join(svg), encoding="utf-8")
print("Generated assets/radar.svg")
