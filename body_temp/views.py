from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.urls import reverse_lazy
from .models import BodyTemp


class BodyTempDayArchiveView(DayArchiveView):
    """ 体温測定結果の日毎の一覧表示 """
    model = BodyTemp
    date_field = 'created_at'
    month_format='%m'
    allow_empty = True
    context_object_name = 'body_temp_list'
    template_name = 'body_temp/day.html'

    def get_queryset(self):
        """ 所属部署ごと名前のアイウエオ順に変更 """
        queryset = super().get_queryset()
        queryset = queryset.order_by('name__department', 'name__family_name', 'name__given_name')
        return queryset


class BodyTempTodayArchiveView(TodayArchiveView):
    """ 体温測定結果の日毎の一覧表示 """
    model = BodyTemp
    date_field = 'created_at'
    allow_empty = True
    context_object_name = 'body_temp_list'
    template_name = 'body_temp/day.html'

    def get_queryset(self):
        """ 所属部署ごと名前のアイウエオ順に変更 """
        queryset = super().get_queryset()
        queryset = queryset.order_by('name__department', 'name__family_kana', 'name__given_kana')
        return queryset


class BodyTempCreateView(CreateView):
    """ 体温測定結果の入力 """
    model = BodyTemp
    template_name = 'body_temp/new.html'
    fields = ['name', 'temp','created_at']


class BodyTempUpdateView(UpdateView):
    """ 体温測定結果の変更 """
    model = BodyTemp
    template_name = 'body_temp/edit.html'
    fields = ['name', 'temp', 'created_at']


class BodyTempDeleteView(DeleteView):
    """ 体温測定結果の削除 """
    model = BodyTemp
    context_object_name = 'body_temp'
    template_name = 'body_temp/delete.html'
    success_url = reverse_lazy('body_temp:today')