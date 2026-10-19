"""第1回: 履歴を持ったLLMと対話するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする

過去の対話を記憶するように history = [] をつけた

講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse

from google import genai
from google.genai import errors, types

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"

history: list[types.Content] = []

def ask(question: str) -> str:   
    client = genai.Client(api_key=get_api_key()) 
    history.append(types.Content(role="user", parts=[types.Part(text=question)]))
    response = client.models.generate_content(model=MODEL, contents=history)
    history.append(types.Content(role="model", parts=[types.Part(text=response.text)]))
    usage = response.usage_metadata
    if usage is not None:
        print(
            f"[tokens] input: {usage.prompt_token_count}, "
            f"output: {usage.candidates_token_count}"
        )

    return response.text


def main() -> None:
    parser = argparse.ArgumentParser(description="履歴を持つLLMとの対話になる")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    print(f"[model] {MODEL}")
    print("(空行または'q'で終了)\n")

    question = args.question
    while True:
        print(f"[質問] {question}\n")
        try:
            print(ask(question))
        except errors.APIError as e:
            print(api_error_message(e.code, e.message))
            raise SystemExit(1)

        question = input("\n> ").strip()
        if question in ("", "q", "quit"):
            break


if __name__ == "__main__":
    main()

