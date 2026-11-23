# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の glossary_search_glossary({'query': '３つのレベル'})
- STEP 3 の [tool call]：fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
- STEP 4 の [tool call]：aws_aws___search_documentation({'topics': ['general'], 'search_phrase': 'Amazon S3 versioning overview'})
- 気づき・疑問：STEP 4を実行したところ、利用したtoolは二つだった。しかし、講師の出力では三つ使われていた。そこで、複数回入力しても２回だったため、質問を変えて尋ねると三つ使われていた。ツール呼び出しの設定に問題はなかった。たまたま、二つのツールでよいとagentが判断したためだと考えた。

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
