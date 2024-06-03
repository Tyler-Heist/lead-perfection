from . import utils


class Leads(object):
    def __init__(self, access_token, server_id):
        self.server_id = server_id
        self.headers = {
            'Authorization': f'Bearer {access_token}',
            'accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    def get_inbound_lead_info(
            self,
            start_date: str = None,
            end_date: str = None,
            pro_id: int = None,
            log_number: str = None,
            page_size: int = None,
            start_index: int = None
    ):
        data = {
            'startdate': start_date,
            'enddate': end_date,
            'pro_id': pro_id,
            'lognumber': log_number,
            'PageSize': page_size,
            'StartIndex': start_index
        }
        url = f'https://{self.server_id}.leadperfection.com/api/Customers/GetInboundLeadInfo'
        return utils.make_request(url, data, self.headers)

    def get_leads_forward_look(self):

        url = f'https://{self.server_id}.leadperfection.com/api/Customers/GetLeadsForwardLook'
        return utils.make_request(url, data, self.headers)


    def lead_add(self):

        url = f'https://{self.server_id}.leadperfection.com/api/Customers/LeadAdd'
        return utils.make_request(url, data, self.headers)


    def get_leads_inbounds(self):

        url = f'https://{self.server_id}.leadperfection.com/api/Customers/GetLeadsInbounds'
        return utils.make_request(url, data, self.headers)


    def get_lead_data(self):

        url = f'https://{self.server_id}.leadperfection.com/api/Customers/GetLeadData'
        return utils.make_request(url, data, self.headers)


    def get_leads_settings(self):

        url = f'https://{self.server_id}.leadperfection.com/api/Customers/GetLeadsSettings'
        return utils.make_request(url, data, self.headers)


    def get_leads_source_sub_promoter(self):

        url = f'https://{self.server_id}.leadperfection.com/api/Customers/GetLeadsSourceSubPromoter'
        return utils.make_request(url, data, self.headers)


    def update_leads_perspective_detail(self):

        url = f'https://{self.server_id}.leadperfection.com/api/Customers/UpdateLeadsPerspectiveDetail'
        return utils.make_request(url, data, self.headers)


    def leads_login_message(self):

        url = f'https://{self.server_id}.leadperfection.com/api/Customers/LeadsLoginMessage'
        return utils.make_request(url, data, self.headers)


    def get_leads_confirmed_message(self):

        url = f'https://{self.server_id}.leadperfection.com/api/Customers/GetLeadsConfirmedMessage'
        return utils.make_request(url, data, self.headers)


    def add_spectrum_lead(self):

        url = f'https://{self.server_id}.leadperfection.com/api/Customers/AddSpectrumLead'
        return utils.make_request(url, data, self.headers)


    def get_spectrum_results(self):

        url = f'https://{self.server_id}.leadperfection.com/api/Customers/GetSpectrumResults'
        return utils.make_request(url, data, self.headers)


