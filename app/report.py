import openai


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
    response = openai.ChatCompletion.create(
        model="gemini-2.5-flash", messages=[{"role": "user", "content": prompt}]
    )

    insights = response.choices[0].message["content"]

    with open(out_path, "w") as f:
        f.write(stats + "\n\n" + insights)

    print(f"📊 Report saved to {out_path}")
