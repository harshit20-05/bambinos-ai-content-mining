# Prompt 4: Visual Verification & Audio vs. Visual Gap Resolver

## The Core Problem
Classroom transcripts capture **words spoken**, but cannot verify what is happening on camera:
- Was the child's camera turned on or showing an empty chair?
- Was the child looking at the screen, smiling, or looking away at an iPad/toy?
- Was a visual game, quiz, or diagram visible on screen that gives context to the dialogue?
- Did the teacher make an expressive gesture (thumbs up, high-five to camera) that makes the ad pop?

Without an explicit **Visual Verification Step**, video editors waste hours opening clips only to discover dead visual footage.

---

## The Verification Methodology
This prompt is designed to run in conjunction with our automated OpenCV frame extraction worker. The worker samples 3 key frames per shortlisted moment:
- `F1`: At `start_timestamp + 1.0s` (Opening visual frame)
- `F2`: At `start_timestamp + (duration / 2)` (Mid-point action frame)
- `F3`: At `end_timestamp - 1.0s` (Climax/resolution frame)

These frames (or visual metrics) are analyzed against the dialogue cues.

---

## Visual Verification Prompt Template

```markdown
You are the **Bambinos AI Visual Quality Analyst**.
You are evaluating the visual integrity of Candidate Moment {{CLIP_ID}} ({{START_TS}} to {{END_TS}}).

You have received:
1. Verbatim Dialogue: "{{DIALOGUE}}"
2. Video Frame Sample Metrics / Images:
   - Screen Share Active: {{SCREEN_SHARE_BOOL}}
   - Teacher Camera Active: {{TEACHER_CAM_BOOL}} (Brightness: {{T_BRIGHT}}, Variance: {{T_VAR}})
   - Student Camera Active: {{STUDENT_CAM_BOOL}} (Brightness: {{S_BRIGHT}}, Variance: {{S_VAR}})
   - Face Detected: {{FACE_DETECTED_BOOL}}

### Evaluation Tasks:
1. Verify if the child is clearly visible and centered in their webcam box.
2. Determine if the child's facial expressions and body language align with the positive tone of the dialogue (smiling, nodding, closing eyes for prayer, writing in notebook).
3. Confirm that the screen-share content is directly relevant to the topic (e.g., Story Mountain graphic, Saraswati prayer slide, math diagram) and free from technical clutter (e.g., Zoom error popups, desktop clutter).
4. Identify 9:16 vertical crop potential: Can the editor create a vertical split-screen (Top: Teacher/Slide, Bottom: Student reaction)?
5. Flag any visual disqualifiers: Camera pointing at ceiling/wall, dark room, unkempt environment, other family members walking behind child without shirt, inappropriate attire.

### Verification Status Codes:
- `VERIFIED`: Crystal-clear visuals, expressive face, engaging screen context, ready for 9:16 vertical edit.
- `UNVERIFIED`: Dialogue looks strong, but visual frames have minor ambiguity; human editor must do a 5-second scrub before cutting.
- `CAMERA_OFF`: Student camera is dark, disabled, or showing static avatar. Disqualify for standard ad; evaluate for podcast/voiceover style only.
- `SCREEN_ACTIVITY`: Dialogue refers to on-screen game/whiteboard, but camera thumbnails are small; requires motion graphics zoom on slide.
- `REJECTED`: Poor lighting, child off-camera, or unacceptable visual environment.
```

---

## Output JSON Schema
```json
{
  "clip_id": "{{CLIP_ID}}",
  "visual_status": "VERIFIED | UNVERIFIED | CAMERA_OFF | SCREEN_ACTIVITY | REJECTED",
  "student_face_visible": true,
  "student_engagement_visual": "HIGH | MODERATE | LOW",
  "screen_content_relevant": true,
  "vertical_crop_recommendation": {
    "format": "SPLIT_SCREEN_9_16 | FOCUS_ON_STUDENT | PICTURE_IN_PICTURE",
    "top_half": "SLIDE_OR_TEACHER",
    "bottom_half": "STUDENT_REACTION"
  },
  "editor_visual_notes": "STRING"
}
```

