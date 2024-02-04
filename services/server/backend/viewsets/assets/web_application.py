from pecoret.core.viewsets import PeCoReTModelViewSet
from pecoret.core import permissions
from backend.serializers.assets.web_application import WebApplicationSerializer
from backend.models import WebApplication


class WebApplicationViewSet(PeCoReTModelViewSet):
    permission_classes = [
        permissions.PRESET_PENTESTER_OR_READONLY
    ]
    api_scope = "scope_all_projects"
    queryset = WebApplication.objects.none()
    serializer_class = WebApplicationSerializer
    search_fields = ["name", "base_url"]

    def get_queryset(self):
        return WebApplication.objects.for_project(self.request.project)

    def perform_create(self, serializer):
        serializer.save(project=self.request.project)
