import gradio as gr

def upload_file(files):
    file_paths = [file.name for file in files]
    return file_paths[0]

with gr.Blocks() as demo:
    file_output = gr.Textbox(interactive=True)
    upload_button = gr.UploadButton("Click to Upload a File", file_types=["image", "video"], file_count="multiple")
    upload_button.upload(upload_file, upload_button, file_output)

demo.launch()

