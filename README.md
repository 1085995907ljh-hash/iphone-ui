# iPhone UI

给 Codex 使用的 iPhone App 设计技能。从产品描述出发，逐步完成页面布局、低保真、视觉方案、AI 整屏效果图和可交互手机原型，并整理供 SwiftUI 开发使用的交接包。

当前版本：**0.5.1**。默认面向美国市场，界面使用美式英语，设计说明使用对话语言；可以按用户要求调整。

## 工作流程

1. 理解产品，列出主要页面和每页任务。
2. 规划页面上、中、下内容、信息层级、图片位置和首屏密度。
3. 制作覆盖全部主要页面的灰阶低保真，等待布局确认。
4. 提供配色、字体、图片与控件的视觉方案，等待选择。
5. 使用 Image Gen，按已确认布局逐页生成整屏效果图，迭代并确认整套设计。
6. 从确认图提炼设计规范，开发 HTML/CSS/JS 可交互 Demo。
7. 对照效果图检查视觉和流程，整理开发交接包。

默认有三个确认点：低保真布局、视觉方案、高保真效果图。用户可以明确调整流程。已确认阶段和选择记录在项目的 `design/decisions.md`，避免重复确认。

## 安装

需要 Git 和可使用本地技能的 Codex。完整克隆仓库，以保留脚本、模板和参考文件：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/1085995907ljh-hash/iphone-ui.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/iphone-ui"
```

私有仓库需要先取得访问权限并完成 GitHub 身份验证。若目标目录已经存在，先检查并备份已有修改，不要直接覆盖或删除。安装后确认 `SKILL.md`、`agents`、`references`、`scripts` 和 `assets` 均存在；在新对话中调用技能。

## 使用示例

在产品项目目录中向 Codex 发送：

```text
使用 $iphone-ui，为我的 iPhone App 设计原型。
产品描述：[填写目标用户、核心任务和已有需求，或提供文档路径]
先梳理主要页面，制作完整低保真供我确认，再选择视觉方案、生成整屏效果图。
效果图确认后开发可交互 Demo，并交付 SwiftUI 开发所需的设计与状态规格。
```

已有设计时，提供文件路径和已确认的版本。技能会沿用确认记录，局部修正不需要重走全部流程。

## 交付内容

- 可打开的 HTML 手机原型及独立素材。
- `design.md` 设计规范、设计变量、页面与状态规格。
- 已确认的整屏效果图及版本记录。
- 基准视口的截图与验证证据。
- SwiftUI 交接说明与 ZIP 包。

具体内容取决于已完成的阶段。默认交付浏览器原型，不自动创建 Xcode 工程，不承诺 HTML 自动转换为原生代码。不同 iPhone 尺寸、大字和原生键盘等适配要求写入交接文档，交由原生实现验证。

## 环境与工具

| 用途 | 条件 |
| --- | --- |
| 设计与文件生成 | 能读取和写入项目文件的 Codex |
| 整屏效果图 | 可用的 Image Gen 工具及对应 imagegen 技能 |
| 方案对比页 | Python 3.10+；仓库内附生成器与 HTML 模板 |
| 浏览器截图 | Node.js 22+ 与本机 Chrome、Chromium 或 Edge |

安装本技能不会自动安装上述工具。生成器和截图脚本用法见 [工具说明](references/tools.md)。Image Gen 不可用时应说明缺口，不用网页截图冒充生成效果图。

Apple 设计约束贯穿流程。已安装的 `ios-ui-ux-reviewer` 可提供规则参考，仓库也包含后备规则快照；版本敏感规则需要核对 Apple 当前官方文档。浏览器验证不等于真实 iOS 设备验证。

## 文件说明

- [SKILL.md](SKILL.md)：技能入口和阶段约束。
- [布局与高保真](references/layout-and-hifi.md)：布局、视觉选择和整屏生成要求。
- [图片规划](references/imagery.md)：图片用途与素材约束。
- [iPhone 交互规则](references/iphone-patterns.md)：交互与状态设计。
- [验收说明](references/review.md)：视觉与流程检查。
- [SwiftUI 交接](references/swiftui-handoff.md)：交付包和原生适配要求。
- [来源记录](UPSTREAM.md)：上游来源与修改范围。

## 来源与许可

基于 `oil-oil/oil-ui` 0.18.1 的部分开源工具改编，非 Oil UI 官方版本。保留 MIT [LICENSE](LICENSE) 和来源记录，不自动同步上游。iPhone 专用流程及参考文件的改编范围见 [UPSTREAM.md](UPSTREAM.md)。
