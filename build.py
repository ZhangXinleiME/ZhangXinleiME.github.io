#!/usr/bin/env python3
"""Build the bilingual static personal homepage. Python standard library only.
Edit the content blocks below, then run:
    python build.py
"""
from pathlib import Path
from html import escape
import re

ROOT=Path(__file__).resolve().parent

def h(s): return escape(str(s), quote=True)

def r(s):
    """Escape, then convert **bold** markers into <strong> emphasis.
    Use in body copy where selected phrases should stand out."""
    return re.sub(r'\*\*(.+?)\*\*', r'<strong class="hl">\1</strong>', h(s))

def plain(s):
    """Escape and drop ** markers — for meta tags and attributes (plain text only)."""
    return h(str(s).replace('**',''))
def a(url, label, cls='', new=True):
    if not url:return ''
    props=' target="_blank" rel="noopener noreferrer"' if new and not url.startswith('#') and not url.startswith('mailto:') else ''
    return f'<a class="{cls}" href="{h(url)}"{props}>{label}</a>'

DOI='https://doi.org/'

# ---------------------------------------------------------------- publications
# (title, venue, year, rating_zh, rating_en, author_role, doi, desc_zh, desc_en)
PUBLICATIONS=[
    ('Staff Competency Assessment and Task Allocation Methods Considering AI Augmentation: A Study Based on the E-CARGO Model','IEEE Transactions on Systems, Man, and Cybernetics: Systems',2025,'SCI 一区 TOP','SCI Q1 · Top-tier','first','10.1109/TSMC.2025.3599525',
     '面向 AI 由工具向能力增强型助手演进后的任务协同问题，构建多维能力建模与任务配置框架，刻画 AI 介入对人员能力与资源配置的影响。','Builds a competency-modeling and task-allocation framework that captures how AI augmentation reshapes individual capability and resource configuration.'),
    ('Role-Based Human-Machine Collaboration Task-Allocation Strategy in Multiagent Environment','IEEE Transactions on Human-Machine Systems',2025,'SCI 二区','SCI Q2','first','10.1109/THMS.2025.3591603',
     '统一刻画异构主体的独立能力与协作能力，构建角色分配与任务优化方法，并针对 NP-hard 特性设计多层求解策略。','Jointly models independent and collaborative capabilities of heterogeneous agents, with a multi-layer solver for the NP-hard assignment problem.'),
    ('An Emergency Rescue Model Considering Dynamic Rendezvous and Environmental Interference','IEEE Transactions on Computational Social Systems',2026,'SCI 二区','SCI Q2','first','10.1109/TCSS.2026.3724942',
     '将环境状态、主体能力、任务需求与时空约束统一纳入离散路网决策空间，研究动态任务规划与自适应资源配置。','Maps environment states, agent capabilities, and spatio-temporal constraints into a unified decision space for dynamic planning and adaptive allocation.'),
    ('Group Role Assignment with Auxiliary Effects and Cooperation-Conflict Factors','IEEE Systems, Man, and Cybernetics Magazine',2026,'SCI 三区','SCI Q3','first',None,
     '研究辅助能力、合作收益与冲突因素共同作用下的群体角色优化分配。','Studies group role assignment under auxiliary capabilities, cooperation gains, and conflict effects.'),
    ('虚拟现实多人多通道协同交互方法','《指挥与控制学报》',2024,'北大核心 · CSCD','Chinese Core · CSCD','first','10.3969/j.issn.2096-0204.2024.03.0319',
     '融合手势、语音和眼动交互，实现异地多用户实时协作与虚拟沙盘交互；获中国指挥与控制学会官方号首页推荐。','Fuses gesture, speech, and gaze interaction for real-time remote multi-user collaboration in virtual reality.'),
    ('N-Sand Table: A Multi-User Interactive Virtual Sand Table Based on NeRF Technology','Computer Animation and Social Agents (CASA 2024) · 国际学术会议',2025,'CCF C · EI · Oral','CCF C · EI · Oral','first','10.1007/978-981-96-2684-7_3',
     '结合 NeRF 场景重建与多用户协作，研发可交互的三维虚拟沙盘。','Combines NeRF scene reconstruction with multi-user interaction for a collaborative 3D virtual sand table.'),
    ('Group Role Assignment Considering Auxiliary Effects in Human-Machine Teams','IEEE E-CARGO 2025 国际学术会议（1st International Symposium on E-CARGO and Applications）',2025,'EI · 最佳论文一等奖','EI · Best Paper Award (First Prize)','first','10.1109/E-CARGO65996.2025.11139227',
     '建立考虑单向辅助效应的群体角色分配模型，获国际学术会议最佳论文一等奖。','Introduces auxiliary-effect-aware group role assignment; received the Best Paper Award (First Prize).'),
    ('Supervision-Aware Group Role Assignment in Human-Machine-AI Hybrid Environments','IEEE E-CARGO 2026 国际学术会议（2nd International Symposium on E-CARGO and Applications）',2026,'EI · 最佳论文二等奖','EI · Best Paper Award (Second Prize)','first','10.1109/E-CARGO70110.2026.11670812',
     '联合优化任务执行与监督资源，实现人—机器—AI 混合团队的效能与可靠性平衡；获国际学术会议最佳论文二等奖。','Jointly optimizes execution and supervision resources in human–machine–AI hybrid teams; Best Paper Award (Second Prize).'),
    ('Three-way Decision-guided Hierarchical Reinforcement Learning for High-frequency Trading','Information Sciences',2026,'SCI 一区 TOP','SCI Q1 · Top-tier','second','10.1016/j.ins.2026.123880',
     '融合三支决策的不确定性认知与分层强化学习，分解高噪声、非平稳环境下的智能体序列决策过程。','Integrates three-way decision uncertainty modeling with hierarchical RL for sequential decisions in noisy, non-stationary environments.'),
    ('Performance-Balanced Task Allocation in Leader-Member Teams: A Group Multirole Assignment Approach Using E-CARGO','IEEE Transactions on Computational Social Systems',2026,'SCI 二区','SCI Q2','second','10.1109/TCSS.2026.3668139',
     '通过差异化能力评价与绩效均衡目标，优化领导者—成员型团队的多角色任务配置。','Improves multi-role assignment in leader–member teams by balancing overall performance and task-level fairness.'),
    ('An Integrated Model of Crowd Evacuation Considering the Coupling Effects of Temperature, Density, and Fall Risk','Physica A: Statistical Mechanics and its Applications',2025,'SCI 二区','SCI Q2','second','10.1016/j.physa.2025.131169',
     '建立耦合温度、密度和跌倒风险的人群疏散仿真模型，为应急疏散规划提供依据。','Models coupled temperature, crowd density, and fall risk to inform emergency evacuation planning.'),
    ('面向兵棋战场态势的智能辅助决策系统研究','《火力与指挥控制》',2025,'北大核心 · CSCD','Chinese Core · CSCD','second','10.3969/j.issn.1002-0640.2025.12.019',
     '集成目标威胁评估与改进 A* 路径规划，构建复杂态势下的智能辅助决策系统。','Combines threat assessment and improved A* path planning in an intelligent decision-support system.'),
    ('Enhanced Whale Optimization Algorithm and Its Application in 3D Flight Path Planning for Unmanned Aerial Vehicles','2024 12th China Conference on Command and Control (C2 2024) · 国际学术会议',2024,'EI · Springer','EI · Springer','second','10.1007/978-981-97-7774-7_11',
     '改进鲸鱼优化算法的初始化和搜索机制，用于复杂约束下的无人机三维航迹规划。','Enhances whale optimization for constrained three-dimensional UAV flight-path planning.'),
]

# (title, venue, status_zh, status_en, rating_zh, rating_en, desc_zh, desc_en)
UNDER_REVIEW=[
    ('Multi-Space Group Role Assignment for Human-Machine-AI Collaboration in Cyber-Physical Hybrid Teams','IEEE Transactions on Cybernetics',
     '在审 · 第 2 轮','Under review · 2nd round','SCI 一区 TOP','SCI Q1 · Top-tier',
     '面向人类、物理机器与自主 AI 共同参与复杂任务的混合智能系统，构建跨物理—信息空间的异构主体角色配置框架，研究能力耦合、跨空间协作与整体效能优化。',
     'Proposes a cross physical–cyber role configuration framework for hybrid teams of humans, physical machines, and autonomous AI agents.'),
    ('Governance-Constrained Role Configuration for Human-Machine-AI Collaboration in Cyber-Physical Engineering Systems','Advanced Engineering Informatics',
     '在审','Under review','SCI 一区 TOP','SCI Q1 · Top-tier',
     '将角色配置、监督关系与治理约束纳入统一决策框架，研究不同自主程度 AI 主体的权限边界与监督机制，探索自主性、系统效能与可控性之间的平衡。',
     'Unifies role configuration, supervision relations, and governance constraints to balance agent autonomy, system performance, and controllability.'),
    ('Evaluating Online LLM Control in Multi-Echelon Supply Chains: Role-Assignment Sensitivity, Prompt Effects, and Residual Coordination Gaps','AAAI Conference on Artificial Intelligence',
     '在审','Under review','CCF A 类会议','CCF A Conference',
     '面向 LLM 作为自主 Agent 参与多级供应链在线控制的新场景，系统比较模型能力、角色配置与 Prompt 策略对动态决策绩效的影响，分析其残余协调缺口。',
     'Systematically evaluates how model capability, role assignment, and prompting affect online LLM control in multi-echelon supply chains.'),
]

NEWS={
'zh':[
('2026.08','一作论文发表于 IEEE Transactions on Computational Social Systems，研究动态会合与环境干扰下的应急救援优化。'),
('2026.07','一作论文获 IEEE E-CARGO 2026 国际学术会议最佳论文二等奖，研究人—机器—AI 混合团队中的监督感知角色分配。'),
('2026.07','合作论文发表于 Information Sciences（SCI 一区 TOP），研究三支决策引导的分层强化学习。'),
('2026.06','进入腾讯小微 Agent 核心业务，从事大模型应用算法实践（RAG 评测、智能体评测与模型后训练）。'),
('2026.03','启动视频智能体与自动化内容生成实践，两条链路实现每日自动运行。'),
('2026.01','加入南京大学智能装备新技术研究中心，负责海冰区航路规划与应急调度算法研发。'),
('2025.09','一作论文发表于 IEEE Transactions on Systems, Man, and Cybernetics: Systems（SCI 一区 TOP）。'),
('2025.08','一作论文发表于 IEEE Transactions on Human-Machine Systems。'),
('2025.07','一作论文获 IEEE E-CARGO 2025 国际学术会议最佳论文一等奖。'),
('2025.06','博士生国家自然科学基金申报获 2025 年南京大学 G 口校内遴选第 1。'),
],
'en':[
('Aug 2026','First-authored paper published in IEEE Transactions on Computational Social Systems on emergency rescue optimization.'),
('Jul 2026','Received Best Paper Award (Second Prize) at the IEEE E-CARGO 2026 international symposium.'),
('Jul 2026','Co-authored paper published in Information Sciences (SCI Q1, top-tier) on three-way decision-guided hierarchical RL.'),
('Jun 2026','Joined the Tencent Xiaowei Agent core business as an LLM application algorithm intern.'),
('Mar 2026','Launched a video-agent and automated content generation practice with two daily-running pipelines.'),
('Jan 2026','Joined the NJU Research Center for Novel Technology of Intelligent Equipment as an algorithm researcher.'),
('Sep 2025','First-authored paper published in IEEE Transactions on Systems, Man, and Cybernetics: Systems (SCI Q1, top-tier).'),
('Aug 2025','First-authored paper published in IEEE Transactions on Human-Machine Systems.'),
('Jul 2025','Received Best Paper Award (First Prize) at the IEEE E-CARGO 2025 international symposium.'),
('Jun 2025','NSFC Young Student Basic Research proposal ranked 1st in the NJU internal selection.'),
]}

RESEARCH={
'zh':[
('01','人-机-AI 协同与能力建模','Human–Machine–AI Collaboration','刻画 AI 介入对人员能力结构与任务绩效的影响，研究能力动态变化下的协同决策与任务匹配。','HUMAN × MACHINE × AI'),
('02','异构主体角色配置与任务优化','Role Assignment & Optimization','面向人、物理机器与不同自主程度 AI 主体，研究群体角色分配、任务规划与联合资源优化。','MULTI-AGENT'),
('03','LLM / AI Agent 决策与评测','LLM Agents & Evaluation','研究智能体任务规划、工具调用、RAG、能力评测、后训练与可信协作机制。','AGENT SYSTEMS'),
('04','复杂动态环境中的智能决策','Dynamic Decision & Learning','研究动态约束下的任务调度、路径规划、组合优化与强化学习决策方法。','OPTIMIZATION'),
],
'en':[
('01','Human–Machine–AI Collaboration','Capability Modeling','Characterizing how AI augmentation reshapes human capability and task performance, and how teams adapt under capability dynamics.','HUMAN × MACHINE × AI'),
('02','Role Assignment & Task Optimization','Heterogeneous Agents','Group role assignment, task planning, and joint resource optimization across humans, machines, and AI agents.','MULTI-AGENT'),
('03','LLM / AI Agent Decision & Evaluation','Reliable Agent Systems','Agentic planning, tool use, RAG, capability evaluation, post-training, and trustworthy collaboration.','AGENT SYSTEMS'),
('04','Decision Making in Dynamic Systems','Optimization & Learning','Scheduling, routing, combinatorial optimization, and reinforcement learning under dynamic constraints.','OPTIMIZATION'),
]}

# Dual-track positioning: (eyebrow, title, summary, [(label, text), ...])
TRACKS={
'zh':[
('TRACK A / ACADEMIA','高校教职 讲师 / 研究员 / 助理教授',
 '匹配控制科学与工程、管理科学与工程及人工智能交叉方向，具备独立开题能力、基金申报经历与完整教学准备。',
 [('研究主线','聚焦于人工智能从能力增强工具向自主决策主体演进过程中，复杂智能系统的协同组织、任务配置与优化决策问题。以多智能体系统、角色协作理论与组合优化为基础，围绕「智能增强与能力建模 — 异构主体协同与任务优化 — 混合智能决策 — 自主智能体可信协作」形成持续深入的研究主线，问题明确、方法自洽且尚有大量未解问题，可支撑入职后独立开题与长期产出。'),
  ('研究能力','在机制建模、智能算法与系统实现三个层面均有积累：机制层面建立主体能力、协作关系与任务结构的可计算表征；算法层面覆盖多智能体决策、强化学习、组合优化与分层求解；系统层面具备大模型评测、后训练与 Agent 工程化能力。既能把实际问题抽象为科学问题，也能把模型实现为可验证的系统。'),
  ('基金基础','独立完成博士生国家自然科学基金申报，获 2025 年南京大学 G 口校内遴选第 1；主持 3 项省级项目 + 1 项校级培优项目，联合主持基础加强项目（唯一学生主持人）。'),
  ('教学准备','方法类课程：强化学习与智能决策、运筹学与智能优化、多智能体系统与任务规划、复杂系统分析与优化；交叉课程：人机协同与智能系统、大模型与 AI Agent 应用。'),
  ('育人实践','具备创新创业与学科竞赛获奖经历，可指导大创、科研创新项目及高水平学科竞赛。')]),
('TRACK B / INDUSTRY','业界 AI Agent / 大模型算法工程师',
 '目标 Agent 算法、大模型应用与智能决策岗位，具备从线上问题发现到后训练验证的完整算法闭环经验。',
 [('Agent 方向','Agent Workflow 编排、Tool Calling、智能体多维评测体系、LLM Judge 校准、在线难例挖掘与失败模式归因。'),
  ('大模型方向','RAG 多路召回与链路级错误归因、SFT/DPO 数据建设、隔离回归验证、生成安全治理与后训练效果评估。'),
  ('智能决策方向','任务分配、组合优化、混合整数规划、动态调度、路径规划、启发式与分层求解、强化学习。'),
  ('线上结果','人机评测一致率 71.0% → 94.6%；后训练后相关性 +12.15 pct、正确性 +8.00 pct；安全风险率 1.12% → 0.11%；生成安全专项通过率 70% → 80%。'),
  ('工程落地','参与 10+ 科研与工程课题、交付 20+ 软件系统与算法模块；核心参与的 AI 产品累计注册用户 1 万+、周调用 5,000+。')]),
],
'en':[
('TRACK A / ACADEMIA','Faculty — Lecturer / Research Fellow / Assistant Professor',
 'Targeting control science & engineering, management science & engineering, and AI-interdisciplinary departments, with proven ability to define independent research directions, grant experience, and full teaching preparation.',
 [('Research agenda','My work addresses collaborative organization, task configuration, and optimal decision making in complex intelligent systems as AI evolves from a capability-augmenting tool into an autonomous decision-making agent. Grounded in multi-agent systems, role-based collaboration theory, and combinatorial optimization, it follows a sustained line: intelligence augmentation and capability modeling — heterogeneous agent collaboration and task optimization — hybrid intelligence decision making — trustworthy collaboration with autonomous agents. The agenda is well-posed, methodologically coherent, and far from exhausted — a solid basis for an independent research program.'),
  ('Research capability','Depth across three levels — mechanism, algorithm, and system. At the mechanism level, building computable representations of agent capability, collaboration relations, and task structure; at the algorithm level, multi-agent decision making, reinforcement learning, combinatorial optimization, and hierarchical solvers; at the system level, LLM evaluation, post-training, and agent engineering. I can both abstract practical problems into scientific ones and realize models as verifiable systems.'),
  ('Grant experience','Independently prepared an NSFC Young Student Basic Research proposal, ranked 1st in the 2025 NJU internal selection; led 3 provincial projects and 1 university-level program, and co-led a national foundation-strengthening project as its sole student PI.'),
  ('Teaching readiness','Methods courses: Reinforcement Learning & Intelligent Decision Making, Operations Research & Intelligent Optimization, Multi-Agent Systems & Task Planning, Complex Systems Analysis. Interdisciplinary courses: Human–Machine Collaboration, LLM & AI Agent Applications.'),
  ('Student mentoring','Award-winning experience in innovation/entrepreneurship and academic competitions; prepared to mentor undergraduate research and competition teams.')]),
('TRACK B / INDUSTRY','Industry — AI Agent / LLM Algorithm Engineer',
 'Targeting agent algorithms, applied LLM systems, and intelligent decision roles, with end-to-end experience from online problem discovery to post-training validation.',
 [('Agent systems','Agent workflow orchestration, tool calling, multi-dimensional agent evaluation, LLM-as-a-Judge calibration, online hard-case mining, and failure-mode attribution.'),
  ('LLM systems','Multi-route RAG with chain-level error attribution, SFT/DPO data construction, isolated regression validation, generation-safety governance, and post-training evaluation.'),
  ('Decision optimization','Task allocation, combinatorial optimization, mixed-integer programming, dynamic scheduling, routing, heuristic and hierarchical solvers, reinforcement learning.'),
  ('Production results','Human–judge agreement 71.0% → 94.6%; post-training relevance +12.15 pct and correctness +8.00 pct; safety risk rate 1.12% → 0.11%; generation-safety pass rate 70% → 80%.'),
  ('Engineering delivery','Contributed to 10+ research and engineering projects, delivering 20+ software systems and algorithm modules; co-built an AI product with 10,000+ registered users and 5,000+ weekly calls.')]),
]}

PROJECTS={
'zh':[
('01','腾讯小微 Agent · 智能体多维评测与模型后训练','2026','将智能体线上效果拆解为相关性、正确性、时效性与安全合规等维度，设计上线内网多人标注平台沉淀人工 Gold Case，并围绕不一致样本持续校准 LLM Judge。','人机评测一致率 71.0% → 94.6%','评测体系 / LLM Judge / SFT','RAG & AGENTS'),
('02','腾讯小微 Agent · 经验库 RAG 评测与偏好优化','2026','围绕多路召回 → RRF 融合 → LLM Filter 建立链路级错误归因，从大规模线上流量挖掘真实 Bad Case；构建高风险样本挖掘流程并支撑全参数 DPO 后训练。','约 6,000 条真实分布回归集 · 606 组偏好数据','RAG / DPO / 在线回归','LLM SYSTEMS'),
('03','万卷公文 · 智能公文写作平台','2024 — 至今','基于 LLM、RAG 与 Agent Harness 构建流程型智能体系统，统一编排素材解析、知识检索、初稿撰写、润色、校对与格式输出；完成公司注册并入驻南京大学产业园区。','注册用户 1 万+ · 周调用 5,000+ · 付费占比近 10%','LLM / RAG / 产品落地','AI PRODUCT'),
('04','海冰区船舶航路规划与多任务调度','2026','将海冰浓度、天气、危险区域与任务优先级抽象为约束路径规划—任务配置联合优化问题，设计启发式求解算法并封装 API 接入项目软件。','百级任务 · 千级节点 · 典型场景 4 秒内出方案','组合优化 / 路径规划 / 调度','OPTIMIZATION'),
('05','智能工厂应急调度与动态重规划','2026','构建融合能力差异、角色适配、任务优先级、动态会合与环境干扰的应急调度模型，实现资源与环境变化下的任务-资源动态重构。','算法模块以 API 形式集成至应急管理软件','多智能体 / 混合整数优化','DECISION MAKING'),
('06','视频智能体与自动化内容生成','2026 — 至今','设计 Agent Workflow 统一编排定时触发、信息采集、内容理解、任务规划、Tool Calling、规则审核与视频生成，实现任务状态传递与异常重试。','新闻解读与量化持仓分析两条链路每日自动运行','Agent Workflow / Tool Calling','AGENT WORKFLOW'),
],
'en':[
('01','Tencent Xiaowei Agent · Agent Evaluation & Post-Training','2026','Decomposed online agent quality into relevance, correctness, timeliness, and safety; shipped an internal multi-annotator platform for gold cases and iteratively calibrated the LLM judge.','Human–judge agreement 71.0% → 94.6%','Evaluation / LLM Judge / SFT','RAG & AGENTS'),
('02','Tencent Xiaowei Agent · RAG Evaluation & Preference Optimization','2026','Built chain-level error attribution across multi-route retrieval, RRF fusion, and LLM filtering; mined real bad cases from large-scale production traffic to support full-parameter DPO.','~6,000 production-distribution regression cases · 606 preference pairs','RAG / DPO / Online Regression','LLM SYSTEMS'),
('03','Wanjuan · AI Document Writing Platform','2024 — Present','Built a workflow-style agent system with LLMs, RAG, and an agent harness, orchestrating material parsing, retrieval, drafting, polishing, proofreading, and formatted output.','10,000+ registered users · 5,000+ weekly calls · ~10% paid','LLM / RAG / Product','AI PRODUCT'),
('04','Sea-Ice Route Planning & Multi-Task Scheduling','2026','Abstracted sea-ice concentration, weather, hazard zones, and task priorities into a joint constrained-routing and task-allocation problem; delivered a heuristic solver behind a project API.','Hundreds of tasks · thousands of nodes · <4s per scenario','Optimization / Routing / Scheduling','OPTIMIZATION'),
('05','Smart-Factory Emergency Scheduling & Replanning','2026','Modeled emergency scheduling with capability differences, role fitness, task priority, dynamic rendezvous, and environmental interference for online task–resource reconfiguration.','Integrated into emergency-management software via API','Multi-Agent / MIP','DECISION MAKING'),
('06','Video Agents & Automated Content Generation','2026 — Present','Designed an agent workflow orchestrating scheduled triggers, information gathering, content understanding, planning, tool calling, rule-based review, and video generation.','Two daily-running pipelines: news analysis and portfolio review','Agent Workflow / Tool Calling','AGENT WORKFLOW'),
]}

# (role, title, note)
GRANTS={
'zh':[
('主持','江苏省研究生科研创新项目（省级）','具身智能 + 数字智能 + 人类智能下的跨模态协作研究'),
('主持','江苏省科研创新-实践创新项目（省级）','基于虚实融合的科研教育交互平台'),
('主持','江苏省大学生优秀创业项目（省级）','基于新媒体的线上课堂服务平台'),
('联合主持','基础加强项目（导师主导 · 唯一学生主持人）','面向陆域无人系统的多“基”协同智能决策技术'),
('主持','南京大学培优项目','人、机、AI 视角下的多“基”智能体群智协同与优化调度研究'),
('申报','国家自然科学基金青年学生基础研究项目（博士生国自然）','面向“人工智能+”行动的多“基”智能体群智协同与优化调度研究 · 2025 年南京大学 G 口校内遴选第 1'),
('参与','国家自然科学基金、装备预先研究及共用技术项目等','承担需求抽象、技术路线设计、模型与算法方案论证及研发工作'),
],
'en':[
('Principal Investigator','Jiangsu Postgraduate Research Innovation Program (provincial)','Cross-modal collaboration under embodied, digital, and human intelligence'),
('Principal Investigator','Jiangsu Research & Practice Innovation Program (provincial)','Virtual–real fusion platform for research-oriented education'),
('Principal Investigator','Jiangsu Outstanding Student Entrepreneurship Program (provincial)','New-media-based online classroom service platform'),
('Co-PI','National Foundation-Strengthening Project (advisor-led · sole student PI)','Multi-base collaborative intelligent decision-making for ground unmanned systems'),
('Principal Investigator','NJU Excellence Cultivation Program','Multi-base swarm-intelligence collaboration and optimal scheduling from human–machine–AI perspectives'),
('Proposal','NSFC Young Student Basic Research Project','Multi-base swarm-intelligence collaboration and scheduling for the "AI Plus" initiative · ranked 1st in the 2025 NJU internal selection'),
('Participant','NSFC projects, equipment pre-research and shared-technology programs','Requirement abstraction, technical-route design, model/algorithm validation, and development'),
]}

# (kind, title, note)
OUTPUTS={
'zh':[
('发明专利 · 在审','一种基于多源多模态数据融合的态势识别方法及系统','公开号 CN121723081A'),
('发明专利 · 在审','一种基于小样本学习的兵棋推演作战意图识别方法及设备','公开号 CN121705583A'),
('软件著作权','鑫聚—低空冲突检测算法软件 V1.0','登记号 2024SR1257777'),
('软件著作权','多装备智能地面侦察算法软件 V1.0','登记号 2024SR1649446'),
('软件著作权','智胜—公野混合路径规划算法软件','登记号 2022SR0341975'),
('软件著作权','面向一人多机的多通道控制软件系统','登记号 2022SR0303777'),
('专著 · 参编','《兵棋推演原理与应用》','哈尔滨工程大学出版社，2023.09 · 参与兵棋推演与智能辅助决策相关章节，约 2.5 万字'),
],
'en':[
('Patent · pending','Situation recognition method and system based on multi-source multimodal data fusion','Publication no. CN121723081A'),
('Patent · pending','Few-shot-learning-based intent recognition method and device for wargaming','Publication no. CN121705583A'),
('Software copyright','Xinju — Low-Altitude Conflict Detection Algorithm Software V1.0','Reg. 2024SR1257777'),
('Software copyright','Multi-Equipment Intelligent Ground Reconnaissance Algorithm Software V1.0','Reg. 2024SR1649446'),
('Software copyright','Zhisheng — Road–Offroad Hybrid Path Planning Algorithm Software','Reg. 2022SR0341975'),
('Software copyright','Multi-Channel Control System for One-Operator Multi-Robot Teams','Reg. 2022SR0303777'),
('Book · contributing author','Principles and Applications of Wargaming','Harbin Engineering University Press, Sep 2023 · ~25,000 words on wargaming and intelligent decision support'),
]}

# (dates, org, role, [bullet, ...])
WORK={
'zh':[
('2026.06 — 至今','腾讯 · 小微 Agent 核心业务','大模型应用算法实习生',[
 '**经验库 RAG 评测与线上回归体系：**针对合成评测集与真实线上流量的分布偏移，围绕「多路召回 → RRF 融合 → LLM Filter」建立链路级错误归因，从大规模线上流量挖掘真实 Bad Case 并补充长尾场景，**将约 300 条合成数据扩展为约 6,000 条符合线上分布的回归集**，并沉淀经验新增/更新后的增量评测流程。',
 '**智能体多维评测与 LLM Judge：**将智能体线上效果拆解为相关性、正确性、时效性与安全合规等核心维度，设计并上线内网多人标注平台沉淀人工 Gold Case；围绕 Judge 与人工判断不一致的典型样本开展误差分析与迭代，**将人机一致率由 71.0% 提升至 94.6%**，支撑版本迭代的规模化自动评测。',
 '**生成安全与偏好数据闭环：****回溯近 20 天约 200 万条线上流量**，构建「快速筛选 → 大模型判别 → 人工复核」的高风险样本挖掘流程；结合教师模型改写、拒绝采样与人工质检构造 **606 组偏好数据**，支持全参数 DPO 后训练，**专项通过率由 70% 提升至 80%**。',
 '**SFT 数据建设与隔离回归：**针对角色错位、缺少可靠信息源问询等失败模式，从真实 Bad Case 反向归纳并构造约 1,000 条 SFT 数据，建立训练数据与回归样本隔离的前后对比验证流程；**线上验证相关性提升 12.15 pct、正确性提升 8.00 pct，安全风险率由 1.12% 降至 0.11%**。']),
('2026.01 — 2026.05','南京大学智能装备新技术研究中心','算法研究员',[
 '**海冰区船舶航路规划与多任务调度：**将海冰浓度、天气、危险区域与任务优先级等多源信息抽象为约束路径规划—任务配置联合优化问题；设计启发式求解算法，**支持百级任务、千级节点/实体规模的并发规划，典型场景 4 秒内生成方案**，并封装 API 接入项目软件。',
 '**智能工厂应急调度与动态重规划：**构建融合能力差异、角色适配、任务优先级、动态会合与环境干扰的应急调度模型；设计多角色任务配置与动态重分配算法，在资源状态与环境变化下重构任务-资源匹配关系，以 API 形式集成至应急管理软件。',
 '结合大模型实现方案的辅助生成与结果解释，降低非专业用户理解与使用优化结果的门槛。']),
('2023.09 — 至今','南京大学复杂工程管理研究所','科研项目研究员 · 产学研',[
 '长期参与复杂系统智能决策与任务规划类产学研项目，覆盖基础加强、国防预研及军工单位/科研院所横纵向课题，**累计参与十余项**任务规划、多主体协同、路径优化、行为建模与复杂系统验证项目。',
 '承担需求抽象、技术路线设计、模型与算法方案论证及研发工作，将非结构化任务需求转化为可计算、可求解、可实现的模型与软件方案。',
 '多次赴项目现场与军工单位及科研院所开展需求对接、方案评审、阶段汇报与系统联调；**累计交付 20+ 软件系统与算法模块**，形成多项技术报告、软件著作权及项目验收成果。']),
],
'en':[
('Jun 2026 — Present','Tencent · Xiaowei Agent Core Business','LLM Application Algorithm Intern',[
 '**RAG evaluation and online regression:** addressed distribution shift between synthetic benchmarks and production traffic by building chain-level error attribution across multi-route retrieval, RRF fusion, and LLM filtering; mined real bad cases and long-tail scenarios to expand ~300 synthetic cases into ~6,000 production-distribution regression cases.',
 '**Agent evaluation and LLM-as-a-Judge:** decomposed online agent quality into relevance, correctness, timeliness, and safety; shipped an internal multi-annotator platform for gold cases and iterated on judge–human disagreements, raising agreement from 71.0% to 94.6% to enable automated evaluation at scale.',
 '**Generation safety and preference data:** reviewed ~2M requests over 20 days through a screen → LLM-classify → human-review pipeline for high-risk cases; constructed 606 preference pairs via teacher rewriting, rejection sampling, and QA to support full-parameter DPO, lifting the project pass rate from 70% to 80%.',
 '**SFT data and isolated regression:** induced ~1,000 SFT examples from real failure modes such as role misalignment and missing source grounding, with strict train/eval isolation; production validation showed +12.15 pct relevance, +8.00 pct correctness, and safety risk down from 1.12% to 0.11%.']),
('Jan 2026 — May 2026','NJU Research Center for Novel Technology of Intelligent Equipment','Algorithm Researcher',[
 '**Sea-ice route planning and multi-task scheduling:** abstracted sea-ice concentration, weather, hazard zones, and task priorities into a joint constrained-routing and task-allocation problem; designed a heuristic solver supporting hundreds of tasks and thousands of nodes, generating plans within 4 seconds and exposed through a project API.',
 '**Smart-factory emergency scheduling and replanning:** built a model integrating capability differences, role fitness, task priority, dynamic rendezvous, and environmental interference; designed multi-role allocation and dynamic reassignment algorithms, integrated into emergency-management software via API.',
 'Used LLMs for plan-assisted generation and result explanation, lowering the barrier for non-expert users to interpret optimization outputs.']),
('Sep 2023 — Present','NJU Institute for Complex Engineering Management','Research Project Researcher',[
 'Contributed to 10+ applied research projects on intelligent decision making and task planning for complex systems, spanning national foundation-strengthening programs, defense pre-research, and joint projects with industry and research institutes.',
 'Responsible for requirement abstraction, technical-route design, model and algorithm validation, and development — turning unstructured requirements into computable, solvable, and deliverable models and software.',
 'Conducted on-site requirement analysis, design reviews, milestone reporting, and system integration; delivered 20+ software systems and algorithm modules, producing technical reports, software copyrights, and project acceptance outcomes.']),
]}

# (dates, school, degree, badge, dept_line, detail_line)
EDUCATION={
'zh':[
('2023.09 — 预计 2027.06','南京大学','管理科学与工程 · 博士研究生','985 · C9','工程管理学院 · 控制科学与智能工程系培养','专业排名 1/24，获国家奖学金、英才奖学金'),
('2020.09 — 2023.06','南京大学','电子信息 · 硕士','985 · C9','工程管理学院','专业排名 3/37，获华为奖学金、校一等奖学金'),
('2016.09 — 2020.06','江南大学','自动化 · 工学学士','211','物联网工程学院','专业排名 2/219，获国家奖学金、远翔特别奖学金'),
],
'en':[
('Sep 2023 — Expected Jun 2027','Nanjing University','Ph.D. Candidate · Management Science and Engineering','985 · C9','School of Engineering Management · Dept. of Control Science and Intelligence Engineering','Ranked 1/24 · National Scholarship, Yingcai Scholarship'),
('Sep 2020 — Jun 2023','Nanjing University','M.Eng. · Electronic Information','985 · C9','School of Engineering Management','Ranked 3/37 · Huawei Scholarship, University First-Class Scholarship'),
('Sep 2016 — Jun 2020','Jiangnan University','B.Eng. · Automation','211','School of Internet of Things Engineering','Ranked 2/219 · National Scholarship, Yuanxiang Special Scholarship'),
]}

AWARDS={
'zh':[
('国家奖学金 · 两次','分别于博士与本科阶段获得，表彰学业、科研与综合表现。'),
('IEEE E-CARGO 国际学术会议最佳论文奖 · 两届','2025 年最佳论文一等奖、2026 年最佳论文二等奖，均为第一作者论文。'),
('华为奖学金 · 英才奖学金 · 远翔特别奖学金','分别于硕士与博士阶段获得的专项奖学金。'),
('校一等奖学金 · 若干次','本科、硕士与博士阶段多次获得校级一等奖学金。'),
('南京大学 / 江南大学优秀毕业生','两校均获优秀毕业生称号。'),
('学科与创新创业竞赛','中国大学生服务外包创新创业大赛全国一等奖；中国国际大学生创新创业大赛全国铜奖；全国青年科普创新实验暨作品大赛全国优秀奖（江苏赛区第一）。'),
],
'en':[
('National Scholarship of China · twice','Awarded during both doctoral and undergraduate study for academic and research excellence.'),
('IEEE E-CARGO Best Paper Award · twice','First Prize (2025) and Second Prize (2026) at the international symposium, both for first-authored papers.'),
('Huawei · Yingcai · Yuanxiang Special Scholarships','Competitive scholarships during master\u2019s and doctoral study.'),
('University First-Class Scholarship · multiple times','Awarded repeatedly across undergraduate, master\u2019s, and doctoral study.'),
('Outstanding Graduate · NJU and Jiangnan University','Awarded at both institutions.'),
('Academic & entrepreneurship competitions','National First Prize, China Service Outsourcing Innovation Competition; National Bronze, China International College Students\u2019 Innovation Competition; National Excellence Award (1st in Jiangsu), National Youth Science Popularization Competition.'),
]}

LABEL={
'zh':{
 'title':'张鑫磊 · 个人主页','brand':'张鑫磊 · 个人主页',
 'tagline':'人-机-AI 协同 · 多智能体协同配置 · LLM Agent 决策',
 'person':'张鑫磊','subtitle':'Xinlei Zhang',
 'role':'南京大学 · 管理科学与工程博士研究生（控制科学与智能工程系培养 · 预计 2027.06 毕业）',
 'intro':'我的研究聚焦于 **AI 从辅助工具向自主决策主体演进**过程中，复杂智能系统的**协同组织、任务配置与优化决策**问题。以多智能体系统、角色协作理论与组合优化为基础，研究 AI 介入如何重塑主体能力结构、异构主体如何实现高效协同，以及自主智能体如何可信地参与决策；**博士阶段已发表第一作者论文 8 篇**，代表性成果见于 IEEE TSMC: Systems、IEEE THMS 等期刊。与此同时，我在**腾讯小微 Agent 核心业务**从事大模型应用算法实践，负责 RAG 链路评测、智能体多维评测与 LLM Judge 校准、SFT/DPO 数据建设与后训练验证，让研究问题始终接受真实线上系统的检验。',
 'portraitAlt':'张鑫磊的证件照',
 'nav':['关于我','教育背景','研究与实习','求职意向','研究方向','近一年动态','论文成果','科研课题','项目实践','荣誉奖励','联系我'],
 'heroBtns':['查看论文成果','邮件联系'],
 'heroSmall':'2027 届博士毕业生 · 同步关注高校教职与业界 Agent 算法岗位',
 'metrics':[('13','篇已发表论文（博士阶段）'),('8','篇第一作者'),('3','篇一作在审（含 CCF-A）'),('2','次国家奖学金')],
 'sections':['关于我','教育背景','研究与实习经历','求职意向','研究方向','近一年动态','论文成果','科研课题与知识产权','项目实践','荣誉奖励','联系我'],
 'kickers':['ABOUT ME','EDUCATION','EXPERIENCE','POSITIONING','RESEARCH','RECENT NEWS','PUBLICATIONS','GRANTS & OUTPUTS','PROJECTS','HONORS','GET IN TOUCH'],
 'about1':'我的研究方向是**人-机-AI 协同**与**AI Agent 智能决策**——研究人、物理机器与 AI 智能体构成的异构系统中的协同机制与智能任务配置，关注 AI 从辅助工具向自主决策主体演进所带来的**能力建模、角色配置与可信协同**问题。我是南京大学管理科学与工程专业博士研究生（2023.09 入学，预计 2027.06 毕业），由控制科学与智能工程系培养，**专业排名 1/24**。',
 'about2':'研究方法以多智能体系统、角色协作理论与组合优化为基础，综合运用混合整数规划、启发式与分层求解、强化学习等建模与求解手段，并进一步延伸至**大模型评测、后训练与 AI Agent 在线决策**。除学术研究外，我长期参与复杂系统智能决策类产学研课题，并在腾讯小微 Agent 核心业务从事**真实线上**的大模型应用算法实践。',
 'stageNote':'关于本页成果范围：本主页列出的论文、课题、奖励与项目**均为 2023 年 9 月进入博士阶段之后产出（约三年）**，硕士及本科阶段的成果未在此展开。',
 'aboutTag':'研究与技术关键词',
 'eduLead':'本科自动化、硕士电子信息、博士管理科学与工程，形成控制、信息与管理决策的交叉培养背景。',
 'eduNote':'**学科背景与交叉研究：**我由南京大学控制科学与智能工程系培养，攻读管理科学与工程博士学位。研究**融合管理科学、控制科学与人工智能**，聚焦复杂组织与工程系统中的多主体协同、智能决策及资源优化，具有鲜明的学科交叉特色。**因控制科学与工程博士点于 2025 年获批，而我于 2023 年入学，故学位归属管理科学与工程。**',
 'trackLead':'我同时关注高校教职与业界 Agent 算法岗位。以下按两条路径分别说明研究延续性与工程落地能力。',
 'researchLead':'以“主体能力 — 协作关系 — 任务配置 — 在线决策”为主线，连接管理科学、组合优化与智能体系统。',
 'newsLead':'近一年的部分研究进展与重要节点',
 'pubLead':'下列为博士阶段（2023.09 起）已发表的期刊与会议论文，**共 13 篇，作者排名均为前二，其中第一作者 8 篇**。',
 'filter':['全部论文','第一作者','期刊论文','会议论文'],'pubCount':'篇博士阶段已发表论文',
 'first':'第一作者','second':'第二作者','pubNo':'待发表',
 'reviewTitle':'一作在审稿件',
 'reviewLead':'目前我围绕**“自主 AI 进入复杂系统后的协同秩序”**这一问题持续推进研究：一方面研究跨物理—信息空间混合团队中异构主体的**能力耦合与角色配置**，另一方面研究不同自主程度 AI 主体的**治理约束、权限边界与监督机制**，并进一步评估 LLM 作为自主决策主体时的**能力边界与残余协调缺口**。相关成果形成以下三篇第一作者稿件。',
 'projLead':'围绕**“把复杂业务需求抽象为可计算、可求解、可交付的决策问题”**这条主线，以下项目覆盖真实线上大模型业务、工程优化系统与独立 AI 产品三类场景。',
 'grantLead':'博士阶段主持与参与的科研课题、基金申报情况，以及专利、软件著作权与专著成果。',
 'grantTitle':'科研课题与基金','outputTitle':'知识产权与专著',
 'workLead':'博士阶段的研究、算法与产业实践经历。',
 'awardLead':'博士及此前阶段获得的部分荣誉与奖励。',
 'contactHeading':'欢迎求职沟通与学术交流',
 'contactText':'欢迎就高校教职、业界 Agent 算法岗位，以及人-机-AI 协同、多智能体任务配置、LLM Agent 决策与评测等方向交流。完整简历（高校版 / 业界版，中英文）可邮件索取。',
 'contactBtn':'发送邮件','contactInfo':'出于隐私考虑，本站不展示手机号；简历与联系方式可通过邮件索取。',
 'footer':'个人主页 · Built for GitHub Pages','back':'返回顶部','skip':'跳到主要内容','emailCopied':'邮箱已复制','siteLang':'EN',
 },
'en':{
 'title':'Xinlei Zhang · Personal Homepage','brand':'Xinlei Zhang · Homepage',
 'tagline':'Human–Machine–AI Collaboration · Multi-Agent Coordination · LLM Agent Decision Making',
 'person':'Xinlei Zhang','subtitle':'张鑫磊',
 'role':'Ph.D. Candidate · Management Science & Engineering, Nanjing University (trained in the Dept. of Control Science and Intelligence Engineering · expected Jun 2027)',
 'intro':'My research addresses **collaborative organization, task configuration, and optimal decision making** in complex intelligent systems as **AI evolves from an assistive tool into an autonomous decision-making agent**. Grounded in multi-agent systems, role-based collaboration theory, and combinatorial optimization, I study how AI intervention reshapes agent capability structures, how heterogeneous agents coordinate efficiently, and how autonomous agents can participate in decisions in a trustworthy way. **During my Ph.D. I have published 8 first-authored papers**, with representative work in IEEE TSMC: Systems and IEEE THMS. In parallel, I work on applied LLM algorithms in the **Tencent Xiaowei Agent core business** — RAG chain evaluation, multi-dimensional agent evaluation and LLM-judge calibration, and SFT/DPO data construction with post-training validation — keeping my research questions tested against real production systems.',
 'portraitAlt':'Portrait of Xinlei Zhang',
 'nav':['About','Education','Experience','Positioning','Research','News','Publications','Grants','Projects','Honors','Contact'],
 'heroBtns':['View publications','Get in touch'],
 'heroSmall':'Graduating in 2027 · Open to faculty positions and industry agent-algorithm roles',
 'metrics':[('13','Papers published during PhD'),('8','First-authored'),('3','First-authored under review'),('2','National Scholarships')],
 'sections':['About','Education','Research & Industry Experience','Positioning','Research Interests','Recent News','Publications','Grants, Patents & Books','Projects','Honors & Awards','Contact'],
 'kickers':['ABOUT ME','EDUCATION','EXPERIENCE','POSITIONING','RESEARCH','RECENT NEWS','PUBLICATIONS','GRANTS & OUTPUTS','PROJECTS','HONORS','GET IN TOUCH'],
 'about1':'My research areas are **human–machine–AI collaboration** and **AI agent decision making** — studying coordination mechanisms and intelligent task allocation in heterogeneous systems of humans, physical machines, and AI agents, and the problems of **capability modeling, role configuration, and trustworthy collaboration** that arise as AI evolves from an assistive tool into an autonomous decision maker. I am a Ph.D. candidate in Management Science and Engineering at Nanjing University (enrolled Sep 2023, expected graduation Jun 2027), trained in the Department of Control Science and Intelligence Engineering and **ranked 1/24 in my program**.',
 'about2':'My methodology builds on multi-agent systems, role-based collaboration theory, and combinatorial optimization, drawing on mixed-integer programming, heuristic and hierarchical solvers, and reinforcement learning, and extending to **LLM evaluation, post-training, and online AI agent decision making**. Beyond academic work, I have contributed to applied research projects on intelligent decision making for complex systems, and I currently work on **production** LLM algorithms in the Tencent Xiaowei Agent core business.',
 'stageNote':'Scope of this page: all publications, projects, awards, and grants listed here **were produced after I began my Ph.D. in September 2023** (roughly a three-year window). Master\u2019s and undergraduate work is not included.',
 'aboutTag':'Research & technical keywords',
 'eduLead':'Automation (B.Eng.), Electronic Information (M.Eng.), and Management Science & Engineering (Ph.D.) — an interdisciplinary background across control, information, and decision science.',
 'eduNote':'**Disciplinary background and interdisciplinary research:** I am trained in the Department of Control Science and Intelligence Engineering at Nanjing University, pursuing a doctorate in Management Science and Engineering. My work **integrates management science, control science, and artificial intelligence**, focusing on multi-agent collaboration, intelligent decision making, and resource optimization in complex organizational and engineering systems — a distinctly interdisciplinary profile. **Because the doctoral program in Control Science and Engineering was approved in 2025, after my enrollment in 2023, my degree is conferred under Management Science and Engineering.**',
 'trackLead':'I am pursuing both academic and industry paths. The two tracks below outline research continuity and engineering delivery respectively.',
 'researchLead':'A continuous agenda connecting agent capability, collaboration structure, task allocation, and online decision making.',
 'newsLead':'Selected milestones from the past year',
 'pubLead':'Peer-reviewed journal and conference papers published during my Ph.D. (since Sep 2023): **13 in total, all as first or second author, including 8 as first author**.',
 'filter':['All Papers','First Author','Journal','Conference'],'pubCount':'papers published during PhD',
 'first':'First author','second':'Second author','pubNo':'To appear',
 'reviewTitle':'First-authored manuscripts under review',
 'reviewLead':'My ongoing work centers on **coordination order once autonomous AI enters complex systems**: **capability coupling and role configuration** among heterogeneous agents in cross physical–cyber hybrid teams; **governance constraints, authority boundaries, and supervision mechanisms** for AI agents at varying autonomy levels; and the **capability boundaries and residual coordination gaps** of LLMs acting as autonomous decision makers. This work has produced the three first-authored manuscripts below.',
 'projLead':'Organized around one through-line — **turning complex business requirements into decision problems that are computable, solvable, and deliverable** — the projects below span production LLM systems, engineering optimization, and independent AI products.',
 'grantLead':'Research projects led and joined during my Ph.D., grant applications, and patents, software copyrights, and book contributions.',
 'grantTitle':'Research Projects & Grants','outputTitle':'Patents, Software & Books',
 'workLead':'Research, algorithm, and industry experience during my doctoral studies.',
 'awardLead':'Selected honors and awards from my doctoral and earlier studies.',
 'contactHeading':'Open to recruiting conversations',
 'contactText':'I welcome conversations about faculty positions and industry agent-algorithm roles, as well as human–machine–AI collaboration, multi-agent task allocation, and LLM agent decision making and evaluation. Full CVs (academic and industry versions, in Chinese and English) are available on request by email.',
 'contactBtn':'Send an email','contactInfo':'Phone number omitted for privacy; CV and contact details are available by email.',
 'footer':'Personal homepage · Built for GitHub Pages','back':'Back to top','skip':'Skip to main content','emailCopied':'Email copied','siteLang':'中文',
 }}

KEYWORDS=['Human–Machine–AI Collaboration','Role Assignment & E-CARGO','AI Augmentation','Multi-Agent Decision Making','Combinatorial Optimization','LLM Agents','RAG & LLM Judge','SFT / DPO','Reinforcement Learning']
HERO_TAGS=['Human–Machine–AI Collaboration','Multi-Agent Decision Making','LLM Agents','RAG & Post-Training']

EMAIL='ZhangShine@smail.nju.edu.cn'
NAVIDS=['about','education','experience','positioning','research','news','publications','grants','projects','honors','contact']

# ---- SEO ----
SITE='https://zhangxinleime.github.io'

# Google Search Console 所有权验证码。验证通过后也不要删——删掉会导致验证失效、
# Search Console 停止提供数据。换站点时在 GSC 重新获取并替换此处。
GOOGLE_VERIFY='HGMWTCL0xuLLuoXf51bVLZwl76zY8WahN2dQPouRXxk'

# 搜索结果里显示的标题。含姓名 + 单位 + 研究方向，便于被长尾词命中。
SEO_TITLE={
 'zh':'张鑫磊 | 南京大学博士研究生 · 人-机-AI 协同与 AI Agent 智能决策',
 'en':'Xinlei Zhang | Ph.D. Candidate, Nanjing University · Human–Machine–AI Collaboration',
}
# 搜索结果摘要。控制在 150 字以内，否则被截断。
SEO_DESC={
 'zh':'张鑫磊，南京大学管理科学与工程博士研究生（控制科学与智能工程系培养），研究人-机-AI 协同、多智能体协同配置与 LLM Agent 智能决策。博士阶段已发表论文 13 篇（第一作者 8 篇），现于腾讯小微 Agent 核心业务从事大模型应用算法实践。求职联系：ZhangShine@smail.nju.edu.cn',
 'en':'Ph.D. candidate at Nanjing University. Research on human–machine–AI collaboration, multi-agent task configuration, and LLM agent decision making. 13 papers, 8 first-authored.',
}
SEO_KEYWORDS={
 'zh':'张鑫磊,南京大学,博士研究生,人机AI协同,人-机-AI 协同,AI Agent,智能决策,多智能体系统,角色配置,E-CARGO,组合优化,大模型评测,管理科学与工程,控制科学与智能工程系,求职,个人主页',
 'en':'Xinlei Zhang,Nanjing University,PhD candidate,Human-Machine-AI Collaboration,AI Agent,Multi-Agent Systems,Role Assignment,E-CARGO,Combinatorial Optimization,LLM Evaluation,Management Science and Engineering,academic job market',
}

def jsonld(lang):
    """Person 结构化数据 — 让搜索引擎把本页识别为「人物主页」，
    有机会在结果页右侧展示知识面板，并明确姓名的中英对应关系。"""
    import json
    d={
      "@context":"https://schema.org",
      "@type":"Person",
      "name":"张鑫磊" if lang=='zh' else "Xinlei Zhang",
      "alternateName":["Xinlei Zhang","张鑫磊","ZXL"],
      "url":SITE+('/' if lang=='zh' else '/en.html'),
      "mainEntityOfPage":{"@type":"WebPage","@id":SITE+('/' if lang=='zh' else '/en.html')},
      "image":SITE+'/assets/portrait.jpg',
      "email":"mailto:"+EMAIL,
      "jobTitle":"博士研究生" if lang=='zh' else "Ph.D. Candidate",
      "description":SEO_DESC[lang],
      "affiliation":{"@type":"CollegeOrUniversity","name":"南京大学" if lang=='zh' else "Nanjing University","url":"https://www.nju.edu.cn","sameAs":"https://en.wikipedia.org/wiki/Nanjing_University"},
      "alumniOf":[
        {"@type":"CollegeOrUniversity","name":"南京大学" if lang=='zh' else "Nanjing University"},
        {"@type":"CollegeOrUniversity","name":"江南大学" if lang=='zh' else "Jiangnan University"},
      ],
      "knowsAbout":(["人-机-AI 协同","多智能体系统","智能任务配置","角色协作理论 E-CARGO","组合优化","强化学习","大模型评测","AI Agent 智能决策"] if lang=='zh'
                    else ["Human–Machine–AI Collaboration","Multi-Agent Systems","Intelligent Task Allocation","Role-Based Collaboration (E-CARGO)","Combinatorial Optimization","Reinforcement Learning","LLM Evaluation","AI Agent Decision Making"]),
      "knowsLanguage":["zh-CN","en"],
    }
    return json.dumps(d,ensure_ascii=False,separators=(',',':'))

ICON_MAIL='<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'
ICON_EXT='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 5h5v5M19 5l-9 9"/><path d="M19 13v5a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h5"/></svg>'
ICON_ARROW='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h16m-7-7 7 7-7 7"/></svg>'
ICON_COPY='<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h3"/></svg>'


def make_page(lang):
    L=LABEL[lang]; en=lang=='en'; target='index.html' if en else 'en.html'
    title=h(L['title'])
    nav=''.join(f'<a class="nav-link" href="#{NAVIDS[i]}">{h(n)}</a>' for i,n in enumerate(L['nav']))
    metrics=''.join(f'<div class="stat"><strong>{h(n)}</strong><span>{h(t)}</span></div>' for n,t in L['metrics'])
    herotags=''.join(f'<span>{h(t)}</span>' for t in HERO_TAGS)
    parts=[]
    parts.append(f'''<!doctype html>
<html lang="{lang if en else 'zh-CN'}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{h(SEO_TITLE[lang])}</title>
<meta name="description" content="{plain(SEO_DESC[lang])}">
<meta name="keywords" content="{h(SEO_KEYWORDS[lang])}">
<meta name="author" content="{h(L['person'])}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta name="google-site-verification" content="{GOOGLE_VERIFY}">
<meta name="theme-color" content="#f6f8fb">
<link rel="canonical" href="{SITE}/{'' if lang=='zh' else 'en.html'}">
<link rel="alternate" hreflang="zh-CN" href="{SITE}/">
<link rel="alternate" hreflang="en" href="{SITE}/en.html">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta property="og:type" content="profile">
<meta property="og:site_name" content="{h(L['person'])}">
<meta property="og:locale" content="{'zh_CN' if lang=='zh' else 'en_US'}">
<meta property="og:url" content="{SITE}/{'' if lang=='zh' else 'en.html'}">
<meta property="og:title" content="{h(SEO_TITLE[lang])}">
<meta property="og:description" content="{plain(SEO_DESC[lang])}">
<meta property="og:image" content="{SITE}/assets/portrait.jpg">
<meta property="profile:first_name" content="{'鑫磊' if lang=='zh' else 'Xinlei'}">
<meta property="profile:last_name" content="{'张' if lang=='zh' else 'Zhang'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{h(SEO_TITLE[lang])}">
<meta name="twitter:description" content="{plain(SEO_DESC[lang])}">
<meta name="twitter:image" content="{SITE}/assets/portrait.jpg">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">{jsonld(lang)}</script>
</head>
<body>
<a href="#main" class="skip-link">{h(L['skip'])}</a>
<div class="reading-progress" id="progress" aria-hidden="true"></div>
<header class="site-header" id="top"><div class="header-inner container">
  <a href="#top" class="brand" aria-label="{h(L['person'])} home"><span class="brand-mark">ZXL<span class="brand-point">.</span></span><span class="brand-label">{h(L['brand'])}</span></a>
  <nav class="site-nav" aria-label="Primary navigation">{nav}</nav>
  <div class="header-actions"><a class="lang-toggle" href="{target}" aria-label="Switch language">{h(L['siteLang'])}<span aria-hidden="true"> ↗</span></a><button type="button" class="mobile-toggle" aria-controls="mobile-nav" aria-expanded="false" aria-label="Menu"><span></span><span></span><span></span></button></div>
</div><nav class="mobile-nav" id="mobile-nav" aria-label="Mobile navigation">{nav}</nav></header>
<main id="main">
<section class="hero-section container" aria-labelledby="hero-title">
<div class="hero-head">
<div class="hero-visual"><div class="portrait-stage"><div class="portrait-frame"><img src="assets/portrait.jpg" alt="{h(L['portraitAlt'])}" width="750" height="1050" fetchpriority="high"></div><div class="portrait-bottom"><span class="portrait-mini">NJU · PHD CANDIDATE</span><span>2023—2027</span></div></div></div>
<div class="hero-identity">
<div class="eyebrow"><span class="eyebrow-dot"></span> {h('NANJING UNIVERSITY  /  AI & DECISION SCIENCE')}</div>
<div class="hero-introline">{h(L['tagline'])}</div>
<h1 id="hero-title">{h(L['person'])}<span class="hero-english">{h(L['subtitle'])}</span></h1>
<p class="hero-role">{h(L['role'])}</p>
</div></div>
<div class="hero-copy">
<p class="hero-description">{r(L['intro'])}</p>
<div class="hero-tags">{herotags}</div>
<div class="hero-actions"><a class="btn btn-primary" href="#publications">{h(L['heroBtns'][0])} {ICON_ARROW}</a><a class="btn btn-outline" href="mailto:{EMAIL}">{ICON_MAIL} {h(L['heroBtns'][1])}</a></div>
<div class="hero-footnote"><span class="pulse"></span>{h(L['heroSmall'])}</div>
</div>
<div class="hero-stats">{metrics}</div></section>''')

    def heading(i):
        return f'<div class="section-header"><div class="section-number">{i+1:02d} / {h(L["kickers"][i])}</div><h2>{h(L["sections"][i])}</h2></div>'

    # 01 About
    kw=''.join(f'<span>{h(k)}</span>' for k in KEYWORDS)
    parts.append(f'''<section id="about" class="section section-about"><div class="container">
{heading(0)}<div class="about-layout"><div class="about-text"><p>{r(L['about1'])}</p><p>{r(L['about2'])}</p><p class="stage-note">{r(L['stageNote'])}</p></div><div class="about-aside"><span class="aside-heading">{h(L['aboutTag'])}</span><div class="tag-cloud">{kw}</div></div></div>
</div></section>''')

    # 02 Education
    eds=''.join(f'''<article class="edu-card"><div class="edu-top"><span class="edu-years">{h(d)}</span><span class="edu-badge">{h(badge)}</span></div><h3>{h(org)}</h3><div class="edu-degree">{h(degree)}</div><div class="edu-dept">{h(dept)}</div><p>{h(note)}</p></article>''' for d,org,degree,badge,dept,note in EDUCATION[lang])
    parts.append(f'''<section id="education" class="section section-soft"><div class="container">
{heading(1)}<p class="section-lead">{h(L['eduLead'])}</p><div class="edu-grid">{eds}</div><p class="stage-note edu-note">{r(L['eduNote'])}</p></div></section>''')

    # 03 Research & industry experience
    timeline=''.join(f'<div class="timeline-item"><div class="timeline-date">{h(d)}</div><div class="timeline-content"><h4>{h(org)}</h4><div class="timeline-role">{h(role)}</div><ul class="work-points">{"".join("<li>"+r(b)+"</li>" for b in bullets)}</ul></div></div>' for d,org,role,bullets in WORK[lang])
    parts.append(f'''<section id="experience" class="section"><div class="container">
{heading(2)}<p class="section-lead">{h(L['workLead'])}</p><div class="timeline timeline-wide">{timeline}</div></div></section>''')

    # 04 Positioning (dual track)
    tracks=''
    for eyebrow,ttl,summary,rows in TRACKS[lang]:
        items=''.join(f'<li><span class="track-label">{h(lab)}</span><p>{r(txt)}</p></li>' for lab,txt in rows)
        tracks+=f'<article class="track-card"><div class="track-eyebrow">{h(eyebrow)}</div><h3>{h(ttl)}</h3><p class="track-summary">{h(summary)}</p><ul class="track-list">{items}</ul></article>'
    parts.append(f'''<section id="positioning" class="section section-soft"><div class="container">
{heading(3)}<p class="section-lead">{h(L['trackLead'])}</p><div class="track-grid">{tracks}</div></div></section>''')

    # 05 Research
    cards=''.join(f'<article class="research-card"><div class="research-index">{h(n)} <span>{h(mark)}</span></div><h3>{h(head)}</h3><p class="research-en">{h(sub)}</p><p class="research-desc">{h(desc)}</p><span class="card-corner" aria-hidden="true">↗</span></article>' for n,head,sub,desc,mark in RESEARCH[lang])
    parts.append(f'''<section id="research" class="section"><div class="container">
{heading(4)}<p class="section-lead">{h(L['researchLead'])}</p><div class="research-grid">{cards}</div></div></section>''')

    # 06 News
    lines=''.join(f'<li class="news-item"><time>{h(date)}</time><p>{h(msg)}</p></li>' for date,msg in NEWS[lang])
    parts.append(f'''<section id="news" class="section section-soft"><div class="container">{heading(5)}<p class="section-lead">{h(L['newsLead'])}</p><ol class="news-list">{lines}</ol></div></section>''')

    # 07 Publications + under review
    pubs=[]
    for idx,p in enumerate(PUBLICATIONS,1):
        ptitle,venue,year,qzh,qen,auth,doi,desczh,descen=p
        y=f'{year}' if year else ('已发表' if not en else 'Published')
        typ='conference' if ('Conference' in venue or 'E-CARGO' in venue or 'CASA ' in venue) else 'journal'
        flags=f'{typ} '+('first' if auth=='first' else 'second')
        iconrole=L['first'] if auth=='first' else L['second']
        desc=descen if en else desczh
        rating=qen if en else qzh
        linktext='DOI / Paper' if en else '论文原文'
        link=(a(DOI+doi,linktext+ICON_EXT,'paper-link') if doi else f'<span class="paper-no-link">{h(L["pubNo"])}</span>')
        pubs.append(f'''<article class="paper-card" data-category="{flags}">
<div class="paper-number">{idx:02d}</div><div class="paper-main"><div class="paper-top"><span class="paper-type">{('Conference' if typ=='conference' else 'Journal') if en else ('国际会议' if typ=='conference' else '期刊论文')}</span><span class="paper-year">{h(y)}</span><span class="paper-author {auth}">{h(iconrole)}</span></div>
<h3>{h(ptitle)}</h3><div class="paper-venue">{h(venue)} <span class="venue-separator">·</span> {h(rating)}</div><p class="paper-abstract">{h(desc)}</p></div><div class="paper-action">{link}</div>
</article>''')
    tabs=''.join(f'<button class="filter-btn{(" active" if i==0 else "")}" data-filter="{["all","first","journal","conference"][i]}" aria-pressed="{str(i==0).lower()}">{h(label)}</button>' for i,label in enumerate(L['filter']))
    reviews=''
    for item in UNDER_REVIEW:
        rtitle,rvenue,szh,sen,qzh,qen,dzh,den=item
        reviews+=f'''<article class="review-card"><div class="review-top"><span class="review-status">{h(sen if en else szh)}</span><span class="review-rating">{h(qen if en else qzh)}</span><span class="paper-author first">{h(L['first'])}</span></div><h4>{h(rtitle)}</h4><div class="paper-venue">{h(rvenue)}</div><p class="paper-abstract">{h(den if en else dzh)}</p></article>'''
    parts.append(f'''<section id="publications" class="section section-soft"><div class="container">
{heading(6)}<p class="section-lead">{r(L['pubLead'])}</p><div class="pub-toolbar"><div class="pub-filters" role="group" aria-label="Publication filters">{tabs}</div><div class="pub-total"><b id="pub-count">13</b> {h(L['pubCount'])}</div></div>
<div class="paper-list" id="paper-list">{''.join(pubs)}</div>
<div class="review-block"><h3 class="review-heading">{h(L['reviewTitle'])}<span class="review-count">{len(UNDER_REVIEW)}</span></h3><p class="review-lead">{r(L['reviewLead'])}</p><div class="review-grid">{reviews}</div></div></div></section>''')

    # 08 Grants & outputs
    gl=''.join(f'<li><span class="grant-role">{h(role)}</span><div class="grant-body"><strong>{h(gtitle)}</strong><p>{h(note)}</p></div></li>' for role,gtitle,note in GRANTS[lang])
    ol=''.join(f'<li><span class="output-kind">{h(kind)}</span><div class="grant-body"><strong>{h(otitle)}</strong><p>{h(note)}</p></div></li>' for kind,otitle,note in OUTPUTS[lang])
    parts.append(f'''<section id="grants" class="section"><div class="container">{heading(7)}<p class="section-lead">{h(L['grantLead'])}</p>
<div class="grant-layout"><div class="grant-panel"><h3 class="panel-heading">{h(L['grantTitle'])}</h3><ul class="grant-list">{gl}</ul></div><div class="grant-panel"><h3 class="panel-heading">{h(L['outputTitle'])}</h3><ul class="grant-list output-list">{ol}</ul></div></div></div></section>''')

    # 09 Projects
    pr=''.join(f'''<article class="project-card"><div class="project-head"><span class="project-index">{h(n)} / {h(kind)}</span><span class="project-date">{h(date)}</span></div><h3>{h(ptitle)}</h3><p class="project-text">{h(desc)}</p><div class="project-impact"><span class="impact-symbol">✳</span>{h(impact)}</div><div class="project-tags">{''.join('<span>'+h(item.strip())+'</span>' for item in tech.split('/'))}</div></article>''' for n,ptitle,date,desc,impact,tech,kind in PROJECTS[lang])
    parts.append(f'''<section id="projects" class="section section-soft"><div class="container">{heading(8)}<p class="section-lead">{r(L['projLead'])}</p><div class="project-grid">{pr}</div></div></section>''')

    # 10 Honors
    aw=''.join(f'<li><strong>{h(atitle)}</strong><span>{h(desc)}</span></li>' for atitle,desc in AWARDS[lang])
    parts.append(f'''<section id="honors" class="section"><div class="container">{heading(9)}<p class="section-lead">{h(L['awardLead'])}</p><ul class="award-list award-grid">{aw}</ul></div></section>''')

    # 11 Contact
    parts.append(f'''<section id="contact" class="section contact-section"><div class="container contact-container">{heading(10)}<div class="contact-box"><div><h3><span class="contact-asterisk">✳</span>{h(L['contactHeading'])}</h3><p>{h(L['contactText'])}</p><div class="contact-email">{a('mailto:'+EMAIL,h(EMAIL),'email-anchor')}<button class="copy-email" aria-label="Copy email" data-copy="{h(EMAIL)}" data-message="{h(L['emailCopied'])}" title="Copy email">{ICON_COPY}</button></div><div class="privacy-note">{h(L['contactInfo'])}</div></div><a href="mailto:{EMAIL}" class="contact-circle" aria-label="{h(L['contactBtn'])}">{ICON_ARROW}</a></div></div></section>
</main><footer class="site-footer"><div class="container footer-inner"><div><span class="footer-mark">ZXL.</span> © 2026 Xinlei Zhang · {h(L['footer'])}</div><div><a href="#top" class="back-top">{h(L['back'])} ↑</a></div></div></footer>
<div class="toast" role="status" aria-live="polite" id="toast"></div>
<script src="script.js" defer></script>
</body></html>''')
    return '\n'.join(parts)

for lang,out in [('zh','index.html'),('en','en.html')]:
    (ROOT/out).write_text(make_page(lang),encoding='utf-8')
    print('Created',ROOT/out)

# ---- SEO 附属文件 ----
import datetime
_today=datetime.date.today().isoformat()

# sitemap.xml：告诉搜索引擎本站有哪些页面、哪个是中文哪个是英文
_sitemap=f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>{SITE}/</loc>
    <lastmod>{_today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
    <xhtml:link rel="alternate" hreflang="zh-CN" href="{SITE}/"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE}/en.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/"/>
  </url>
  <url>
    <loc>{SITE}/en.html</loc>
    <lastmod>{_today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="zh-CN" href="{SITE}/"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE}/en.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/"/>
  </url>
</urlset>
'''
(ROOT/'sitemap.xml').write_text(_sitemap,encoding='utf-8')
print('Created',ROOT/'sitemap.xml')

# robots.txt：允许全部抓取，并指明 sitemap 位置
_robots=f'''User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
'''
(ROOT/'robots.txt').write_text(_robots,encoding='utf-8')
print('Created',ROOT/'robots.txt')
