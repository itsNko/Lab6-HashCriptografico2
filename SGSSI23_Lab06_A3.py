import os
import sys
import random
import SGSSI23_Lab05_A3_Functions as Lab05

if __name__ == "__main__":
    # Check input names:
    if (len(sys.argv) != 3):
        print("Use: python SGSSI23_Lab06_A1.py <blueprint-file-path> <directory-path>")
        exit(1)

    # Input and output file paths
    blueprint_file_path = sys.argv[1]
    directory_path = sys.argv[2]

    # List all files in the input_folder
    files = os.listdir(directory_path)

    file_count = 0
    valid_file_count = 0
    proof_of_work_file = ''
    valid_files = []
    hash_zeros = 0
    # Iterate through each file in the folder
    print('File\tCompiles\tHash0Count')
    for file in files:
        # Check if the file is a .txt file
        if file.endswith(".txt"):
            # Get the full path of the file
            file_path = os.path.join(directory_path, file)
            file_count += 1
            complies = Lab05.lab05A3(blueprint_file_path, file_path)
            hash_zeros = Lab05.count_concatenated_zeros(Lab05.calculate_sha256_file(file_path))
            if (complies):
                valid_file_count += 1
                valid_files.append(file_path)
                if (hash_zeros > Lab05.count_concatenated_zeros(Lab05.calculate_sha256_file(proof_of_work_file))):
                    proof_of_work_file = file_path
            print(file + '\t' + str(complies) + '\t' + str(hash_zeros))

    print('\nValid Files: ' + str(valid_file_count) + '/' + str(file_count) + '\tRandom_Candidate: ' + random.choice(valid_files) + '\tBest_Candidate: ' + proof_of_work_file)