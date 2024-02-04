from rest_framework.test import APITestCase
from pecoret.core.test import PeCoReTTestCaseMixin
from backend.models.company_contact import CompanyContact


class CompanyContactListViewTestCase(APITestCase, PeCoReTTestCaseMixin):
    def setUp(self) -> None:
        self.init_mixin()
        self.company = self.project1.company
        self.url = self.get_url("backend:companies:contact-list", company=self.company.pk)

    def test_allowed(self):
        users = [
            self.management1, self.management2, self.pentester1, self.read_only1, self.customer1
        ]
        for user in users:
            self.client.force_login(user)
            self.basic_status_code_check(self.url, self.client.get, 200)

    def test_forbidden(self):
        users = [
            self.pentester2, self.user1, self.vendor1, self.vendor2,
            self.advisory_manager1, self.customer2
        ]
        for user in users:
            self.client.force_login(user)
            self.basic_status_code_check(self.url, self.client.get, 403)


class CompanyContactDeleteViewTestCase(APITestCase, PeCoReTTestCaseMixin):
    def setUp(self) -> None:
        self.init_mixin()
        self.company_contact = self.create_instance(CompanyContact)
        self.url = self.get_url("backend:companies:contact-detail", company=self.company_contact.company.pk,
                                pk=self.company_contact.pk)

    def test_management2(self):
        self.client.force_login(self.management2)
        self.basic_status_code_check(self.url, self.client.delete, 204)

    def test_management1(self):
        self.client.force_login(self.management1)
        self.basic_status_code_check(self.url, self.client.delete, 204)

    def test_forbidden(self):
        users = [
            self.read_only1, self.pentester1, self.pentester2, self.user1, self.customer2
        ]
        for user in users:
            self.client.force_login(user)
            self.basic_status_code_check(self.url, self.client.delete, 403)


class CompanyContactUpdateViewTestCase(APITestCase, PeCoReTTestCaseMixin):
    def setUp(self) -> None:
        self.init_mixin()
        self.company_contact = self.create_instance(CompanyContact)
        self.url = self.get_url("backend:companies:contact-detail", company=self.company_contact.company.pk,
                                pk=self.company_contact.pk)
        self.data = {"last_name": "fromtest"}

    def test_allowed(self):
        users = [
            self.management1, self.management2
        ]
        for user in users:
            self.client.force_login(user)
            self.basic_status_code_check(self.url, self.client.patch, 200, data=self.data)

    def test_customer(self):
        self.client.force_login(self.customer1)
        self.company_contact = self.create_instance(CompanyContact, company=self.project1.company)
        self.url = self.get_url('backend:companies:contact-detail', company=self.project1.company.pk,
                                pk=self.company_contact.pk)
        self.basic_status_code_check(self.url, self.client.patch, 200, data=self.data)

    def test_forbidden(self):
        users = [
            self.pentester2, self.pentester1, self.read_only1, self.user1, self.customer2, self.customer1
        ]
        for user in users:
            self.client.force_login(user)
            self.basic_status_code_check(self.url, self.client.patch, 403, data=self.data)
