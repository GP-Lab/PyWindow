import gradio as gr

def greet(name):
    return "Hello, " + name + "!"

io = gr.Interface(
    greet,
    "textbox",
    gr.inputs.Textbox(label="Enter your name here..."),
    "textbox",
    gr.outputs.Textbox(label="Greeting")
)

io.launch()
