from ingest import load_leads, save_leads
from ai import process_lead
from emailer import send_email
from report import generate_report


def run_pipeline():
    leads = load_leads("data/leads.csv")
    enriched = []

    for lead in leads:
        enriched_lead = process_lead(lead)
        send_email(enriched_lead)  # goes to MailHog
        enriched.append(enriched_lead)

    save_leads(enriched, "data/leads_enriched.csv")
    generate_report(enriched, "reports/campaign_summary.md")


if __name__ == "__main__":
    run_pipeline()
