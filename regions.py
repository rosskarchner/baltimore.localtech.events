from calgen.location_utils import extract_location_info
from calgen.regions import EventRejected

_REGIONS = [
    {'slug': 'baltimore', 'name': 'Baltimore City'},
    {'slug': 'md', 'name': 'Maryland'},
    {'slug': 'pa', 'name': 'Pennsylvania'},
]

_STATE_TO_SLUG = {
    'MD': 'md',
    'PA': 'pa',
}

# Known Baltimore area suburbs and their region mappings
_CITY_TO_REGION = {
    'Baltimore': 'baltimore',
    'Towson': 'md',
    'Ellicott City': 'md',
    'Columbia': 'md',
    'Annapolis': 'md',
    'Bel Air': 'md',
    'Glen Burnie': 'md',
    'Catonsville': 'md',
    'Timonium': 'md',
    'Dundalk': 'md',
    'Pikesville': 'md',
    'Hunt Valley': 'md',
    'Hampstead': 'md',
    'Westminster': 'md',
    'Reisterstown': 'md',
    'Fallston': 'md',
    'Havre de Grace': 'md',
    'Edgewood': 'md',
    'Arnold': 'md',
    'Glen Arm': 'md',
    'Owings Mills': 'md',
    'Parkville': 'md',
    'Randallstown': 'md',
    'Severn': 'md',
    'Odenton': 'md',
    'Laurel': 'md',
    'Jessup': 'md',
    'Savage': 'md',
    'Woodstock': 'md',
    'Windsor Mill': 'md',
    'Lithicum': 'md',
    'Linthicum': 'md',
}

# US state codes that are clearly not in the Baltimore metro area
_EXCLUDED_STATES = {
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'FL', 'GA',
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'RI', 'SC',
    'SD', 'TN', 'TX', 'UT', 'VT', 'WA', 'WY',
    'PR', 'VI', 'GU', 'MP', 'AS',
}


def list_regions():
    return _REGIONS


def location_to_region(location_str):
    city_name, state = extract_location_info(location_str or '')
    if not state:
        return None

    state_upper = state.upper()

    if state_upper in _EXCLUDED_STATES:
        raise EventRejected(f"Event is in {state_upper}, outside Baltimore metro area")

    # Check if we know this city specifically
    if city_name:
        city_title = city_name.title()
        if city_title in _CITY_TO_REGION:
            return _CITY_TO_REGION[city_title]

    # Fall back to state-based mapping
    return _STATE_TO_SLUG.get(state_upper)
