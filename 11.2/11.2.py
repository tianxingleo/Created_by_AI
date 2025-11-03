import random
import math

# 假名表（平假名, 片假名）
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

def chunk_list(lst, size):
    """将列表按 size 切块，返回块列表"""
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def make_markdown_table(cells, per_row):
    """
    cells: 列表，每个元素是要放入表格单元格的字符串
    per_row: 每行单元格数
    返回完整的 markdown 表格文本（包含分隔线），会在最后一行填充空单元格以保证列数一致
    """
    rows = chunk_list(cells, per_row)
    # 填充最后一行空单元格（保证每行都有 per_row 个单元格）
    if rows:
        last = rows[-1]
        if len(last) < per_row:
            last += [""] * (per_row - len(last))
            rows[-1] = last
    # 构造表格
    header = "| " + " | ".join(["题目"] * per_row) + " |"
    sep = "| " + " | ".join(["---"] * per_row) + " |"
    body_lines = []
    for r in rows:
        body_lines.append("| " + " | ".join(r) + " |")
    return "\n".join([header, sep] + body_lines) + "\n"

def generate_quiz(num_hira=400, num_kata=200, per_row=5):
    random.shuffle(kana_pairs)
    # 随机选题
    hira_quiz = random.choices(kana_pairs, k=num_hira)
    kata_quiz = random.choices(kana_pairs, k=num_kata)

    lines = []
    lines.append("# 日语假名填空题（打印版）\n")
    # 提示：打印时请使用等宽字体（Consolas / Courier New）以保证对齐
    lines.append("_提示：打印或导出为 PDF 时建议使用等宽字体 (Consolas / Courier New)。_\n\n")

    # 平假名部分
    lines.append("## 一、平假名（填写假名）\n")
    # 分 50 题一组生成（每组一个可折叠的题块 + 答案）
    for group_start in range(0, num_hira, 50):
        group = hira_quiz[group_start:group_start+50]
        abs_start_no = group_start + 1
        # 构造题目单元格，格式 "编号. 罗马音（____）"
        cells = [f"{abs_start_no + i}. {group[i][0]}（____）" for i in range(len(group))]
        table_md = make_markdown_table(cells, per_row)
        lines.append(f"### 第 {abs_start_no}～{abs_start_no+len(group)-1} 题\n")
        lines.append(table_md)
        # 答案（折叠）
        answer_cells = [f"{abs_start_no + i}. {group[i][1]}" for i in range(len(group))]
        answer_table_md = make_markdown_table(answer_cells, per_row)
        lines.append("<details><summary>✅ 答案（点击展开）</summary>\n\n")
        lines.append(answer_table_md)
        lines.append("</details>\n\n---\n")

    # 片假名部分
    lines.append("## 二、片假名（填写假名）\n")
    # 题号从 num_hira+1 开始
    for group_idx, group_start in enumerate(range(0, num_kata, 50)):
        group = kata_quiz[group_start:group_start+50]
        abs_start_no = num_hira + group_start + 1
        cells = [f"{abs_start_no + i}. {group[i][0]}（____）" for i in range(len(group))]
        table_md = make_markdown_table(cells, per_row)
        lines.append(f"### 第 {abs_start_no}～{abs_start_no+len(group)-1} 题\n")
        lines.append(table_md)
        # 答案（片假名）
        answer_cells = [f"{abs_start_no + i}. {group[i][2]}" for i in range(len(group))]
        answer_table_md = make_markdown_table(answer_cells, per_row)
        lines.append("<details><summary>✅ 答案（点击展开）</summary>\n\n")
        lines.append(answer_table_md)
        lines.append("</details>\n\n---\n")

    return "\n".join(lines)

if __name__ == "__main__":
    md_text = generate_quiz(400, 200, per_row=5)
    with open("nihongo_quiz_printable_fixed.md", "w", encoding="utf-8") as f:
        f.write(md_text)
    print("已生成：nihongo_quiz_printable_fixed.md")
