# spec/ — データレイアウトの一次情報（source of truth）

各データレイアウトの**正本**は、この `spec/*.json` です。
`docs/*.md` の項目テーブルと `samples/*_列名.csv` は、これらの JSON から
[`tools/build.py`](../tools/build.py) で**生成**されます。

> 📝 **今後の修正は `docs/` ではなく、この `spec/*.json` を編集してください。**
> 編集後に `python3 tools/build.py` を実行すると docs と samples が更新されます。

## ファイル対応

| spec | docs | sample (列名) |
|------|------|---------------|
| `invoice.json` | 送り状発行データレイアウト | `B2送り状発行_列名.csv` |
| `eazy.json` | EAZY送り状発行データレイアウト | `EAZY送り状発行_列名.csv` |
| `recipient.json` | お届け先データレイアウト | `B2お届け先_列名.csv` |
| `sender.json` | ご依頼主データレイアウト | `B2ご依頼主_列名.csv` |
| `item.json` | 品名データレイアウト | `B2品名_列名.csv` |

## JSON 構造

```jsonc
{
  "slug": "invoice",                 // 識別子（ファイル名と一致）
  "title": "…データレイアウト…",      // docs 見出し（生成では未使用、参照用）
  "system": "B2クラウド",
  "last_verified": "2026-06-03",     // 公式確認日（docs 冒頭に表示）
  "sources": [{ "label": "…", "url": "https://…" }],
  "file_formats": [{ "format": ".CSV", "note": "…" }],
  "required_columns": ["宅急便 必須", "クロネコゆうメール 必須"],
  "has_eazy_column": false,          // true の場合「EAZY 設定」列を生成
  "doc": "docs/….md",               // 生成先
  "sample_csv": "samples/….csv",    // 生成先（Shift_JIS/CRLF）
  "fields": [
    {
      "no": 1,                        // 項目番号（1 から連番。列記号 A,B,C… は no から自動算出）
      "name": "お客様管理番号",
      "type": "半角英数字",
      "max": "50文字",
      "required": { "宅急便 必須": "" },   // "○" / "（○）" / ""（値は表示文字列そのまま）
      "eazy": "**「1」固定**",            // has_eazy_column=true の spec のみ
      "csv_name": "予備1",                // サンプルCSV列名が name と異なる場合のみ（重複「予備」対策）
      "note": "…備考…"
    }
  ]
}
```

## 生成・検証コマンド

```bash
python3 tools/build.py           # spec → docs テーブル + samples/*_列名.csv を再生成
python3 tools/build.py --check   # 生成結果と現状に差分があれば非ゼロ終了（CI 用、書き込みなし）
```

## 注意

- `docs/*.md` の `<!-- AUTO-GENERATED … -->` 〜 `<!-- /AUTO-GENERATED -->` で囲まれた
  テーブルは自動生成です。マーカー外の本文（前提条件・注記・リンク等）は手動で編集します。
- `samples/*_記入例.csv`（ダミー値入り）は生成対象外です（手動管理）。
- 仕様を更新したら `last_verified` と出典、`CHANGELOG.md` も更新してください。
