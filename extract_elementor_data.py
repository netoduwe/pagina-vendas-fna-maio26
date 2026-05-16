import json
import os

json_path = r'c:\Users\netos\Downloads\elementor-26077-2026-05-16.json'
output_path = r'c:\Users\netos\NEY\docs\elementor_extracted_content.md'

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

md_content = ["# Conteúdo Oficial Extraído do Elementor (FNA T8)\n"]

def parse_elements(elements, depth=1):
    res = []
    for el in elements:
        settings = el.get('settings', {})
        wtype = el.get('widgetType', el.get('elType', ''))
        
        title = settings.get('title', '')
        editor = settings.get('editor', '')
        image = settings.get('image', {}).get('url', '')
        items = settings.get('items', [])
        icon_list = settings.get('icon_list', [])
        carousel = settings.get('carousel', [])
        carousel_items = settings.get('carousel_items', [])
        text = settings.get('text', '')
        link = settings.get('link', {}).get('url', '')
        
        if title:
            res.append(f"### Título ({wtype}):\n```html\n{title}\n```\n")
        if editor:
            res.append(f"### Texto ({wtype}):\n```html\n{editor}\n```\n")
        if image:
            res.append(f"### Imagem ({wtype}):\n{image}\n")
        if text:
            res.append(f"### Botão ({wtype}): `{text}` -> `{link}`\n")
            
        if icon_list:
            res.append(f"### Lista de Ícones ({wtype}):\n")
            for item in icon_list:
                res.append(f"- {item.get('text', '')}\n")
            res.append("\n")
            
        if items:
            res.append(f"### Accordion/Items ({wtype}):\n")
            for item in items:
                res.append(f"#### {item.get('item_title', item.get('title', ''))}\n{item.get('item_description', item.get('description', ''))}\n")
            res.append("\n")
            
        if carousel:
            res.append(f"### Carrossel de Imagens ({wtype}):\n")
            for item in carousel:
                res.append(f"- {item.get('url', '')}\n")
            res.append("\n")
            
        if carousel_items:
            res.append(f"### Carrossel de Trilhas ({wtype}):\n")
            for item in carousel_items:
                res.append(f"- {item.get('slide_title', '')}\n")
            res.append("\n")
            
        if el.get('elements'):
            res.extend(parse_elements(el.get('elements'), depth + 1))
            
    return res

for col in data.get('content', []):
    sec_title = col.get('settings', {}).get('_title', col.get('id', 'Seção Sem Título'))
    md_content.append(f"\n## Seção: {sec_title}\n")
    bg_img = col.get('settings', {}).get('background_image', {}).get('url', '')
    if bg_img:
        md_content.append(f"**Fundo da Seção:** {bg_img}\n\n")
        
    elements = col.get('elements', [])
    md_content.extend(parse_elements(elements))

with open(output_path, 'w', encoding='utf-8') as f:
    f.write("".join(md_content))

print(f"Extração concluída com sucesso para {output_path}")
