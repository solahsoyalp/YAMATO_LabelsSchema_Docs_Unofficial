#!/usr/bin/env python3
"""spec/*.json（一次情報）から、各 docs/*.md の項目テーブルと samples/*_列名.csv を再生成する。
使い方:  python3 tools/build.py [--check]
  --check: 生成結果と現状の差分があれば非ゼロ終了（CI 用）。書き込みは行わない。"""
import os, sys, json, csv, io, glob, difflib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECK = "--check" in sys.argv

def col(n):
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s

def build_table(spec):
    head = ["列", "項目番号", "項目名称", "文字形式", "最大入出力文字数"]
    head += spec["required_columns"]
    if spec["has_eazy_column"]:
        head.append("EAZY 設定")
    head.append("備考")
    rows = ["| " + " | ".join(head) + " |",
            "|" + "|".join(["---"] * len(head)) + "|"]
    for f in spec["fields"]:
        cells = [col(f["no"]), str(f["no"]), f["name"], f["type"], f["max"]]
        cells += [f["required"].get(rc, "") for rc in spec["required_columns"]]
        if spec["has_eazy_column"]:
            cells.append(f.get("eazy", ""))
        cells.append(f.get("note", ""))
        rows.append("| " + " | ".join(cells) + " |")
    return rows

MARK_START = "<!-- AUTO-GENERATED: spec/{slug}.json → tools/build.py で生成。直接編集しないでください -->"
MARK_END = "<!-- /AUTO-GENERATED -->"

def render_doc(path, spec):
    lines = open(path, encoding="utf-8").read().split("\n")
    ms = MARK_START.format(slug=spec["slug"])
    block = [ms] + build_table(spec) + [MARK_END]
    if ms in lines and MARK_END in lines:
        s = lines.index(ms)
        e = lines.index(MARK_END)
        return "\n".join(lines[:s] + block + lines[e + 1:])
    # 初回: 既存テーブルを検出してマーカーで包む
    hidx = next(i for i, l in enumerate(lines)
                if l.startswith("|") and "文字形式" in l and "最大入出力文字数" in l)
    end = hidx
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    return "\n".join(lines[:hidx] + block + lines[end:])

def render_csv(spec):
    header = [f.get("csv_name", f["name"]) for f in spec["fields"]]
    buf = io.StringIO()
    csv.writer(buf, lineterminator="\r\n").writerow(header)
    return buf.getvalue().encode("cp932")

def main():
    diffs = 0
    for sp in sorted(glob.glob(os.path.join(ROOT, "spec", "*.json"))):
        spec = json.load(open(sp, encoding="utf-8"))
        # 妥当性チェック
        nos = [f["no"] for f in spec["fields"]]
        assert nos == list(range(1, len(nos) + 1)), f"{spec['slug']}: 項目番号が連番でない"

        docp = os.path.join(ROOT, spec["doc"])
        new_doc = render_doc(docp, spec)
        cur_doc = open(docp, encoding="utf-8").read()
        if new_doc != cur_doc:
            diffs += 1
            if CHECK:
                print(f"[DIFF] {spec['doc']}")
            else:
                open(docp, "w", encoding="utf-8").write(new_doc)
                print(f"[WRITE] {spec['doc']}")

        csvp = os.path.join(ROOT, spec["sample_csv"])
        new_csv = render_csv(spec)
        cur_csv = open(csvp, "rb").read() if os.path.exists(csvp) else b""
        if new_csv != cur_csv:
            diffs += 1
            if CHECK:
                print(f"[DIFF] {spec['sample_csv']}")
            else:
                open(csvp, "wb").write(new_csv)
                print(f"[WRITE] {spec['sample_csv']}")

    if CHECK and diffs:
        print(f"\n{diffs} file(s) out of sync with spec/. Run: python3 tools/build.py")
        sys.exit(1)
    print("OK" if not diffs else f"\nupdated {diffs} file(s).")

if __name__ == "__main__":
    main()
