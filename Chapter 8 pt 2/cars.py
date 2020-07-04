#8-14: Cars -
def car_profile(manufacturer, model, **car_info):
    """Build a dictionary containing information about car."""
    information = {}
    information['manufacturer'] = manufacturer
    information['model'] = model
    for key, value in car_info.items():
        information[key] = value
    return information

car_profile = car_profile('dodge', 'challenger',
    color='gray',
    engine='hemi')
print(car_profile)