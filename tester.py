from bs4 import BeautifulSoup
import requests

def run():
    url = "https://www.pdga.com/course-directory/advanced?title=&field_course_location_country=US&field_course_location_locality=&field_course_location_administrative_area=All&field_course_location_postal_code=&field_course_type_value=All&rating_value=All&field_course_holes_value=All&field_course_total_length_value=All&field_course_target_type_value=All&field_course_tee_type_value=All&field_location_type_value=All&field_course_camping_value=yes&field_course_facilities_value=All&field_course_fees_value=All&field_course_handicap_value=All&field_course_private_value=All&field_course_signage_value=All&page=52"
    # r = requests.get(url3)
    # for resp in r:
    #     print(resp)
    # page = requests.get(url)
    #
    # soup = BeautifulSoup(page.text)
    # # print(soup)
    # # print(soup.find_all('td', class_='views-field views-field-title'))
    # courses = soup.find_all('td', class_='views-field views-field-title')
    # for course in courses:
    #     print(course.find('a'))

if __name__ == '__main__':
    run()