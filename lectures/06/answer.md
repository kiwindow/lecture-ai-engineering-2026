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

- 取り組んだレベル：基礎
- やったこと：app/mcp_server.pyに　server.tool()(tools.get_lecture_summary)を1行追加。
　　　　　　　エージェント側 (mcp_servers.json, mcp_agent.py)は不変
- 結果：--list-tools に glossary_get_lecture_summary が増えた
　　　　変更前は、呼ばれたツールが glossary_search_glossary({'query':'第2回'})だったが、
　　　　変更後は、glossary_get_lecture_summary({'lecture':2})が呼ばれた。
　　　　ツールが返す結果も、LoRAの定義だけだったのが、第2回ファインチューニンンとLoRAから始まる要点が列挙されるようになった。
　　　　入力 5,489 → 5,944、出力　137 → 193
- 気づき・疑問：新しいツールが公開され、Agentはその新しいツールの方がqueryへの回答に適していると判断した模様。
　　　　変更前は講義資料以外の自らの知識から答えたQLoRAの話が含まれていたが、変更後は講義内容に忠実になった。
　　　　変更後にコードが壊れていないかを見るために、pytestを行ったが、無事passした。
