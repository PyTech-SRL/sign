# Copyright 2026 Simone Rubino - PyTech
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from .common import Common


class TestReport(Common):
    def test_multi_serial(self):
        """The Report can be printed when a request line has multiple lots."""
        request = self.ppe_sn_request
        request.accept_request()
