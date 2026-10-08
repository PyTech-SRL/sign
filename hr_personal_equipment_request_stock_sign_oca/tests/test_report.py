# Copyright 2026 Simone Rubino - PyTech
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from .common import Common


class TestReport(Common):
    def test_multi_serial(self):
        """The Report can be printed when a request line has multiple lots."""
        # Arrange
        self.env.company.ppe_report_show_sn = True
        report = self.report
        request = self.ppe_sn_request
        quantity = request.line_ids.quantity
        lots = self.ppe_sn_product_lots[:quantity]
        request.accept_request()
        picking = request.picking_ids
        immediate_wizard_action = picking.button_validate()
        self.env[immediate_wizard_action["res_model"]].with_context(
            **immediate_wizard_action["context"]
        ).create({}).process()

        # Act
        report_content, _type = report._render_qweb_pdf(report.report_name, request.ids)

        # Assert
        report_content = report_content.decode()
        for lot in lots:
            self.assertIn(lot.name, report_content)
