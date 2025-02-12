# 导入自定义节点类
from .ollama_node import OllamaNode, OllamaTranslateNode

# 导出节点类
NODE_CLASS_MAPPINGS = {
    "OllamaNode": OllamaNode,
    "OllamaTranslateNode": OllamaTranslateNode
}

# 导出节点显示名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "OllamaNode": "Ollama Node",
    "OllamaTranslateNode": "Ollama Translate Node"
}

# 可选：导出 Web 目录（如果有前端资源）
WEB_DIRECTORY = None

# 可选：导出模块信息
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]