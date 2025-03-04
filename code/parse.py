import os
import markdown

def parse_folder_and_create_markdown(base_folder):
    md_content = []

    for subfolder_name in os.listdir(base_folder):
        subfolder_path = os.path.join(base_folder, subfolder_name)
        if os.path.isdir(subfolder_path):
            pdf_filename = subfolder_name + ".pdf"
            pdf_path = os.path.join(subfolder_path, pdf_filename)

            if os.path.exists(pdf_path):
                # new_pdf_path = pdf_path[]
                link = f"[{subfolder_name}](https://kreier.github.io/force-curves{pdf_path[2:].replace('\\', '/').replace(' ', '%20')}) |"
                md_content.append(link)

    markdown_content = "\n".join(md_content)
    with open("output.md", "w") as md_file:
        md_file.write(markdown_content)

# Example usage
base_folder_path = "../_data"
parse_folder_and_create_markdown(base_folder_path)
