from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from asianapp.models import *
from asianapp.forms import *
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# Create your views here.

def home(request):
    try:
        social_links_data = SocialLink.objects.all()
        new_update_data = NewsUpdate.objects.all()
        slider_data = Slider.objects.all()
        contact_data = Contact.objects.all().first()
        category_data = Category.objects.all()
        subcategory_data = SubCategory.objects.all()

        box_ads_data = Advertisement.objects.filter(type__icontains='box', is_featured=True).order_by('sort_order')
        rectangle_ad1_data = Advertisement.objects.filter(type__icontains='rectangle', is_featured=True).order_by('sort_order').first()
        rectangle_ad2_data = Advertisement.objects.filter(type__icontains='rectangle', is_featured=True).order_by('sort_order').last()

        data_list = {
        'social_link': social_links_data,
        'new_updates': new_update_data,
        'sliders': slider_data,
        'contact': contact_data,
        'categories': category_data,
        'subcategories': subcategory_data,
        'box_ads': box_ads_data,
        'rectangle_ad1': rectangle_ad1_data,
        'rectangle_ad2': rectangle_ad2_data,
        }
        return render(request, 'website/index.html', data_list)
    except AttributeError as error:
        return HttpResponse('Ads not found')

    except Exception:
        return HttpResponse('Not found')



def aboutus(request):
    try:
        aboutus_data = Content.objects.filter(title="About us").first()
        box_ads_data = Advertisement.objects.filter(type__icontains='box', is_featured=False).order_by('sort_order')
        rectangle_ad1_data = Advertisement.objects.filter(type__icontains='rectangle', is_featured=True).order_by('sort_order').first()
        rectangle_ad2_data = Advertisement.objects.filter(type__icontains='rectangle', is_featured=True).order_by('sort_order').last()

        data_list = {
        'content': aboutus_data,
        'box_ads': box_ads_data,
        'rectangle_ad1': rectangle_ad1_data,
        'rectangle_ad2': rectangle_ad2_data,
        }
        return render(request, 'website/about.html', data_list)

    except Exception:
        return HttpResponse('Not found')

def contact(request):
    # try:
        box_ads_data = Advertisement.objects.filter(type__contains='box', is_featured=False).order_by('sort_order')
        rectangle_ad1_data = Advertisement.objects.filter(type__contains='rectangle', is_featured=True).order_by('sort_order').first()
        rectangle_ad2_data = Advertisement.objects.filter(type__contains='rectangle', is_featured=True).order_by('sort_order').last()
        form_data = CustomerEmailForms()
        data_list = {
        'box_ads': box_ads_data,
        'rectangle_ad1': rectangle_ad1_data,
        'rectangle_ad2': rectangle_ad2_data,
        'form' : form_data
        }

        return render(request, 'website/contact.html', data_list)
    # except AttributeError as error:
        # return HttpResponse('Not found')
    # except Exception:
        # return HttpResponse('Not found')

def video_details(request,pk):
    try:
        video_data = get_object_or_404(Video, pk=pk)

    except Video.ObjectDoesNotExist:

        raise Http404("Video is not found!")

    try:
        box_ads_data = Advertisement.objects.filter(type__icontains='box', is_featured=False).order_by('sort_order')
        rectangle_ad1_data = Advertisement.objects.filter(type__icontains='rectangle', is_featured=True).order_by('sort_order').first()
        rectangle_ad2_data = Advertisement.objects.filter(type__icontains='rectangle', is_featured=True).order_by('sort_order').first()

        video_list = {
        'video': video_data,
        'box_ads': box_ads_data,
        'rectangle_ad1': rectangle_ad1_data,
        'rectangle_ad2': rectangle_ad2_data,
        }
        return render(request, 'website/video-detail.html', video_list)
    except Exception:
        return HttpResponse('Not found')


def customer_email(request):

    if request.method == 'POST' and 'fname' in request.POST and 'lname' in request.POST and 'email' in request.POST and 'message' in request.POST:
        print('your email is on the way, please wait a moment')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        form = CustomerEmailForms(request.POST) # A form bound to the POST data
        if form.is_valid(): # True

            custom_email_obj = CustomerEmail()
            custom_email_obj.firstname = first_name
            custom_email_obj.lastname = last_name
            custom_email_obj.customeremails = email
            custom_email_obj.customermessage = message
            custom_email_obj.status = True
            custom_email_obj.save()
            print('email sent thanks')

            return redirect('index')
            # return HttpResponse('you have successfully sent your email, we will get back to you soon!!!') # Redirect after POST
        else:
            # Do something in case if form is not valid
            raise Http404
    return HttpResponse('not saved email')
