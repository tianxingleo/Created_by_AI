import random
import math

# 假名表（平假名 + 片假名）
kana_pairs = [
    ("a", "あ", "ア"), ("i", "い", "イ"), ("u", "う", "ウ"), ("e", "え", "エ"), ("o", "お", "オ"),
    ("ka", "か", "カ"), ("ki", "き", "キ"), ("ku", "く", "ク"), ("ke", "け", "ケ"), ("ko", "こ", "コ"),
    ("sa", "さ", "サ"), ("shi", "し", "シ"), ("su", "す", "ス"), ("se", "せ", "セ"), ("so", "そ", "ソ"),
    ("ta", "た", "タ"), ("chi", "ち", "チ"), ("tsu", "つ", "ツ"), ("te", "て", "テ"), ("to", "と", "ト"),
    ("na", "な", "ナ"), ("ni", "に", "ニ"), ("nu", "ぬ", "ヌ"), ("ne", "ね", "ネ"), ("no", "の", "ノ"),
    ("ha", "は", "ハ"), ("hi", "ひ", "ヒ"), ("fu", "ふ", "フ"), ("he", "へ", "ヘ"), ("ho", "ほ", "ホ"),
    ("ma", "ま", "マ"), ("mi", "み", "ミ"), ("mu", "む", "ム"), ("me", "め", "メ"), ("mo", "も", "モ"),
    ("ya", "や", "ヤ"), ("yu", "ゆ", "ユ"), ("yo", "よ", "ヨ"),
    ("ra", "ら", "ラ"), ("ri", "り", "リ"), ("ru", "る", "ル"), ("re", "れ", "レ"), ("ro", "ろ", "ロ"),
    ("wa", "わ", "ワ"), ("wo", "を", "ヲ"), ("n", "ん", "ン"),
    ("ga", "が", "ガ"), ("gi", "ぎ", "ギ"), ("gu", "ぐ", "グ"), ("ge", "げ", "ゲ"), ("go", "ご", "ゴ"),
    ("za", "ざ", "ザ"), ("ji", "じ", "ジ"), ("zu", "ず", "ズ"), ("ze", "ぜ", "ゼ"), ("zo", "ぞ", "ゾ"),
    ("da", "だ", "ダ"), ("de", "で", "デ"), ("do", "ど", "ド"),
    ("ba", "ば", "バ"), ("bi", "び", "ビ"), ("bu", "ぶ", "ブ"), ("be", "べ", "ベ"), ("bo", "ぼ", "ボ"),
    ("pa", "ぱ", "パ"), ("pi", "ぴ", "ピ"), ("pu", "ぷ", "プ"), ("pe", "ぺ", "ペ"), ("po", "ぽ", "ポ"),
    ("kya", "きゃ", "キャ"), ("kyu", "きゅ", "キュ"), ("kyo", "きょ", "キョ"),
    ("sha", "しゃ", "シャ"), ("shu", "しゅ", "シュ"), ("sho", "しょ", "ショ"),
    ("cha", "ちゃ", "チャ"), ("chu", "ちゅ", "チュ"), ("cho", "ちょ", "チョ"),
    ("nya", "にゃ", "ニャ"), ("nyu", "にゅ", "ニュ"), ("nyo", "にょ", "ニョ"),
    ("hya", "ひゃ", "ヒャ"), ("hyu", "ひゅ", "ヒュ"), ("hyo", "ひょ", "ヒョ"),
    ("mya", "みゃ", "ミャ"), ("myu", "みゅ", "ミュ"), ("myo", "みょ", "ミョ"),
    ("rya", "りゃ", "リャ"), ("ryu", "りゅ", "リュ"), ("ryo", "りょ", "リョ"),
    ("gya", "ぎゃ", "ギャ"), ("gyu", "ぎゅ", "ギュ"), ("gyo", "ぎょ", "ギョ"),
    ("bya", "びゃ", "ビャ"), ("byu", "びゅ", "ビュ"), ("byo", "びょ", "ビョ"),
    ("pya", "ぴゃ", "ピャ"), ("pyu", "ぴゅ", "ピュ"), ("pyo", "ぴょ", "ピョ")
]

def generate_quiz(num_hira=400, num_kata=200, per_row=5):
    random.shuffle(kana_pairs)

    hira_quiz = random.choices(kana_pairs, k=num_hira)
    kata_quiz = random.choices(kana_pairs, k=num_kata)

    lines = ["# 日语假名填空题（打印版）\n\n"]
    index = 1

    def make_table(data, is_katakana=False, start_index=1):
        rows = []
        total = len(data)
        total_rows = math.ceil(total / per_row)
        for r in range(total_rows):
            row = []
            for c in range(per_row):
                idx = r * per_row + c
                if idx < total:
                    roma = data[idx][0]
                    row.append(f"{start_index+idx}. {roma}（____）")
            rows.append("| " + " | ".join(row) + " |")
        # 对齐表格分隔线
        header_line = "| " + " | ".join(["----"] * per_row) + " |"
        table = "\n".join([header_line] + rows + ["\n"])
        return table

    def make_answer(data, is_katakana=False, start_index=1):
        rows = []
        total = len(data)
        total_rows = math.ceil(total / per_row)
        for r in range(total_rows):
            row = []
            for c in range(per_row):
                idx = r * per_row + c
                if idx < total:
                    ans = data[idx][2] if is_katakana else data[idx][1]
                    row.append(f"{start_index+idx}. {ans}")
            rows.append("| " + " | ".join(row) + " |")
        header_line = "| " + " | ".join(["----"] * per_row) + " |"
        return "\n".join([header_line] + rows + ["\n"])

    # 平假名题目
    lines.append("## 一、平假名（填写假名）\n\n")
    for i in range(0, num_hira, 50):
        batch = hira_quiz[i:i+50]
        lines.append(f"### 第 {i+1}～{i+len(batch)} 题\n")
        lines.append(make_table(batch, False, i+1))
        lines.append("\n<details><summary>✅ 答案</summary>\n\n")
        lines.append(make_answer(batch, False, i+1))
        lines.append("</details>\n\n---\n")

    # 片假名题目
    lines.append("## 二、片假名（填写假名）\n\n")
    for i in range(0, num_kata, 50):
        batch = kata_quiz[i:i+50]
        start = num_hira + i + 1
        lines.append(f"### 第 {start}～{start+len(batch)-1} 题\n")
        lines.append(make_table(batch, True, start))
        lines.append("\n<details><summary>✅ 答案</summary>\n\n")
        lines.append(make_answer(batch, True, start))
        lines.append("</details>\n\n---\n")

    return "\n".join(lines)

if __name__ == "__main__":
    text = generate_quiz(400, 200)
    with open("nihongo_quiz_printable.md", "w", encoding="utf-8") as f:
        f.write(text)
    print("✅ 已生成文件：nihongo_quiz_printable.md（可直接打印A4）")
