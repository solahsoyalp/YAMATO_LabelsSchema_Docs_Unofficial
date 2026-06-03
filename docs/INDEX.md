# Document Index / ドキュメント索引

A cross-reference of the Japanese document files with English slugs and descriptions.
日本語ファイル名は URL エンコードで可読性が落ちるため、英語スラッグと説明を併記します。

## Data layouts (B2クラウド / current)

| English slug | 日本語ファイル | Description |
|--------------|----------------|-------------|
| invoice-issue | [B2送り状発行データレイアウト入出力用](B2送り状発行データレイアウト入出力用.md) | Shipping label (invoice) issue layout — 97 fields |
| eazy-invoice-issue | [EAZY送り状発行データレイアウト入出力用](EAZY送り状発行データレイアウト入出力用.md) | EAZY (oki-hai / leave-at-door) issue settings + full field list |
| recipient | [B2お届け先データレイアウト入出力用](B2お届け先データレイアウト入出力用.md) | Delivery destination (recipient) layout — 33 fields |
| sender | [B2ご依頼主データレイアウト入出力用](B2ご依頼主データレイアウト入出力用.md) | Sender layout — 11 fields |
| item | [B2品名データレイアウト入出力用](B2品名データレイアウト入出力用.md) | Item / product layout — 5 fields |

## References / 参考資料

| English slug | 日本語ファイル | Description |
|--------------|----------------|-------------|
| invoice-type-matrix | [送り状種類別必須項目](送り状種類別必須項目.md) | Required fields & constraints by invoice type |
| glossary | [用語集](用語集.md) | Glossary of B2クラウド terms |
| archive | [archive/](archive/) | Legacy B2 / B2Web / Ver.6.xx layouts |

## Sample CSVs / サンプルCSV

Header-only sample CSVs (Shift_JIS / CP932, CRLF) are under [`../samples/`](../samples/).
列名のみのサンプルCSV（Shift_JIS / CRLF）は [`../samples/`](../samples/) にあります。
