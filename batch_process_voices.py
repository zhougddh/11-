#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
批量处理音色ID，使用POST请求避免URL长度限制
"""
import json
import os
import requests

def get_all_voice_ids():
    """从fish_voices_export.json中获取所有音色ID"""
    export_json_path = os.path.join(os.path.dirname(__file__), 'fish_voices_export.json')
    
    try:
        with open(export_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        voice_ids = []
        for category, info in data.items():
            if 'list' in info:
                for voice in info['list']:
                    voice_ids.append({
                        'name': voice.get('name', ''),
                        'id': voice.get('vid', '')
                    })
        
        print(f"成功提取 {len(voice_ids)} 个音色ID")
        return voice_ids
        
    except Exception as e:
        print(f"提取音色ID失败: {e}")
        return []

def batch_process_voices(voice_ids, batch_size=50):
    """批量处理音色ID，使用POST请求避免URL长度限制"""
    api_key = 'sk-B4V1pwfJF1OzG8PLGEuvo6hvBNonBrb8oWRtHVIUxsRYdPVD'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    # 分批次处理
    for i in range(0, len(voice_ids), batch_size):
        batch = voice_ids[i:i+batch_size]
        print(f"处理第 {i//batch_size + 1} 批，共 {len(batch)} 个音色")
        
        # 构建请求数据
        data = {
            'voices': batch
        }
        
        try:
            # 使用POST请求
            response = requests.post(
                'https://api.302.ai/fish-audio/model/batch',
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"批次处理成功: {result}")
            else:
                print(f"批次处理失败: {response.status_code}")
                print(f"响应内容: {response.text}")
                
        except Exception as e:
            print(f"处理批次时出错: {e}")

def create_voice_id_list():
    """创建音色ID列表文件，用于复制粘贴"""
    voice_ids = get_all_voice_ids()
    
    # 创建ID列表文件
    id_list_path = os.path.join(os.path.dirname(__file__), 'voice_ids.txt')
    with open(id_list_path, 'w', encoding='utf-8') as f:
        for voice in voice_ids:
            f.write(f"{voice['id']},{voice['name']}\n")
    
    print(f"成功创建音色ID列表文件: {id_list_path}")
    print(f"文件包含 {len(voice_ids)} 个音色ID")

if __name__ == '__main__':
    print("开始处理音色ID...")
    
    # 获取所有音色ID
    voice_ids = get_all_voice_ids()
    
    # 创建音色ID列表文件
    create_voice_id_list()
    
    print("\n处理完成！")
    print("你可以使用voice_ids.txt文件中的ID列表进行批量操作")
