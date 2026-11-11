import json
import csv
import os

moments = [
    {
        "clip_id": "BAM-GITA-2125422751-01",
        "class_subject": "Bhagavad Gita (Little Yogi)",
        "source_file": "Gita_2125422751.mp4",
        "start_timestamp": "00:47:32.000",
        "end_timestamp": "00:48:32.000",
        "duration_seconds": 60.0,
        "cut_recommendation_duration": 22.0,
        "cut_subsegment": "00:47:32.000 -> 00:47:54.000 & 00:48:04.000 -> 00:48:15.000",
        "three_second_hook": "My 6-year-old wouldn't sit still for 2 minutes... until she started learning Gita.",
        "moment_bucket": "Real Learning Demonstration & Cultural Pride (Bucket 6)",
        "verbatim_dialogue": "NANCY SHUKLA: Close your eyes. Okay, say it properly. Close your eyes. Close your eyes. Now, tell me, with what sound we start our prayer? Big Om... but do we stretch the sound of Om? Very good! Now, who we are praying to, take the name of that Goddess?\nANAYA: Saraswati!\nNANCY SHUKLA: Very good! And now what we gonna say next to Saraswati?\nANAYA: Namastubhyam Varade!\nNANCY SHUKLA: Super, perfect! You have remembered those two words, very good! Now, the next words are Varade... Varade means that we are asking for her blessings.",
        "ai_score": 94,
        "score_breakdown": {
            "stopping_power": 24,
            "educational_value": 25,
            "audio_visual_clarity": 18,
            "emotional_authenticity": 14,
            "sound_off_legibility": 13
        },
        "geography_fit": "US, UK, GCC, Canada, Australia & India Metros (High NRI Appeal)",
        "parent_value": "Shows a young child living in the modern diaspora effortlessly chanting Sanskrit and understanding its deeper philosophical meaning with joy, proving learning goes beyond rote school.",
        "visual_verification": "VERIFIED (Both teacher and student webcams active; child closes eyes, joins hands, smiles; slide shows Goddess Saraswati artwork)",
        "compliance_flags": "PASS (Child's surname 'Mahato' in transcript is omitted from creative overlay; first name 'Anaya' kept or audio-softened; strictly secular character/moral framing)",
        "editor_instructions": "Create 9:16 vertical split. Top 55%: Saraswati slide illustration + teacher Nancy smiling. Bottom 45%: Student webcam centered. Opening hook text: 'Teaching our 6-year-old timeless Sanskrit values'. Kinetic yellow/white captions highlighting 'Om', 'Saraswati', 'Namastubhyam', 'Varade'. End CTA: 'Connect your child to their roots. Book Free Trial'.",
        "recommendation": "APPROVE (Priority 1 Paid Creative)"
    },
    {
        "clip_id": "BAM-ENG-2125604619-01",
        "class_subject": "English (Creative Writing)",
        "source_file": "English_2125604619.mp4",
        "start_timestamp": "00:15:47.000",
        "end_timestamp": "00:16:25.000",
        "duration_seconds": 38.0,
        "cut_recommendation_duration": 18.0,
        "cut_subsegment": "00:15:47.000 -> 00:16:18.000",
        "three_second_hook": "Does your child know the 'Story Mountain' formula for creative writing?",
        "moment_bucket": "The Eureka Moment (Bucket 1)",
        "verbatim_dialogue": "CHILD: Which part of the story mountain involves solving main problems? The ending. What do you think to do?\nMRIDULA BOSE: Which part of the story mountain involves solving the problem? In which part of the story mountain will you solve the problem?\nCHILD: The ending.\nMRIDULA BOSE: No, solving the problem is resolution!\nCHILD: Oh yeah! I chose some... resolution! Okay, I choose it! I choose it!",
        "ai_score": 86,
        "score_breakdown": {
            "stopping_power": 22,
            "educational_value": 24,
            "audio_visual_clarity": 16,
            "emotional_authenticity": 12,
            "sound_off_legibility": 12
        },
        "geography_fit": "India Metros, GCC (Dubai/Sharjah/Riyadh), UK & US",
        "parent_value": "Demonstrates structured cognitive thinking—teaching children that great stories aren't random, but follow a 5-step narrative arc (Problem -> Climax -> Resolution).",
        "visual_verification": "VERIFIED (Slide shows dynamic visual Story Mountain graphic with color-coded stages; student camera active, animated hand gestures)",
        "compliance_flags": "PASS (Child's name 'Zian' referred to conversationally; anonymize to initial 'Z.' in caption; positive encouraging guidance)",
        "editor_instructions": "9:16 vertical split. Top 50%: Story Mountain graphic zooming into 'Problem vs Resolution' apex. Bottom 50%: Student face when eureka realization hits ('Oh yeah! Resolution!'). Add subtle lightbulb sound effect (SFX) at 00:16:17. CTA: 'Help your child write stories teachers love. Book Free Creative Writing Trial'.",
        "recommendation": "APPROVE (Priority 2 Paid Creative)"
    },
    {
        "clip_id": "BAM-GITA-2125422751-02",
        "class_subject": "Bhagavad Gita (Little Yogi)",
        "source_file": "Gita_2125422751.mp4",
        "start_timestamp": "00:39:39.000",
        "end_timestamp": "00:40:58.000",
        "duration_seconds": 79.0,
        "cut_recommendation_duration": 19.0,
        "cut_subsegment": "00:39:45.000 -> 00:40:10.000 & 00:40:55.000 -> 00:41:00.000",
        "three_second_hook": "How we teach 6-year-olds to beat digital distraction in 60 seconds.",
        "moment_bucket": "Confidence Transformation & Mindfulness (Bucket 4)",
        "verbatim_dialogue": "NANCY SHUKLA: Just sit like this, bow, and I'll play the Om chant. Ready? I'll play the Om chant now. And Anaya, the rule is: try to focus on your breathing. Breathing. How are you breathing in and breathing out... [Student sits upright, closes eyes, completely serene] ...Very good. Now you can open your eyes. So how was it? Was it good?",
        "ai_score": 88,
        "score_breakdown": {
            "stopping_power": 23,
            "educational_value": 22,
            "audio_visual_clarity": 18,
            "emotional_authenticity": 13,
            "sound_off_legibility": 12
        },
        "geography_fit": "Global (US, UK, Canada, GCC, India Metros)",
        "parent_value": "Addresses the #1 parental pain point in 2026: digital overstimulation, ADHD-like hyperactivity, and screen addiction. Shows mindfulness made accessible for young kids.",
        "visual_verification": "VERIFIED (Full camera view of child seated calmly, eyes closed, breathing peacefully, high visual contrast to chaotic social media feeds)",
        "compliance_flags": "PASS (No religious preaching, strictly breath-work and mindfulness training; child safe and relaxed)",
        "editor_instructions": "High contrast peaceful opening. First 3s text: 'Every parent is worried about screen time. Here is what we do instead.' Gentle binaural ambient audio ducked behind teacher's soothing voice. End card: 'Building calm minds & unshakable focus. Bambinos Little Yogi. Free Trial'.",
        "recommendation": "APPROVE (Priority 2 Paid Creative)"
    },
    {
        "clip_id": "BAM-ENG-2125604619-02",
        "class_subject": "English (Public Speaking & Vocabulary)",
        "source_file": "English_2125604619.mp4",
        "start_timestamp": "00:12:09.000",
        "end_timestamp": "00:12:45.000",
        "duration_seconds": 36.0,
        "cut_recommendation_duration": 16.0,
        "cut_subsegment": "00:12:18.000 -> 00:12:35.000",
        "three_second_hook": "How we turn hesitant young speakers into expressive storytellers.",
        "moment_bucket": "Student Participation & Conversational Fluency (Bucket 2)",
        "verbatim_dialogue": "CHILD: Imagine... a sand and water and we were picnic and we were eating salmon!\nMRIDULA BOSE: What did you see? What did you hear? You saw... I saw!\nCHILD: Okay teacher! And I see turtles, I saw a crab, I saw a fish, I saw so many stuff and I saw sandwich and I saw food and people and animals!",
        "ai_score": 77,
        "score_breakdown": {
            "stopping_power": 18,
            "educational_value": 19,
            "audio_visual_clarity": 16,
            "emotional_authenticity": 12,
            "sound_off_legibility": 12
        },
        "geography_fit": "India Metros & Tier 1/2, GCC",
        "parent_value": "Demonstrates real-time gentle coaching: teacher nudges child from fragmented speech to rich descriptive vocabulary and correct past-tense storytelling.",
        "visual_verification": "VERIFIED (Child expressive and gesturing, teacher smiling warmly)",
        "compliance_flags": "PASS (Wholesome interaction, safe learning environment)",
        "editor_instructions": "Focus on the child's animated face in lower 50%. Pop animated illustrated stickers of turtles, crabs, and sandwiches on screen as the child lists them to enhance sound-off engagement.",
        "recommendation": "REVIEW (Secondary Creative / Requires Tight Editing)"
    },
    {
        "clip_id": "BAM-SCI-2125687282-01",
        "class_subject": "Science (Interactive Biology)",
        "source_file": "Science_2125687282.mp4",
        "start_timestamp": "00:17:30.000",
        "end_timestamp": "00:18:35.000",
        "duration_seconds": 65.0,
        "cut_recommendation_duration": 20.0,
        "cut_subsegment": "00:17:40.000 -> 00:18:05.000",
        "three_second_hook": "Science isn't memorizing textbooks. It's understanding how life responds.",
        "moment_bucket": "Interactive Learning & Gamified Discovery (Bucket 3)",
        "verbatim_dialogue": "MARY JAMES: There is a student who touches a Touch-Me-Not plant. What happens to the leaves when you touch it?\nDEVNANDA: Folds inwards!\nMARY JAMES: When you touch it, what happens is that it folds inwards! But on the other hand, if she steps onto a dry wooden twig, it just breaks. Why? Because the plant is alive and responding to stimulus!",
        "ai_score": 67,
        "score_breakdown": {
            "stopping_power": 16,
            "educational_value": 18,
            "audio_visual_clarity": 13,
            "emotional_authenticity": 10,
            "sound_off_legibility": 10
        },
        "geography_fit": "South India (Kerala Diaspora / Bilingual Target)",
        "parent_value": "Shows biological stimuli explained through everyday objects (plant vs dry twig) rather than abstract jargon.",
        "visual_verification": "VERIFIED (Slide illustration of plant active; student webcam active)",
        "compliance_flags": "PASS on tone; CAUTION on language code-mixing (teacher uses conversational Malayalam in surrounding sentences; audio requires careful trimming to keep only English dialogue)",
        "editor_instructions": "Trim tightly to the 20-second English-only dialogue segment. Add split comparison graphics: Live plant leaf folding on left vs dry twig snapping on right.",
        "recommendation": "REVIEW / BORDERLINE (Regional Campaign Only)"
    },
    {
        "clip_id": "BAM-MATH-2125736982-NEG",
        "class_subject": "Maths (Measurement)",
        "source_file": "Maths_2125736982.mp4",
        "start_timestamp": "00:37:40.000",
        "end_timestamp": "00:48:15.000",
        "duration_seconds": 635.0,
        "cut_recommendation_duration": 0.0,
        "cut_subsegment": "N/A (Disqualified)",
        "three_second_hook": "N/A (Disqualified)",
        "moment_bucket": "HARD EXCLUSION: Negative Teacher Tone & Student Shaming",
        "verbatim_dialogue": "NAAZISH KHANAM: Silly simple thing you are not understanding... how many times do I need to say that one segment is one meter... This way I will not teach you Shree Shah. Thus, this is enough. You are not at all learning at home... 10 points out of 8 questions... is it a good score? From next time you will score full zero... your father always say that she doesn't study at home at all.\nSTUDENT: I didn't understand measurement... Will you teach me in the next class?\nNAAZISH KHANAM: I don't think that it is of any use.",
        "ai_score": 12,
        "score_breakdown": {
            "stopping_power": 5,
            "educational_value": 3,
            "audio_visual_clarity": 2,
            "emotional_authenticity": 1,
            "sound_off_legibility": 1
        },
        "geography_fit": "NONE (Disqualified Globally)",
        "parent_value": "ZERO. Extremely damaging to brand trust. Would cause instant public backlash and brand destruction if published.",
        "visual_verification": "REJECTED (Child visibly demoralized, camera displays tension)",
        "compliance_flags": "CRITICAL FAIL: Red Line 1 (PII: Student full name 'Shree Shah / Shrisha' repeatedly exposed; father's private comments cited); Red Line 2 (Teacher Impatience & Shaming: 'silly', 'waste of time', 'I will not teach you'); Red Line 3 (Child Distress & Humiliation).",
        "editor_instructions": "DO NOT EDIT. DO NOT PUBLISH. Auto-quarantined. Incident report auto-generated and dispatched to Head of Academic Operations and Faculty Training Lead.",
        "recommendation": "REJECT & ESCALATE (Incident #BAM-QA-902)"
    }
]

# Write JSON
with open('outputs/extracted_moments.json', 'w', encoding='utf-8') as f:
    json.dump(moments, f, indent=2)
print("Saved outputs/extracted_moments.json")

# Write CSV
csv_fields = [
    'clip_id', 'class_subject', 'source_file', 'start_timestamp', 'end_timestamp', 
    'duration_seconds', 'three_second_hook', 'moment_bucket', 'verbatim_dialogue', 
    'ai_score', 'geography_fit', 'parent_value', 'visual_verification', 
    'compliance_flags', 'editor_instructions', 'recommendation'
]

with open('outputs/extracted_moments.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=csv_fields, extrasaction='ignore')
    writer.writeheader()
    for m in moments:
        writer.writerow(m)
print("Saved outputs/extracted_moments.csv")

