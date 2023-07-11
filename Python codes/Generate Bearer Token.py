import requests
def vra_token(hostfqdn,refreshToken):

    """

    Builds an authentication token for the user. Takes input of the fqdn, username,

    password

    """

    url = https://{}/iaas/api/login.format(hostfqdn)

    payload = {"refreshToken": refreshToken}

    headers = {

        'accept': "application/json",

        'content-type': "application/json",

        }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)

    #print ("Response Code for function vra_token:{}".format(response.status_code))

    if response.status_code == 200:

        j = response.json()['token']

        auth = "Bearer " + j

        #print(response)

    else:

        auth = None

    return auth

if __name__ == "__main__":
    bearertoken = vra_token(hostfqdn="XXX",refreshToken="XXX")