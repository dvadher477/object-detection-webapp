import gradio as gr
from PIL import Image
from inference.predict import predict

def detect_objects(image):
    annotated_image, predictions = predict(image)
    return annotated_image, predictions

interface = gr.Interface(
    fn=detect_objects,
    inputs=gr.Image(type="file"),
    outputs=[gr.Image(type="pil"), "json"],
    title="BCCD Object Detection",
    description="Upload an image to detect RBC, WBC, and Platelets with bounding boxes and confidence scores."
)

interface.launch()