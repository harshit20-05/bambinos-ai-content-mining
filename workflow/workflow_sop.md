# Deliverable B: End-to-End Workflow Architecture & SOP

**Author:** Harshit (AI Program Manager, Marketing)  
**System:** Bambinos AI Creative Mining & Production Engine (ACM-PE)  
**Pipeline Velocity:** 10x Speedup (from 50 min manual review to <3 min editor review per class)

---

## 1. High-Level Pipeline Architecture

The pipeline processes live Zoom/Google Meet recordings through an automated 10-stage assembly line with automated gates and human-in-the-loop quality controls:

```mermaid
flowchart TD
    subgraph Stage1["1. INGESTION & PREPROCESSING"]
        A[Class Recording Ends<br>Zoom / Meet Cloud] -->|Webhook / API| B[Audio / Video Storage<br>AWS S3 / Google Cloud]
        B --> C[Whisper AI / AssemblyAI<br>Timestamped WebVTT]
        C --> D[Transcript Normalizer<br>Speaker Diarization & Cleanup]
    end

    subgraph Stage2["2. AI MOMENT MINING & INTELLIGENCE"]
        D --> E[LLM Mining Agent<br>Claude 3.5 Sonnet / Gemini Pro]
        E --> F[Moment Bucket Classification<br>6 Creative Taxonomies]
        F --> G[100-Point Scoring Engine<br>Stopping Power, Pedagogy, Clarity]
        G --> H{Hard Exclusions Gate<br>PII, Tone, Safety}
    end

    subgraph Stage3["3. VISUAL VERIFICATION & INTEGRITY"]
        H -- Hard Fail --> Z1[Auto-Reject & Academic QA Alert]
        H -- Pass --> I[OpenCV Video Frame Extractor<br>Sample 3 Key Frames: F1, F2, F3]
        I --> J[Visual Status Validator<br>Face Visibility, Camera On, Slides]
    end

    subgraph Stage4["4. HUMAN APPROVAL & EDITOR HANDOFF"]
        J --> K[Airtable / Sheet Creative Hub<br>Populated Brief & Frame Previews]
        K --> L{Creative Lead QA Gate<br>Approve / Tweak / Reject}
        L -- Approved --> M[Video Editor Workspace<br>Frame.io / CapCut Pro]
        M --> N[Final 9:16 Vertical Creative<br>Kinetic Captions, Split-Screen, CTA]
        N --> O[Performance Feedback Loop<br>Meta Ads Manager ROAS & Thumbstop]
    end

    classDef ing fill:#e1f5fe,stroke:#0288d1;
    classDef ai fill:#e8f5e9,stroke:#388e3c;
    classDef vis fill:#fff3e0,stroke:#f57c00;
    classDef human fill:#f3e5f5,stroke:#7b1fa2;
    classDef reject fill:#ffebee,stroke:#c62828;

    class A,B,C,D ing;
    class E,F,G ai;
    class H,I,J vis;
    class K,L,M,N,O human;
    class Z1 reject;
```

---

## 2. Production Tooling Stack Matrix

We intentionally select a robust, cost-effective, low-code/AI stack designed for marketing operations without requiring custom backend engineering:

| Pipeline Stage | Primary Tool Selected | Fallback / Alternative | Rationale & Operational Role |
| :--- | :--- | :--- | :--- |
| **Ingestion & Storage** | **AWS S3 / Google Cloud Storage** | Zoom Cloud Storage | Immutable, secure cloud storage with pre-signed URLs for automated downstream processing. |
| **Transcription & Diarization** | **Whisper API / AssemblyAI** | Deepgram Nova-2 | Generates accurate millisecond-timestamped WebVTT with speaker diarization across diverse accents (Indian, US, UK, Middle East). |
| **Workflow Orchestration** | **n8n (Self-hosted or Cloud)** | Make.com / Zapier | Enterprise-grade webhook handling, branching logic, JSON transformations, and API orchestration at 1/10th the cost of Zapier. |
| **LLM Mining & Scoring** | **Claude 3.5 Sonnet / Gemini 1.5 Pro** | GPT-4o | Massive context window (handles entire 50-minute transcripts in a single call), superior nuance in detecting teacher tone and pedantic shaming. |
| **Visual Verification Engine** | **Python + OpenCV Worker** | Cloudinary / Twelve Labs | Automated lightweight sampling of 3 frames per moment; checks webcam brightness, face presence, and slide variance in <2 seconds per clip. |
| **Creative Hub & Database** | **Airtable (Enterprise)** | Google Sheets + AppSheet | Relational database linking Class IDs, Video URLs, Moment Briefs, Visual Status, Editor Status, and Performance Meta KPIs. |
| **Video Editing & Assembly** | **CapCut Pro / Adobe Premiere** | OpusClip / Descript | Rapid 9:16 vertical re-framing, auto-caption generation with dynamic styling, split-screen templates, and branding overlays. |
| **Review & Handoff** | **Frame.io / Airtable Interfaces** | Google Drive Comments | Frame-accurate creative review, timestamped annotations, and one-click editor approvals. |

---

## 3. Solving the "Audio vs. Visual" Gap

### The Core Vulnerability
A transcript records *phonemes and text*, but cannot see:
- When a child's camera is turned off, pointing at the ceiling, or blacked out.
- When an animated visual exercise (e.g., interactive digital whiteboard, animated story slide) makes dialogue comprehensible that would otherwise sound abstract.
- When a child looks miserable despite polite words ("Yes ma'am").
- When a teacher makes high-energy physical gestures (waving hands, miming an animal) that drive thumbstop rate.

### The 4-Step Automated Visual Verification Protocol

```mermaid
sequenceDiagram
    autonumber
    participant LLM as AI Mining Agent
    participant Worker as OpenCV Visual Worker
    participant DB as Airtable Creative Hub
    participant Editor as Human Video Editor

    LLM->>Worker: Send Candidate (Clip ID, Start_TS, End_TS, Duration)
    Worker->>Worker: Sample F1 (Start+1s), F2 (Mid), F3 (End-1s)
    Worker->>Worker: Calculate Metrics (Brightness, StdDev, Face Presence)
    alt Student Camera Off or Black Screen
        Worker->>DB: Tag Status: CAMERA_OFF / Score = 0 (Reject)
    else Visual Context on Slide Only
        Worker->>DB: Tag Status: SCREEN_ACTIVITY (Editor note: Zoom slide)
    else Student Visible & Engaged
        Worker->>DB: Tag Status: VERIFIED (Include Frame Thumbnails)
    end
    DB->>Editor: Editor views pre-filtered brief with 3 preview frames
    Note over Editor: Editor approves/edits in <30 seconds without scrubbing raw 50m video!
```

### Visual Verification Status Taxonomy
1. **`VERIFIED` (Green):**
   - Student face clearly detected, camera brightly lit, natural head/hand movement.
   - Ready for standard 9:16 split-screen edit.
2. **`SCREEN_ACTIVITY` (Yellow):**
   - Key action occurs on the shared screen (digital puzzle, math diagram, story graphic).
   - Editor instruction: Re-frame slide as full 9:16 canvas with student webcam in a circular bottom-right picture-in-picture (PiP).
3. **`CAMERA_OFF` (Red):**
   - Student webcam is dark, static, or disabled.
   - Action: Auto-rejected for direct video ads; flagged for potential voiceover/testimonial animation if audio is extraordinary.
4. **`UNVERIFIED` (Orange):**
   - Ambiguity in frame extraction; flagged for a 5-second human scrub before opening Premiere/CapCut.
5. **`REJECTED` (Black):**
   - Inappropriate background, camera pointing at ceiling/wall, or visual distress detected.

---

## 4. Standard Operating Procedure (SOP): Video Editor Handoff

### Editor Workflow & SLA
- **Target SLA:** 24 hours from Class Session to Published Short-Form Ad.
- **Editor Review Time:** < 2 minutes per brief (down from 45 minutes of raw scrubbing).

### The 9:16 Vertical Creative Template Spec:
1. **Canvas Aspect Ratio:** 9:16 (1080x1920 pixels) optimized for Instagram Reels, Meta Ads, and YouTube Shorts.
2. **Split-Screen Layout:**
   - **Top 55%:** Teacher interaction or high-contrast presentation slide/digital activity.
   - **Bottom 45%:** Child face, expressive reactions, and live verbal participation.
3. **The 3-Second Visual Hook (Thumbstop):**
   - Large bold text overlay in top-third: High-contrast yellow/white sans-serif font (Montserrat / The Bold Font) with black drop shadow.
   - Hook text must match the brief's opening line (e.g., *"How 6-year-olds connect with Sanskrit"*).
4. **Subtitles & Kinetic Captions (Sound-Off Optimization):**
   - Word-by-word synchronized animated captions centered in the lower-middle screen.
   - Key emotional words highlighted in brand green/gold.
5. **Audio Mastering:**
   - Teacher and student audio normalized to -14 LUFS.
   - Background hum removed via Adobe Podcast AI / CapCut voice enhancement.
   - Gentle, upbeat, royalty-free acoustic/lo-fi background music ducked at -24 dB beneath dialogue.
6. **Closing Call-to-Action (Final 3 Seconds):**
   - Bambinos.live logo + *"Book Your Child's Free Trial Class"* CTA banner.
   - Visual cue pointing to the caption link / "Sign Up" button.

