import cv2
import pickle
import numpy as np
from insightface.app import FaceAnalysis

# Model
app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0, det_size=(640, 640))

# Bazani yuklash
with open("embeddings.pkl", "rb") as f:
    data = pickle.load(f)

known_embeddings = data["embeddings"]
known_names = data["names"]

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    faces = app.get(frame)

    for face in faces:
        emb = face.embedding

        best_name = "Unknown"
        best_score = -1

        for known_emb, name in zip(known_embeddings, known_names):
            score = np.dot(emb, known_emb) / (
                np.linalg.norm(emb) * np.linalg.norm(known_emb)
            )

            if score > best_score:
                best_score = score
                best_name = name

        if best_score < 0.45:
            best_name = "Unknown"

        x1, y1, x2, y2 = map(int, face.bbox)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(
            frame,
            f"{best_name} ({best_score:.2f})",
            (x1, y1-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    cv2.imshow("Face ID", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()
print("Embeddinglar soni:", len(known_embeddings))
print("Ismlar:", known_names)