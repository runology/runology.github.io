import argparse
import os

import convert_obsidian_md
import article_index
import sidebar_generator

"""
约定规则：
1. 每个子模块，如English，高内聚，和其他模块尽量做到0耦合。
- 模块内的image统一存放在模块目录/_images下，每个模型块都有
- _images因格式统一，双链图片URL的拼接统一只在前面加上../_images 
- 其他双链 仍然使用统一逻辑转标准markdown链接
"""

if __name__ == "__main__":


    parser = argparse.ArgumentParser(description='Convert Obsidian links to standard markdown links')
    parser.add_argument('--dir', default='.', help='Root directory to scan (default: current directory)')
    args = parser.parse_args()
    print(args.dir)

    base_dir = args.dir

    # generator = sidebar_generator.SidebarGenerator(base_dir)
    # generator.save()
    # print("已生成sidebar和navbar")

    generator = article_index.ArticleIndexGenerator(base_dir)
    index_path = os.path.join(base_dir, '.github', 'filename_index.json')
    index = generator.save_index(index_path, with_extension=True)

    # Get all files
    print(f"生成索引,文件路径： {index} ")

    write_doc = convert_obsidian_md.process_markdown_files(base_dir)
    print(f"重新生成链接,更新文档数： {write_doc} ")
