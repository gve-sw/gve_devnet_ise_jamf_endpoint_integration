from jamf_api import get_all_computer_mac_addresses, get_all_device_mac_addresses
from ise import ise_auth, pull_group, bulk_create, pull_group_endpoints, bulk_delete
from apscheduler.schedulers.blocking import BlockingScheduler



ise_address = ""
ise_user = ""
ise_password = ""

def chunks(lst, n):
    """Yield successive n-sized chunks from list."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def delete():
    """
    Bulk delete all devices
    """
    auth = ise_auth(address=ise_address, username=ise_user, password=ise_password)
    group = pull_group(auth=auth, group_name="iMacs")
    for endpoints in chunks(pull_group_endpoints(auth=auth, group=group), 5000):
        while True:
            response = bulk_delete(auth=auth, devices=endpoints)
            print(response.status_code)
            if response.status_code != 500:
                break




def create():
    """
    Bulk create all devices
    """
    auth = ise_auth(address=ise_address, username=ise_user, password=ise_password)
    jamf_computer_mac_addresses = get_all_computer_mac_addresses()
    jamf_device_mac_addresses = get_all_device_mac_addresses()

    group = pull_group(auth=auth, group_name="iMacs")


    for mac_address_chunk in chunks(jamf_computer_mac_addresses, 500):

        while True:
            response = bulk_create(auth=auth, group=group, devices=mac_address_chunk)
            print(response.status_code)
            if response.status_code != 500:
                break


    for mac_address_chunk in chunks(jamf_device_mac_addresses, 500):

        while True:
            response = bulk_create(auth=auth, group=group, devices=mac_address_chunk)
            print(response.status_code)
            if response.status_code != 500:
                break







if __name__ == "__main__":

    create()

    #OPTIONAL SCHEDULAR EXAMPLE BELOW:

    # scheduler = BlockingScheduler()
    # scheduler.add_job(delete, 'interval', hours=1)
    # scheduler.add_job(create, 'interval', hours=1)
    # scheduler.start()
