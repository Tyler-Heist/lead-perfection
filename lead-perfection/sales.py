from . import utils


class Sales(object):
    def __init__(self, access_token, server_id):
        self.server_id = server_id
        self.headers = self.headers = utils.headers(access_token=access_token)

    def add_job_images(
            self,
            job_id: int = None,
            file_name: str = None,
            doc_descr: str = None,
            doc_type_id: int = None,
            file_bytes: list = None
    ):
        data = {
            'jobid': job_id,
            'filename': file_name,
            'docdescr': doc_descr,
            'dtyid': doc_type_id,
            'filebytes': file_bytes
        }
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/AddJobImages'
        return utils.make_request(url, data, self.headers)

    def add_notes(self, rec_type: str = None, rec_id: int = None, notes: str = None):
        # Record Type: cst=Prospect, ils=Issued Lead, job=Job Detail
        data = {'rectype': rec_type, 'recid': rec_id, 'notes': notes}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/AddNotes'
        return utils.make_request(url, data, self.headers)

    def add_sales_job_commission(
            self,
            job_id: int = None,
            sales_rep_id: int = None,
            commission_pay_amt: float = None,
            commission_type: int = None,
            comments: str = None
    ):
        data = {
            'jobid': job_id,
            'comslrid': sales_rep_id,
            'compmtamount': commission_pay_amt,
            'cptid': commission_type,
            'comments': comments
        }
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/AddSalesJobCommission'
        return utils.make_request(url, data, self.headers)

    def add_sales_job_payment(
            self,
            job_id: int = None,
            payment_date: str = None,
            payment_amt: float = None,
            payment_type_id: str = None,
            payment_method_id: str = None,
            payment_notes: str = None,
            ar_batch_num: int = 0,
            inc_batch_num: int = 0
    ):
        data = {
            'jobid': job_id,
            'pmtdate': payment_date,
            'pmtamount': payment_amt,
            'pmtid': payment_type_id,
            'pmmid': payment_method_id,
            'pmtnotes': payment_notes,
            'arbatchno': ar_batch_num,
            'incbatchno': inc_batch_num
        }
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/AddSalesJobPayment'
        return utils.make_request(url, data, self.headers)

    def add_sales_job_cost(
            self,
            job_id: int = None,
            mat_id: str = None,
            qty: int = None,
            cost: float = None,
            price: float = None,
            comm_flag: bool = False,
            override_flag: bool = False,
            invoice_date: str = None,
            invoice_number: str = None,
            comments: str = None,
            entered_by: int = None,
            est_qty: int = None,
            est_cost: float = None
    ):
        data = {
            'job_id': job_id,
            'mat_id': mat_id,
            'qty': qty,
            'cost': cost,
            'price': price,
            'commFlag': comm_flag,
            'overrideFlag': override_flag,
            'invoiceDate': invoice_date,
            'invoiceNumber': invoice_number,
            'comments': comments,
            'enteredBy': entered_by,
            'estQty': est_qty,
            'estCost': est_cost,
        }
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/AddSalesJobCost'
        return utils.make_request(url, data, self.headers)

    def add_salesman_images(
            self,
            ils_id: int = None,
            file_name: str = None,
            doc_descr: str = None,
            doc_type_id: int = None,  # use /api/SalesApi/GetSalesApptDispProd with type=y to enumerate possible values
            file_bytes: list = None
    ):
        data = {
            'ilsid': ils_id,
            'filename': file_name,
            'docdescr': doc_descr,
            'dtyid': doc_type_id,
            'filebytes': file_bytes
        }
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/AddSalesmanImages'
        return utils.make_request(url, data, self.headers)

    def get_links(self, rec_type: str = None, rec_id: int = None):
        data = {'rectype': rec_type, 'recid': rec_id}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetLinks'
        return utils.make_request(url, data, self.headers)

    def get_prospect_job_id(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetProspectJobID'
        return utils.make_request(url, data, self.headers)

    def get_sales_appt_disp_prod(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetSalesApptDispProd'
        return utils.make_request(url, data, self.headers)

    def get_sales_appt_cal(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetSalesApptCal'
        return utils.make_request(url, data, self.headers)

    def get_sales_appt_day_list(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetSalesApptDayList'
        return utils.make_request(url, data, self.headers)

    def get_sales_appt_detail(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetSalesApptDetail'
        return utils.make_request(url, data, self.headers)

    def get_sales_appt_detail_date_range(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetSalesApptDetailDateRange'
        return utils.make_request(url, data, self.headers)

    def get_sales_appt_list(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetSalesApptList'
        return utils.make_request(url, data, self.headers)

    def get_sales_job_detail(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetSalesJobDetail'
        return utils.make_request(url, data, self.headers)

    def get_sales_open(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetSalesOpen'
        return utils.make_request(url, data, self.headers)

    def get_sales_sched_cal(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetSalesSchedCal'
        return utils.make_request(url, data, self.headers)

    def get_sales_sched_detail(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetSalesSchedDetail'
        return utils.make_request(url, data, self.headers)

    def get_sales_stats(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/GetSalesStats'
        return utils.make_request(url, data, self.headers)

    def sales_login_message(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/SalesLoginMessage'
        return utils.make_request(url, data, self.headers)

    def update_sales_appt_detail(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/UpdateSalesApptDetail'
        return utils.make_request(url, data, self.headers)

    def update_sales_appt_detail2(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/UpdateSalesApptDetail2'
        return utils.make_request(url, data, self.headers)

    def update_sales_appt_detail3(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/UpdateSalesApptDetail3'
        return utils.make_request(url, data, self.headers)

    def update_sales_job_cost(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/UpdateSalesJobCost'
        return utils.make_request(url, data, self.headers)

    def update_sales_job_detail(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/UpdateSalesJobDetail'
        return utils.make_request(url, data, self.headers)

    def update_sales_ack(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/UpdateSalesAck'
        return utils.make_request(url, data, self.headers)

    def update_sales_sched_detail(self):
        data = {}
        url = f'https://{self.server_id}.leadperfection.com/api/SalesApi/UpdateSalesSchedDetail'
        return utils.make_request(url, data, self.headers)
