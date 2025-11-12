import os
import sys
import shutil

from copy_static_to_public import copy_files_recursive
from generate_page import generate_pages_recursive

def main():
    # --- 1. Basepath setup ---
    # Allow an optional CLI argument (for GitHub Pages build)
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"🏗️  Building site with basepath: {basepath}")

    # --- 2. Define directories ---
    dir_path_static = "./static"
    dir_path_output = "./docs"      # use 'docs' for GitHub Pages
    dir_path_content = "./content"
    template_path = "./template.html"

    # --- 3. Clean output directory ---
    print("🧹 Deleting output directory...")
    if os.path.exists(dir_path_output):
        shutil.rmtree(dir_path_output)

    # --- 4. Copy static assets ---
    print("📂 Copying static files to output directory...")
    copy_files_recursive(dir_path_static, dir_path_output)

    # --- 5. Generate all pages recursively ---
    print("🧩 Generating pages recursively...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_output, basepath)

    print("✅ Site build complete!")

if __name__ == "__main__":
    main()
