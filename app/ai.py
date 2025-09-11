import json
from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def process_lead(lead):
    prompt = f"""
    You are an assistant that enriches sales leads.

    Lead info: {lead}

    Return ONLY valid JSON. 
    Do not include explanations, markdown, or code fences. Just raw JSON.

    Format:
    {{
    "priority_score": <integer between 1-10>,
    "persona": "<string>",
    "outreach_email": "<string, short personalized email>",
    "status": "Contacted"
    }}
    """

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    result = response.choices[0].message.content.strip()
    print("RAW RESULT:", result)

    try:
        parsed = json.loads(result)
    except json.JSONDecodeError:
        print("Failed to parse JSON, falling back to defaults.")
        parsed = {
            "priority_score": 5,
            "persona": "Unknown",
            "outreach_email": "Hi there, would love to connect.",
            "status": "Contacted",
        }

    lead.update(parsed)
    return lead
