# Loom Video Walkthrough Script (2–3 Minutes)

**Role:** AI Program Manager (Marketing) — Take-Home Case  
**Candidate:** Harshit (B.Tech CSE/IT — Track: Marketing)  
**Tone:** Confident, analytical, structured, growth-oriented, executive-ready.  
**Video Goal:** Walk the Function Head through the problem, the live assets analysis, the compliance catch, and the business ROI in under 3 minutes.

---

### [0:00 – 0:30] Hook & Business Context
*(Camera on you / Screen showing GitHub README or Slide 1)*

> "Hi everyone, I'm Harshit, and this is my walkthrough for the Bambinos.live AI Program Manager Take-Home Case: building an end-to-end AI pipeline to turn live class recordings into scroll-stopping marketing content.
> 
> Today, Bambinos' highest-converting ads are authentic, unscripted classroom moments where a scrolling parent stops and realizes: *'Something is happening here that doesn't happen in my child's regular school.'*
> 
> But finding these moments manually is our biggest bottleneck. Marketing executives spend 45 to 50 minutes scrubbing each 50-minute recording, and 85 to 90% of sessions yield zero usable ad clips. Across 500 weekly classes, that’s 375 wasted human hours. My mission was to build an automated pipeline that does this in under 2.5 minutes per session—a 10x to 15x operational speedup."

---

### [0:30 – 1:15] Creative Taxonomy & The Maths Session Compliance Trap
*(Screen showing `evaluation/scoring_rubric.md` or Extracted Outputs Table)*

> "Before writing a single prompt, I established a rigorous creative foundation. I analyzed Meta Ad Library strategies across PlanetSpark, Bhanzu, and BrightCHAMPS, and built a 6-Bucket Creative Taxonomy:
> - Eureka Moments
> - Conversational Fluency
> - Gamified Discovery
> - Mindfulness & Focus
> - Inspiring Mentorship
> - Real Learning & Cultural Pride
> 
> To evaluate moments objectively, I created a 100-Point Scoring Rubric covering Stopping Power, Proof of Learning, Production Clarity, Emotional Authenticity, and Sound-Off Legibility.
> 
> Crucially, our pipeline enforces 7 Hard Compliance Exclusions. And this was battle-tested on the official assets:
> When I analyzed the provided Maths session (`2125736982`), the teacher repeatedly scolded the student, called her silly, threatened zero marks, and leaked the student's full name. 
> A naive AI searching for keywords would have passed this clip. But our compliance gate caught the negative tone, student distress, and PII violations, immediately scoring it 12/100 and auto-quarantining it to Academic QA."

---

### [1:15 – 2:00] Real Asset Hits & The Audio vs. Visual Engine
*(Screen showing Extracted Output Table or `outputs/editor_briefs.md`)*

> "On the positive side, the pipeline extracted exceptional ad briefs:
> - In our Bhagavad Gita session, a 6-year-old flawlessly recited *'Saraswati Namastubhyam Varade'* and explained its meaning with pure joy. This scored a massive 94/100 as a Tier-1 Priority 1 creative with huge appeal for NRI parents in the US and GCC.
> - In English, we captured a brilliant Eureka moment where a student grasped the narrative arc of the Story Mountain formula, scoring 86/100.
> 
> To solve the critical 'Audio vs. Visual' gap—where transcripts can't see if a child's camera is off—our automated OpenCV worker extracts 3 keyframes per moment, checks lighting, face centering, and slide relevance, ensuring editors never waste time cutting dead footage."

---

### [2:00 – 2:45] Business Impact, Unit Economics & 30-60-90 Day Rollout
*(Screen showing ROI Table in PDF Report or README)*

> "Let's talk business impact. Modeling this at Bambinos' baseline volume of 500 classes per week:
> - We reduce human review time per class from 45 minutes to 2.5 minutes—a 94.4% reduction.
> - We save 354 human hours every week, unlocking 8.9 full-time employees from video scrubbing to focus on creative strategy.
> - Our discovery cost per approved ad clip drops from $85 to $8.75.
> - Net annual operational savings exceed $218,000 with a 77x net ROI multiple.
> 
> My 30-60-90 day roadmap rolls this out in three distinct phases:
> - Day 1 to 30: Pilot test with 25 sessions, establish editor alignment in Airtable, and achieve an 80% AI acceptance rate.
> - Day 31 to 60: Deploy n8n cloud automation with Whisper and OpenCV, launching instant Slack editor alerts.
> - Day 61 to 90: Scale to all 500 weekly classes, introduce geographic routing, and close the loop with Meta Ads ROAS telemetry.
> 
> Everything is fully documented, tested, and reproducible in the repository, and compiled into the executive PDF report. Thank you, and I look forward to our live case review!"
