from rest_framework.test import APITestCase
from checklists.models import AssetChecklist, Checklist
from pecoret.core.test import PeCoReTTestCaseMixin


class AssetChecklistListView(APITestCase, PeCoReTTestCaseMixin):
    def setUp(self):
        self.init_mixin()
        self.checklist1 = self.create_asset_checklist(project=self.project1,
                                                      component=self.asset1)
        self.checklist2 = self.create_asset_checklist(project=self.project2,
                                                      component=self.asset2)
        self.url = self.get_url("checklists:projects:checklist-list", project=self.project1.pk)

    def test_allowed(self):
        users = [
            self.pentester1, self.management1, self.read_only1
        ]
        for user in users:
            self.client.force_login(user)
            response = self.basic_status_code_check(self.url, self.client.get, 200)
            self.assertEqual(response.json()["count"], 1)
            results = response.json()["results"]
            self.assertEqual(results[0]["pk"], self.checklist1.pk)

    def test_component_filter(self):
        self.client.force_login(self.pentester1)
        self.url = self.url + f"?web_application={self.asset1.pk}"
        response = self.basic_status_code_check(self.url, self.client.get, 200)
        self.assertEqual(response.json()["count"], 1)

    def test_component_filter_invalid(self):
        self.client.force_login(self.pentester1)
        self.url = self.url + f"?web_application={self.asset2.pk}"
        response = self.basic_status_code_check(self.url, self.client.get, 200)
        self.assertEqual(response.json()["count"], 0)

    def test_forbidden(self):
        users = [
            self.pentester2, self.management2, self.advisory_manager1,
            self.user1
        ]
        for user in users:
            self.client.force_login(user)
            self.basic_status_code_check(self.url, self.client.get, 403)


class AssetChecklistCreateView(APITestCase, PeCoReTTestCaseMixin):
    def setUp(self):
        self.init_mixin()
        self.checklist = self.create_instance(Checklist)
        self.url = self.get_url("checklists:projects:checklist-list", project=self.project1.pk)
        self.data = {
            "checklist_id": self.checklist.checklist_id,
            "component": {"type": self.asset1.asset_type, "pk": self.asset1.pk}
        }

    def test_allowed(self):
        users = [
            self.pentester1, self.management1
        ]
        for user in users:
            self.client.force_login(user)
            self.basic_status_code_check(self.url, self.client.post, 201, data=self.data)
            AssetChecklist.objects.all().delete()

    def test_forbidden(self):
        users = [
            self.pentester2, self.management2, self.read_only1,
            self.user1, self.advisory_manager1
        ]
        for user in users:
            self.client.force_login(user)
            self.basic_status_code_check(self.url, self.client.post, 403, data=self.data)

    def test_foreign_asset(self):
        self.data["component"]["pk"] = self.asset2.pk
        self.client.force_login(self.pentester1)
        self.basic_status_code_check(self.url, self.client.post, 400, data=self.data)
