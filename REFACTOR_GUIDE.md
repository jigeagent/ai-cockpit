# AI Cockpit 子页面重构指引

> 目标：将 5 个子页面（about / agents / workshop / academy / skills）从旧版 Linear 紫风格统一为首页 index.html 的暗黑+琥珀金玻璃质感风格。
> 基准：`index.html`（2026-05-15 版）为唯一设计范式。
> 操作方式：每个文件**整段替换 `<style>` 块**，然后微调 HTML 结构以匹配新 CSS 类名。

---

## 一、设计系统对比

| 维度 | 旧版（当前子页） | 新版（index.html 范式） |
|------|-----------------|------------------------|
| 背景色 | `#0d1117` | `oklch(6% 0.003 250)`（更深的暗蓝黑） |
| 品牌色 | `#5E6AD2`（Linear 紫） | `oklch(68% 0.18 60)`（琥珀金） |
| 辅助色 | `#3fb950`绿 `#f85149`红 | `oklch(58% 0.17 145)`绿 `oklch(52% 0.18 25)`红 |
| 卡片 | 纯色 `#161b22` + 1px 边框 | `backdrop-filter: blur(16px)` 玻璃卡片 + hover 光晕 |
| 按钮 | `border-radius: 10px` 方块 | `border-radius: 100px` 胶囊形 |
| 导航栏 | 56px 高，"AI驾驶舱"文字 | 60px 高，`◈ AI Cockpit` Logo |
| Hero | 70vh，径向渐变 | 100vh，Unsplash 地球图+渐变叠加 |
| 最大宽度 | `1100px` | `1280px` |
| 动画 | 无 | `.animate-in` 滚动淡入 + `#ambient` 背景光晕漂移 |
| 品牌名 | "AI驾驶舱" | "AI Cockpit" |
| Footer | 单行居中 | 5列网格 + 底部栏 |

---

## 二、每个文件必须改的 7 件事

### 1. CSS `:root` 变量 —— 整段替换

```css
:root{
  --bg:oklch(6% 0.003 250);
  --surface:oklch(14% 0.005 250);
  --surface-2:oklch(18% 0.005 250);
  --fg:oklch(92% 0.005 80);
  --fg-secondary:oklch(65% 0.01 80);
  --fg-muted:oklch(42% 0.008 80);
  --border:oklch(24% 0.008 250);
  --border-light:oklch(30% 0.008 250 / 40%);
  --accent:oklch(68% 0.18 60);
  --accent-dim:oklch(55% 0.14 60);
  --accent-glow:oklch(68% 0.18 60 / 12%);
  --accent-bg:oklch(68% 0.18 60 / 7%);
  --danger:oklch(52% 0.18 25);
  --danger-bg:oklch(52% 0.18 25 / 10%);
  --success:oklch(58% 0.17 145);
  --success-bg:oklch(58% 0.17 145 / 10%);
  --font-display:-apple-system,BlinkMacSystemFont,'SF Pro Display','Segoe UI',system-ui,sans-serif;
  --font-body:-apple-system,BlinkMacSystemFont,'SF Pro Text','Segoe UI',system-ui,sans-serif;
  --font-mono:ui-monospace,'SF Mono','JetBrains Mono',Menlo,monospace;
  --radius:12px;
  --radius-sm:8px;
  --max-width:1280px;
  --glass-bg:oklch(12% 0.005 250 / 55%);
}
```

**所有旧变量**（`--text`、`--brand`、`--card`、`--gold` 等）**全部删除**，改用上面这套。

### 2. 新增 `#ambient` 背景光晕层

在 `<body>` 开头、`<nav>` 之前插入：

```html
<!-- Ambient glow -->
<div id="ambient" aria-hidden="true">
  <span class="g1 ambient-drift"></span>
  <span class="g2 ambient-drift"></span>
  <span class="g3 ambient-drift"></span>
  <span class="g4 ambient-drift"></span>
</div>
```

对应 CSS：

```css
#ambient{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}
#ambient span{position:absolute;border-radius:50%;will-change:transform}
#ambient .g1{width:60vw;height:60vw;top:-10%;right:-10%;background:radial-gradient(circle,oklch(68% 0.18 60/6%),transparent 70%)}
#ambient .g2{width:40vw;height:40vw;bottom:15%;left:-5%;background:radial-gradient(circle,oklch(68% 0.18 60/4%),transparent 70%);animation-delay:-6s}
#ambient .g3{width:50vw;height:50vw;top:40%;right:20%;background:radial-gradient(circle,oklch(58% 0.14 60/3%),transparent 70%);animation-delay:-12s}
#ambient .g4{width:30vw;height:30vw;bottom:30%;right:5%;background:radial-gradient(circle,oklch(68% 0.18 60/5%),transparent 70%);animation-delay:-3s}
.ambient-drift{animation:ambient-drift 20s ease-in-out infinite alternate}

@keyframes ambient-drift{
  0%{transform:translate(0,0) scale(1)}
  33%{transform:translate(3%,-4%) scale(1.05)}
  66%{transform:translate(-2%,2%) scale(0.95)}
  100%{transform:translate(4%,-2%) scale(1.03)}
}
```

### 3. 导航栏重构

**HTML 结构改为：**

```html
<nav>
  <div class="container">
    <a href="index.html" class="logo"><span>◈</span> AI Cockpit</a>
    <ul class="nav-links">
      <li><a href="agents.html">智能体</a></li>
      <li><a href="workshop.html">工坊</a></li>
      <li><a href="academy.html">商学院</a></li>
      <li><a href="skills.html">技能</a></li>
      <li><a href="about.html">关于</a></li>
    </ul>
  </div>
</nav>
```

**CSS：**

```css
nav{
  position:fixed;top:0;left:0;right:0;z-index:100;
  background:oklch(6% 0.003 250/75%);
  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-bottom:1px solid oklch(24% 0.008 250/50%);
}
nav .container{display:flex;align-items:center;height:60px;gap:2rem}
nav .logo{font-family:var(--font-display);font-weight:700;font-size:1.15rem;letter-spacing:-0.02em;color:var(--fg);text-decoration:none;white-space:nowrap}
nav .logo span{color:var(--accent)}
nav .nav-links{display:flex;gap:1.5rem;list-style:none;margin-left:auto}
nav .nav-links a{color:var(--fg-secondary);text-decoration:none;font-size:.875rem;font-weight:500;transition:color .2s}
nav .nav-links a:hover{color:var(--fg)}
```

**要点：**
- 去掉 `nav-inner`、`nav-brand`、`nav-toggle`（不要汉堡菜单，桌面端固定）
- 品牌名统一为 `◈ AI Cockpit`
- 导航栏高度 60px
- 当前页高亮靠 JS 或手动加 class（可选）

### 4. Hero 区重构

**结构：**

```html
<section class="hero">
  <div class="hero-bg"></div>
  <div class="container">
    <div class="hero-eyebrow">页面标签</div>
    <h1>主标题</h1>
    <p>副标题描述</p>
    <!-- CTA 按钮可选 -->
  </div>
</section>
```

**CSS：**

```css
.hero{
  position:relative;min-height:100vh;display:flex;align-items:center;
  overflow:hidden;padding:120px 0 80px
}
.hero-bg{
  position:absolute;inset:0;z-index:0;
  background:url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80') center/cover no-repeat;
}
.hero-bg::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,oklch(6% 0.003 250/92%) 0%,oklch(6% 0.003 250/70%) 50%,oklch(6% 0.003 250/88%) 100%);
}
.hero .container{position:relative;z-index:2;text-align:center;max-width:880px}
.hero-eyebrow{
  display:inline-flex;align-items:center;gap:.5rem;
  font-size:.75rem;font-weight:500;letter-spacing:.08em;text-transform:uppercase;
  color:var(--accent);font-family:var(--font-mono);
  background:var(--accent-bg);border:1px solid var(--accent-glow);
  padding:.4rem .9rem;border-radius:100px;margin-bottom:2rem;
}
.hero h1{
  font-size:clamp(2.25rem,5.5vw,4.25rem);
  margin-bottom:1.25rem;
  background:linear-gradient(180deg,var(--fg) 60%,oklch(75% 0.008 80));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.hero p{
  font-size:clamp(1rem,1.4vw,1.2rem);color:var(--fg-secondary);
  line-height:1.6;max-width:680px;margin:0 auto 2.5rem;
}
```

**要点：**
- `min-height` 从 `70vh` 改为 `100vh`
- `hero-badge` → `hero-eyebrow`（类名变，样式也变：更紧凑、大写、等宽字体）
- 背景图用 Unsplash（与首页同一张）
- 标题渐变色从紫色改为 `var(--fg)`（白色）渐变
- `.container` 居中，`max-width: 880px`
- 旧版 `hero::before` 径向渐变**删掉**

### 5. Section 和卡片样式

**Section 基础：**

```css
.container{max-width:var(--max-width);margin:0 auto;padding:0 clamp(1rem,3vw,2.5rem);position:relative;z-index:1}

section{padding:clamp(4rem,8vw,7rem) 0}
section.alt{background:oklch(8% 0.003 250)}

.section-label{font-size:.75rem;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin-bottom:.75rem}

.section-header{
  display:flex;justify-content:space-between;align-items:flex-end;
  margin-bottom:2.5rem;flex-wrap:wrap;gap:1rem
}
.section-header p{color:var(--fg-secondary);font-size:.95rem;max-width:480px}
```

**HTML 结构改为：**

```html
<section>
  <div class="container">
    <div class="section-label">— 标签</div>
    <div class="section-header">
      <h2>标题</h2>
      <p>描述文字</p>
    </div>
    <!-- 内容网格 -->
  </div>
</section>
```

**交替深色背景用 `<section class="alt">`**（而不是内联 `background`）

**卡片（玻璃效果）：**

```css
.glass{
  background:var(--glass-bg);
  backdrop-filter:blur(16px);
  -webkit-backdrop-filter:blur(16px);
  border:1px solid var(--border-light);
  border-radius:var(--radius);
  transition:border-color .3s,box-shadow .3s,transform .3s;
}
.glass:hover{border-color:var(--accent-dim);box-shadow:0 0 30px var(--accent-glow),inset 0 1px 0 oklch(100% 0 0/4%);transform:translateY(-2px)}
```

**旧版 `.panel` 全部替换为 `.glass`**（纯色 → 玻璃）

### 6. 按钮重构

```css
.btn{
  display:inline-flex;align-items:center;gap:.5rem;
  padding:.75rem 1.75rem;border-radius:100px;
  font-size:.95rem;font-weight:500;text-decoration:none;
  transition:all .25s;cursor:pointer;border:none;
}
.btn-primary{
  background:var(--accent);color:oklch(8% 0.003 250);
  box-shadow:0 0 20px oklch(68% 0.18 60/25%);
}
.btn-primary:hover{background:oklch(72% 0.2 60);transform:translateY(-1px);box-shadow:0 0 30px oklch(68% 0.18 60/35%)}
.btn-secondary{
  background:transparent;color:var(--fg);
  border:1px solid var(--border-light);
}
.btn-secondary:hover{border-color:var(--accent-dim);background:var(--accent-bg)}
```

**要点：**
- `border-radius: 10px` → `border-radius: 100px`（胶囊形）
- 背景色从 `#5E6AD2` 改为 `var(--accent)`（琥珀金）
- 去掉内联 style 覆盖，用 class

### 7. Footer 重构

**结构：**

```html
<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo"><span>◈</span> AI Cockpit</a>
        <p>一句话描述</p>
      </div>
      <div class="footer-col">
        <h4>模型</h4>
        <ul>
          <li><a href="./agents.html">排行榜</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>技能</h4>
        <ul>
          <li><a href="./skills.html">技能库</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>工作坊</h4>
        <ul>
          <li><a href="./workshop.html">铸造流水线</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>学院</h4>
        <ul>
          <li><a href="./academy.html">文档中心</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>AI Cockpit · 企业级 Agent 质量工程 · © 2026</p>
      <div class="social-links">
        <a href="#">GitHub</a>
        <a href="#">Twitter</a>
        <a href="#">微信公众号</a>
      </div>
    </div>
  </div>
</footer>
```

**CSS：**

```css
footer{border-top:1px solid var(--border);padding:3.5rem 0 2rem;margin-top:0}
.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr;gap:2.5rem}
.footer-brand .logo{font-family:var(--font-display);font-weight:700;font-size:1.15rem;letter-spacing:-0.02em;color:var(--fg);text-decoration:none;display:inline-block;margin-bottom:.6rem}
.footer-brand .logo span{color:var(--accent)}
.footer-brand p{font-size:.8rem;color:var(--fg-muted);line-height:1.6;max-width:280px}
.footer-col h4{font-size:.75rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--fg-muted);margin-bottom:.9rem}
.footer-col ul{list-style:none;display:flex;flex-direction:column;gap:.5rem}
.footer-col ul a{color:var(--fg-secondary);text-decoration:none;font-size:.82rem;transition:color .2s}
.footer-col ul a:hover{color:var(--accent)}
.footer-bottom{border-top:1px solid var(--border);margin-top:2.5rem;padding-top:1.5rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem}
.footer-bottom p{font-size:.75rem;color:var(--fg-muted)}
.footer-bottom .social-links{display:flex;gap:1rem}
.footer-bottom .social-links a{color:var(--fg-muted);text-decoration:none;font-size:.75rem;transition:color .2s}
.footer-bottom .social-links a:hover{color:var(--accent)}
```

### 8. 滚动动画（可选但推荐）

**CSS：**

```css
.animate-in{opacity:0;transform:translateY(24px);transition:opacity .7s ease,transform .7s ease}
.animate-in.visible{opacity:1;transform:translateY(0)}
.animate-in.d1{transition-delay:0s}
.animate-in.d2{transition-delay:.1s}
.animate-in.d3{transition-delay:.2s}
.animate-in.d4{transition-delay:.3s}
```

**JS（`</body>` 之前）：**

```html
<script>
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.15 });
document.querySelectorAll('.animate-in').forEach(el => observer.observe(el));
</script>
```

---

## 三、各页面特殊处理

### about.html
- 保留 timeline（三人核心圈），但卡片改 `.panel` → `.glass`
- 信念列表保留，边框颜色改为 `var(--border-light)`
- CTA 按钮改胶囊形

### agents.html
- 四维度卡片（dim-card）改 `.glass`
- Agent 卡片（agent-card）改 `.glass`，tags 改用 `.model-chip` 样式
- 团队 Agent 网格（our-agent-grid）改 `.glass`

### workshop.html
- 四大模块卡片改 `.glass`
- 5 个铸造案例卡片改首页 `.case-card` 样式（含图片+标签）
- 行业痛点网格改 `.glass`
- CTA 按钮改胶囊形

### academy.html
- 统计数据卡片改首页 `.data-card` 样式（大数字渐变色）
- 认证学员卡片改 `.glass`
- AIQ 诊断框改 `.glass`
- 命名对照表用首页 `.comp-table` 样式

### skills.html
- 技能卡片改首页 `.skill-card` 样式（SVG 图标 + 玻璃效果）
- 去掉 `.skill-tabs`，改为直接展示
- 占位区域改 `.glass`

---

## 四、操作顺序

1. 先改 **about.html**（最简单，验证流程）
2. 再改 **agents.html** + **skills.html**（结构类似，可以并行）
3. 最后改 **workshop.html** + **academy.html**（内容最多）
4. 每个文件改完后用浏览器打开验证
5. 全部改完后 `git commit` + `git push`

---

## 五、负面清单（不要犯的错误）

1. ❌ 不要彩虹色块堆叠（只用 `var(--accent)` 琥珀金）
2. ❌ 不要用 emoji 当图标（用 SVG inline）
3. ❌ 不要用超过 700 的字重（标题最高 600，数字可用 700）
4. ❌ 不要用纯白 `#ffffff` 做文字（用 `var(--fg)` = `oklch(92%...)`）
5. ❌ 不要用 `#5E6AD2` 紫色（旧版遗留）
6. ❌ 不要保留 `.panel` 类名（全部替换为 `.glass`）
7. ❌ 不要保留汉堡菜单按钮 `nav-toggle`
8. ❌ 不要用内联 `style` 覆盖按钮样式（用 `.btn-primary` / `.btn-secondary` class）

---

*生成时间：2026-05-15 22:50*
*基准文件：index.html（已部署到 GitHub Pages）*
