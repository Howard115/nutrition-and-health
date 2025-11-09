import re

with open("口頭報告.md", "r", encoding="utf-8") as f:
    content = f.read()

# content="test 123 中文"
chinese_chars = re.findall(r"[\u4e00-\u9fff]", content)
count = len(chinese_chars)
print(f"中文字數: {count}")
