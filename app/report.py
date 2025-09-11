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

def generate_report(leads, out_path):
    total = len(leads)
    contacted = sum(1 for l in leads if l["status"] == "Contacted")

    stats = f"""
    # Campaign Summary
    - Total leads: {total}
    - Contacted: {contacted}
    """

    # Ask AI to add insights
    prompt = f"Here are campaign stats:\n{stats}\n\nGenerate insights."
    response = client.chat.completions.create(
        model="gemini-2.5-flash", messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content

    with open(out_path, "w") as f:
        f.write(stats + "\n\n" + result)

    print(f"Report saved to {out_path}")
