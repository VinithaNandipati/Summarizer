import os
import json
from dotenv import load_dotenv
import whisper
from openai import OpenAI

# --- Load API key ---
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

# --- Step 1: Local transcription using Whisper ---
audio_file = "final_test_audio.mp3"  # put your audio file in project folder
model = whisper.load_model("base")   # "base", "small", "medium", "large"
result = model.transcribe(audio_file)
transcript_text = result["text"]

print("\n----- FULL TRANSCRIPT -----\n")
print(transcript_text)

# --- Step 2: Generate summary + action items using GPT ---
prompt = f"""
Summarize this meeting transcript into:
1. KEY DECISIONS (bulleted)
2. ACTION ITEMS (task, owner, deadline if mentioned)

Transcript:
{transcript_text}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

summary_text = response.choices[0].message.content

print("\n----- SUMMARY & ACTION ITEMS -----\n")
print(summary_text)

# --- Step 3: Save results ---
with open("meeting_summary.json", "w", encoding="utf-8") as f:
    json.dump({"transcript": transcript_text, "summary": summary_text}, f, indent=2)

print("\nMeeting summary saved to meeting_summary.json")
