# 第三方组件与内容来源

本仓库包含或分发的第三方内容及其许可证如下。

---

## 1. 词库内容（原始词条）

- **来源**：哔哩哔哩 UP 主 **0X114-**（UID 3546888452179991）的视频
  [《GTNH词库发布，从此告别打字难》](https://www.bilibili.com/video/BV1fKxp6ZEjc/)（BV1fKxp6ZEjc）。
- **说明**：`phrases.txt` 中的词条来源于该作者整理的 GTNH 词库，本项目只做
  "全拼词条 → 首字母缩写短语"的格式转换，**不主张对词条内容的著作权**。
- **分发方式**：原始 txt 由原作者通过蓝奏云链接分发，本仓库不二次分发原文件，
  使用者请从原视频简介处获取。
- 如原作者对本仓库的转换结果有异议，请提 Issue，会立即移除相关内容。

## 2. PinyinLexTool

- **项目**：<https://github.com/mchudie/PinyinLexTool>
- **作用**：读写微软拼音 `ChsPinyinEUDPv1.lex`，实现自定义短语的批量导入 / 导出 / 备份。
- **分发**：`tools/PinyinLexTool.exe` 不随仓库提交；Release 中的整合包内含该二进制，
  依据其 MIT 许可证原样分发，未做任何修改。

```
MIT License

Copyright (c) 2025 mchudie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 3. pypinyin

- **项目**：<https://github.com/mozillazg/python-pinyin>
- **作用**：`gen_phrases.py` 用它把汉字转成拼音首字母。
- **许可证**：MIT（仅作为 Python 依赖在运行时使用，本仓库不包含其代码）

```
The MIT License (MIT)

Copyright (c) 2012 mozillazg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 4. 游戏与商标

"GregTech: New Horizons"、"Minecraft" 及相关名称是各自权利人的商标或作品名称。
本项目与 GTNH 开发组、Mojang、微软公司均无隶属关系，仅为玩家自制工具。
