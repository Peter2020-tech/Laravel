import pyclamd

def scan_file_for_malware(file_path):
    try:
        clamav = pyclamd.ClamdAgnostic()
        scan_result = clamav.scan_file(file_path)
        if scan_result[file_path] == 'OK':
            return "File is clean"
        else:
            return "Malicious file detected"
    except Exception as e:
        return "Error: " + str(e)

file_path = "path_to_your_malicious_file.exe"  # Replace with the actual file path
result = scan_file_for_malware(file_path)
print(result)
