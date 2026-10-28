# 张鑫磊 · Xinlei Zhang — 个人主页

一个**无需安装依赖、可直接部署到 GitHub Pages** 的中英双语个人主页，面向**高校教职 + 业界算法岗双轨求职**场景设计。

线上地址：**https://zhangxinleime.github.io/**

> 📌 **AI 助手请先读 [`AI助手交接说明.md`](AI助手交接说明.md)** —— 内含全部内容约定、排版规则、隐私红线与待办清单。

## 页面结构（11 个章节）

| # | 章节 | 作用 |
|---|------|------|
| 01 | 关于我 | 个人定位 + **成果范围说明**（明确所有成果均为博士阶段产出） |
| 02 | 教育背景 | 三张卡片（博/硕/本）+ **学科背景与交叉研究说明** |
| 03 | 研究与实习经历 | 全宽时间轴，每段含量化结果 |
| 04 | 求职意向 | **双轨板块**：Track A 高校教职 / Track B 业界 AI Agent 岗 |
| 05 | 研究方向 | 4 个方向卡片 |
| 06 | 近一年动态 | 10 条博士阶段里程碑 |
| 07 | 论文成果 | 13 篇已发表（可筛选）+ **3 篇一作在审**（独立分区，不计入已发表统计） |
| 08 | 科研课题与知识产权 | 课题/基金 + 专利/软著/专著 |
| 09 | 项目实践 | 代表性项目（线上业务算法 / 工程决策 / 独立产品） |
| 10 | 荣誉奖励 | 两列栅格 |
| 11 | 联系我 | 公开邮箱；简历邮件索取 |

## 关键内容约定

- **成果范围声明**：`关于我` 末尾有一段 `stage-note` 高亮说明，明确所有论文、课题、奖励均为 2023.09 进入博士阶段后约三年内的产出，避免被误读为全部学术生涯的总量。
- **术语统一**：全站统一使用 **人-机-AI 协同 / Human–Machine–AI Collaboration**，不再使用"人机智能协同"。
- **在审稿件**：`UNDER_REVIEW` 独立于 `PUBLICATIONS` 渲染，带"在审"状态标签，**不计入**页面顶部与筛选器的已发表篇数。
- **站点定位中性化**：标题为"个人主页 / Personal Homepage"，不再是"学术主页"，避免对业界读者偏学术。
- **隐私**：不展示手机号、出生年月、政治面貌；不提供简历 PDF 下载，联系区写明可邮件索取。

## 本地预览

```bash
python -m http.server 8000
```

然后访问 <http://localhost:8000/>。也可直接双击 `index.html`。

## 发布到 GitHub Pages

1. 创建**公开仓库**，推荐命名为 `你的GitHub用户名.github.io`。
2. 上传本文件夹内**全部文件**（`index.html`、`en.html`、`style.css`、`script.js`、`assets/`），不要只上传 `index.html`。
3. **Settings → Pages** → Build and deployment 选 **Deploy from a branch**，分支 `main`，目录 `/(root)`，保存。
4. 访问地址通常为 `https://你的GitHub用户名.github.io/`。

网站使用相对路径，普通项目仓库（带 `/仓库名/`）同样可部署。

## 如何修改内容

**所有内容都在 `build.py` 里，只依赖 Python 标准库。** 改完运行 `python build.py` 重新生成两个 HTML。

| 变量 | 内容 |
|------|------|
| `PUBLICATIONS` | 已发表论文（标题、期刊、年份、分区、作者位次、DOI、中英文简介） |
| `UNDER_REVIEW` | 在审稿件（含状态文案，如"在审 · 第 2 轮"） |
| `NEWS` | 近一年动态 |
| `RESEARCH` | 4 个研究方向卡片 |
| `TRACKS` | **双轨求职板块**，每条是 `(眼标, 标题, 概述, [(标签, 正文), ...])` |
| `PROJECTS` | 项目实践卡片 |
| `GRANTS` | 科研课题与基金（含主持/参与/申报角色） |
| `OUTPUTS` | 专利、软件著作权、专著 |
| `WORK` / `EDUCATION` / `AWARDS` | 经历、教育、荣誉 |
| `KEYWORDS` / `HERO_TAGS` | 关键词标签云 / 首屏标签 |
| `LABEL['zh']` / `LABEL['en']` | 全站所有文案，包括章节标题、导航、声明段落 |
| `EMAIL` | 公开邮箱 |

> 直接编辑 HTML 也可以，但下次运行 `build.py` 会被覆盖。

### 论文发表后如何从"在审"转入"已发表"

1. 从 `UNDER_REVIEW` 删除该条。
2. 在 `PUBLICATIONS` 按格式新增一条，补上年份与 DOI。
3. 把 `LABEL` 里 `pubLead` / `metrics` / `pubCount` 中出现的篇数（13、8）与 `build.py` 中 `<b id="pub-count">13</b>` 一并更新。
4. 在 `NEWS` 顶部加一条动态。

## 待你确认的事项

- `Group Role Assignment with Auxiliary Effects and Cooperation-Conflict Factors`（IEEE SMC Magazine）**仍缺 DOI**，页面显示"出版链接待补充"。拿到后填入 `PUBLICATIONS` 第 4 条的 `doi` 字段。
- 期刊分区沿用你简历中的标准，不代表实时 JCR / 中科院分区，发布前请复核。
- 在审稿件标题已按你的要求公开。若某篇转为"已接收"或遇到撞题顾虑，可随时从 `UNDER_REVIEW` 调整。
- `assets/portrait.jpg` 来自你的简历照片。

## 文件结构

```text
Xinlei_Zhang_Academic_Homepage_GitHub_Pages/
├── index.html             中文首页（由 build.py 生成）
├── en.html                English version（由 build.py 生成）
├── style.css              完整样式与响应式布局
├── script.js              论文筛选、导航高亮、复制邮箱等交互
├── build.py               内容源 + 双语生成脚本
├── assets/
│   ├── portrait.jpg       照片
│   └── favicon.svg        网站图标
└── README.md
```
