# token-saver-skill

「省 token 本地资料库」自建技能：**零依赖、纯 markdown、跨机器可搬运**。
把「本地优先 / 一抓多用 / 状态沉淀 / 锚点引用 / 输出纪律 / 记忆文件」六条
token 节省纪律装成任何 agent（OpenCode / Claude Code / Codex 等）都能触发的技能。

## 为什么做它

agent 会话里最大的 token 消耗不是输出，是**重复输入**：同一段语料、同一份
裁决、同一条踩过的坑，每个会话重新读一遍。本技能 = 把"重复"变成"查表":

| 纪律 | 解决什么 | 一次生效场景 |
|---|---|---|
| 1 本地优先 | 重复联网检索 | 同一问题第二次问 |
| 2 一抓多轮复用 | 网页重抓 | 平台政策/判例类资料 |
| 3 状态沉淀 HANDOFF | 重复贴上下文 | 新会话冷启动 |
| 4 锚点引用 | 通读长文件 | 语料/日志复查 |
| 5 输出纪律 | 重复叙述 | 长回答 |
| 6 MEMORY.md | 结论重推 | 裁决类知识 |

## 安装（新机器）

```bash
git clone https://github.com/<你的用户名>/token-saver-skill.git
cd token-saver-skill
# OpenCode / 通用：拷整目录进技能目录
mkdir -p ~/.agents/skills
cp -r . ~/.agents/skills/token-saver-skill
# Claude Code 用户则拷到 ~/.claude/skills/token-saver-skill
```

技能文件发现后自动生效；触发词：`save tokens`、「省 token」、`local KB`、「本地资料库」等。

## 第一次使用（每个项目 30 秒）

在项目内建两个文件（技能会帮你维护）：

```bash
# 1. 状态沉淀文件（八章结构模板见 templates/HANDOFF.template.md）
cp ~/.agents/skills/token-saver-skill/templates/HANDOFF.template.md ./notes/HANDOFF.md
# 2. 结论层记忆（模板含已确定结论/口径与陷阱/未决/已作废四区）
cp ~/.agents/skills/token-saver-skill/templates/MEMORY.template.md ./MEMORY.md
```

## 备份到 GitHub（首次，在有凭据的机器上）

```bash
cd token-saver-skill
gh repo create token-saver-skill --public --source=. --push
# 无 gh CLI 时等价做法：
#   1. GitHub 网页上新建空仓库 token-saver-skill
#   2. git remote add origin git@github.com:<你>/token-saver-skill.git
#   3. git push -u origin main
```

## 换机 / 备用恢复

```bash
git clone https://github.com/<你的用户名>/token-saver-skill.git && cd token-saver-skill
cp -r . ~/.agents/skills/token-saver-skill   # 装好即用
```

之后每次改技能（加纪律/改模板）记得 `git add -A && git commit -m "..." && git push`，
新机器 `git pull` 即同步。

## 卸载

```bash
rm -rf ~/.agents/skills/token-saver-skill
```

## 可选增强（不影响本技能运行）

- **mykg**：长期知识图谱版本地库（`raw/`+`wiki/`+索引三层），适合跨项目知识沉淀
- **caveman CLI**：真实 token 计量（`caveman learn report` 找最大消耗点再定向裁）
- 两者未装时跳过即可，本技能零依赖自洽

## 参与 / 促进进化

公开仓就是为「被人用了 → 改了 → 回流升级」而设：

- **用**：`cp -r` 本仓到你的技能目录即可（见上「安装」）。
- **改**：fork → 新建分支 → 按 Conventional Commits 提交 → 开 PR。
- **回流**：PR 通过 CI（`python3 scripts/selftest.py`）后合并，改进进入主线，所有人 `git pull` 得到升级。
- 规则见 `CONTRIBUTING.md`；请在 PR 描述里写清 **what / why / 怎么测**。

## 许可

MIT（见 `LICENSE`）。技能描述与纪律条目可自由修改，改动回流欢迎开 PR。

