def extract_loaded_values(file_content):
    loaded_values = []
    start_search = False

    for line in file_content:
        if "_ZN2ft26TxtHighBayWarehouseStorage14fetchContainerEv" in line:
            start_search = True
        elif "loaded values" in line and start_search:
            loaded_value = line.split()[-1]
            if "_ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E" in line:
                break
            elif "loaded values: 0" in line:
                loaded_values.append(loaded_value)
                break
            else:
                #loaded_value = line.split()[-1]
                if loaded_value != "-1":
                    loaded_values.append(loaded_value)

    return loaded_values

def process_file(file_name):
    with open(file_name, "r") as file:
        file_content = file.readlines()
        loaded_values = extract_loaded_values(file_content)
        return loaded_values

# Process fetch7.txt file
fetch7_values = process_file("fetch7.txt")
print("Loaded values from fetch7.txt:")
print(fetch7_values)

# Process fetch8-ch.txt file
fetch8_ch_values = process_file("fetch8-ch.txt")
print("Loaded values from fetch8-ch.txt:")
print(fetch8_ch_values)

