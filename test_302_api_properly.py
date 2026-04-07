#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
正确测试302.ai的API功能
"""
import requests
import json

def test_302_api():    """正确测试302.ai的API"""
    api_key = 'sk-B4V1pwfJF1OzG8PLGEuvo6hvBNonBrb8oWRtHVIUxsRYdPVD'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    print("测试302.ai的获取声音列表API...")
    # 测试获取声音列表API
    try:
        response = requests.get(
            'https://api.302.ai/fish-audio/model',
            headers=headers,
            params={
                'page_size': 10,
                'page_number': 1
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ 获取声音列表API测试成功!")
            print(f"获取到 {result.get('total', 0)} 个音色")
            print("前5个音色:")
            for i, item in enumerate(result.get('items', [])[:5]):
                print(f"  {i+1}. {item.get('title')} (ID: {item.get('_id')})")
        else:
            print(f"❌ 获取声音列表API测试失败: {response.status_code}")
            print(f"响应内容: {response.text}")
            
    except Exception as e:
        print(f"❌ API测试失败: {e}")
    
    print("\n测试302.ai的文字转语音API...")
    # 测试文字转语音API
    try:
        test_text = "这是一个测试语音，用于验证302.ai的TTS功能是否正常工作。"
        test_voice_id = "c4f09481bf514fd2a864977042119f07"  # 台湾机车妹
        
        response = requests.post(
            'https://api.302.ai/fish-audio/v1/tts',
            headers=headers,
            json={
                'text': test_text,
                'reference_id': test_voice_id,
                'format': 'mp3',
                'mp3_bitrate': 64,
                'normalize': True,
                'chunk_length': 200,
                'latency': 'normal'
            },
            params={
                'response_format': 'url'
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ 文字转语音API测试成功!")
            print(f"生成的语音URL: {result.get('url')}")
        else:
            print(f"❌ 文字转语音API测试失败: {response.status_code}")
            print(f"响应内容: {response.text}")
            
    except Exception as e:
        print(f"❌ TTS API测试失败: {e}")

def batch_test_voice_ids(voice_ids):    """批量测试音色ID"""
    api_key = 'sk-B4V1pwfJF1OzG8PLGEuvo6hvBNonBrb8oWRtHVIUxsRYdPVD'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    print(f"\n批量测试 {len(voice_ids)} 个音色ID...")
    
    # 测试前5个音色ID
    test_ids = voice_ids[:5]
    
    for voice in test_ids:
        print(f"\n测试音色: {voice['name']} (ID: {voice['id']})")
        
        try:
            response = requests.post(
                'https://api.302.ai/fish-audio/v1/tts',
                headers=headers,
                json={
                    'text': f"这是 {voice['name']} 的测试语音",
                    'reference_id': voice['id'],
                    'format': 'mp3',
                    'mp3_bitrate': 64,
                    'normalize': True
                },
                params={
                    'response_format': 'url'
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"  ✅ 成功: {result.get('url')}")
            else:
                print(f"  ❌ 失败: {response.status_code} - {response.text}")
                
        except Exception as e:
            print(f"  ❌ 错误: {e}")

def get_voice_ids_from_file():
    """从文件中读取音色ID"""
    import os
    
    file_path = os.path.join(os.path.dirname(__file__), 'voice_ids.txt')
    voice_ids = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(',', 1)
                    if len(parts) == 2:
                        voice_ids.append({
                            'id': parts[0],
                            'name': parts[1]
                        })
        
        print(f"成功从文件中读取 {len(voice_ids)} 个音色ID")
        return voice_ids
        
    except Exception as e:
        print(f"读取音色ID文件失败: {e}")
        return []

if __name__ == '__main__':
    print("开始测试302.ai API...")
    
    # 测试API基本功能
    test_302_api()
    
    # 从文件中读取音色ID并测试
    voice_ids = get_voice_ids_from_file()
    if voice_ids:
        batch_test_voice_ids(voice_ids)
    
    print("\nAPI测试完成!")
