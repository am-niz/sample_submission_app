from odoo import fields, models, api


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    def _create_payments(self):
        res = super(AccountPaymentRegister, self)._create_payments()
        if self.line_ids.move_id:
            inv_id = self.line_ids.move_id
            sample_submission_id = self.env["sample.submission"].search([("id", "=", inv_id.sample_submission_id.id)])
            print(sample_submission_id, "+++++++++++++++")
            sample_submission_id.write({
                "invoice_status": inv_id.state,
                "collected_payment": self.amount,
                "balance": inv_id.amount_residual,
                "sum_of_cost": inv_id.amount_untaxed_signed,
                "profit": inv_id.amount_total_in_currency_signed - inv_id.amount_untaxed_signed,
            })
        return res