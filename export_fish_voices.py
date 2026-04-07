#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
导出ys.json文件中fish分类和全部分类的音色信息
"""
import json
import os

def export_fish_voices():
    """导出fish分类和全部分类的音色信息"""
    # 读取ys.json文件
    ys_json_path = os.path.join(os.path.dirname(__file__), 'ys.json')
    
    try:
        with open(ys_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 提取fish分类和全部分类的音色
        fish_voices = {}
        
        if 'fish' in data:
            fish_voices['fish'] = data['fish']
        
        if '全部分类' in data:
            fish_voices['全部分类'] = data['全部分类']
        
        # 导出为新的JSON文件
        output_path = os.path.join(os.path.dirname(__file__), 'fish_voices_export.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(fish_voices, f, ensure_ascii=False, indent=4)
        
        print(f"成功导出fish分类和全部分类的音色信息到 {output_path}")
        print(f"导出的分类数量: {len(fish_voices)}")
        
        # 统计每个分类的音色数量
        for category, info in fish_voices.items():
            if 'list' in info:
                print(f"{category}: {len(info['list'])} 个音色")
        
        return True
        
    except Exception as e:
        print(f"导出失败: {e}")
        return False

def test_302_api():
    """测试302.ai的API是否可以使用"""
    import requests
    
    try:
        # 测试获取声音列表API
        headers = {
            'Authorization': 'Bearer sk-B4V1pwfJF1OzG8PLGEuvo6hvBNonBrb8oWRtHVIUxsRYdPVD'
        }
        
        response = requests.get('https://api.302.ai/fish-audio/model', headers=headers)
        
        if response.status_code == 200:
            result = response.json()
            print(f"\n302.ai API测试成功!")
            print(f"获取到 {result.get('total', 0)} 个音色")
            print(f"前5个音色:")
            for i, item in enumerate(result.get('items', [])[:5]):
                print(f"{i+1}. {item.get('title')} (ID: {item.get('_id')})")
            return True
        else:
            print(f"302.ai API测试失败: {response.status_code}")
            print(f"响应内容: {response.text}")
            return False
            
    except Exception as e:
        print(f"API测试失败: {e}")
        return False

if __name__ == '__main__':
    print("开始导出fish分类和全部分类的音色信息...")
    export_fish_voices()
    
    print("\n测试302.ai API...")
    test_302_api()