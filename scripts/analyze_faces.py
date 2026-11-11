import cv2
import glob
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

frames = sorted(glob.glob('scripts/frames/*.jpg'))
print(f"Analyzing {len(frames)} frames...")

for f in frames:
    img = cv2.imread(f)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    avg_brightness = gray.mean()
    print(f"{os.path.basename(f)}: Brightness={avg_brightness:.1f}, Detected Faces={len(faces)}")
    for (x, y, w, h) in faces:
        print(f"   Face at x={x}, y={y}, w={w}, h={h} (rel pos: x={x/img.shape[1]:.2f}, y={y/img.shape[0]:.2f})")

