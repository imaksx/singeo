from django.contrib import admin

from .models import New, Product, About, Project, ProjectProduct, ProjectRegion, Region, Map, MapRegion, TagForProject, TagProject, TagForProduct, TagProduct

admin.site.register(New)
admin.site.register(Product)
admin.site.register(About)
admin.site.register(Project)
admin.site.register(Region)
admin.site.register(ProjectProduct)
admin.site.register(ProjectRegion)
admin.site.register(Map)
admin.site.register(MapRegion)
admin.site.register(TagForProject)
admin.site.register(TagProject)
admin.site.register(TagForProduct)
admin.site.register(TagProduct)
