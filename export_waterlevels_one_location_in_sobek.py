import os
import pandas as pd
import matplotlib.pyplot as plt
import hkvsobekpy as hkv

def export_1_location_all_cases(location_id, his_file_path):
    """Export water level data of a location from a HIS file to a CSV and generate a plot."""
    plot_file_name = f"{location_id}.png"
    csv_file_name = f"{location_id}.csv"
    
    try:
        calcpnt = hkv.read_his.ReadMetadata(his_file_path)
    except FileNotFoundError:
        print(f"The file {his_file_path} does not exist. Please check your path.")
        return

    locations = calcpnt.GetLocations()
    
    if location_id not in locations:
        print(f"The location id {location_id} does not exist in the HIS file.")
        return

    timestamps = calcpnt.GetTimestamps()
    parameters = calcpnt.GetParameters()

    df = calcpnt.EnkeleWaardenArray(location_id, parameters[0])

    ax = df.plot(legend=True)
    ax.set_ylabel('m NAP')

    current_dir = os.path.dirname(os.path.abspath(__file__))

    plt.savefig(os.path.join(current_dir, plot_file_name))
    df.to_csv(os.path.join(current_dir, csv_file_name))

    print(f"Data exported to {os.path.join(current_dir, csv_file_name)} and plot saved as {os.path.join(current_dir, plot_file_name)}")

if __name__ == "__main__":
    location_id = '1184'
    his_file_path = r'c:\sob21205\risico.lit\4\CALCPNT.HIS'

    export_1_location_all_cases(location_id, his_file_path)
