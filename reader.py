from flask import *
import json, time
import shutil
import pandas as pd
from configparser import ConfigParser

try:

    config = ConfigParser()
    config.read('api_config.ini')


    # Source and Destination folders for copying
    smwsource = config['source']['sMWmasterlist']
    smwdestination = config['destination']['sMWmasterlist']
    omlo33source = config['source']['omlo33']
    omlo33destination = config['destination']['omlo33']
    orl42source = config['source']['orl42']
    orl42destination = config['destination']['orl42']
    oulr22cmsource = config['source']['oulr22cm']
    oulr22cmdestination = config['destination']['oulr22cm']
    # mmwsource = config['source']['mmw']
    # mmwdestination = config['destination']['mmw']

    def copy_smw():
        shutil.copy(smwsource, smwdestination)
        smwloc = config['copiedfiles']['sMWmasterlist']
        smwmasterlist_csv_file = fr"{smwloc}"
        smwmasterlist_read = pd.read_csv(smwmasterlist_csv_file)
        smwoutput = smwmasterlist_read.to_json(indent=1, orient='records')
        print("SmwMasterlist copied successfully.")
        return smwoutput

    def copy_omlo33():
        shutil.copy(omlo33source, omlo33destination)
        omlo33loc = config['copiedfiles']['omlo33']
        omlo33_csv_file = fr"{omlo33loc}"
        omlo33_read = pd.read_csv(omlo33_csv_file)
        omlo33output = omlo33_read.to_json(indent=1, orient='records')
        print("Omlo33 file copied successfully.")
        return omlo33output

    def copy_orl42():
        shutil.copy(orl42source, orl42destination)
        orl42loc = config['copiedfiles']['orl42']
        orl42_csv_file = fr"{orl42loc}"
        orl42_read = pd.read_csv(orl42_csv_file)
        orl42output = orl42_read.to_json(indent=1, orient='records')
        print("orl42 file copied successfully.")
        return orl42output

    def copy_oulr22cm():
        shutil.copy(oulr22cmsource, oulr22cmdestination)
        oulr22loc = config['copiedfiles']['oulr22cm']
        oulr22_csv_file = fr"{oulr22loc}"
        oulr22_read = pd.read_csv(oulr22_csv_file)
        oulr22output = oulr22_read.to_json(indent=1, orient='records')
        print("oulr22cm file copied successfully.")
        return oulr22output

    # shutil.copy(mmwsource, mmwdestination)


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


    app = Flask(__name__)

    @app.route('/', methods=['GET'])

    def home_page():
        data_set = {'Page': 'Home', 'Message': 'Successfully loaded home page', 'Timestamp': time.time()}
        json_dump = json.dumps(data_set)

        return json_dump

    @app.route('/smwResults', methods=['POST'])

    def smwmasterlist_results():
        return copy_smw()


    @app.route('/omlo33Results', methods=['POST'])
    def omlo33_results():
        return copy_omlo33()


    @app.route('/orl42Results', methods=['POST'])
    def orl42_results():
        return copy_orl42()


    @app.route('/oulr22cmResults', methods=['POST'])
    def oulr22cm_results():
        return copy_oulr22cm()


    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=7777)


except Exception as error : 
    print("Error Msg: ",error )