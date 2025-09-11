from ingest import load_leads, save_leads
from ai import process_lead
from emailer import send_email
from report import generate_report
import os


def run_pipeline():
    leads = load_leads("../data/leads.csv")
    enriched = []

    for lead in leads:
        enriched_lead = process_lead(lead)

        # Try to send email and track success
        email_sent = send_email(enriched_lead)
        enriched_lead["email_sent"] = email_sent

        enriched.append(enriched_lead)

    # Ensure reports directory exists
    os.makedirs("reports", exist_ok=True)

    save_leads(enriched, "../data/leads_enriched.csv")
    generate_report(enriched, "reports/campaign_summary.md")


if __name__ == "__main__":
    run_pipeline()
