import cv2
import numpy as np
import glob
import os
from PIL import Image

for f in sorted(glob.glob('scripts/frames/*.jpg')):
    im = Image.open(f)
    w, h = im.size
    # Check top right corner (often student/teacher video in Zoom)
    # Check main area (slides)
    arr = np.array(im)
    main_area_var = np.var(arr[:, :int(w*0.75)])
    side_area_var = np.var(arr[:, int(w*0.75):])
    print(f"{os.path.basename(f)}: size={w}x{h}, main_var={main_area_var:.0f}, side_var={side_area_var:.0f}")

