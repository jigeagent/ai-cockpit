import re
import os

BASE = r'D:\OpenClaw\workspace\ai-cockpit-website'

def load(name):
    with open(os.path.join(BASE, name), 'r', encoding='utf-8') as f:
        return f.read()

def save(name, content):
    with open(os.path.join(BASE, name), 'w', encoding='utf-8') as f:
        f.write(content)

files = ['index.html', 'agents.html', 'workshop.html', 'academy.html', 'skills.html', 'about.html']

for name in files:
    html = load(name)
    changes = 0

    # ====== GLOBAL FOOTER FIXES ======
    # Social links
    old = '<a href="#">GitHub</a>'
    new = '<a href="https://github.com/jigeagent">GitHub</a>'
    if old in html: html = html.replace(old, new); changes += 1

    old = '<a href="#">Twitter</a>'
    new = '<a href="https://x.com/jigeagent">Twitter</a>'
    if old in html: html = html.replace(old, new); changes += 1

    old = '<a href="#">微信公众号</a>'
    new = '<a href="javascript:void(0)">微信公众号</a>'
    if old in html: html = html.replace(old, new); changes += 1

    # Footer doc links
    old = '<a href="#">文档中心</a>'
    new = '<a href="academy.html#docs">文档中心</a>'
    if old in html: html = html.replace(old, new); changes += 1

    old = '<a href="#">API 文档</a>'
    new = '<a href="academy.html#api">API 文档</a>'
    if old in html: html = html.replace(old, new); changes += 1

    old = '<a href="#">学术论文</a>'
    new = '<a href="academy.html#docs">学术论文</a>'
    if old in html: html = html.replace(old, new); changes += 1

    old = '<a href="#">社区</a>'
    new = '<a href="about.html#contact">社区</a>'
    if old in html: html = html.replace(old, new); changes += 1

    # Footer other dead links
    old = '<a href="#">基准测试</a>'
    new = '<a href="academy.html#docs">基准测试</a>'
    if old in html: html = html.replace(old, new); changes += 1

    old = '<a href="#">案例库</a>'
    new = '<a href="workshop.html#cases">案例库</a>'
    if old in html: html = html.replace(old, new); changes += 1

    old = '<a href="#">最佳实践</a>'
    new = '<a href="workshop.html">最佳实践</a>'
    if old in html: html = html.replace(old, new); changes += 1

    old = '<a href="#">模板</a>'
    new = '<a href="skills.html">模板</a>'
    if old in html: html = html.replace(old, new); changes += 1

    old = '<a href="#">视频教程</a>'
    new = '<a href="academy.html#docs">视频教程</a>'
    if old in html: html = html.replace(old, new); changes += 1

    # Skill footer links
    old = '<a href="#">Sales Assistant</a>'
    new = '<a href="skills.html#all-skills">Sales Assistant</a>'
    if old in html: html = html.replace(old, new); changes += 1

    old = '<a href="#">Code Review</a>'
    new = '<a href="skills.html#all-skills">Code Review</a>'
    if old in html: html = html.replace(old, new); changes += 1

    old = '<a href="#">Customer Service</a>'
    new = '<a href="skills.html#all-skills">Customer Service</a>'
    if old in html: html = html.replace(old, new); changes += 1

    old = '<a href="#">Report Analysis</a>'
    new = '<a href="skills.html#all-skills">Report Analysis</a>'
    if old in html: html = html.replace(old, new); changes += 1

    # ====== PAGE-SPECIFIC CTA FIXES ======
    if name == 'index.html':
        old = '免费 AIQ 诊断 →'
        # find the link containing this text
        html = re.sub(
            r'<a href="#"([^>]*)>免费 AIQ 诊断 →</a>',
            r'<a href="academy.html#aiq-diagnosis"\1>免费 AIQ 诊断 →</a>',
            html
        )
        html = re.sub(
            r'<a href="#"([^>]*)>企业批量铸造</a>',
            r'<a href="workshop.html#casting-form"\1>企业批量铸造</a>',
            html
        )

    elif name == 'agents.html':
        html = re.sub(
            r'<a href="#"([^>]*)>开始 AIQ 诊断 →</a>',
            r'<a href="academy.html#aiq-diagnosis"\1>开始 AIQ 诊断 →</a>',
            html
        )
        html = re.sub(
            r'<a href="#"([^>]*)>提交评估</a>',
            r'<a href="workshop.html#casting-form"\1>提交评估</a>',
            html
        )

    elif name == 'workshop.html':
        html = re.sub(
            r'<a href="#"([^>]*)>开始铸造 →</a>',
            r'<a href="workshop.html#casting-form"\1>开始铸造 →</a>',
            html
        )
        html = re.sub(
            r'<a href="#"([^>]*)>查看案例</a>',
            r'<a href="#cases"\1>查看案例</a>',
            html
        )

    elif name == 'academy.html':
        html = re.sub(
            r'<a href="#"([^>]*)>开始学习 →</a>',
            r'<a href="academy.html#docs"\1>开始学习 →</a>',
            html
        )
        html = re.sub(
            r'<a href="#"([^>]*)>开始诊断 →</a>',
            r'<a href="academy.html#aiq-diagnosis"\1>开始诊断 →</a>',
            html
        )

    elif name == 'skills.html':
        html = re.sub(
            r'<a href="#"([^>]*)>浏览全部 Skill →</a>',
            r'<a href="skills.html#all-skills"\1>浏览全部 Skill →</a>',
            html
        )
        html = re.sub(
            r'<a href="#"([^>]*)>关注进展</a>',
            r'<a href="https://github.com/jigeagent"\1>关注进展</a>',
            html
        )
        # Install buttons → disabled span
        html = re.sub(
            r'<a href="#"([^>]*)>▸ Install</a>',
            r'<span class="btn-disabled"\1>即将上线</span>',
            html
        )

    elif name == 'about.html':
        html = re.sub(
            r'<a href="#"([^>]*)>探索方法论</a>',
            r'<a href="academy.html#methodology"\1>探索方法论</a>',
            html
        )

    save(name, html)
    print(f'{name}: {changes} footer fixes + page CTAs')

print('\nAll files updated.')
