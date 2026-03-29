import sys
import os
import datetime

# 你的记录统一存放在这个主目录下
RECORD_DIR = os.path.expanduser("~/.openclaw/workspace/my_collections")

def save_record(category, content):
    if not os.path.exists(RECORD_DIR):
        os.makedirs(RECORD_DIR)
        
    # 每个分类对应一个 Markdown 文件，例如 "电影.md", "人设图.md"
    file_path = os.path.join(RECORD_DIR, f"{category}.md")
    
    # 获取当前时间
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 将记录追加到对应的 Markdown 文件中
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"### 🕒 {now}\n")
        # 判断内容类型
        if content.startswith("http://") or content.startswith("https://"):
            # 网页链接，直接输出为超链接（无法嵌入，只能跳转）
            f.write(f"[🔗 {content}]({content})\n\n")
        elif "/" in content or "\\" in content:
            # 本地文件路径，嵌入为图片
            f.write(f"![image]({content})\n\n")
        else:
            # 纯文本内容
            f.write(f"{content}\n\n")
            
    print(f"Success: Saved to {category}.md")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python save_item.py <category> <content>")
        sys.exit(1)
        
    cat = sys.argv[1].strip()
    cont = sys.argv[2].strip()
    save_record(cat, cont)