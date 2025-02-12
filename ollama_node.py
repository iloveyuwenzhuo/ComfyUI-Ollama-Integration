import comfy
import requests
import json

class OllamaNode:
    def __init__(self):
        self.url = "http://localhost:11434/api/generate"  # Ollama 的 API 地址
        self.models = self.get_local_models()  # 获取本地模型列表

    def get_local_models(self):
        """获取本地已下载的 Ollama 模型列表"""
        try:
            response = requests.get("http://localhost:11434/api/tags")
            response.raise_for_status()  # 检查请求是否成功
            data = response.json()
            models = [model["name"] for model in data.get("models", [])]
            return models
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Ollama models: {e}")
            return ["llama2"]  # 默认模型

    @classmethod
    def INPUT_TYPES(cls):
        # 动态加载模型列表
        try:
            models = cls().models
        except:
            models = ["llama2"]

        return {
            "required": {
                "text": ("STRING", {"multiline": True}),  # 输入文本
                "model": (models, {"default": models[0]}),  # 模型选择
                "max_tokens": ("INT", {"default": 100, "min": 1, "max": 2048}),  # 最大生成长度
                "task_type": ("STRING", {
                    "multiline": False,
                    "default": "美化并细化一下画面内容，并翻译",
                    "help": "指定任务类型，例如：翻译、对话、总结等"
                })
            },
        }

    RETURN_TYPES = ("STRING",)  # 输出类型
    RETURN_NAMES = ("response",)  # 输出名称
    FUNCTION = "generate"  # 节点执行函数
    CATEGORY = "Ollama"  # 节点分类

    def generate(self, text, model, max_tokens, task_type):
        # 构造请求数据
        payload = {
            "model": model,
            "prompt": f"任务类型：{task_type}\n内容：{text}",
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "max_tokens": max_tokens
            }
        }

        headers = {
            "Content-Type": "application/json"
        }

        # 发送请求
        try:
            response = requests.post(self.url, data=json.dumps(payload), headers=headers)
            response.raise_for_status()
            result = response.json()

            if 'response' in result:
                return (result['response'],)
            else:
                return ("Error: Invalid response format from Ollama",)

        except requests.exceptions.RequestException as e:
            return (f"Error: {str(e)}",)


class OllamaTranslateNode:
    def __init__(self):
        self.url = "http://localhost:11434/api/generate"  # Ollama 的 API 地址
        self.models = self.get_local_models()  # 获取本地模型列表

    def get_local_models(self):
        """获取本地已下载的 Ollama 模型列表"""
        try:
            response = requests.get("http://localhost:11434/api/tags")
            response.raise_for_status()  # 检查请求是否成功
            data = response.json()
            models = [model["name"] for model in data.get("models", [])]
            return models
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Ollama models: {e}")
            return ["llama2"]  # 默认模型

    @classmethod
    def INPUT_TYPES(cls):
        # 动态加载模型列表
        try:
            models = cls().models
        except:
            models = ["llama2"]

        return {
            "required": {
                "chinese_text": ("STRING", {"multiline": True}),  # 输入中文文本
                "model": (models, {"default": models[0]}),  # 模型选择
                "max_tokens": ("INT", {"default": 100, "min": 1, "max": 2048}),  # 最大生成长度
            },
        }

    RETURN_TYPES = ("STRING",)  # 输出类型
    RETURN_NAMES = ("translated_text",)  # 输出名称
    FUNCTION = "translate"  # 节点执行函数
    CATEGORY = "Ollama/Translation"  # 节点分类

    def translate(self, chinese_text, model, max_tokens):
        # 构造翻译任务的提示词
        prompt = f"将以下中文翻译成英文：\n{chinese_text}"

        # 构造请求数据
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "max_tokens": max_tokens,
            }
        }
        headers = {
            "Content-Type": "application/json"
        }

        # 发送请求
        try:
            response = requests.post(self.url, data=json.dumps(payload), headers=headers)
            response.raise_for_status()  # 检查请求是否成功
            result = response.json()
            return (result["response"],)  # 返回翻译结果
        except requests.exceptions.RequestException as e:
            return (f"Error: {str(e)}",)  # 返回错误信息


# 注册节点
NODE_CLASS_MAPPINGS = {
    "OllamaNode": OllamaNode,
    "OllamaTranslateNode": OllamaTranslateNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OllamaNode": "Ollama Node",
    "OllamaTranslateNode": "Ollama Translate Node"
}