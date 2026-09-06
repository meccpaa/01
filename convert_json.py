import json
import os

# Load your JSON data
with open('chapters.json', 'r') as f:
    data = json.load(f)

# Create a folder for your notes
output_dir = '道德经多版本对照'
os.makedirs(output_dir, exist_ok=True)

for chapter in data['chapters']:
    chapter_num = chapter['chapter']
    filename = f"{output_dir}/{chapter_num:02d}章_{chapter.get('title', '')}.md"
    
    content = f"""---
title: "{chapter.get('title', f'第{chapter_num}章')}"
chapter: {chapter_num}
tags: [道德经, 多版本]
---

# 第{chapter_num}章 {chapter.get('title', '')}

## 原文
{chapter.get('original', '')}

## 现代汉语译文
{chapter.get('modern_chinese', '')}

## 各家注释

### 王弼注
{chapter.get('wangbi_note', '')}

### 河上公注
{chapter.get('heshanggong_note', '')}

### 苏辙注
{chapter.get('suzhe_note', '')}

### 憨山德清注
{chapter.get('hanshandeqing_note', '')}

### 王夫之注
{chapter.get('wangfuzhi_note', '')}

### 帛书本
{chapter.get('postsilk_text', '')}

### 郭店楚简本
{chapter.get('guodian_text', '')}

### 英文翻译（Lau）
{chapter.get('english_lau', '')}

---
*此文件由JSON自动生成*
"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {filename}")
