#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""GTNH 词库 -> 微软拼音自定义短语（简拼）转换器。

输出 PinyinLexTool 导入格式：  <缩写> <候选位置> <词条>

用法:
    python gen_phrases.py [词库文件] [--out phrases.txt] [--report report.md]

约定:
  * 缩写 = 每个汉字拼音首字母（小写），非汉字原样保留字母；
  * 同一缩写最多 9 条（PinyinLexTool 位置只能是 1..9），超出部分单独报告；
  * 单字词跳过（打全拼本来就只有一两下，缩写反而抢候选）；
  * 缩写长度 > 32 或首字母为 u/v 的词，用全拼兜底。
"""
import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor"))
from pypinyin import lazy_pinyin, Style  # noqa: E402

MAX_CODE_LEN = 32
MAX_POS = 9


def initials(word: str) -> str:
    parts = lazy_pinyin(word, style=Style.FIRST_LETTER, errors="default")
    code = "".join(parts).lower()
    return re.sub(r"[^a-z0-9]", "", code)


def full_pinyin(word: str) -> str:
    parts = lazy_pinyin(word, style=Style.NORMAL, errors="default")
    return re.sub(r"[^a-z0-9]", "", "".join(parts).lower())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", nargs="?", default=os.path.join(os.path.expanduser("~"), "Downloads", "GTNH_dedup.txt"))
    ap.add_argument("--out", default="phrases.txt")
    ap.add_argument("--report", default="report.md")
    args = ap.parse_args()

    raw = [line.strip() for line in open(args.source, encoding="utf-8-sig") if line.strip()]
    seen, words = set(), []
    for w in raw:
        if w not in seen:
            seen.add(w)
            words.append(w)

    groups = collections.OrderedDict()
    single, fallback = [], []
    for w in words:
        if len(w) == 1:
            single.append(w)
            continue
        code = initials(w)
        if not code or len(code) > MAX_CODE_LEN or code[0] in "uv":
            code = full_pinyin(w)
            fallback.append((w, code))
        if not code:
            continue
        groups.setdefault(code, []).append(w)

    lines, overflow = [], []
    for code, ws in groups.items():
        for pos, w in enumerate(ws, 1):
            if pos <= MAX_POS:
                lines.append((code, pos, w))
            else:
                overflow.append((code, w))

    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        for code, pos, w in lines:
            f.write(f"{code} {pos} {w}\n")

    dup = {c: ws for c, ws in groups.items() if len(ws) > 1}
    hist = collections.Counter(len(ws) for ws in groups.values())
    with open(args.report, "w", encoding="utf-8", newline="\n") as f:
        f.write("# GTNH 简拼短语生成报告\n\n")
        f.write(f"- 源文件：`{args.source}`\n")
        f.write(f"- 去重后词条：{len(words)}\n")
        f.write(f"- 写入短语：{len(lines)}\n")
        f.write(f"- 不同缩写：{len(groups)}\n")
        f.write(f"- 有重码的缩写：{len(dup)}\n")
        f.write(f"- 超出 9 个候选被丢弃：{len(overflow)}\n")
        f.write(f"- 单字跳过：{len(single)}\n")
        f.write(f"- 全拼兜底：{len(fallback)}\n\n")
        f.write("## 重码分布\n\n| 同码词数 | 缩写个数 |\n| --- | --- |\n")
        for k in sorted(hist):
            f.write(f"| {k} | {hist[k]} |\n")
        f.write("\n## 重码缩写明细（同码 ≥3）\n\n")
        for code, ws in sorted(dup.items(), key=lambda kv: -len(kv[1])):
            if len(ws) >= 3:
                f.write(f"- `{code}`：" + "、".join(ws) + "\n")
        if overflow:
            f.write("\n## 超出 9 个候选、未写入的词条\n\n")
            for code, w in overflow:
                f.write(f"- `{code}` {w}\n")
    print(f"wrote {args.out}: {len(lines)} phrases, {len(groups)} codes, {len(dup)} colliding codes, "
          f"{len(overflow)} dropped, {len(single)} single-char skipped, {len(fallback)} fallback")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
