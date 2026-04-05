import argparse
import os
import datetime

# 你的记录统一存放在这个主目录下
RECORD_DIR = os.path.expanduser("~/.openclaw/workspace/my_collections")

def save_record(category, content, image_paths_str=None):
    if not os.path.exists(RECORD_DIR):
        os.makedirs(RECORD_DIR)

    # 每个分类对应一个 Markdown 文件，例如 "电影.md", "人设图.md"
    file_path = os.path.join(RECORD_DIR, f"{category}.md")

    # 获取当前时间
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # 解析图片路径列表（用分号分隔）
    image_paths = []
    if image_paths_str:
        image_paths = [p.strip() for p in image_paths_str.split(";") if p.strip()]

    # 将记录追加到对应的 Markdown 文件中
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"### 🕒 {now}\n")

        # 写入文本内容
        if content.startswith("http://") or content.startswith("https://"):
            # 网页链接，输出为超链接
            f.write(f"[🔗 {content}]({content})\n\n")
        else:
            # 纯文本内容（描述）
            f.write(f"{content}\n\n")

        # 写入图片（如果有）
        for img_path in image_paths:
            f.write(f"![image]({img_path})\n\n")

    print(f"Success: Saved to {category}.md")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="智能灵感收集器 - 保存收藏项目")
    parser.add_argument("category", help="分类名称，如：电影、人设、构图参考")
    parser.add_argument("content", help="记录内容（文本描述或链接）")
    parser.add_argument("--images", help="图片本地路径，多个路径用 ; 分号分隔", default=None)

    args = parser.parse_args()
    save_record(args.category, args.content, args.images)