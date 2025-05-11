"""
Fetches and saves ONC sensor metadata from the Burrard Inlet (locationCode: 'BIIP').
"""

from scripts.connect_onc import connect_to_onc
import os
import pandas as pd

def main():
    """
    Connects to the ONC API, retrieves device metadata for Burrard Inlet,
    and writes the fromatted results to a CSV file.
    """

    # Connect to Oceans 3.0 API via helper script
    my_onc = connect_to_onc()

    # Set query parameters to return results for the Burrard Inlet Underwater Network 
    params = {
        "locationCode": "BIIP"
    }

    # Fetch a list of device dictionaries matching the locationCode parameter 
    devices = my_onc.getDevices(params)

    print("Devices at Burrard Inlet Underwater Network (BIIP):\n")

    # Initialize a list to collect structured device metadata
    device_records = []

    # Iterate through each device returned by the API
    for device in devices:
        # Extract device metadata with default value in case a field is missing
        device_name = device.get('deviceName', 'Unknown') 
        device_category = device.get('deviceCategoryCode', 'Unknown')
        device_id = device.get('deviceId', 'Unknown')
        properties = device.get('properties', [])

        # Print readable device metadata to console
        print(f"Device Name: {device_name}")
        print(f"Device Category: {device_category}")
        print(f"Device ID: {device_id}")
        print(f"Available Properties: {properties}")
        print()

        # Append the metadata as a dictionary to the records list
        # If 'properties' is a list, it is converted to a comma-separated string
        device_records.append({
            "Device Name": device_name,
            "Device Category": device_category,
            "Device ID": device_id,
            "Properties": ", ".join(properties) if properties else ""
        })

    # Ensure the output directory exists before writing the file
    output_folder = 'scripts/api_practice/data'
    os.makedirs(output_folder, exist_ok=True)

    # Define output file path
    output_file = f'{output_folder}/burrard_inlet_devices.csv'

    # Convert the list of device dictionaries to a pandas DataFrame and write to CSV
    df = pd.DataFrame(device_records)
    df.to_csv(output_file, index=False)

    print(f"\nDevice list saved to {output_file}")

if __name__ == "__main__":
    main()
