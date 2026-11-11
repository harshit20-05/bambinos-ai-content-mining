# Executive Interview Preparation Guide: Live Case Review with Function Head

**Role:** AI Program Manager (Marketing)  
**Company:** Bambinos.live  
**Candidate:** Harshit (B.Tech CSE/IT — Track: Marketing)  
**Context:** Stage 2 Take-Home Case Defense & Deep Dive with Function Head (Marketing & Growth)

---

## 1. Top 10 Anticipated Grilling Questions & Model Answers

### Q1: "Why did you choose a 6-bucket creative taxonomy rather than just looking for any engaging 15 seconds?"
**Model Answer:**
> *"Looking for 'engagement' in the abstract is where most AI marketing pipelines fail, because engagement is subjective. 
> By auditing Meta Ad Library campaigns across PlanetSpark, Bhanzu, and BrightCHAMPS, I observed that parent-converting hooks fall into distinct psychological triggers:
> 1. Cognitive proof (*The Eureka Moment*)
> 2. Airtime & Confidence (*Student Participation*)
> 3. Screen-time replacement (*Interactive Gamification*)
> 4. Hyperactivity reduction (*Mindfulness & Focus*)
> 5. Trust in educators (*Inspiring Mentorship*)
> 6. Cultural identity (*Real Learning & Heritage Pride*)
>
> Categorizing into these 6 buckets serves two critical growth functions:
> First, it guarantees creative diversity on paid social—we don't fatigue audiences by running 10 identical clips of kids reading slides. 
> Second, it maps directly to audience segmentation: our Little Yogi 'Cultural Pride' bucket routes to high-LTV NRI audiences in New Jersey and Dubai, while the 'Story Mountain Eureka' bucket routes to Metro India parents preparing kids for school entrance exams."*

---

### Q2: "In the test assets, what did you observe in the Maths session? Walk me through how your system handled it."
**Model Answer:**
> *"The Maths session (`Maths_2125736982`) was a crucial stress test for the pipeline's negative guardrails. 
> In that session, the teacher repeatedly lost patience with the student ('Shrisha / Shree Shah'):
> - At 37:40, she said: 'Silly simple thing you are not understanding... how many times do I need to say...'
> - At 38:14: 'This way I will not teach you... why you don't study at home?'
> - At 45:27: '10 points out of 8 questions... next time you will score full zero... your father always say that she doesn't study at home.'
> - And when the child hesitantly asked if she would teach her in the next class, the teacher replied: 'I don't think that it is of any use.'
>
> A naive LLM scanning for keywords like 'maths', 'measurement', 'quiz', or 'score' might have flagged this as an interactive assessment moment. 
> But our pipeline has 7 non-negotiable Hard Red Lines. The Compliance Gatekeeper detected:
> 1. Negative Teacher Tone & Sarcasm (Red Line 2)
> 2. Child Demoralization & Distress (Red Line 3)
> 3. PII Exposure (student full name and father's comments cited; Red Line 1)
>
> It immediately overrode the score to 12/100, quarantined the session from the ad pool in 0 minutes, and generated an automated QA escalation ticket for Academic Operations. This protects the brand from catastrophic social backlash."*

---

### Q3: "How does your pipeline solve the 'Audio vs. Visual' gap without eating up hours of human review?"
**Model Answer:**
> *"A transcript only captures text and audio phonemes; it cannot confirm whether a child's camera was on, whether they were looking at the screen, or if an action was happening on an interactive whiteboard.
> Instead of asking an editor to scrub the raw video, we built an automated OpenCV Keyframe Extraction Worker.
> Whenever the LLM identifies a high-scoring dialogue window, the worker automatically extracts 3 strategic frames:
> - F1 (Start + 1s): Opening visual state.
> - F2 (Midpoint): Active engagement / screen share context.
> - F3 (End - 1s): Resolution / emotional payoff.
>
> The worker calculates webcam variance, face presence, and slide complexity, and tags the brief with a clear Visual Status:
> - `VERIFIED`: Faces centered, brightly lit, high expression. Ready for 9:16 vertical split.
> - `SCREEN_ACTIVITY`: Visual game on screen; re-frame slide as full 9:16 with student PiP.
> - `CAMERA_OFF`: Camera dark or disabled; auto-rejected from video ad pipeline.
> - `UNVERIFIED`: Minor ambiguity; flagged for a 5-second human glance.
>
> In our Airtable interface, the video editor sees these 3 preview frames directly on the brief card. They know the visual quality before they even launch CapCut or Premiere."*

---

### Q4: "Video editors and performance marketers are notoriously skeptical of AI tools. How will you drive adoption in your first 30 days?"
**Model Answer:**
> *"The #1 mistake AI Program Managers make is handing video editors raw JSON, terminal scripts, or low-quality suggestions that waste their time.
> To win over the editing team:
> 1. Treat the Editor as a Master Craftsman, Not a Scrubbing Detective: The editor's job shifts from spending 45 minutes scrubbing boring video to spending 20 minutes doing high-leverage creative styling (pacing, kinetic typography, audio mastering).
> 2. Zero Code Interface: Editors work entirely in Airtable and Frame.io. Each brief has a 1-click trim link, the exact verbatim dialogue, the 3 preview frames, the opening 3-second hook text, and pre-written subtitles.
> 3. Rapid Feedback Loop: If an editor rejects a brief, they click a single tag (e.g., 'Awkward Angle', 'Audio Hiss', 'Pacing Too Slow'). That tag logs to telemetry and directly updates our prompt's few-shot negative examples in weekly prompt calibrations.
> 4. Creative Performance Alignment: We align editor incentives with performance marketing wins (e.g., celebrating when an AI-discovered clip hits a >35% thumbstop rate on Meta Reels)."*

---

### Q5: "Why did you choose n8n over Zapier or Make.com, and Claude/Gemini over GPT-4o?"
**Model Answer:**
> *"This choice comes down to unit economics and technical capabilities:
> - Orchestration (n8n vs Zapier): At 500 classes/week, Zapier's task-based pricing model scales exponentially and would cost $500–$800/month. Self-hosted or cloud n8n handles complex webhook branching, binary file handling, and internal script execution for a fraction of that cost, while offering robust error handling and execution logging.
> - LLM Selection (Claude 3.5 Sonnet / Gemini 1.5 Pro vs GPT-4o): Analyzing an entire 50-minute classroom transcript requires processing 15,000 to 25,000 tokens per call. Gemini 1.5 Pro and Claude 3.5 Sonnet feature massive context windows with virtually zero 'needle-in-a-haystack' retrieval degradation. Furthermore, in our testing, Claude 3.5 Sonnet demonstrates superior sensitivity to subtle interpersonal nuances—such as identifying when a teacher's tone shifts from encouraging to pedantic or sarcastic."*

---

### Q6: "How did you arrive at the $218,000 annual savings figure? Walk me through the unit economics."
**Model Answer:**
> *"The math is grounded in conservative operational realities:
> - Volume: 500 live classes per week across India, GCC, and International tracks.
> - Manual Baseline: A human reviewer takes ~45 minutes to scrub a 50-minute session and verify transcripts. 500 * 0.75 hours = 375 human hours/week (~9.4 full-time equivalents).
> - AI Pipeline: Automated ingestion, transcription, mining, scoring, and OpenCV frame extraction runs asynchronously in ~1.5 minutes of compute time. The human Creative Lead reviews only the pre-filtered Tier 1 and Tier 2 candidate cards in Airtable, taking ~2.5 minutes per class. 500 * (2.5 / 60) = 20.8 hours/week (~0.5 FTE).
> - Labor Capacity Freed: 375 - 20.8 = 354.2 hours saved per week, or ~18,418 hours annualized.
> - Financial Value: At a blended fully loaded operational cost of $12.00/hour in Bengaluru, 18,418 hours * $12 = $221,020 in gross labor capacity reallocated.
> - AI Infrastructure Costs: Whisper API ($0.006/min for audio) + Claude API (input/output tokens) + cloud storage = ~$0.078 per class, or $2,028/year.
> - Net Savings: $221,020 - $2,028 = ~$218,096 net annual savings, yielding a 77.8x net ROI multiple."*

---

### Q7: "What happens if a parent revokes consent after a live class clip is published as a Meta ad?"
**Model Answer:**
> *"This is a critical data governance consideration. Our SOP includes three structural safeguards:
> 1. CRM Marketing Consent Flag: Before any recording is processed by the AI pipeline, the class ID is cross-referenced with HubSpot/LeadSquared CRM to verify that all participating students have an active parental marketing release on file. Sessions with unconsented students are never processed for public ads.
> 2. Relational Asset Registry in Airtable: Every published ad is tagged with `Session_ID`, `Student_CRM_ID`, and `Meta_Ad_Creative_ID`.
> 3. Instant Kill-Switch Protocol: If a parent revokes consent, entering their CRM ID into the Airtable registry automatically calls the Meta Ads API via n8n to pause and delete the active creative in under 5 minutes, followed by purging the video asset from public CDN storage."*

---

### Q8: "How does the pipeline handle multi-lingual or regional dialect sessions like the Science class?"
**Model Answer:**
> *"In the Science session (`Science_2125687282`), we observed code-mixing between English and Malayalam (`Ariandakai Kondarha Arikind...`). 
> For a global pan-English ad set, dialect mixing creates friction for sound-off subtitle legibility.
> Our pipeline uses Whisper's language probability telemetry:
> - If non-English vocabulary exceeds 15% of the dialogue window, the clip is tagged with a `DIALECT_MIX` flag and scored as Tier 2 (Review).
> - Rather than discarding the clip, the pipeline routes it to localized regional campaigns (e.g., targeted specifically to Kerala and South Indian diaspora cohorts in Dubai and Kuwait), where regional code-mixing actually builds cultural intimacy and converts higher than neutral English."*

---

### Q9: "How do you close the loop between Meta Ads performance (ROAS) and the AI Moment Mining prompt?"
**Model Answer:**
> *"In Phase 3 (Days 61–90), we establish a closed-loop feedback pipeline:
> - Every published ad creative is linked via UTM parameters and Meta Ad ID back to its Airtable record (tracking its Moment Bucket, Hook Text, and AI Score).
> - Weekly, an n8n webhook pulls creative performance telemetry from Meta Ads Manager: 3-Second Thumbstop Rate (3s video plays / Impressions), Hold Rate (15s plays / 3s plays), and Cost per Trial Booking (CPA).
> - If Bucket 6 (Cultural Pride / Shlokas) consistently achieves a 42% thumbstop rate while Bucket 2 (Fluency) achieves 26%, the scoring weights dynamically adjust to prioritize cultural pride moments.
> - Top-performing verbatim hooks are dynamically injected into the LLM prompt's few-shot examples, making the AI smarter and more aligned with our audience's evolving tastes every week."*

---

### Q10: "If hired tomorrow, what are your exact priorities in Week 1?"
**Model Answer:**
> *"In Week 1, my focus is on people, data, and baseline alignment:
> 1. Shadowing Video Editors & Marketing Execs: Spend 2 days observing their exact current manual scrubbing process to understand friction points, their favorite tools, and editing bottlenecks.
> 2. Establishing the Airtable Creative Hub: Stand up the standardized schema with 9:16 split-screen templates and preview thumbnails.
> 3. Running the 25-Class Pilot Cohort: Run our prompt prototype across 25 diverse sessions (English, Gita, Maths, Chess, Science), audit edge cases with the Creative Lead, and calibrate our 100-point scoring weights to achieve a >75% initial editor approval rate."*
