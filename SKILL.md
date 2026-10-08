---
name: token-saver
description: >
  Cut input/output token spend in agent sessions: local knowledge base first,
  fetch-once cache web research, compact state handoffs instead of re-pasted
  context, anchored citations so verification needs grep not full reads, and
  terse output discipline. Use when a user asks to save tokens, reduce cost,
  build/reuse a local knowledge base, or avoid re-reading the same material
  every session. Works on any machine with zero dependencies.
---

# Token Saver — 本地知识库 & 省 Token 纪律

核心原则：**答案不在对话里，在场外**。重复出现的信息，第一次消化、第二次查表、
永远不重贴。以下六条纪律按收益排序，每条独立可用。

## 1. 本地优先（Local-First）

任何研究会话开始前，先查本地，后联网：

1. 查项目内 `resources/research/`、`notes/`、`corpus_deepdive/`、MEMORY.md、index
2. 语料/文档已在本地 → grep 定位 + 按锚点抽读，**禁止**通读全文当上下文
3. 只有本地无 → 才发一次网络检索

## 2. The Fetch-Once Cache（一抓多轮复用）

网上资料的真实成本 = 抓取 token + 之后每次重抓。原则：**一次外取，多轮内用**。

1. 抓到一个网页/论文/政策页，当天就提炼：结论 3-5 条 + 关键数据 + 原文 URL
2. 落盘为本地 md（如 `resources/research/<主题>.md`），标注抓取日期与可信度
3. 之后所有轮次引用**本地文件**，永不重抓同一 URL
4. 外部知识中「会变的」（平台政策/竞品动态）标注 `expiry: 月底复查`；
   「不变的」（判例/机制/基准数据）直接沉淀，永不复查

## 3. State Handoff（状态沉淀，替代重复搬运）

每个持续项目维护一个 `状态文件`（如 `notes/协作/HANDOFF.md`），任何会话
（本 agent 或其他工具）从中读 8 段、写 1 段，替代全文重贴：

> 目标 / 重要细节（放口径与陷阱）/ 工作状态（完成/进行/被阻塞）/ 下一步 /
> 相关文件 / 用户指令约束 / 验收状态 / 待办任务

- 写状态文件时：结论一行一条，选项压缩，禁止叙述性段落
- 新会话开工 = 读状态文件 + 只读它指向的 2-3 个文件，不做全库通读
- 每完成一个里程碑，立即更新状态文件（防丢失），耗时 < 2 分钟
- 会话结束后（或每天睡前）输出一次压缩 handoff（≤2 KB）备下次冷启动

## 4. 带锚点引用（Anchored Citations）

省 token 的关键不是少读，是**读每一层的最小量**：

1. 长文档（语料/日志）按行锚引用 `<file>:行号`，之后重访只 grep 锚点行，不重读文件
2. 引文计算等代价高的工作（行号口径/计数/翻译）**落盘结论**，不重算
3. 被验证过的事实标注 `[V]`（已核）；未核实的推标注 `[推]`——后续引用不再重复验证
4. 口径差异记录在文件头一次（如「:3=单行格式」「grep/python 行号不同」），
   跨文档引用时直接读口径声明，不再踩坑

## 5. 输出纪律（Output Discipline）

- 先表格/列表后正文；每条陈述独立成立，不依赖上文
- 不复述已知内容；回答以「结论先行」开头
- 大型调研走压缩模式（如环境提供 caveman/短句模式），长输出分块
- HTML/图表只给增量结构，文字版打底（无渲染环境仍可读）

## 6. 记忆文件（MEMORY.md）

每个长期项目一个 MEMORY.md，只存**结论层**（不存过程）：

```markdown
## 已确定结论（含日期与证据强度）
- [V] 2026-10-04 主角名=江迟（v2.5 §8）
- [V] 番茄18.1套话/百章 → v2每卷≤1次（P8）
## 口径与陷阱
- 章文件:3行制，\r分段 — grep行号≠python行号
## 未决（等谁）
- §6.2适配 → 等1号重写定稿
```

更新时机：每次裁决/结论产生即追加一行；每个会话开始只读一次。

## 建议行为序列（每次会话开始 30 秒内）

1. 检查 `状态文件` 与 `MEMORY.md` 是否存在 → 有则读入状态，无则创建
2. 用户重复请求已答过的内容 → 指向 MEMORY.md 行号，不重跑
3. 会话结束前：把**新结论**追加 MEMORY.md、更新状态文件
4. 遇大型输出 → 用表格+分块，一切以「下轮不用重讲」为准

## 可选进阶（非必需，按机器能力启用）

- **mykg**（知识图谱 wiki）：适合多项目长期知识：raw→wiki 两层 + 索引互通
- **caveman CLI**：真实 token 计量（`caveman learn report`）→ 找出最大 token 消耗点
  再定向裁；未装机时跳过，本技能自身零依赖即可用
- **provider 级 prompt cache**：固定前缀（长 system prompt / 大文档）
  对支持缓存的模型按缓存价计费 —— 前面纪律做到后，效果自然叠加
