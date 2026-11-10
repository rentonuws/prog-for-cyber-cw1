incident_manager = {    #Defined a dictionary to store the incident details
    "username" : "UWS",
    "ip_address" : "10.99.11.210",
    "event_type" : "Unauthorized Access attempted",
    "risk_level" : "Medium"
}

print(f"The username is : {incident_manager['username']}")  #Displaying the username from the incident_manager dictionary
print(f"The IP address is : {incident_manager['ip_address']} \n")   #Displaying the IP address from the incident_manager dictionary

incident_manager["status"] = "Investigating"  #Adding a new key-value pair to the incident_manager dictionary to indicate the status of the incident

incident_manager["risk_level"] = "High" #Updating the value of the "risk_level" key in the incident_manager dictionary to indicate that the risk level has been changed to "High"

del incident_manager["status"] #Deleting the "status" key-value pair from the incident_manager dictionary as the investigation is complete

print("The remaining keys and values are as below: ")

for key in incident_manager:    #Iterating through the incident_manager dictionary to display the remaining key-value pairs
    print(f"{key} : {incident_manager[key]}")

print(f"\nTotal number of key-value pairs is : {len(incident_manager)}") #Displaying the total number of key-value pairs remaining in the incident_manager dictionary after the deletion of the "status" key-value pair
