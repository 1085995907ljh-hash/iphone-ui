# 0.6.0 兼容性验证

安装器支持不代表宿主完整流程可用。本文件记录 2026-10-19 的验证范围，不将以前设计案例视为本版跨宿主验收。

| 目标 | 安装与资源读取 | 基础设计流程 | 参考图生图至 Demo 验收 |
| --- | --- | --- | --- |
| Codex | Skills CLI 本地源安装通过，24 个资源文件逐字节一致；宿主会话发现待实测 | 本版待宿主实测 | 本版待宿主实测 |
| Claude Code | Skills CLI 本地源安装通过，24 个资源文件逐字节一致；宿主会话发现待实测 | 待宿主实测 | 待宿主实测，需已配置生图能力 |
| WorkBuddy | ZIP 结构、25 个文件及 SHA-256 通过；界面导入待实测 | 待宿主实测 | 待宿主实测，需确认参考图输入与结果保存 |
| Cursor、Gemini CLI、CodeBuddy 等 | 按 Skills CLI 支持列表提供入口，未逐个实装 | 待实测 | 待实测 |

## 验收步骤

1. 安装到隔离目录，确认只有一份 iphone-ui，全部脚本、引用文件和素材齐全。
2. 在实际宿主开启新会话，调用技能，读取宿主适配说明与 HTML 模板。
3. 用简单的两页 iPhone App 需求制作低保真，在基准视口截图并查看，停在布局确认点。
4. 用户选择视觉方案后，以各页低保真作参考生成整屏图，查看并保存；缺能力时正确停在该阶段。
5. 整套效果图确认后实现交互 Demo，操作、截图、看图对照并交付。
6. 关闭后在新会话或另一宿主续接，确认页面 ID、已选版本与确认点保留。

ZIP 根目录和带 iphone-ui/ 顶层目录两种布局分别检查引用资源及 SHA-256；导入器接受哪种布局须以实际导入为准。安装检查不调用付费生图，不代替第 2–6 步。

## 本次本地证据

macOS 环境，Skills CLI 1.7.2。在独立临时项目目录执行以下命令，未改动用户级已安装技能：

```bash
npx --yes skills add <本地完整源码路径> --skill iphone-ui -a codex -a claude-code --copy -y
npx --yes skills list
```

安装器识别到一个 iphone-ui，分别写入项目 `.agents/skills/iphone-ui` 和 `.claude/skills/iphone-ui`。逐字节对比入口、许可证、来源说明及 agents/references/scripts/assets/docs 下共 24 个资源文件，均与源码一致；README 另外包含在 ZIP 中。此结果仅验证本地源码安装；远程安装和 Release 下载需要另行核对。

Skill frontmatter 校验、本地 Markdown 文件链接、截图脚本帮助入口通过。两种 ZIP 均为 25 个文件，内容与源码一致；重复构建结果一致，已有同名输出被拒绝覆盖。未运行新的设计任务、付费生图、WorkBuddy 导入、Windows 环境或各宿主界面验收。

## 发布后命令复测

从公开 GitHub 仓库执行用户级安装，以 Node 测试预加载器将 homedir 定位到独立临时目录，未更改真实用户的 HOME 或已有技能。指定 `-a codex -a claude-code` 安装成功，默认方式将资源写入临时用户 `.agents/skills/iphone-ui`，并链接到 `.claude/skills/iphone-ui`；24 个资源文件与发布源码逐字节一致。

不指定 `-a` 的通用命令在本次 Agent 执行环境中自动选择了多个目标，虽安装成功，但产生“PromptScript 不支持全局安装”的局部失败提示。因此 README 默认改为明确指定目标软件，不把 CLI 的自动选择当作稳定入口。

公开 Release 中的 WorkBuddy ZIP 已通过匿名 HTTPS 直接下载，SHA-256 与发布校验和一致，ZIP 完整且根目录含 SKILL.md。公开 Git 克隆、从克隆源码运行打包命令和 `skills update iphone-ui -g` 检查均通过；更新检查结果为已是最新版本，不代表测试了跨版本升级。

`skills remove iphone-ui -g -y` 也已在该隔离用户目录成功卸载。测试中的 `-y` 用于跳过确认，README 不带 `-y` 的卸载命令会保留交互确认。
