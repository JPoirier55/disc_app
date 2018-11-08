from django.shortcuts import render
from bs4 import BeautifulSoup
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_protect
import requests
import json

def geo_to_city(request):
    return render(request, 'test_location.html')

def location(request):
    #TODO split method into url handler for both pdga and for google maps
    lat = request.GET.get('lat', '')
    long = request.GET.get('long', '')
    print(request)
    # zipcode = request.POST['zip']
    postal_code = '00000'
    url3 = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat +"," + long +"&key=AIzaSyAuZbeei_JtF-5mHhcSw6uZ9L0__8hcqgk"
    r = requests.get(url3)
    json_obj = json.loads(r.text)
    resp_obj = []
    if json_obj['status'] == 'OK':
        for component in json_obj['results']:
            for part in component['address_components']:
                if part['types'] == ['postal_code']:
                    postal_code = part['long_name']
        print(postal_code)

        if postal_code != '00000':
            url = "https://www.pdga.com/course-directory/advanced?title=" \
                  "&field_course_location_country=US" \
                  "&field_course_location_locality=" \
                  "&field_course_location_administrative_area=All" \
                  "&field_course_location_postal_code=" + postal_code + \
                  "&field_course_type_value=All" \
                  "&rating_value=All" \
                  "&field_course_holes_value=All" \
                  "&field_course_total_length_value=All" \
                  "&field_course_target_type_value=All" \
                  "&field_course_tee_type_value=All" \
                  "&field_location_type_value=All" \
                  "&field_course_camping_value=All" \
                  "&field_course_facilities_value=All" \
                  "&field_course_fees_value=All" \
                  "&field_course_handicap_value=All" \
                  "&field_course_private_value=All" \
                  "&field_course_signage_value=All"
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text)
            courses = soup.find_all('tr')
            for course in courses:
                if course.find('a') is not None:
                    course_obj = {}
                    course_obj['name'] = innerHTML(course.find('a')).strip().decode()
                    course_obj['link'] = "https://www.pdga.com" + course.find('a', href=True)['href']
                    course_obj['distance'] = innerHTML(course.find('td', class_='views-field views-field-field-geofield-distance')).strip().decode()
                    course_obj['city'] = innerHTML(course.find('td', class_='views-field views-field-field-course-location')).strip().decode()
                    course_obj['stars'] = innerHTML(course.find('div', class_='star star-1 star-odd star-first').find('span')).strip().decode()
                    resp_obj.append(course_obj)
    else:
        print('not place')


    return render(request, 'test_location.html', {'data': resp_obj})

def innerHTML(element):
    return element.encode_contents()

def course_search(request):
    city = request.POST['city']


# Create your views here.
