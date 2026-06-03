#!/usr/bin/env python3
"""一回限りのブートストラップ: 現行 docs/*.md の項目テーブルを解析し spec/*.json を生成する。
以後の編集は spec/*.json を一次情報とし、tools/build.py で docs と samples を再生成する。"""
import re, json, csv, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOCS = [
    ("invoice",   "docs/B2送り状発行データレイアウト入出力用.md",   "samples/B2送り状発行_列名.csv"),
    ("eazy",      "docs/EAZY送り状発行データレイアウト入出力用.md", "samples/EAZY送り状発行_列名.csv"),
    ("recipient", "docs/B2お届け先データレイアウト入出力用.md",     "samples/B2お届け先_列名.csv"),
    ("sender",    "docs/B2ご依頼主データレイアウト入出力用.md",     "samples/B2ご依頼主_列名.csv"),
    ("item",      "docs/B2品名データレイアウト入出力用.md",         "samples/B2品名_列名.csv"),
]

def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]

for slug, docrel, csvrel in DOCS:
    text = open(os.path.join(ROOT, docrel), encoding='utf-8').read()
    lines = text.split('\n')
    title = next(l[2:].strip() for l in lines if l.startswith('# '))

    # メタ: 最終確認日・出典
    last_verified, sources = None, []
    for l in lines:
        if '最終確認日' in l:
            m = re.search(r'(\d{4}-\d{2}-\d{2})', l)
            if m: last_verified = m.group(1)
            for lbl, url in re.findall(r'\[([^\]]+)\]\((http[^)]+)\)', l):
                sources.append({"label": lbl, "url": url})
    # ファイル形式
    file_formats = []
    for i, l in enumerate(lines):
        if l.strip().startswith('## 対応ファイル形式'):
            j = i + 1
            while j < len(lines) and lines[j].startswith('|'):
                c = cells(lines[j])
                if len(c) == 2 and c[0] not in ('ファイル形式',) and not set(c[0]) <= set('-'):
                    file_formats.append({"format": c[0], "note": c[1]})
                j += 1
            break
    # 項目テーブル
    hidx = next(i for i, l in enumerate(lines)
                if l.startswith('|') and '文字形式' in l and '最大入出力文字数' in l)
    header = cells(lines[hidx])
    # required 列 = 最大入出力文字数 の後ろ〜備考 の前（EAZY 設定 を除く）
    i_max = header.index('最大入出力文字数')
    i_note = len(header) - 1  # 備考は最終列
    req_cols, eazy_col_idx = [], None
    for k in range(i_max + 1, i_note):
        if header[k] == 'EAZY 設定':
            eazy_col_idx = k
        else:
            req_cols.append(header[k])
    has_eazy = eazy_col_idx is not None

    # CSV 列名（重複「予備」等の正規化名）
    with open(os.path.join(ROOT, csvrel), encoding='cp932', newline='') as f:
        csv_names = next(csv.reader(f))

    fields, ci = [], 0
    j = hidx + 2
    while j < len(lines) and lines[j].startswith('|'):
        c = cells(lines[j])
        no = int(c[1]); name = c[2]
        req = {rc: c[i_max + 1 + idx] for idx, rc in enumerate(req_cols)}
        # eazy セルの位置（req_cols の後、備考の前）
        field = {
            "no": no,
            "name": name,
            "type": c[3],
            "max": c[4],
            "required": req,
            "note": c[i_note],
        }
        if has_eazy:
            field["eazy"] = c[eazy_col_idx]
        cn = csv_names[ci] if ci < len(csv_names) else name
        if cn != name:
            field["csv_name"] = cn
        fields.append(field); ci += 1
        j += 1

    spec = {
        "slug": slug,
        "title": title,
        "system": "B2クラウド",
        "last_verified": last_verified,
        "sources": sources,
        "file_formats": file_formats,
        "required_columns": req_cols,
        "has_eazy_column": has_eazy,
        "doc": docrel,
        "sample_csv": csvrel,
        "fields": fields,
    }
    out = os.path.join(ROOT, "spec", slug + ".json")
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f"{slug}: {len(fields)} fields, req={req_cols}, eazy={has_eazy} -> spec/{slug}.json")
