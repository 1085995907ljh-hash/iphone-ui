# 开源来源与修改范围

本地派生 Skill，非 Oil UI 官方版本。2026-10-13 基于本机已安装的 oil-oil/oil-ui 0.18.1；上游 https://github.com/oil-oil/oil-ui ，MIT 许可见 LICENSE。

复制保留：scripts/build_explorer.py、scripts/shoot.mjs、LICENSE。改编：assets/style-explorer.html（独立品牌、手机视口、独立存储键、去掉原站链接/Logo/外部字体依赖、禁用 Pro 标记）。SKILL.md 与 references 为 iPhone 专用流程重新编写，继承比较工具、截图验证与评审方法。0.3.0 按用户确认调整为低保真布局先行、Image Gen 整屏效果图确认后开发，不再沿用先选风格的顺序。未复制 Pro、上游更新检查、推广脚本或桌面专属参考。

上游原文件 SHA-256：

- SKILL.md: 116ac740ecd105896fcd56679a7dd430a23061da00e19058abe599c0a548fb3c
- scripts/build_explorer.py: ef7cde976456159ef97153955ea81359b3d1e47bd11d6e16f3151cce0c59e379
- scripts/shoot.mjs: 3b3279db97844b79e4b7220707d655a758317c8f88c9c252be0ef9ac36c808d3
- assets/style-explorer.html: c92664e901da57024bc0069b7236ce3bfebd1cbd1f77068432751b4ff0b8819d

不自动同步上游；将来按文件差异选择性更新，保留本地约束。模板内部 desktop/mobile 字段为兼容生成器而保留，实际均为手机尺寸。

0.2.0 加入用户维护的 ios-ui-ux-reviewer 规范来源。references/apple-baseline/ 内 design-rules.md 与 audit-matrix.md 为 2026-10-13 从该本地 Skill 复制的未改动快照，规则日期为 2026-10-12，保留原文的 Apple 来源链接和适用限制。运行优先读取已安装 reviewer 的规则，快照仅作可移植后备；未复制 reviewer 的原生执行工具链。
