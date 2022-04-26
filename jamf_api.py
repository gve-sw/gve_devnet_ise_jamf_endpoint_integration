import jamf
import json

test = True

def get_all_computer_mac_addresses():
	"""
	Get all computer mac addresses from jamf server
	:return: list of mac addresses
	"""
	mac_addresses=[]
	if not test:

		api = jamf.API()

		invalid_mac_address_count = 0

		for computer in api.get('computers/subset/basic')['computers']['computer']:
			if computer['mac_address'] == None:
				print(computer)
				invalid_mac_address_count += 1
			else:
				mac_addresses.append(computer['mac_address'])


		print("Invalid Mac Address Count: " + str(invalid_mac_address_count))
		return mac_addresses

	else:
		with open('jamf_api.txt') as json_file:
			data = json.load(json_file)

		for computer in data['computers']['computer']:
			if computer['mac_address'] == None:
				print(computer)
			else:
				mac_addresses.append(computer['mac_address'])

		return mac_addresses


def get_all_device_mac_addresses():
	"""
	Get all device mac addresses from jamf server
	:return: list of mac addresses
	"""

	mac_addresses = []
	if not test:

		api = jamf.API()

		invalid_mac_address_count = 0

		for device in api.get('mobiledevices')['mobile_devices']['mobile_device']:
			if device['wifi_mac_address'] == None:
				print(device)
				invalid_mac_address_count += 1
			else:
				mac_addresses.append(device['wifi_mac_address'])

		print("Invalid Mac Address Count: " + str(invalid_mac_address_count))
		return mac_addresses

	else:
		with open('jamf_devices_api.txt') as json_file:
			data = json.load(json_file)
		for device in data['mobile_devices']['mobile_device']:
			if device['wifi_mac_address'] == None:
				print(device)
			else:
				mac_addresses.append(device['wifi_mac_address'])

		return mac_addresses





if __name__ == '__main__':
	print(get_all_device_mac_addresses())











