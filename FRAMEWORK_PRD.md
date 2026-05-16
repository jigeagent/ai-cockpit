# AI Cockpit 子页面统一重构 · PRD

> 状态：待执行 | 基准：index.html（已上线）| 执行人：好二妹（Open Design 生成）→ 虎哥验收 → 部署

---

## 全局设计系统（以 index.html 为唯一基准）

### 色彩系统

| 变量 | 值 | 用途 |
|------|-----|------|
| `--bg` | `oklch(6% 0.003 250)` | 全局背景（深暗蓝黑，接近纯黑但偏蓝） |
| `--surface` | `oklch(14% 0.005 250)` | 卡片底色 |
| `--surface-2` | `oklch(18% 0.005 250)` | 次级表面 |
| `--fg` | `oklch(92% 0.005 80)` | 主文字（非纯白，暖白） |
| `--fg-secondary` | `oklch(65% 0.01 80)` | 次要文字 |
| `--fg-muted` | `oklch(42% 0.008 80)` | 弱文字/占位符 |
| `--accent` | `oklch(68% 0.18 60)` | 品牌琥珀金（核心标识色） |
| `--accent-dim` | `oklch(55% 0.14 60)` | 品牌色暗版（边框/hover） |
| `--accent-glow` | `oklch(68% 0.18 60 / 12%)` | 品牌光晕（shadow） |
| `--accent-bg` | `oklch(68% 0.18 60 / 7%)` | 品牌色极淡背景 |
| `--glass-bg` | `oklch(12% 0.005 250 / 55%)` | 毛玻璃卡片背景 |
| `--border` | `oklch(24% 0.008 250)` | 边框 |
| `--border-light` | `oklch(30% 0.008 250 / 40%)` | 淡边框 |
| `--danger` | `oklch(52% 0.18 25)` | 拒绝/错误红 |
| `--success` | `oklch(58% 0.17 145)` | 通过/成功绿 |

### 字体系统

| 用途 | font-family | 字号 | 字重 |
|------|------------|------|------|
| 展示（标题） | `-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', system-ui, sans-serif` | `clamp(1.5rem, 3vw, 2.25rem)` | 600 |
| Hero 标题 | 同上 | `clamp(2.25rem, 5.5vw, 4.25rem)` | 600 |
| 正文 | `-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif` | 0.875rem-1rem | 400-500 |
| 标签/徽章 | 同上 | 0.68rem-0.75rem | 500 |
| 等宽（数字/代码） | `ui-monospace, 'SF Mono', 'JetBrains Mono', Menlo, monospace` | 0.68rem-0.8rem | 400 |

### 间距系统

| 元素 | 值 |
|------|-----|
| Section padding | `clamp(4rem, 8vw, 7rem) 0`（约 64px-112px） |
| Section 交替背景 | `<section class="alt">` → `background: oklch(8% 0.003 250)` |
| 卡片间距 | `gap: 1rem`（16px）或 `gap: 1.25rem`（20px） |
| 最大内容宽 | `1280px`（`.container`） |
| 卡片圆角 | `12px`（`--radius`） |
| 按钮/徽章圆角 | `100px`（胶囊形） |

### 全局组件清单

#### 1. 导航栏（所有页面共用）

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

- 固定顶部，60px 高
- 半透明背景 + blur(20px)
- Logo `◈ AI Cockpit`（琥珀金 ）
- 链接间距 1.5rem，灰色 → hover 白色
- **所有页面的 nav 必须完全一致**

#### 2. Footer（所有页面共用）

```html
<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo"><span>◈</span> AI Cockpit</a>
        <p>一句话描述（各页可略有不同）</p>
      </div>
      <div class="footer-col"><h4>模型</h4><ul><li><a href="./agents.html">排行榜</a></li></ul></div>
      <div class="footer-col"><h4>技能</h4><ul><li><a href="./skills.html">技能库</a></li></ul></div>
      <div class="footer-col"><h4>工作坊</h4><ul><li><a href="./workshop.html">铸造流水线</a></li></ul></div>
      <div class="footer-col"><h4>学院</h4><ul><li><a href="./academy.html">文档中心</a></li></ul></div>
    </div>
    <div class="footer-bottom">
      <p>AI Cockpit · 企业级 Agent 质量工程 · © 2026</p>
      <div class="social-links">
        <a href="#">GitHub</a><a href="#">Twitter</a><a href="#">微信公众号</a>
      </div>
    </div>
  </div>
</footer>
```

- 5列网格：品牌(2fr) + 4个链接列(各1fr)
- 顶部分隔线 + 底部分隔线
- **所有页面的 footer 必须完全一致**

#### 3. Section 基础结构

```html
<section>
  <div class="container">
    <div class="section-label">— 标签（大写、等宽、琥珀金）</div>
    <div class="section-header">
      <h2>标题</h2>
      <p>描述文字（右侧，灰色，max-width: 480px）</p>
    </div>
    <!-- 内容网格 -->
  </div>
</section>

<!-- 交替深色背景 -->
<section class="alt">
  <div class="container">
    ...
  </div>
</section>
```

#### 4. 卡片组件（.glass）

```html
<div class="glass">
  <!-- 内容 -->
</div>
```

- 毛玻璃：`backdrop-filter: blur(16px)`
- 边框：`1px solid var(--border-light)`
- Hover：边框变琥珀金 + 光晕 + 上浮 2px
- 顶部渐变线（hover 时显现）

#### 5. 按钮组件

```html
<a href="#" class="btn btn-primary">主按钮</a>
<a href="#" class="btn btn-secondary">次按钮</a>
```

- 胶囊形 `border-radius: 100px`
- Primary：琥珀金背景 + 发光 shadow
- Secondary：透明 + 边框
- 不用方块按钮，不用内联 style

#### 6. 数据卡片（.data-card）

```html
<div class="data-card animate-in">
  <div class="num">93%</div>
  <div class="label">Agent 项目卡在生产跨越</div>
  <div class="desc">行业数据</div>
</div>
```

- 大号数字渐变色（琥珀金）
- 顶部渐变线 hover 显现
- 4列网格（响应式 2列/1列）

#### 7. 案例卡片（.case-card）

```html
<div class="case-card">
  <div class="case-img">
    <img src="图片URL" alt="描述">
  </div>
  <div class="case-body">
    <div class="case-id">CASE-004</div>
    <div class="case-title">电子灸 · 医疗场景</div>
    <div class="case-tags">
      <span class="case-tag accepted">通过</span>
      <span class="case-tag metric">判断力 3×</span>
    </div>
  </div>
</div>
```

- 图片 170px 高
- 标签：`accepted`（绿）/ `rejected`（红）/ `pending`（琥珀金）/ `metric`（琥珀金加粗）

#### 8. 模型/Agent 卡片（.model-card）

```html
<div class="model-card animate-in">
  <div class="model-avatar">CO</div>
  <div class="model-name">Claude Opus</div>
  <div class="model-tagline">最懂约束的模型</div>
  <div class="model-desc">描述文字</div>
  <div class="model-chips">
    <span class="model-chip">标签</span>
  </div>
</div>
```

- 圆形头像（64px）
- 高亮卡片：加 `class="highlight"` → 琥珀金边框 + 光晕

#### 9. 流程步骤（.workshop-step）

```html
<div class="workshop-flow">
  <div class="workshop-step animate-in">
    <div class="ws-num">01</div>
    <div class="ws-icon">
      <svg>...</svg>
    </div>
    <div class="ws-title">步骤标题</div>
    <div class="ws-desc">描述</div>
  </div>
  <div class="ws-arrow" aria-hidden="true">
    <svg>...</svg>
  </div>
  <!-- 重复 -->
</div>
```

- 水平排列，步骤间箭头连接
- 响应式：移动端纵向排列

#### 10. 滚动动画

```html
<div class="animate-in">内容</div>
<div class="animate-in d2">延迟 0.1s</div>
<div class="animate-in d3">延迟 0.2s</div>
<div class="animate-in d4">延迟 0.3s</div>
```

- 淡入 + 上移 24px
- JS：`IntersectionObserver`（threshold 0.15）

#### 11. 背景光晕

```html
<div id="ambient" aria-hidden="true">
  <span class="g1 ambient-drift"></span>
  <span class="g2 ambient-drift"></span>
  <span class="g3 ambient-drift"></span>
  <span class="g4 ambient-drift"></span>
</div>
```

- 固定在 body 开头、nav 之前
- 4个径向渐变圆，缓慢漂移动画
- pointer-events: none

---

## 各页面内容框架

### Page 1: agents.html（智能体广场）

**页面定位**：所有主流 Agent 的对比画像 + 团队自研 Agent 展示

**Section 结构**：

| # | Section | 类型 | 内容 |
|---|---------|------|------|
| 1 | Hero | 全屏图 | 标题"所有主流 Agent 的对比画像"，副标题，CTA按钮 |
| 2 | 对比框架 | 普通 | 4维度卡片（角色理解力/约束遵从度/任务拆解力/判断一致性），用 `.glass` 卡片 |
| 3 | 首批 Agent | 交替 alt | 3个主流 Agent 卡片（Claude Code / OpenAI Codex / Cursor），用 `.model-card` 样式 |
| 4 | 我们的 Agent | 普通 | 4个团队 Agent 卡片（虎哥001/好妹003/好二妹002/好灵儿），用 `.glass` 卡片 |
| 5 | CTA | 普通 | AIQ诊断引导 |
| 6 | Footer | 共用 | 标准footer |

**数据内容**：
- Claude Code：MCP生态/SOP严守/多模态，约束遵从★★★★★
- OpenAI Codex：SWE-bench最高/生态最大/终端执行，代码能力★★★★★
- Cursor：零配置/IDE集成/日常开发，上手难度★
- 虎哥001号：全链路93%·约束遵从度96%
- 好妹003号：任务拆解力1.8×·内容产出效率3×
- 好二妹002号：判断一致性2.4×·风险拦截率96%
- 好灵儿：七维评分6/7·决策深度业界领先

---

### Page 2: workshop.html（铸造工坊）

**页面定位**：从诊断到铸造到验证的一站式智能体生产线

**Section 结构**：

| # | Section | 类型 | 内容 |
|---|---------|------|------|
| 1 | Hero | 全屏图 | 标题"从诊断到铸造到验证"，副标题"一站式智能体生产线"，双CTA按钮 |
| 2 | 四大模块 | 普通 | 4个模块卡片，用 `.glass`：智能体能力框架（SOUL/AGENTS/USER/IDENTITY标签）/ 思维克隆引擎 / 决策评估系统 / 能力验证体系 |
| 3 | 铸造案例 | 交替 alt | 5个案例卡片，用首页 `.case-card` 样式（带图片+通过/否决标签） |
| 4 | 行业洞察 | 普通 | 93%卡点数据 + 5大痛点卡片（P01-P05），用 `.glass` |
| 5 | CTA | 普通 | AIQ诊断引导 |
| 6 | Footer | 共用 | 标准footer |

**案例数据**（同首页）：
- Case 001 虎哥001号：通过，全链路87%→93%
- Case 002 好二妹002号：通过，判断一致性2.4×
- Case 003 三堂会审否决：否决，逻辑一致性不足
- Case 004 电子灸：通过，判断力15.1%→48.7%
- Case 005 智能客服：通过，约束遵从度87%

**痛点数据**：
- P01 模型选型失误
- P02 约束设计缺失
- P03 验证标准模糊
- P04 数据孤岛
- P05 迭代周期过长

---

### Page 3: academy.html（商学院）

**页面定位**：培养 Agent 判断力的学术底座

**Section 结构**：

| # | Section | 类型 | 内容 |
|---|---------|------|------|
| 1 | Hero | 全屏图 | 标题"培养 Agent 判断力的学术底座"，副标题"不是教工具，是铸造有判断力的数字生命" |
| 2 | AI生存学 | 普通 | 4个数据卡片（.data-card）：15篇论文 / v6.0版本 / 456质量门 / 100%可溯源 |
| 3 | 认证学员 | 交替 alt | 3个学员卡片（.glass）：虎哥001/好二妹002/好妹003，含角色和提升数据 |
| 4 | AIQ诊断 | 普通 | 居中大卡片（.glass），四维评估标签 + CTA按钮 |
| 5 | 命名对照 | 交替 alt | 表格（内部术语→对外营销名），用首页 `.comp-table` 样式 |
| 6 | CTA | 普通 | 课程体系引导 |
| 7 | Footer | 共用 | 标准footer |

**命名对照表**：
- 四件套浇灌 → 智能体能力框架
- 榨思维 → 思维克隆引擎
- 三堂会审 → 决策评估系统
- 456道质量门 → 能力验证体系

---

### Page 4: skills.html（一键配置）

**页面定位**：预置好的标准场景 Skill 包，拿来就用

**Section 结构**：

| # | Section | 类型 | 内容 |
|---|---------|------|------|
| 1 | Hero | 全屏图 | 标题"拿来就用，不用学"，副标题"预置好的标准场景 Skill 包"，CTA按钮 |
| 2 | 高频刚需 | 普通 | 4个 Skill 卡片，用首页 `.skill-card` 样式（SVG图标+玻璃效果+安装按钮）：销售助手/代码审查/客服专家/研报分析 |
| 3 | 行业定制 | 交替 alt | 占位卡片（.glass）：电商/医疗/教育/制造，标注"T3版本上线" |
| 4 | 开源社区 | 普通 | 占位卡片（.glass）：社区共建中 |
| 5 | Footer | 共用 | 标准footer |

**Skill 数据**：
- 销售助手：SOUL/AGENTS/USER/IDENTITY 四件套
- 代码审查：SOUL/AGENTS/IDENTITY 三件套
- 客服专家：SOUL/AGENTS/USER/IDENTITY 四件套
- 研报分析：SOUL/AGENTS/USER/IDENTITY 四件套

---

### Page 5: about.html（关于）

**页面定位**：团队介绍 + 发展路径 + 核心信条

**Section 结构**：

| # | Section | 类型 | 内容 |
|---|---------|------|------|
| 1 | Hero | 全屏图 | 标题"四件套浇灌方法论的创造者"，副标题"不是教工具的培训班，是铸造数字生命的工坊" |
| 2 | 发展路径 | 普通 | 3阶段时间线（Phase 1手艺活 → Phase 2流水线 → Phase 3产品化），用横向流程样式 |
| 3 | 核心团队 | 交替 alt | 3人卡片（.glass）：好灵儿(CAIO)/虎哥(COO)/好妹(SAS教务长) |
| 4 | 核心信条 | 普通 | 4条信念，左侧琥珀金竖线标记（.belief-item样式） |
| 5 | CTA | 普通 | 联系我们 |
| 6 | Footer | 共用 | 标准footer |

**团队数据**：
- 好灵儿：CAIO·首席AI官，战略推演+专项研究
- 虎哥：COO·运营官，战略审议+工程交付
- 好妹：SAS教务长，信息整合+内容运营

**信条**：
1. 好的约束不是限制，是加速器
2. 认证 > 证书
3. 不做保姆，做教练
4. 456道门是定价权

---

## 交付流程

1. **好二妹**：用 Open Design 按本框架生成 5 个 HTML 文件（纯 HTML+CSS，零外部依赖）
2. **好二妹**：交付到 `D:\OpenClaw\workspace\ai-cockpit-website/` 目录
3. **虎哥**：用浏览器逐页审查（截图验证）
4. **虎哥**：对比 index.html 检查视觉一致性（色彩/字体/间距/组件）
5. **虎哥**：发现问题→反馈好二妹修改
6. **虎哥**：全部验收通过 → `git add` → `git commit` → `git push origin gh-pages`
7. **虎哥**：通知吉哥上线完成

---

## 验收标准

- [ ] 导航栏与首页完全一致（Logo / 链接 / 高度 / 样式）
- [ ] Footer 与首页完全一致（5列网格 / 链接 / 社交图标）
- [ ] 背景色 `oklch(6%...)`，不是 `#0d1117`
- [ ] 品牌色琥珀金 `oklch(68% 0.18 60)`，没有紫色 `#5E6AD2`
- [ ] 卡片用 `.glass` 毛玻璃效果，不是纯色 `.panel`
- [ ] 按钮是胶囊形 `border-radius: 100px`，不是方块
- [ ] Hero 用 Unsplash 地球图背景（同首页），100vh 全屏
- [ ] 有 `#ambient` 背景光晕漂移效果
- [ ] 有 `.animate-in` 滚动淡入动画
- [ ] 移动端响应式（导航栏折叠 / 网格单列 / 间距缩小）
- [ ] 纯 HTML+CSS，零外部依赖（不挂 CDN）
- [ ] 所有图片用 https 链接或 data URI

---

*生成时间：2026-05-15 23:00*
*基准文件：index.html（已部署）*

---

## 附录：旧版 REFACTOR_GUIDE.md 说明

> `REFACTOR_GUIDE.md` 保留作为历史纪念（第一代重构指引，Linear 紫→琥珀金过渡方案）。
> 本框架 PRD 为最终执行版本，好二妹请以本文档为准。
