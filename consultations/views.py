from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Consultation

# Create your views here.

def all_consultations(request):
    """ A view to show all consultations, including sorting and search queries """

    consultations = Consultation.objects.all()  # Initialize consultations here
    query = None
    sort = None
    direction = None

    if request.GET:
        # Sorting logic
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                consultations = consultations.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            consultations = consultations.order_by(sortkey)

        # Search query logic
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('consultations'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            consultations = consultations.filter(queries)

    current_sorting = f'{sort}_{direction}' if sort and direction else None

    context = {
        'consultations': consultations,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'consultations/consultations.html', context)

def consultation_detail(request, consultation_id):
    """ A view to show individual product details """

    consultation = get_object_or_404(Consultation, pk=consultation_id)

    context = {
        'consultation': consultation,
    }

    return render(request, 'consultations/consultation_detail.html', context)


def add_consultation(request):
    """ Add a consultation to the store """
    if request.method == 'POST':
        form = ConsultationForm(request.POST, request.FILES)
        if form.is_valid():
            consultation = form.save()
            messages.success(request, 'Successfully added consultation!')
            return redirect(reverse('consultation_detail', args=[consultation.id]))
        else:
            messages.error(request, 'Failed to add consultation. Please ensure the form is valid.')
    else:
        form = ConsultationForm()
        
    template = 'consultations/add_consultation.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_consultation(request, product_id):
    """ Edit a consultation in the store """
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    if request.method == 'POST':
        form = ConsultationForm(request.POST, request.FILES, instance=consultation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated consultation!')
            return redirect(reverse('consultation-detail', args=[consultation.id]))

        else:
            messages.error(request, 'Failed to update consultation. Please ensure the form is valid.')
    else:
        form = ConsultationForm(instance=consultation)
        messages.info(request, f'You are editing {consultation.name}')

    template = 'consultation/edit_consultation.html'
    context = {
        'form': form,
        'consultation': consultation,
    }

    return render(request, template, context)

def delete_consultation(request, consultation_id):
    """ Delete a consultation from the store """
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    consultation.delete()
    messages.success(request, 'Consultation deleted!')
    return redirect(reverse('consultation'))