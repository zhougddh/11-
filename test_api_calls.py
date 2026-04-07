#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
测试302.AI API的正确调用方式
"""
import requests
import json
import os
import datetime

def test_302_api_direct():
    """直接测试302.AI API"""
    print("=== 直接测试302.AI API ===")
    
    # 配置
    api_key = "sk-B4V1pwfJF1OzG8PLGEuvo6hvBNonBrb8oWRtHVIUxsRYdPVD"
    base_url = "https://api.302.ai"
    tts_endpoint = "/fish-audio/v1/tts"
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    # 测试数据
    test_data = {
        "text": "您好，这是一个测试语音，用于验证302.AI API的调用方式。",
        "reference_id": "c4f09481bf514fd2a864977042119f07",  # 台湾机车妹
        "chunk_length": 200,
        "normalize": True,
        "format": "mp3",
        "mp3_bitrate": 64,
        "latency": "normal"
    }
    
    try:
        response = requests.post(
            f"{base_url}{tts_endpoint}",
            headers=headers,
            json=test_data
        )
        
        print(f"状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        
        if response.status_code == 200:
            result = response.json()
            if "url" in result:
                print(f"音频URL: {result['url']}")
                # 下载音频
                audio_response = requests.get(result['url'])
                if audio_response.status_code == 200:
                    output_file = f"test_direct_{datetime.datetime.now().timestamp()}.mp3"
                    with open(output_file, 'wb') as f:
                        f.write(audio_response.content)
                    print(f"音频已保存: {output_file}")
    except Exception as e:
        print(f"测试失败: {e}")

def test_local_api():
    """测试本地API服务"""
    print("\n=== 测试本地API服务 ===")
    
    # 本地服务地址
    local_url = "http://127.0.0.1:39903/fish/tts"
    
    # 测试数据
    test_data = {
        "text": "您好，这是一个测试语音，用于验证本地API服务的调用方式。",
        "voice": "c4f09481bf514fd2a864977042119f07"  # 台湾机车妹
    }
    
    try:
        response = requests.post(
            local_url,
            json=test_data
        )
        
        print(f"状态码: {response.status_code}")
        
        if response.status_code == 200:
            # 保存音频文件
            output_file = f"test_local_{datetime.datetime.now().timestamp()}.mp3"
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"音频已保存: {output_file}")
        else:
            print(f"响应内容: {response.text}")
    except Exception as e:
        print(f"测试失败: {e}")

def test_api302_route():
    """测试/api302/tts路由"""
    print("\n=== 测试/api302/tts路由 ===")
    
    # 本地服务地址
    local_url = "http://127.0.0.1:39903/api302/tts"
    
    # 测试数据
    test_data = {
        "text": "您好，这是一个测试语音，用于验证/api302/tts路由的调用方式。",
        "voice": "c4f09481bf514fd2a864977042119f07"  # 台湾机车妹
    }
    
    try:
        response = requests.post(
            local_url,
            json=test_data
        )
        
        print(f"状态码: {response.status_code}")
        
        if response.status_code == 200:
            # 保存音频文件
            output_file = f"test_api302_{datetime.datetime.now().timestamp()}.mp3"
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"音频已保存: {output_file}")
        else:
            print(f"响应内容: {response.text}")
    except Exception as e:
        print(f"测试失败: {e}")

if __name__ == "__main__":
    print("开始测试302.AI API调用方式...")
    
    # 测试直接调用302.AI API
    test_302_api_direct()
    
    # 测试本地API服务
    test_local_api()
    
    # 测试/api302/tts路由
    test_api302_route()
    
    print("\n测试完成！")
