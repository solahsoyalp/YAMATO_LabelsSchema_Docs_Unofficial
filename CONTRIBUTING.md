# コントリビューションガイド

本リポジトリは、ヤマト運輸 B2クラウドのデータレイアウトを整理した**非公式**の参考資料です。誤りの報告や改善提案を歓迎します。

## フィードバック・修正提案の方法

### Issue（報告・提案）
誤りや更新の報告は Issue でお願いします。次の情報があると助かります。

- **対象資料 / 項目番号・列**（例: 送り状発行 項目33 / AG列「記事」）
- **現状の記載**
- **正しいと思われる内容**
- **公式の出典**（公式PDF・FAQのURL、確認日など）

### Pull Request（修正）
1. リポジトリを Fork し、ブランチを作成します。
2. **データレイアウトの修正は `spec/*.json` を編集します**（`docs/*.md` の項目テーブルは生成物です）。
3. `python3 tools/build.py` を実行して `docs/` と `samples/` を再生成します。
4. 可能なら出典を明記し、PR を作成します（テンプレートに沿って記入）。

> 📌 **データの一次情報は [`spec/*.json`](spec/) です。**
> `docs/*.md` の `<!-- AUTO-GENERATED -->` で囲まれた項目テーブルと `samples/*_列名.csv` は
> `spec` から [`tools/build.py`](tools/build.py) で生成されます。詳細は [`spec/README.md`](spec/README.md)。
> マーカー外の本文（前提条件・注記など）は `docs/` で直接編集します。

## 記載ルール

- **出典を必ず確認**：ヤマト運輸の公式PDF / 公式FAQ を一次情報とします。
  - 現行（B2クラウド）: <https://bmypage.kuronekoyamato.co.jp/bmypage/pdf/new_exchange1.pdf>
- **編集対象**：データレイアウトは `spec/*.json` を編集し、`tools/build.py` で再生成します（`docs/` の表を直接編集しない）。
- **確認日を更新**：資料を更新したら、`spec/*.json` の `last_verified`・出典と `CHANGELOG.md` を更新してください。
- **整合性**：`python3 tools/build.py --check` が通る状態（spec と docs/samples が同期）でコミットしてください。
- **サンプルCSV**：文字コードは **Shift_JIS(CP932)**、改行は **CRLF** を維持してください（`.gitattributes` で管理）。
- **項目名・文字数・必須区分**は公式表記に合わせてください（「○」必須、「（○）」条件付き必須）。

## 行動規範

建設的で敬意あるやり取りをお願いします。商標（ヤマト運輸・クロネコ・EAZY 等）の権利は各権利者に帰属します（[LICENSE](LICENSE) 参照）。
