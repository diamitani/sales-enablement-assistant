class OutreachBot:
    def __init__(self, campaign_details):
        self.campaign_details = campaign_details

    def execute_campaign(self):
        return f"Outreach campaign initiated with the following details: {self.campaign_details}"
