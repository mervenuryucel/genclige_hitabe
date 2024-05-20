import gradio as gr
import stylecloud
from PIL import Image
import os

# Ön işleme ve stylecloud oluşturma fonksiyonu
def create_stylecloud(file, language, icon):
    # Dosyanın içeriğini ikili formatta oku ve decode et
    text = file.decode("utf-8")

    # Geçici bir stylecloud dosyası oluştur
    output_file = "stylecloud.png"
    
    # StyleCloud oluştur
    stylecloud.gen_stylecloud(text=text,
                              icon_name=icon,
                              output_name=output_file)
    
    # Oluşturulan dosyanın yolunu döndür (indirme için)
    return output_file

# Gradio arayüzünü oluştur
with gr.Blocks() as demo:
    gr.Markdown("StyleCloud Oluşturucu")
    with gr.Row():
        file_input = gr.File(label="Metin Dosyası Yükle", type="binary")
        language = gr.Radio(choices=["tr", "en"], label="Dil Seçimi", value="tr")
        icon = gr.Dropdown(choices=["fas fa-car", "fas fa-star-and-crescent", "fas fa-trophy", "fas fa-heart"], label="İkon Seçimi", value="fas fa-star-and-crescent")
    output_file = gr.File(label="Oluşturulan StyleCloud İndir")
    create_button = gr.Button("Oluştur")
    create_button.click(
        create_stylecloud,
        inputs=[file_input, language, icon],
        outputs=output_file
    )

demo.launch(share=True)