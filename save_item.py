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
        # 判断是否为图片路径（包含/或\）
        if "/" in content or "\\" in content:
            # 纯图片路径，直接嵌入图片
            f.write(f"![image]({content})\n\n")
        else:
            # 文本内容
            f.write(f"{content}\n\n")
            
    print(f"Success: Saved to {category}.md")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python save_item.py <category> <content>")
        sys.exit(1)
        
    cat = sys.argv[1].strip()
    cont = sys.argv[2].strip()
    save_record(cat, cont)