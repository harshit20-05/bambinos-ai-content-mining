import cv2
import os

os.makedirs('scripts/frames', exist_ok=True)

videos = {
    'english': ('repo/marketing/full_class_videos/English_2125604619.mp4', [100, 940, 1260, 2000]),
    'gita': ('repo/marketing/full_class_videos/Gita_2125422751.mp4', [100, 1400, 2430, 2850]),
    'maths': ('repo/marketing/full_class_videos/Maths_2125736982.mp4', [100, 600, 1800, 2300, 2700]),
    'science': ('repo/marketing/full_class_videos/Science_2125687282.mp4', [100, 600, 1600, 2500])
}

for name, (path, sec_list) in videos.items():
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Sampling {name} (FPS: {fps})...")
    for sec in sec_list:
        frame_idx = int(sec * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if ret:
            out_img = f"scripts/frames/{name}_{sec}s.jpg"
            cv2.imwrite(out_img, frame)
            h, w, c = frame.shape
            print(f"  Saved {out_img} ({w}x{h})")
        else:
            print(f"  Failed frame at {sec}s")
    cap.release()

print("Done frame extraction.")

