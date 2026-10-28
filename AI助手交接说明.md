# AI 助手交接说明

> **给下一个 AI 助手**：这是张鑫磊的个人主页项目。请先完整读完本文件，再动手改任何东西。
> 文件末尾的「待办清单」是你接手后要推进的事。

---

## 0. 三十秒速览

| 项目 | 值 |
|---|---|
| 线上网址 | **https://zhangxinleime.github.io/** |
| GitHub 仓库 | `ZhangXinleiME/ZhangXinleiME.github.io`（Public） |
| git 身份 | `ZhangXinleiME` / `602023150020@smail.nju.edu.cn` |
| 用途 | **2027 届博士毕业求职**，同时投高校教职与大厂算法岗 |
| 技术栈 | 纯静态，零依赖。`build.py`（Python 标准库）生成全部 HTML |
| 托管 | GitHub Pages，push 后约 **25 秒**自动上线 |

**最重要的一条规则：只改 `build.py`，永远不要直接编辑 `index.html` / `en.html` / `sitemap.xml` / `robots.txt`** —— 它们都是生成物，重新 build 会被覆盖。

---

## 1. 换电脑后的首次配置

项目文件通过 `git clone` 获得，但有三样东西留在旧电脑上，必须重做。

```bash
# 1) 拉取项目（推荐这种方式，而非 U 盘拷贝）
cd ~/Desktop
git clone https://github.com/ZhangXinleiME/ZhangXinleiME.github.io.git 个人主页
cd 个人主页

# 2) 配置 git 身份（三条，只需一次）
git config --global user.name "ZhangXinleiME"
git config --global user.email "602023150020@smail.nju.edu.cn"
git config --global credential.helper osxkeychain   # Windows 用 manager

# 3) 验证构建能跑（macOS 自带 python3 即可，无需 pip install）
python3 build.py
```

**第三样东西是 GitHub Token** —— 旧 Token 存在旧电脑的钥匙串里，不会跟着文件迁移。需要用户自己到
https://github.com/settings/tokens → Generate new token (classic) → **勾选最上面那个 `repo`** → 生成。

首次 `git push` 时：Username 填 `ZhangXinleiME`，Password 处**粘贴 Token**（不是登录密码）。之后钥匙串会记住。

> ⚠️ **凭据红线**：绝不接受用户提供的密码或 Token。GitHub 2021 年已禁用密码推送（给了也没用）；Token 一旦出现在对话记录即视为泄露，应立即提示用户吊销。此前已发生两次，均已拒绝使用。

---

## 2. 日常修改流程

```bash
# 1) 改 build.py 里对应的变量
# 2) 重新生成
python3 build.py
# 3) 推送上线
git add -A && git commit -m "更新了XXX" && git push
```

本地预览：`python3 -m http.server 8000` → 打开 http://localhost:8000

**改完务必自检**（这套检查已多次发现问题）：

```bash
python3 - <<'PY'
import re, json
for f in ['index.html', 'en.html']:
    s = open(f, encoding='utf-8').read()
    # 标签闭合
    bad = [t for t in ['section','div','p','span','strong','ul','li','h3','h4']
           if len(re.findall(r'<'+t+r'[ >]', s)) != len(re.findall(r'</'+t+'>', s))]
    # 加粗标记是否残留未转换
    stars = s.count('**')
    # JSON-LD 是否合法
    json.loads(re.search(r'ld\+json">(.*?)</script>', s, re.S).group(1))
    print(f, '闭合', bad or 'OK', '| ** 残留', stars, '| 章节', len(re.findall(r'<section id=', s)))
PY
```

期望结果：闭合 `OK`、`**` 残留 `0`、章节 `11`。

---

## 3. build.py 变量对照表

想改什么，去改哪个变量：

| 内容 | 变量 |
|---|---|
| 首屏标语 / 姓名 / 职位 / 简介 | `LABEL['zh'\|'en']` 里的 `tagline` / `person` / `role` / `intro` |
| 关于我两段 + 成果范围声明 | `about1` / `about2` / `stageNote` |
| 教育背景三张卡 + 学科归属说明 | `EDUCATION` / `LABEL[...]['eduNote']` |
| 研究与实习经历 | `WORK`（第 4 字段是 bullet 列表，不是单句） |
| 求职意向两栏 | `TRACKS` |
| 研究方向卡片 | `RESEARCH` |
| 近一年动态 | `NEWS` |
| 论文（已发表） | `PUBLICATIONS` |
| 在审稿件 | `UNDER_REVIEW` |
| 课题基金 / 专利软著 | `GRANTS` / `OUTPUTS` |
| 项目实践 | `PROJECTS` |
| 荣誉奖励 | `AWARDS` |
| 首屏四项统计数字 | `LABEL[...]['metrics']` |
| SEO 标题 / 描述 / 关键词 | `SEO_TITLE` / `SEO_DESC` / `SEO_KEYWORDS` |
| 域名（换自定义域名只改这一处） | `SITE` |

### 加粗机制

build.py 有三个渲染函数，**选错会出 bug**：

- `h(s)` — 纯 HTML 转义。标题、标签、属性用
- `r(s)` — 转义后把 `**文字**` 转成 `<strong class="hl">`。**正文段落用**
- `plain(s)` — 转义并剥离 `**`。**meta 标签必须用这个**，否则 SEO 描述里会露出星号

加粗原则：只加在**数字结果、核心论断、关键定位**上，一段最多 2–4 处。

> **坑**：别用 `r` / `h` / `plain` 当循环变量名。曾因 `for r in UNDER_REVIEW` 与渲染函数 `r()` 撞名报 `UnboundLocalError`。

---

## 4. 用户明确指定的约定 — 不要违反

这些是用户逐条提过要求的，改回去会被立刻发现。

### 定位

1. **不是纯学术简历**。站点定位「个人主页 / Personal Homepage」，不是「学术主页」。需同时服务高校与业界两类读者。
2. **必须声明成果范围是博士阶段**。用户担心论文数量被误读为全部学术生涯产出。已在「关于我」末尾用 `.stage-note` 说明（2023.09 入学起约三年）。
3. **在审稿件公开列出**，但放在 `UNDER_REVIEW` 独立分区，**不计入**已发表篇数统计。
4. **不提供简历 PDF 下载**，联系区写「可邮件索取」。

### 固定措辞

| 要写 | 不要写 |
|---|---|
| 腾讯小微 **Agent** 核心业务 | 腾讯小微核心业务 |
| 控制科学与智能工程系**培养** | 就读于控制科学与智能工程系 |
| 高校教职 讲师 / 研究员 / 助理教授 | ~~师资博士后~~（用户明确不要，别加回） |
| 业界 AI Agent / 大模型算法工程师 | 工业界 · 算法工程师 |
| **业界** | 工业界 |
| **近一年动态** | 最新动态 |
| **第二作者** | 合作署名 |
| 无 DOI 的论文显示「**待发表**」 | 出版链接待补充 |
| 人-机-AI 协同 / Human–Machine–AI Collaboration | ~~人机智能协同~~ |
| AI Agent **智能**决策 | AI Agent 决策 |

其他：
- 论文区必须强调「作者排名均为前二」
- 软著**不写**「第 N 著作权人」
- E-CARGO / CASA / C2 等会议必须标注「**国际学术会议**」
- 荣誉需含「校一等奖学金 · 若干次」
- **不写面向用户自己的解释性说明**（如「点击标签可筛选」「分区仅为便于对照」—— 这类已全部删除，别加回来）
- 章节导语统一用「**围绕…**」的第一人称研究视角，不要写成旁观式的「选取…展示…」
- **`TRACKS`（求职意向）全区禁止加粗**

### 用户原话，不得改写

以下两段是用户亲自给定的措辞，**一字不要动**：

**学科归属说明**（渲染在教育背景末尾 `.edu-note`）：
> 学科背景与交叉研究：我由南京大学控制科学与智能工程系培养，攻读管理科学与工程博士学位。研究融合管理科学、控制科学与人工智能，聚焦复杂组织与工程系统中的多主体协同、智能决策及资源优化，具有鲜明的学科交叉特色。因控制科学与工程博士点于 2025 年获批，而我于 2023 年入学，故学位归属管理科学与工程。

> 背景：原版写成「研究方向与培养过程均属控制领域」，用户指出「显得我只做了控制」。**必须强调学科交叉**。

**Track A 研究主线**：
> 聚焦于人工智能从能力增强工具向自主决策主体演进过程中，复杂智能系统的协同组织、任务配置与优化决策问题。以多智能体系统、角色协作理论与组合优化为基础，围绕「智能增强与能力建模 — 异构主体协同与任务优化 — 混合智能决策 — 自主智能体可信协作」形成持续深入的研究主线…

> **不要在这里列举期刊名**。用户明确说「没必要列举论文」，论文在下面成果区已有。

另外 Track A 第 2 条叫「**研究能力**」（不是「方法储备」），内容是**机制建模 / 智能算法 / 系统实现三层结构**。原版罗列优化方法，用户嫌「显得我只会优化」。不要退回罗列式写法。

---

## 5. 排版约定

- **全站 Times New Roman 优先**。CSS 变量 `--font-body` / `--font-head` / `--font-num` 均以 "Times New Roman" 开头，中文自动 fallback 到 PingFang SC。**禁止引入 Inter / Georgia 作为首选**。
- **照片要小**。`.portrait-frame` 已三轮缩小至 **186×238px**。用户持续要求更小，**不要放大**。
- **左上角 logo 是 `ZXL.`**（页脚 `footer-mark` 同步）。
- **首屏头像在左侧**，与标语、姓名、职位同行。不要改回右侧。
- **章节间距紧凑**：`.section` padding 已三轮压缩至 **46/50px**。用户两次说「模块之间空太多」，不要加回去。
- **所有章节统一用 `.container`**，禁止 `.container narrow`（该类已删除）。曾因混用导致章节左右不齐被用户指出。
- 正文基准 **16.5px**，`section-number` 标签 **15px**（用户都嫌过小）。
- **实习经历必须写细**，带具体数字和方法链路。用户嫌过「说的太空了」。

**章节顺序（11 个，不要随意调整）**：
`about → education → experience → positioning → research → news → publications → grants → projects → honors → contact`

---

## 6. SEO 与搜索引擎收录

目标：**让人搜「南京大学 张鑫磊」能找到这个主页**。

### 已完成的技术基础（build.py 自动生成，无需再管）

title 关键词 / description / canonical / hreflang / robots meta / Open Graph / Twitter Card / schema.org Person 结构化数据 / sitemap.xml / robots.txt / Google Search Console 验证标签。

### 关键约定

- **`GOOGLE_VERIFY` 常量不要删**。那是 Search Console 的所有权验证码，删掉会导致验证失效、GSC 停止提供数据。
- **字数红线**：中文 title ≤ 30 字、desc ≤ 80 字；英文 title ≤ 60 字符、desc ≤ 160 字符。超了会被搜索结果截断。改完务必查长度。
- **不要把 `L['intro']` 塞进 meta description**。它 300+ 字，会被截断。SEO 文案用独立的 `SEO_DESC`。
- og:image / twitter:image **必须是绝对 URL**，相对路径社交平台抓不到。
- 改完 JSON-LD 要验证 `json.loads()` 能过。

### 实体锚点 — 这些词不要删

人名 SEO 的做法不是堆关键词，而是与 Google **已索引的权威页面共享实体词**，让 Google 做实体消歧时把它们关联到同一个人。

已查明 Google 已索引这些含用户真名的页面：
- `grawww.nju.edu.cn` — 2025 江苏省研究生科研创新计划立项名单（KYCX25_0106）
- `sme.nju.edu.cn` — 2026 博士生「铸剑计划」推荐公示
- `sme.nju.edu.cn` — 第十届「学实」博士生学术论坛报道
- `jc2.org.cn` — 《指挥与控制学报》论文《虚拟现实多人多通道协同交互方法》

所以主页**必须保留**这些词：工程管理学院、智能装备新技术研究中心、导师周献中 / 孙宇祥、「具身智能 + 数字智能 + 人类智能下的跨模态协作研究」（省课题官方名，与名单一字不差）、指挥与控制学报。

JSON-LD 的 `affiliation` 是三条数组（校 / 院 / 研究中心），`alternateName` 含 `ZHANG Xinlei`（论文署名式写法）。

> **同名干扰说明**：南大哲学系有一位 2024 届硕士同名（已入职腾讯产品策划）。但他是哲学系 / 硕士 / 产品岗，实体特征完全不重叠，加「工程管理」「博士」「AI」任一限定词即可区分。不必担心。

详细操作手册见 `搜索引擎收录指南.md`。

---

## 7. 隐私红线

**绝对不能出现在站点或仓库里的内容**：
- 手机号
- 出生年月 / 年龄
- 政治面貌
- 身份证号
- 任何 Token / 密码

用户的原始简历 PDF 含这些信息。`.gitignore` 已忽略 `*.pdf` / `*.docx` 防止误传。

**`.workbuddy/` 必须保持忽略状态** —— 该目录存放 AI 工作记忆，含用户手机号，绝不能推到公开仓库。

推送前自检：

```bash
git ls-files | grep -i workbuddy    # 必须无输出
grep -rn "ghp_[A-Za-z0-9]\{20,\}" . --include="*.md" --include="*.py"   # 必须无输出
```

> `README.md` 里出现「出生年月、政治面貌」字样是**隐私声明文案**（说明站点不展示这些），不是真实数据，可以公开。

---

## 8. ⚠️ 待办清单（接手后要推进的事）

### 【高优先级】用户需要自己操作的两件事

这两件只有用户账号能做，AI 做不了。**如果用户说「搜不到我的主页」，先确认这两件做了没有**：

1. **Google Search Console 提交**
   - 左侧「**站点地图**」（中文界面把 Sitemaps 译成这个，用户曾找不到）→ 填 `sitemap.xml` → 提交
   - 左侧「**网址检查**」→ 粘 `https://zhangxinleime.github.io/` → 点「**请求编入索引**」
   - 英文页 `/en.html` 同样操作一次

2. **外链建设** —— 这比所有技术优化加起来都有效
   - **Google Scholar 个人资料 → Homepage 字段**填主页网址 ← 权重最高，论文已被索引，这一步能把「论文作者」和「主页」焊成同一实体
   - ORCID → Websites
   - GitHub Settings → Profile → Website
   - 仓库页 About 区 → Website
   - 邮件签名 + 简历 PDF 里写上网址

### 【待补充】内容类

- **IEEE SMC Magazine 那篇缺 DOI**（Group Role Assignment with Auxiliary Effects and Cooperation-Conflict Factors），页面现显示「待发表」。拿到 DOI 后填 `PUBLICATIONS` 对应条目的 `doi` 字段。
- **论文从「在审」转「已发表」时，需同步更新 4 处篇数**：
  1. `LABEL[...]['pubLead']` 导语里的「共 13 篇…第一作者 8 篇」
  2. `LABEL[...]['metrics']` 首屏统计
  3. build.py 里的 `<b id="pub-count">13</b>`
  4. `SEO_DESC` 里的「已发表论文 13 篇（第一作者 8 篇）」

### 【已结案 — 不要再提】

- 两项 2022 年软著（硕士阶段）与「本页成果均为博士阶段」声明的轻微冲突 —— 用户明确表示「不用管」，相关括注已删除。**不要再提这件事，也不要加回括注。**

---

## 9. 其他需要知道的坑

- **不要在用户正在运行某脚本时修改该脚本文件**。bash 按字节偏移边读边执行，改动会导致偏移错位、报 `syntax error`。已发生过一次。
- **仓库必须保持 Public**。改成 Private 会让 GitHub Pages 立刻下线（免费版不支持私有仓库）。此前旧仓库建成 Private 导致推送 403，排查了很久。
- **macOS 没有 `timeout` 命令**。想让 git 命令不卡在交互提示，用 `GIT_TERMINAL_PROMPT=0 git push`。
- 用户的 Token 已存入 macOS 钥匙串，**助手可以直接代为 push**（`GIT_TERMINAL_PROMPT=0 git push`），无需用户介入。换电脑后需重新存一次。
- GitHub Pages 实际部署比官方说的 1–2 分钟快，**实测约 25 秒**。验证线上时加缓存绕过参数：`curl "https://zhangxinleime.github.io/?cb=$RANDOM" -H "Cache-Control: no-cache"`。

---

## 10. 配套文档

| 文件 | 内容 |
|---|---|
| `README.md` | 项目结构、设计说明、隐私原则 |
| `换电脑与日常维护指南.md` | 面向用户的操作手册（换电脑步骤、报错处置） |
| `搜索引擎收录指南.md` | SEO 完整手册（三平台提交、外链优先级、域名绑定、收录预期） |
| **`AI助手交接说明.md`** | 本文件 — 给 AI 看的 |

---

## 附：关键事实速查

- 南京大学工程管理学院，管理科学与工程博士，控制科学与智能工程系培养，专业排名 1/24，预计 2027.06 毕业
- 导师：周献中 教授、孙宇祥 副教授
- 已发表 13 篇（一作 8 篇），一作在审 3 篇（IEEE TCYB / Advanced Engineering Informatics / AAAI）
- 两届 IEEE E-CARGO 国际学术会议最佳论文（2025 一等奖、2026 二等奖）
- 腾讯小微 Agent 核心业务大模型应用算法实习（2026.06 起）
- 博士生国自然申报获 2025 年南大 G 口校内遴选第 1
- 公开联系邮箱：ZhangShine@smail.nju.edu.cn（站点唯一联系方式）
