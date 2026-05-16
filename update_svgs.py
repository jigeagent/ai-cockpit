import re
import os

base = r"D:\OpenClaw\workspace\ai-cockpit-website"

# 1. agents.html: Insert images into model-cards
agents_imgs = ["agents-01-matrix.svg", "agents-02-neural.svg", "agents-03-dialogue.svg"]

with open(os.path.join(base, "agents.html"), "r", encoding="utf-8") as f:
    html = f.read()

# Find all model-avatar divs and inject image after them
# Pattern: <div class="model-avatar">...</div>
pattern = r'(<div class="model-avatar"[^>]*>.*?</div>)'
matches = list(re.finditer(pattern, html, re.DOTALL))

# Only target the first 3 (platform cards) or all? 
# The prompt says "agents.html ... 3 images". 
# The HTML has 3 platform cards + 4 team cards? 
# Let's check. 
# "agents.html": model-grid has 3 platform cards.
# There might be a second grid with team cards. 
# We should only target the first 3.

for i, m in enumerate(reversed(matches[:3])):
    idx = len(matches[:3]) - 1 - i
    if idx >= len(agents_imgs):
        continue
    avatar_html = m.group(1)
    new_img = f'\n        <div class="card-img" style="height:170px;border-radius:8px;overflow:hidden;margin-top:1rem">\n            <img src="{agents_imgs[idx]}" alt="Agents Illustration" loading="lazy" style="width:100%;height:100%;object-fit:cover">\n        </div>'
    # Insert after the avatar div
    html = html[:m.end()] + new_img + html[m.end():]

with open(os.path.join(base, "agents.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("✅ agents.html updated")

# 2. academy.html: Replace src of existing images
academy_imgs = ["academy-01-knowledge.svg", "academy-02-growth.svg"]

with open(os.path.join(base, "academy.html"), "r", encoding="utf-8") as f:
    html = f.read()

# Find images inside .team-card
# Pattern: <img ... src="...">
# We need to find them in order.
cards = re.finditer(r'<div class="team-card[^>]*">.*?</div>', html, re.DOTALL)
# This is hard with regex for nested.
# Let's find <img src="..."> tags that are inside the file.
# Previous script inserted <img> tags. Let's find <img ... src="...">
# We'll replace the first 2 occurrences of <img ...> inside the main content.

# Simpler: Find all <img src="..."> tags in the body (exclude nav/footer if they have imgs)
# The injected images were: <div class="card-img" ...><img ...>
# We can just find <div class="card-img" ...> and replace the src inside.

for i, img_file in enumerate(academy_imgs):
    # Find the img tag that currently has some src
    # We'll look for <img src="..." alt="...">
    # We want to replace the src value.
    # Let's just find all img tags and replace their srcs.
    pass

# Robust approach:
# Find all <img> tags that are NOT in nav/footer.
# In academy.html, the images we added are in .team-card.
# Let's find <div class="card-img" ...><img src="...">
pattern = r'(<div class="card-img"[^>]*><img\s+[^>]*src=")[^"]*("[^>]*>)'

def replacer(match):
    # We need a counter to pick the right image
    # But re.sub doesn't support state easily.
    return match.group(0) # Placeholder

# Let's do a loop
matches = list(re.finditer(pattern, html, re.DOTALL))
if len(matches) >= len(academy_imgs):
    # Reverse replace to keep indices valid
    for i, m in enumerate(reversed(matches)):
        idx = len(matches) - 1 - i
        if idx >= len(academy_imgs):
            continue
        new_src = f'{academy_imgs[idx]}'
        old_html = m.group(0)
        # Replace src="..."
        new_html = re.sub(r'src="[^"]*"', f'src="{new_src}"', old_html)
        html = html[:m.start()] + new_html + html[m.end():]

with open(os.path.join(base, "academy.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("✅ academy.html updated")

# 3. skills.html: Replace src of existing images
skills_imgs = ["skills-01-terminal.svg", "skills-02-api.svg"]

with open(os.path.join(base, "skills.html"), "r", encoding="utf-8") as f:
    html = f.read()

matches = list(re.finditer(pattern, html, re.DOTALL))
if len(matches) >= len(skills_imgs):
    for i, m in enumerate(reversed(matches)):
        idx = len(matches) - 1 - i
        if idx >= len(skills_imgs):
            continue
        new_src = f'{skills_imgs[idx]}'
        old_html = m.group(0)
        new_html = re.sub(r'src="[^"]*"', f'src="{new_src}"', old_html)
        html = html[:m.start()] + new_html + html[m.end():]

with open(os.path.join(base, "skills.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("✅ skills.html updated")

# 4. about.html: Replace src of existing images
about_imgs = ["about-01-team.svg", "about-02-innovation.svg"]

with open(os.path.join(base, "about.html"), "r", encoding="utf-8") as f:
    html = f.read()

matches = list(re.finditer(pattern, html, re.DOTALL))
if len(matches) >= len(about_imgs):
    for i, m in enumerate(reversed(matches)):
        idx = len(matches) - 1 - i
        if idx >= len(about_imgs):
            continue
        new_src = f'{about_imgs[idx]}'
        old_html = m.group(0)
        new_html = re.sub(r'src="[^"]*"', f'src="{new_src}"', old_html)
        html = html[:m.start()] + new_html + html[m.end():]

with open(os.path.join(base, "about.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("✅ about.html updated")

print("\n🎯 All HTML files updated with new SVGs.")
