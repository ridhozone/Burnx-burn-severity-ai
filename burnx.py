from PIL import Image
from ultralytics import YOLO


def Analyzer(img):
    img = Image.open(img)

    model = YOLO(f"./onnx/burnx-model.onnx", task="detect")

    pred = model.predict(
        source=img,
        conf=0.5,
        iou=0.3,
        device="cpu",
    )

    output = pred[0].plot(
        font_size=18,
        line_width=3,
        color_mode="instance",
    )

    return output
