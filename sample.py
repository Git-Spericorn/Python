# Function to get user data
def get_user_data(self, name, date, place):
    """
            :name: employee name
            :date: joining date
            :place: place
            :return: json
        """
    user_token = self.request.session['user_token']
    headers = {
        "x-auth-token": user_token
    }
    data = {
        "name": name,
        "date": date,
        "place": place,

    }
    url = self.url + '/api/v1/filterUser'
    params = {}
    response = request_retry(url, headers=headers, params=params, json_data=data, method='put')
    return response.json()


import itertools


def iter_primes():
    # an iterator of all numbers between 2 and +infinity
    numbers = itertools.count(2)

    # generate primes forever
    while True:
        # get the first number from the iterator (always a prime)
        prime = next(numbers)
        yield prime

        # this code iteratively builds up a chain of
        # filters...slightly tricky, but ponder it a bit
        numbers = filter(prime.__rmod__, numbers)


for p in iter_primes():
    if p > 1000:
        break
    print(p)
