from import_export import resources
from blog.models import Students

class StudentResource(resources.ModelResource):
    class Meta:
        model = Students