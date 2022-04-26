# gve_devnet_ise_jamf_endpoint_integration
This application is an example of how to integrate JAMF endpoints into ISE.


## Contacts
* Charles Llewellyn

## Solution Components
* Python
*  ISE
*  JAMF


## Installation/Configuration

In App.py set ise address, user and password
```
ise_address = ""
ise_user = ""
ise_password = ""
```

This is as a template, project owner to update

1. pip install requirements.txt
2. Create an Jamf Pro API User
3. Enter hostname, username, and password
4. Test: conf-python-jamf -t
5. Create ISE account that has access to ERS APIs
6. Create Endpoint Group in ISE to store all of the JAMF Endpoints



## Usage


    $ python app.py



# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
