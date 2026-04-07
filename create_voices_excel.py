#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
创建音色ID和名称的Excel表格
"""
import json
import os
import pandas as pd

def create_voices_excel():
    """创建音色ID和名称的Excel表格"""
    # 读取fish_voices_export.json文件
    export_json_path = os.path.join(os.path.dirname(__file__), 'fish_voices_export.json')
    
    try:
        with open(export_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 提取所有音色信息
        voices_data = []
        
        # 遍历所有分类
        for category_name, category_info in data.items():
            if 'list' in category_info:
                for voice in category_info['list']:
                    voices_data.append({
                        '分类': category_name,
                        '音色名称': voice.get('name', ''),
                        '音色ID': voice.get('vid', '')
                    })
        
        # 创建DataFrame
        df = pd.DataFrame(voices_data)
        
        # 保存为Excel文件
        output_path = os.path.join(os.path.dirname(__file__), '音色ID列表.xlsx')
        df.to_excel(output_path, index=False, sheet_name='音色列表')
        
        print(f"成功创建Excel表格: {output_path}")
        print(f"总共有 {len(voices_data)} 个音色")
        
        return True
        
    except Exception as e:
        print(f"创建Excel表格失败: {e}")
        return False

if __name__ == '__main__':
    print("开始创建音色ID和名称的Excel表格...")
    create_voices_excel()
