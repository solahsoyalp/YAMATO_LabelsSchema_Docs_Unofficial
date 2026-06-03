# YAMATO_LabelsSchema_Docs_Unofficial

ヤマト運輸 **B2クラウド** のCSVデータレイアウト（非公式まとめ）
*Unofficial reference for the CSV data layouts of YAMATO Transport's "B2 Cloud" shipping system.*

## 概要 / Overview

このリポジトリは、ヤマト運輸の送り状発行システム **B2クラウド** で取り扱う各種CSVデータレイアウトを整理し、参照できるようにしたものです。現行のB2クラウド版レイアウトに準拠しています。

This repository organizes the CSV data layouts used by YAMATO Transport's "B2 Cloud" shipping-label system, based on the current B2 Cloud specification. All documents are in Japanese; see [`docs/INDEX.md`](docs/INDEX.md) for an English index.

## 免責事項 / Disclaimer

- このリポジトリの内容は**非公式**のものであり、ヤマト運輸株式会社とは一切関係ありません。
- ヤマト運輸の公式な仕様やデータレイアウトについては、[公式レイアウト（B2クラウド）](https://bmypage.kuronekoyamato.co.jp/bmypage/pdf/new_exchange1.pdf) をご確認ください。
- 本リポジトリの内容の正確性については保証できません。ご利用の際は自己責任でお願いします。
- 各資料は記載の「最終確認日」時点の公式情報に基づきます。仕様は変更される可能性があります。

## 商標・著作権 / Trademarks & License

- 「ヤマト運輸」「クロネコ」「クロネコヤマト」「B2」「B2クラウド」「EAZY」「ネコポス」「宅急便」等の名称・ロゴは、ヤマト運輸株式会社又は関連会社の商標又は登録商標です。これらの権利は各権利者に帰属します。
- 本リポジトリの記述・編集物は [CC BY 4.0](LICENSE) の下で提供されます（商標は対象外）。

## ファイル一覧 / Documents

### データレイアウト（現行 B2クラウド）
- **[B2送り状発行データレイアウト入出力用](docs/B2送り状発行データレイアウト入出力用.md)** - 送り状発行データの入出力フォーマット（全97項目）。
- **[EAZY送り状発行データレイアウト入出力用](docs/EAZY送り状発行データレイアウト入出力用.md)** - EAZY（置き配）発行時の項目設定・必須条件と全項目一覧。
- **[B2お届け先データレイアウト入出力用](docs/B2お届け先データレイアウト入出力用.md)** - お届け先データの入出力フォーマット（全33項目）。
- **[B2ご依頼主データレイアウト入出力用](docs/B2ご依頼主データレイアウト入出力用.md)** - ご依頼主データの入出力フォーマット（全11項目）。
- **[B2品名データレイアウト入出力用](docs/B2品名データレイアウト入出力用.md)** - 品名データの入出力フォーマット（全5項目）。

### 参考資料 / References
- **[送り状種類別 必須項目早見表](docs/送り状種類別必須項目.md)** - 送り状種類ごとの必須項目・制約。
- **[用語集](docs/用語集.md)** - 主な用語の説明。
- **[ドキュメント索引（INDEX）](docs/INDEX.md)** - 英語スラッグ付きの索引。
- **[アーカイブ（旧B2 / B2Web / Ver.6.xx版）](docs/archive/)** - 過去版レイアウト。

## サンプルCSV / Sample CSVs

各資料の項目順に並べたサンプルCSVです。`samples/` に格納しています。

| 資料 | 列名のみ | 記入例 |
|------|---------|--------|
| 品名（5列） | [B2品名_列名.csv](samples/B2品名_列名.csv) | [B2品名_記入例.csv](samples/B2品名_記入例.csv) |
| お届け先（33列） | [B2お届け先_列名.csv](samples/B2お届け先_列名.csv) | [B2お届け先_記入例.csv](samples/B2お届け先_記入例.csv) |
| ご依頼主（11列） | [B2ご依頼主_列名.csv](samples/B2ご依頼主_列名.csv) | [B2ご依頼主_記入例.csv](samples/B2ご依頼主_記入例.csv) |
| 送り状発行（97列） | [B2送り状発行_列名.csv](samples/B2送り状発行_列名.csv) | [B2送り状発行_記入例.csv](samples/B2送り状発行_記入例.csv) |
| EAZY送り状発行（97列） | [EAZY送り状発行_列名.csv](samples/EAZY送り状発行_列名.csv) | [EAZY送り状発行_記入例.csv](samples/EAZY送り状発行_記入例.csv) |

> 補足：
> - 文字コードは **Shift_JIS（CP932）**、改行コードは **CRLF** です（B2クラウドの取込仕様に合わせています）。GitHub上では文字化けして表示される場合がありますが、ダウンロードすればそのままB2クラウドに取り込めます。
> - 記入例の値はすべて**ダミー**です。
> - 「予備」項目が複数あるため、サンプル内では `予備1`／`予備2`／`予備3` と区別しています（実レイアウト上はいずれも「予備」）。

## 利用方法 / Usage

1. リポジトリをクローンします。
   ```bash
   git clone https://github.com/solahsoyalp/YAMATO_LabelsSchema_Docs_Unofficial.git
   ```
2. `docs` フォルダ内の各ファイルを参照してください。索引は [`docs/INDEX.md`](docs/INDEX.md)。

## フィードバック / Contributing

本リポジトリの内容についてのフィードバックや修正提案は歓迎します。[CONTRIBUTING.md](CONTRIBUTING.md) を参照のうえ、Issue や Pull Request を通じてご連絡ください。変更履歴は [CHANGELOG.md](CHANGELOG.md) にまとめています。
