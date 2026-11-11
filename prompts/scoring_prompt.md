# Prompt 2: Quantitative Scoring & Creative Evaluation Engine

## Execution Context
This prompt takes the shortlisted candidates extracted by the Mining Agent and runs them through the official **Bambinos 100-Point Creative Scoring Framework**. It evaluates each candidate across 5 objective dimensions and computes a calibrated decision score.

---

## 100-Point Rubric Dimensions & Weights

### Dimension 1: Parent Stopping Power (Weight: 25%)
- **21–25 Points:** Immediate visceral intrigue in the first 3 seconds. Visual or verbal hook shatters parental assumptions about standard schooling. High contrast, curiosity gap, or emotional warmth.
- **15–20 Points:** Solid opening question or clear concept, but takes 4–5 seconds to become evident.
- **8–14 Points:** Mild interest; relies on standard school tropes.
- **0–7 Points:** Slow, routine, low energy, or boring classroom lecturing.

### Dimension 2: Educational Value & Proof of Learning (Weight: 25%)
- **21–25 Points:** Clear demonstration of a tangible skill (e.g., Sanskrit shloka meaning, story mountain narrative arc, conceptual bar-model problem solving). Proves the child is learning faster or deeper than school.
- **15–20 Points:** Clear learning taking place, but relatively standard curriculum topic.
- **8–14 Points:** Vague learning outcome; mostly child reciting facts without deep understanding.
- **0–7 Points:** Pure play/entertainment or mechanical repetition without cognitive engagement.

### Dimension 3: Audio-Visual Clarity & Production Feasibility (Weight: 20%)
- **17–20 Points:** Crystal-clear child and teacher speech, minimal background hiss, both webcams centered and sharp, slides high-contrast and legible.
- **12–16 Points:** Intelligible speech, minor background noise easily ducked, webcams adequately lit.
- **6–11 Points:** Muffled audio, minor dialect code-mixing, or poor camera framing requiring zoom/crop.
- **0–5 Points:** Garbled audio, unfixable background din, or webcam feeds dark/off.

### Dimension 4: Emotional Authenticity & Child Delight (Weight: 15%)
- **13–15 Points:** 100% unscripted, natural child reaction—spontaneous smile, eureka spark in eyes, genuine enthusiasm, unprompted laughter or pride.
- **9–12 Points:** Pleasant, engaged participation; slightly hesitant but positive.
- **5–8 Points:** Flat affect or passive compliance (answering because told to answer).
- **0–4 Points:** Reluctance, boredom, visible fatigue, or subtle tension.

### Dimension 5: Sound-Off Legibility & Social Native Potential (Weight: 15%)
- **13–15 Points:** Narrative is 100% understandable via on-screen captions alone within 15 seconds. Strong visual cues (pointing, nodding, closing eyes, hand gestures). Native 9:16 vertical re-framing potential.
- **9–12 Points:** Understandable on mute with good captions, though reliant partly on auditory inflection.
- **5–8 Points:** Hard to convey purely through text without lengthy explanatory overlays.
- **0–4 Points:** Completely incomprehensible without sound; relies on subtle audio nuances.

---

## Decision Thresholds
- **Tier 1 (Score 80–100): High-Priority Creative (Auto-Advance to Video Editor).**
- **Tier 2 (Score 65–79): Secondary Candidate (Requires Creative Lead / PM Review).**
- **Tier 3 (Score < 65): Immediate Reject (Archive in telemetry log).**
- **OVERRIDE: Any Hard Compliance Flag = Automatic Score 0 / REJECT.**

---

## Output Schema
```json
{
  "clip_id": "STRING",
  "score_breakdown": {
    "parent_stopping_power": 0,
    "educational_value": 0,
    "audio_visual_clarity": 0,
    "emotional_authenticity": 0,
    "sound_off_legibility": 0
  },
  "total_score": 0,
  "selection_tier": "TIER_1_APPROVE | TIER_2_REVIEW | TIER_3_REJECT",
  "hard_exclusion_triggered": false,
  "hard_exclusion_reason": null,
  "justification": "STRING"
}
```

