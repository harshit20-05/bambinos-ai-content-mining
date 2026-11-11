# 5-Minute Executive Presentation Script for Live Case Review

**Audience:** Function Head (Marketing & Growth), Lead Video Producer, Academic Operations Lead  
**Candidate:** Harshit (AI Program Manager — Marketing)  
**Objective:** Deliver a high-conviction, senior-level 5-minute walkthrough of your submission before opening the floor to Q&A.

---

## Slide / Screen 1: The Problem & The North Star (0:00 – 1:00)
*(Display: GitHub README or Cover Page of PDF)*

> "Good morning / afternoon everyone. Thank you for having me.
> 
> When looking at Bambinos.live's growth engine, our highest-converting paid social ads are **unscripted, authentic classroom captures** where a scrolling parent stops and realizes:  
> *'Something is happening in this class that doesn't happen in my child's regular school.'*
> 
> But when I dug into the operations, I found a massive bottleneck:  
> Our team spends **45 to 50 minutes scrubbing each 50-minute recording**, and **85 to 90% of sessions yield zero usable ad moments**. Across 500 weekly classes, that's **375 hours of manual video scrubbing every single week**—the equivalent of 9 full-time employees watching Zoom classes at 1.5x speed.
> 
> My mandate was to build a system that achieves a **10x operational speedup** without compromising child safety, brand reputation, or creative quality."

---

## Slide / Screen 2: The Creative Taxonomy & 100-Point Rubric (1:00 – 2:00)
*(Display: Section 3 & 4 of PDF Report or `evaluation/scoring_rubric.md`)*

> "Before building prompts, I audited the Meta Ad Library across PlanetSpark, Bhanzu, and BrightCHAMPS. I realized that parents don't convert on generic lecturing; they convert on specific psychological triggers. 
> 
> I codified these into a **6-Bucket Creative Taxonomy**:
> 1. *The Eureka Moment* (Cognitive breakthrough)
> 2. *Student Participation & Fluency* (Active airtime)
> 3. *Interactive Gamified Discovery* (Screen-time replacement)
> 4. *Confidence Transformation & Mindfulness* (Focus & anti-distraction)
> 5. *Inspiring Mentorship* (Teacher warmth)
> 6. *Real Learning & Cultural Pride* (Shlokas and heritage values)
> 
> To eliminate subjectivity, I designed a **100-Point Scoring Rubric** evaluating Parent Stopping Power (25%), Proof of Learning (25%), Production Clarity (20%), Emotional Authenticity (15%), and Sound-Off Legibility (15%)."

---

## Slide / Screen 3: Empirical Validation & The Compliance Catch (2:00 – 3:15)
*(Display: Extracted Outputs Table in PDF Report or `outputs/editor_briefs.md`)*

> "I tested the pipeline across all 4 live sessions provided in the assessment data:
> 
> 1. **Our Top Creative Hit:** In our Bhagavad Gita session (`2125422751`), a 6-year-old child joyfully chanted *'Saraswati Namastubhyam Varade'* and explained its meaning. It scored a massive **94/100** as a Tier-1 Priority 1 creative with enormous appeal for Western NRI parents in the US, UK, and GCC.
> 2. **The Eureka Hit:** In English (`2125604619`), we captured an authentic cognitive leap where a student mastered the 'Story Mountain' narrative arc, scoring **86/100**.
> 
> **Crucially, the pipeline caught the test compliance trap:**  
> In the Maths session (`2125736982`), the teacher repeatedly reprimanded the child, called her silly, threatened zero scores, and leaked her full name. 
> A naive AI scanning for 'math quiz' keywords would have approved this. But our pipeline enforced our **7 Hard Compliance Red Lines**, detected negative tone, student distress, and PII, scored it **12/100**, and auto-quarantined it to Academic Operations in zero minutes."

---

## Slide / Screen 4: Solving the Audio vs. Visual Gap & Handoff (3:15 – 4:00)
*(Display: Section 6 & 8 of PDF Report or `workflow/architecture.md`)*

> "A major failure point in audio pipelines is that transcripts can't see what's happening on screen. If a child's camera is off or they are looking away, editors waste hours cutting dead footage.
> 
> We solved this by pairing the LLM with an automated **OpenCV Keyframe Verification Worker**. It samples 3 strategic frames (`Start+1s`, `Midpoint`, `End-1s`) and checks lighting brightness, facial variance, and slide relevance.
> 
> Editors receive a pre-populated Airtable card containing the 3 preview frames, 1-click video trim timestamps, the 3-second hook overlay, and subtitles formatted for a 9:16 vertical split. Editor review time drops from 45 minutes to under 2.5 minutes."

---

## Slide / Screen 5: Business Impact & 30-60-90 Day Rollout (4:00 – 5:00)
*(Display: ROI Table in Section 11 of PDF Report)*

> "Finally, the unit economics at our 500-class weekly volume:
> - **354 human hours saved every single week** (a 94.4% operational time reduction).
> - **8.9 FTE capacity freed up** to focus on creative strategy and rapid ad testing.
> - Discovery cost per approved clip drops from **$85 to $8.75**.
> - Net annual operational savings: **$218,096** at a **77.8x net ROI multiple**.
> - Time-to-publish reduced from **7 days to under 24 hours**.
> 
> My 30-60-90 day plan pilots 25 classes in Month 1, deploys n8n cloud automation in Month 2, and scales to all 500 classes with closed-loop Meta Ads ROAS telemetry in Month 3.
> 
> Thank you, and I'm excited to dive into your questions!"
