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
