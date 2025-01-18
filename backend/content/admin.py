from django.contrib import admin

from .models import New, Product, About, Project, ProjectProduct, ProjectRegion, Region, Map, MapRegion

admin.site.register(New)
admin.site.register(Product)
admin.site.register(About)
admin.site.register(Project)
admin.site.register(Region)
admin.site.register(ProjectProduct)
admin.site.register(ProjectRegion)
admin.site.register(Map)
admin.site.register(MapRegion)
