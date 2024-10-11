from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView, View

from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewListView(ListView):
   model = Review


class ReviewDetailView(DetailView):
   model = Review


class ReviewCreateView(CreateView):
   model = Review
   form_class = ReviewForm
   template_name = 'reviews/review_form.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['encabezado'] = 'Registrar Reseña'
      return context

   def get_success_url(self):
      return reverse('reviews:registro_exitoso')


class ReviewUpdateView(UpdateView):
   model = Review
   form_class = ReviewForm
   template_name = 'reviews/review_form.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['encabezado'] = 'Actualizar Reseña'
      return context

   def get_success_url(self):
      return reverse('reviews:consultar', kwargs={'pk': self.get_object().pk})


class ReviewSuccessView(TemplateView):
   template_name = 'reviews/review_success.html'
