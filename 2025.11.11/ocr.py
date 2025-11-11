import ocrmypdf
import os
import sys # 引入 sys 用于处理 ExitCode

# 注意：为了解决 TypeError，我们移除了所有具体的 ocrmypdf.exceptions 捕获。

def ocr_pdf_with_ocrmypdf(input_pdf_path, output_pdf_path, language='chi_sim+jpn'):
    """
    使用 ocrmypdf 对图片 PDF 进行 OCR 处理，并生成可搜索的 PDF。

    :param input_pdf_path: 输入图片 PDF 的路径
    :param output_pdf_path: 输出可搜索 PDF 的路径
    :param language: OCR 语言代码（多语言用加号连接，例如 'chi_sim+jpn'）
    """
    print(f"📄 正在处理文件: {input_pdf_path}")
    print(f"👅 使用语言模型: {language}")
    
    try:
        # 核心 OCR 调用
        ocrmypdf.ocr(
            input_pdf_path,
            output_pdf_path,
            language=language,
            force_ocr=True,       # 强制运行 OCR
            output_type='pdfa',   # 生成 PDF/A 
            # 删除了 optimize_images 参数，因为它在你的 ocrmypdf 版本中不被识别
        )
        print(f"✅ 恭喜！成功生成可搜索 PDF: {output_pdf_path}")
        
    except Exception as e:
        # 捕获所有可能的错误 (包括 MissingDependencyError, ExitCode, 和 ValueError)
        print("\n" + "="*50)
        print("❌ OCR 任务失败！")
        
        # 尝试提供更清晰的错误信息
        error_message = str(e)
        if "unrecognized arguments" in error_message:
            print(f"错误类型: 参数不被识别 (可能是库版本过旧)。")
            print("请尝试更新 ocrmypdf 库，或删除不被支持的参数。")
        elif "Could not find program" in error_message:
            program_name = error_message.split("'")[1]
            print(f"错误类型: 外部程序缺失 ({program_name})。")
            print("请确保 Tesseract 和 Ghostscript 已安装并添加到系统 PATH。")
        elif "language data for the following requested languages" in error_message:
            print("错误类型: Tesseract 语言包缺失。")
            print(f"请将 {language}.traineddata 文件放入 Tesseract 的 tessdata 目录。")
        else:
            print(f"发生未知错误: {e}")
            
        print("="*50 + "\n")


# --- 脚本入口 ---

# 设定输入和输出文件名
input_file = "scanned_input.pdf"
output_file = "searchable_output.pdf"

# 检查输入文件是否存在
if os.path.exists(input_file):
    # 调用函数，使用中文简体和日文语言包
    ocr_pdf_with_ocrmypdf(input_file, output_file)
else:
    print(f"🚫 错误：找不到输入文件！")
    print(f"请将您的图片 PDF 文件命名为 '{input_file}' 并放在脚本同一目录下。")