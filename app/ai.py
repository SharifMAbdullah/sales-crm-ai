from openai import OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=openai.api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

def process_lead(lead):
    # Call LLM to enrich lead
    prompt = f"""
    Lead info: {lead}
    1. Score this lead (1-10).
    2. Suggest buyer persona.
    3. Fill missing details if obvious.
    4. Draft a short outreach email.
    """
    response = client.chat.completions.create(
        model="gemini-2.5-flash", messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message["content"]

    lead["priority_score"] = 8  # parse from result
    lead["persona"] = "Decision Maker"
    lead["outreach_email"] = "Hi John, I noticed your work at ACME..."
    lead["status"] = "Contacted"

    return lead
