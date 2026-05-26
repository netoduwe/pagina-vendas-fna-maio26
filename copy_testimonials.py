import os
import shutil
import hashlib

src_dir = r"H:\Meu Drive\C-GERAL NEY\01-PRODUTOS\00-FNA\DEPOIMENTOS"
dest_dir = r"c:\Users\netos\NEY\apps\imersao\vendas-fna\public\depoimentos"

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

def get_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

seen_hashes = set()
copied_count = 0
skipped_count = 0

valid_extensions = {'.png', '.jpg', '.jpeg', '.mp4', '.mov'}

for root, _, files in os.walk(src_dir):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in valid_extensions:
            filepath = os.path.join(root, file)
            file_hash = get_hash(filepath)
            
            if file_hash not in seen_hashes:
                seen_hashes.add(file_hash)
                
                # Create a safe filename to avoid issues
                safe_filename = f"depoimento_{copied_count}{ext}"
                dest_path = os.path.join(dest_dir, safe_filename)
                
                shutil.copy2(filepath, dest_path)
                copied_count += 1
            else:
                skipped_count += 1

print(f"Copiados: {copied_count}")
print(f"Repetidos ignorados: {skipped_count}")
