from flask import *
import json, time
import shutil
import pandas as pd
from configparser import ConfigParser

try:

    config = ConfigParser()
    config.read('api_config.ini')
    smwloc = config['apis']['sMWmasterlist']
    omlo33loc = config['apis']['omlo33']
    orl42loc = config['apis']['orl42']
    orl22cmloc = config['apis']['orl22cm']
    # mmwloc = config['apis']['mmw']

    smwsource = config['source']['sMWmasterlist']
    smwdestination = config['destination']['sMWmasterlist']
    omlo33source = config['source']['omlo33']
    omlo33destination = config['destination']['omlo33']
    orl42source = config['source']['orl42']
    orl42destination = config['destination']['orl42']
    orl22cmsource = config['source']['orl22cm']
    orl22cmdestination = config['destination']['orl22cm']
    # mmwsource = config['source']['mmw']
    # mmwdestination = config['destination']['mmw']
    # print(smwloc)
    # print(omlo33loc)
    # print(orl42loc)
    # print(orl22cmloc)
    # print(mmwloc)

    shutil.copy(smwsource, smwdestination)
    shutil.copy(omlo33source, omlo33destination)
    shutil.copy(orl42source, orl42destination)
    shutil.copy(orl22cmsource, orl22cmdestination)
    shutil.copy(mmwsource, mmwdestination)
    print("File copied successfully.")


    # # START : Multiple File Loop
    # Jsonfiles_FolderPath = filedialog.askdirectory()  # Select folder path with all json files
    # ResultsList = list()
    # for file in os.listdir(Jsonfiles_FolderPath):   # Loop through Json files for data and files names
    #     FilePath = str(os.path.join(Jsonfiles_FolderPath,str(file)))
    #     File = open (FilePath, "r")
    #     if file.endswith(".json"):
    #         ResultsList.append({"results": json.loads(File.read()), "filename": str(file) }) # Store files data
    #
    # '''
    # JsonData = json.dumps(ResultsList)      # Convert whole data in List to json format
    # JsonData = json.dumps(ResultsList[0])   # Convert 1st data in List to json format
    # print(JsonData["results"])              # Access results of 1st Data
    # print(JsonData["filename"])             # Access filename of 1st Data
    # '''
    #
    # print(ResultsList)
    #
    # # END : Multiple File Loop
    # dataToSend = json.dumps(ResultsList)


    # smwmasterlist_csv_file = fr"{smwdestination}"
    # smwmasterlist_read = pd.read_csv(smwmasterlist_csv_file)
    # omlo33_csv_file = fr"{omlo33loc}"
    # omlo33_read = pd.read_csv(omlo33_csv_file)
    # orl42_csv_file = fr"{orl42loc}"
    # orl42_read = pd.read_csv(orl42_csv_file)
    # orl22cm_csv_file = fr"{orl22cmloc}"
    # orl22cm_read = pd.read_csv(orl22cm_csv_file)
    # mmw_csv_file = fr"{mmwloc}"
    # mmw_read = pd.read_csv(mmw_csv_file)



    # omlo33_csv_file = r"/Users/johnlee/Desktop/Testing/Alinity_MW/Archive/Archive_20220129/aMW/a0_storg/A7_OMLO33/OMLO33.csv"
    # omlo33_read = pd.read_csv(omlo33_csv_file )

    # smwoutput = smwmasterlist_read.to_json(indent = 1, orient = 'records')
    # omlo33output = omlo33_read.to_json(indent = 1, orient = 'records')
    # orl42output = orl42_read.to_json(indent=1, orient='records')
    # orl22cmoutput = orl22cm_read.to_json(indent=1, orient='records')
    # mmwoutput = mmw_read.to_json(indent=1, orient='records')


    # app = Flask(__name__)
    #
    # @app.route('/', methods=['GET'])
    #
    # def home_page():
    #     data_set = {'Page': 'Home', 'Message': 'Successfully loaded home page', 'Timestamp': time.time()}
    #     json_dump = json.dumps(data_set)
    #
    #     return json_dump
    #
    # @app.route('/smwResults', methods=['POST'])
    #
    # def smwmasterlist_results():
    #     # data_set = {'Page': 'smwResults', 'Message': 'Successfully loaded home page', 'Timestamp': time.time()}
    #     # json_dump = json.dumps(output)
    #     return smwoutput
    #
    # @app.route('/omlo33Results', methods=['GET'])
    #
    # def omlo33_results():
    #     return omlo33output
    #
    #
    #
    # if _name_ == '__main__':
    #     app.run(port=7777)


except Exception as error : 
    print("Error Msg: ",error )