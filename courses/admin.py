# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Course, Text, Quiz

# Register your models here.

class TextInline(admin.StackedInline):
	model = Text

class CourseAdmin(admin.ModelAdmin):
	inlines = [TextInline,]

admin.site.register(Course, CourseAdmin)
admin.site.register(Text)
admin.site.register(Quiz)
