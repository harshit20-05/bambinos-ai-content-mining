import cv2
import numpy as np

def scan_video_cameras(video_path, subject, step_sec=30):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_sec = total_frames / fps if fps > 0 else 0
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    black_screen_count = 0
    cam1_dark_count = 0
    cam2_dark_count = 0
    total_samples = 0
    
    # We sample every step_sec seconds
    for s in range(10, int(duration_sec), step_sec):
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(s * fps))
        ret, frame = cap.read()
        if not ret:
            break
        total_samples += 1
        side_strip = frame[:, int(w*0.75):, :]
        th_h = side_strip.shape[0] // 2
        cam1 = side_strip[:th_h, :, :]
        cam2 = side_strip[th_h:, :, :]
        
        # Check if entire frame is dark
        if frame.mean() < 10:
            black_screen_count += 1
        # Check if student webcam is off (mean < 15 or std < 5)
        if cam2.mean() < 15 or cam2.std() < 5:
            cam2_dark_count += 1
        if cam1.mean() < 15 or cam1.std() < 5:
            cam1_dark_count += 1
            
    cap.release()
    print(f"[{subject}] Samples: {total_samples}, Full Black: {black_screen_count}, Cam1 Off: {cam1_dark_count}, Cam2 (Student) Off: {cam2_dark_count}")

scan_video_cameras('repo/marketing/full_class_videos/English_2125604619.mp4', 'ENGLISH')
scan_video_cameras('repo/marketing/full_class_videos/Gita_2125422751.mp4', 'GITA')
scan_video_cameras('repo/marketing/full_class_videos/Maths_2125736982.mp4', 'MATHS')
scan_video_cameras('repo/marketing/full_class_videos/Science_2125687282.mp4', 'SCIENCE')

