import os
import cv2
import pickle
from insightface.app import FaceAnalysis

print("AI modeli yuklanmoqda...")

app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0, det_size=(640, 640))

print("Model tayyor!")

DATASET = "dataset"

embeddings = []
names = []

for image_name in os.listdir(DATASET):

    image_path = os.path.join(DATASET, image_name)

    if not image_name.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    print(f"Tekshirilmoqda: {image_name}")

    image = cv2.imread(image_path)

    if image is None:
        print("Rasm ochilmadi!")
        continue

    faces = app.get(image)

    if len(faces) == 0:
        print("Yuz topilmadi!")
        continue

    face = faces[0]

    embeddings.append(face.embedding)

    name = os.path.splitext(image_name)[0]

    names.append(name)

    print(f"✓ {name} qo'shildi")

with open("embeddings.pkl", "wb") as f:
    pickle.dump({
        "embeddings": embeddings,
        "names": names
    }, f)

print("\n======================")
print("Jami:", len(names))
print("Saqlandi!")