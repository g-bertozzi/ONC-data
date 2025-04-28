# scripts/api_practice/get_burrard_sensors.py

from scripts.connect_onc import connect_to_onc
import os
import pandas as pd

def main():
    # Connect to ONC
    my_onc = connect_to_onc()

    # Define filter parameters
    params = {
        "locationCode": "BIIP"  # Burrard Inlet Underwater Network
    }

    # Fetch devices
    devices = my_onc.getDevices(params)

    print("🔎 Devices at Burrard Inlet Underwater Network (BIIP):\n")

    # Prepare list for saving
    device_records = []

    for device in devices:
        device_name = device.get('deviceName', 'Unknown')
        device_category = device.get('deviceCategoryCode', 'Unknown')
        device_id = device.get('deviceId', 'Unknown')
        properties = device.get('properties', [])

        # Print
        print(f"Device Name: {device_name}")
        print(f"Device Category: {device_category}")
        print(f"Device ID: {device_id}")
        print(f"Available Properties: {properties}")
        print("-" * 50)

        # Save to list
        device_records.append({
            "Device Name": device_name,
            "Device Category": device_category,
            "Device ID": device_id,
            "Properties": ", ".join(properties) if properties else ""
        })

    # Save results to a CSV file
    output_folder = 'scripts/api_practice/data'
    os.makedirs(output_folder, exist_ok=True)
    output_file = f'{output_folder}/burrard_inlet_devices.csv'

    df = pd.DataFrame(device_records)
    df.to_csv(output_file, index=False)

    print(f"\n✅ Device list saved to {output_file}")

if __name__ == "__main__":
    main()
