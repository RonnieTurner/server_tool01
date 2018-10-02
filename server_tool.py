import requests, base64, json, pprint, os

api_user_name = os.environ['API_USER_NAME']
api_user_pass = os.environ['API_USER_PASS']

def rec_data():
    auth = base64.b64encode(f"{api_user_name}":f"{api_user_pass}".encode())
    headers = {"Authorization": "Basic " + auth.decode(),
                "Content-Type": "application/json",
               }
    r = requests.get("https://api.upcloud.com/1.2/server", headers=headers)
    server_info = r.json()
    #pprint.pprint(server_info)
    return server_info


def list_servers(server_info):
    server_info = server_info
    my_server_list = server_info['servers']['state']
    #  pprint.pprint(my_server_list)
    for h in my_server_list:
        print(h['hostname'])
    #  pprint.pprint(r_obj)
    for l in my_server_list:
        if l['license'] == 0:
            OS = "Linux"
        else:
            OS = "Microsoft"
        print(l['hostname'],l['plan'],'--',OS,'--- ',l['state'])
    #  pprint.pprint(r_obj)

def main():
    server_info = rec_data()
    pprint.pprint(server_info)
    list_servers(server_info)

if __name__ == '__main__':
    main()
