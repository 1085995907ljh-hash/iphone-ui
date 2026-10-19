# 对比页与截图

继承 Oil UI 的生成器与截图工具。以 SKILL.md 所在目录确定绝对 Skill 路径，产物放在任务目录，不依赖某个 Agent 的安装目录。生成器需要 Python 3.10+；附带截图脚本需要 Node 22+ 和本机 Chromium 系浏览器。宿主已有浏览器工具时可以直接截图和操作，无需为此安装另一套运行时；输出仍需满足 references/review.md 的证据要求。失败时按 [宿主适配](agent-compatibility.md) 说明工具缺口。

## 对比页

每个候选先有独立可显示的 HTML。静态 HTML 可内嵌 CSS；相对图片等资源须位于 manifest 目录内。默认不执行候选脚本；内联交互小样可设 interactive:true。依赖服务器的完整原型使用 kind:url，地址仅限本机，不能直接嵌入一个空挂载节点。

```json
{
  "schemaVersion": 1,
  "lang": "zh",
  "project": "App 名称",
  "brief": "所有方案一致的任务",
  "round": "01 · 低保真布局",
  "candidates": [{
    "id": "a",
    "name": "布局方案名称",
    "concept": "指导设计取舍的意图",
    "typography": "实际字体与层级",
    "palette": ["#FFFFFF", "#111111", "#E5E5E5"],
    "traits": ["可观察差异"],
    "kind": "html",
    "source": "a.html"
  }]
}
```

运行：`python3 <skill>/scripts/build_explorer.py <project>/manifest.json --output <project>/style-explorer.html`。默认拒绝覆盖，同轮明确更新可用 --force。源候选不可覆盖。

生成器的文件名和 palette 字段属于继承的工具格式，不意味着先选配色或风格。低保真使用灰阶；高保真轮的候选 HTML 应展示 Image Gen 实际输出的效果图，并链接整套页面与单屏原图，不得用 HTML 界面截图替代生成图。工具容器不能决定设计阶段顺序，以 SKILL.md 为准。

手机比较尺寸为 390×844 与 375×667，属于逻辑测试视口而非特定设备认证。并排视图会缩放，文字判断须进入单张的实际尺寸。外壳支持选择/复制，浏览器选择不会自动写回项目；按用户回复更新 decisions.md 后继续对应轮次。

kind:url 候选应在 manifest 顶层提供 serve.command、serve.cwd、serve.url。打开以前确认服务属于当前项目；端口冲突不随意终止其他服务。

## 截图

`node <skill>/scripts/shoot.mjs <url或文件> --size 375x667,390x844 --out <project>/design/evidence`

`--full` 看整页，`--zoom 2` 为高像素比细节；`--steps 'click "[data-action=next]"' --record --entry` 保存出场与操作帧。更多参数见 --help。检查 report.json 的控制台、溢出与对比度提示，再实际看图片。截图工具不能替代真实 iOS 设备验收。
