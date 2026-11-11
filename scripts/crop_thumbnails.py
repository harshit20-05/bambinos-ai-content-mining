import cv2
import os

os.makedirs('scripts/crops', exist_ok=True)

for vf in ['english_940s.jpg', 'gita_2430s.jpg', 'gita_2850s.jpg', 'maths_2300s.jpg', 'science_1600s.jpg']:
    p = os.path.join('scripts/frames', vf)
    img = cv2.imread(p)
    if img is not None:
        h, w, _ = img.shape
        side_strip = img[:, int(w*0.75):, :]
        slide_area = img[:, :int(w*0.75), :]
        th_h = side_strip.shape[0] // 2
        cam1 = side_strip[:th_h, :, :]
        cam2 = side_strip[th_h:, :, :]
        
        base = vf.replace('.jpg', '')
        cv2.imwrite(f'scripts/crops/{base}_slide.jpg', slide_area)
        cv2.imwrite(f'scripts/crops/{base}_cam1.jpg', cam1)
        cv2.imwrite(f'scripts/crops/{base}_cam2.jpg', cam2)
        print(f"Cropped {vf}: cam1 mean={cam1.mean():.1f}, cam2 mean={cam2.mean():.1f}")

