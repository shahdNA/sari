from django.contrib import admin

from .models import Country, City, Restaurant
admin.site.site_header="resadmin"
admin.site.site_title="resadmin"


class InlineRestaurant(admin.TabularInline):
   model = Restaurant
   extra = 1


class CityAdmin(admin.ModelAdmin):
   inlines = [InlineRestaurant]


class RestaurantAdmin(admin.ModelAdmin):
   fields = ('name','city','address')
   list_display = ('name','city','address','combaine_city_and_name')
   # list_display_links = ('address','city')
   list_editable = ('address','city')
   list_filter = ('city','name')
   search_fields = ('name','city')

   def combaine_city_and_name(self,obj):
      return "{} - {}".format(obj.name,obj.city)


admin.site.register(Country)
admin.site.register(City,CityAdmin)
admin.site.register(Restaurant, RestaurantAdmin)


