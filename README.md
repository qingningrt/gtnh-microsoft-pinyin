# GTNH 微软拼音词库（简拼）

把 GTNH 的 **1664 条**词条（元素、合金、单质、化合物、机器零件……）做成**微软拼音的自定义短语**：
输入每个字的首字母，词条直接出现在候选里，不用再一个字一个字打全拼。

> 适合：在 QQ / 群聊 / 百科里频繁提到 GTNH 材料名的玩家。
> 不适合：用搜狗、微信、百度、Rime 输入法的玩家（见[常见问题](#常见问题)）。

[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%201709%2B%20%7C%2011-lightgrey.svg)](#系统要求)
[![IME](https://img.shields.io/badge/IME-%E5%BE%AE%E8%BD%AF%E6%8B%BC%E9%9F%B3-green.svg)](#系统要求)
[![Phrases](https://img.shields.io/badge/phrases-1664-brightgreen.svg)](phrases.txt)

---

## 效果

| 输入 | 候选 |
| --- | --- |
| `qys` | 1 氢元素　2 铅元素 |
| `hys` | 1 氦元素　2 钬元素　3 铪元素　4 𬭶元素　5 黑曜石 |
| `lys` | 1 锂元素　2 铝元素　3 磷元素 … 9 镥元素（数字键选） |
| `adt` | 阿迪特 |
| `ys`  | 1 圆石　2 荧石　3 乙酸　4 盐水 |

规则很简单：**词条的每个汉字取拼音首字母**，小写连写。长的词条也因此只要 4~6 个字母。

## 为什么导入原来的词库还得打全拼

微软拼音有**两套**东西存在同一个文件里：

- **自学习词库**（`全拼 + 词条`）：只是让输入法"认识"这个词，**照样得打全拼**
- **自定义短语**（`缩写 + 位置 + 词条`）：这才产生简拼

大部分"GTNH 词库"给的是前者，所以导入后没有任何缩写效果。本仓库做的是后者。

## 快速开始

1. 到 [Releases](../../releases) 下载 `GTNH微软拼音简拼包.zip`，解压到任意目录
2. 双击 **`1-一键导入.bat`**（会先自动备份你现有的自定义短语）
3. **切换一次输入法**（`Alt+Shift` 或 `Win+空格`，切到英文再切回微软拼音）
4. 记事本里输入 `qys`，出"氢元素"就成功了

想撤销：双击 **`9-还原备份.bat`**。

> 或者手动导入（已有 PinyinLexTool 的人）：
> ```powershell
> PinyinLexTool.exe import phrases.txt --verbose
> ```

## 📺 我的视频教程

> 视频制作中，**发布后这里补链接**。

<!-- 发布后：把下面这行的“待发布”换成 B站链接，例如
> 📺 [【GTNH】微软拼音简拼词库，从此告别打字难](https://www.bilibili.com/video/BVxxxxxxxxxx)
-->
> 📺 视频教程：**待发布**

## 词库来源与致谢

- **原始词库**：B 站 UP 主 [@0X114-](https://space.bilibili.com/3546888452179991) 的视频
  [《GTNH词库发布，从此告别打字难》](https://www.bilibili.com/video/BV1fKxp6ZEjc/)
  （BV1fKxp6ZEjc）。原始 txt 由作者通过蓝奏云分发，本仓库**不再二次分发原文件**，请从原视频简介获取。
- **格式转换工具**：[PinyinLexTool](https://github.com/mchudie/PinyinLexTool)（MIT，作者 mchudie）
  直接读写微软拼音的 `ChsPinyinEUDPv1.lex`，本项目的导入、备份、校验都靠它。
- **拼音处理**：[pypinyin](https://github.com/mozillazg/python-pinyin)（MIT）
- **游戏**：[GT: New Horizons](https://www.gtnewhorizons.com/)

各方的许可证与版权声明见 [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)。

## 词库统计

| 项目 | 数值 |
| --- | --- |
| 去重后词条 | 1689 |
| 写入短语 | **1664** |
| 不同缩写 | 1472 |
| 有重码的缩写 | 93 |
| 因超过 9 个候选位被丢弃 | 7（`lys` 6 条、`tys` 1 条，见 [重码清单](docs/重码清单.md)） |
| 单字词跳过 | 18（氢、氧、铁……打两三个字母就出来了，做缩写反而抢候选） |

## 自己重新生成

词库更新后想重新生成短语，需要 Python 3：

```powershell
pip install pypinyin
python gen_phrases.py GTNH_dedup.txt --out phrases.txt
```

脚本会同时输出 `report.md`（重码明细、被丢弃词条）。规则：

- 缩写 = 每个汉字拼音首字母（小写）；非汉字原样保留字母
- 同一缩写最多 9 条（PinyinLexTool 的位置只能 1~9），按原词库顺序占位
- 缩写超过 32 字母、或以 `u`/`v` 开头时，用全拼兜底

## 常见问题

**只对微软拼音有效？**
是的。本仓库改的是 `%APPDATA%\Microsoft\InputMethod\Chs\ChsPinyinEUDPv1.lex`，
搜狗 / 微信 / 百度 / Rime 都不读这个文件，需要各自的方案。

**系统要求**
Windows 10 1709 及以上、Windows 11。Windows 10 1607/1703 的 `.lex` 格式不同，不支持。

**杀软报警**
`PinyinLexTool.exe` 是 MIT 开源工具，因为它直接改输入法数据文件，容易被误报。
可以自行到 [Releases](https://github.com/mchudie/PinyinLexTool/releases) 下载比对。

**导入失败 / 提示无权限**
多半是别的程序占着输入法。关掉正在输入的聊天窗口再试；
脚本在直接写入失败时会自动退化到"复制 → 导入 → 覆盖"的流程。

**重码太多怎么办**
93 个缩写有重码，常见的是元素名（`lys` 一组 15 个）。要么用数字键选，
要么用 `gen_phrases.py` 自己改规则（比如只保留常用词、或给元素换更长的缩写）。

**会覆盖我原来的自定义短语吗**
不会。导入是合并写入，且脚本执行前会备份到 `backup\` 目录（带时间戳，可保留多份）。

## 目录结构

```
.
├── 1-一键导入.bat        # 备份 + 导入（主入口）
├── 9-还原备份.bat        # 用最近备份还原
├── phrases.txt           # 1664 条短语，格式：缩写 位置 词条
├── gen_phrases.py        # 词库 → 短语 的转换脚本
├── docs/重码清单.md       # 重码统计与被丢弃词条
├── tools/                # 放 PinyinLexTool.exe（不随仓库分发）
├── THIRD-PARTY-NOTICES.md
└── LICENSE
```

## 免责声明

非官方项目，与 GTNH 开发组、微软、B 站 UP 主均无隶属关系。
词库内容的版权归原始整理者（@0X114-）所有，本仓库只做格式转换与工具链整理；
如原作者有异议，会立即停止分发相关内容。

## License

本仓库的代码（脚本、bat、文档）以 [MIT](LICENSE) 发布。
词库内容与第三方二进制遵循各自的许可证，见 [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)。
