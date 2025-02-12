# ComfyUI-Ollama-Integration

这是一个 ComfyUI 自定义节点项目，用于调用本地运行的 Ollama 大模型进行翻译或对话。

## 使用方法

1. 确保已安装并运行 Ollama，且模型已下载（如 `llama2`）。
2. 将 `custom_nodes/ollama_node.py` 文件放入 ComfyUI 的 `custom_nodes` 目录。
3. 重启 ComfyUI。
4. 在节点列表中找到 "Ollama" 分类下的 "Ollama Node" 或 "Ollama Translate Node"。
5. 连接节点并输入文本，选择模型和参数后运行。

## 节点功能

### Ollama Node
- **text**: 输入的文本内容。
- **model**: 选择的模型（如 `llama2`、`mistral` 等）。
- **max_tokens**: 生成的最大 token 数量。
- **task_type**: 任务类型（例如：翻译、对话、总结等）。

### Ollama Translate Node
- **chinese_text**: 输入的中文文本。
- **model**: 选择的模型（如 `llama2`、`mistral` 等）。
- **max_tokens**: 生成的最大 token 数量。

## 注意事项

- 确保 Ollama 的 API 地址正确（默认 `http://localhost:11434/api/generate`）。
- 如果请求失败，请检查 Ollama 是否正常运行。