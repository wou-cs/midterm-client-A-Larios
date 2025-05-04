import requests
base_url = "http://chrisbrooks.pythonanywhere.com/"

def get_programmer_count():
    """
    Return the number of programmers return from the plural programmers API
    :return: An integer indicating the number of programmers in the plural list.
    """
    r = requests.get(base_url + 'api/programmers')
    programmers = r.json()
    all_programmers = programmers['programmers']
    return len(all_programmers)


def get_programmer_by_id(pid):
    """
    Return the single programmer referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :return: A dictionary containing the matched programmer. Return an empty dictionary if not found
    """
    try:
        int_pid = int(pid)
        r = requests.get(base_url + 'api/programmers/' + str(int_pid))
        programmers_by_id = r.json()
        return programmers_by_id
    except:
        return {}


def get_full_name_from_first(first_name):
    """
    Return the full name of the *first* programmer having the provided first name, concatenating the first and last name with a space between.
    :param first_name:
    :return: A string containing the first and last name of the first programmer in the list of matches.
    """
    try:
        r = requests.get(base_url + 'api/programmers/by_first_name/' + first_name)
        programmers_by_first_name = r.json()
        print(programmers_by_first_name)
        programmer = programmers_by_first_name['programmers'][0]
        full_name = f"{programmer['first']} {programmer['last']}"
        return full_name
    except:
        return None
