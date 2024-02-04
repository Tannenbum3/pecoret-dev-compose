from rest_framework.test import APITestCase
from pecoret.core.test import PeCoReTTestCaseMixin
from backend.models.api_token import APIToken


class APITokenCreateView(APITestCase, PeCoReTTestCaseMixin):
    def setUp(self) -> None:
        self.init_mixin()
        self.url = self.get_url("backend:api-token-list")
        self.data = {
            "name": "test token",
            "scope_companies": "No Access",
            "scope_user": "No Access",
            "scope_all_projects": "No Access",
            "scope_advisories": "No Access"
        }

    def test_allowed(self):
        users = [
            self.pentester2, self.pentester1, self.management2,
            self.management1, self.advisory_manager1
        ]
        for user in users:
            self.client.force_login(user)
            response = self.basic_status_code_check(self.url, self.client.post, 201, data=self.data)
            self.assertIsNotNone(response.json().get("token"))
