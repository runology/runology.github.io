import article_index
import sidebar_generator
import convert_obsidian_md

base_dir = "../../"
# generator = sidebar_generator.SidebarGenerator(base_dir)
# generator.save()
# print(f"已生成: {generator.sidebar_file}")

generator = article_index.ArticleIndexGenerator(base_dir)
index = generator.save_index(base_dir + ".github/filename_index.json", with_extension=True)

# Get all files
print(f"生成索引,文件路径： {index} ")

convert_obsidian_md.process_markdown_files(base_dir, write=False)
