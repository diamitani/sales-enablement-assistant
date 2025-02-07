class SalesPlaybookTemplate:
    def __init__(self, sales_goals, kpis, customer_profile):
        self.sales_goals = sales_goals
        self.kpis = kpis
        self.customer_profile = customer_profile

    def create_document(self):
        return f"""
        Sales Playbook:
        ------------------
        Sales Goals: {self.sales_goals}
        KPIs: {self.kpis}
        Customer Profile: {self.customer_profile}

        Strategies:
        - Define target market and segments
        - Set up multi-channel outreach campaigns
        - Monitor KPIs and iterate on feedback
        """
