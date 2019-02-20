import json
import csv
import sys
import os

def transform(input_file_path, input_file_name, output_file_path, output_file_name):
    with open(os.path.join(input_file_path, input_file_name)) as json_file:
        with open(os.path.join(output_file_path, output_file_name), 'w') as csv_file:
            for line in json_file:
                line_data = json.loads(line)
                #print(line_data['site'])
                csv_line = ''
                for p in line_data['visits']:
                    csv_line = line_data['site'] + ','+ str(p['timeSpent']) + ',' + str(p['contentType']) + ',' + str(p['contentCategory']) + ',' + p['url'] + '\n'
                    print(csv_line)
                    csv_file.write(csv_line)

def main():
    transform('/usr/local/demo/incoming/', 'site-visits.json', '/usr/local/demo/outgoing', 'site-visits.csv')

if __name__ == '__main__':
    main()
