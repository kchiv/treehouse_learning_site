# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from datetime import date
from . import models


class TextInline(admin.StackedInline):
    model = models.Text


class QuizInline(admin.StackedInline):
    model = models.Quiz


class AnswerInline(admin.TabularInline):
    model = models.Answer

class YearListFilter(admin.SimpleListFilter):
	title = 'year created'

	parameter_name = 'year'

	def lookups(self, request, model_admin):
		return (
			('2015', '2015'),
			('2016', '2016'),
		)

	def queryset(self, request, queryset):
		if self.value() == '2015':
			return queryset.filter(created_at__gte=date(2015, 1, 1),created_at__lte=date(2015, 12, 31))
		if self.value() == '2016':
			return queryset.filter(created_at__gte=date(2016, 1, 1),created_at__lte=date(2016, 12, 31))
    
class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline, QuizInline]
    search_fields = ['title', 'description']
    list_filter = ['created_at', YearListFilter]
    list_display = ['title', 'created_at', 'published', 'time_to_complete']
    list_editable = ['published']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,]
    search_fields = ['prompt']
    list_display = ['prompt', 'quiz', 'order']
    list_editable = ['quiz', 'order']
    radio_fields = {'quiz': admin.VERTICAL}

class QuizAdmin(admin.ModelAdmin):
	fields = ['course', 'title', 'description', 'order', 'total_questions']

class TextAdmin(admin.ModelAdmin):
	#fields = ['course', 'title', 'order', 'description', 'content']
	fieldsets = (
		('Details', {'fields': ('course', 'title', 'order', 'description')}),
		('Add content', {'fields': ('content',), 'classes': ('collapse',)})
	)


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Text, TextAdmin)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.MultipleChoiceQuestion, QuestionAdmin)
admin.site.register(models.TrueFalseQuestion, QuestionAdmin)
admin.site.register(models.Answer)