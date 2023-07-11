from towerlib import Tower
import json
import time
def handler(context, inputs):

    ansible_host = inputs["ansible_host"]

    username = inputs["ansible_user"]

    cred = inputs["ansible_password"]

    VMName=inputs["machine_name"]

    ansible_organisation=inputs['ansible_organisation']

    ansible_inventory=inputs['ansible_inventory']

    osType=inputs['OSPlatform'].lower()

    for j in range(5):

        try:

            t = Tower(ansible_host, username, cred, secure=True, ssl_verify=False)

            host_added= t.create_host_in_inventory(organization=ansible_organisation,inventory=ansible_inventory,name=VMName, description='onboarded VM', variables='{}')

            group = ['windows' if osType.lower() == 'windows' else 'linux']

            host_group = t.associate_groups_with_inventory_host(organization=ansible_organisation,inventory=ansible_inventory,hostname=VMName, groups=group)

        except Exception as inst:

            print (inst)

            if j == 4:

                print ("connection to tower failed...")