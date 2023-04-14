import gradio as gr

def load_file(content):
    # 处理上传的文件内容
    return len(content)

upload = gr.File()
output = gr.Textbox()

def process_file_upload(input_file):
    # 读取上传的文件内容
    content = input_file.read()
    # 调用处理函数处理文件内容
    result = load_file(content)
    # 返回处理结果
    return str(result)

interface = gr.Interface(
    fn=process_file_upload,
    inputs=upload,
    outputs=output,
    title="文件上传示例",
    description="上传一个文件并处理其内容"
)

interface.launch()
