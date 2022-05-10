from flask import Flask
import json, time
import shutil
import pandas as pd
import os
from configparser import ConfigParser
from flask_cors import CORS


try:

    config = ConfigParser()
    config.read('api_config.ini')


    # Source and Destination folders for copying
    smw_uat_source = config['source']['sMWmasterlistUAT']
    smw_uat_destination = config['destination']['sMWmasterlistUAT']
    smw_prd_source = config['source']['sMWmasterlistPRD']
    smw_prd_destination = config['destination']['sMWmasterlistPRD']
    omlo33source = config['source']['omlo33']
    omlo33destination = config['destination']['omlo33']
    orl42source = config['source']['orl42']
    orl42destination = config['destination']['orl42']
    oulr22cmsource = config['source']['oulr22cm']
    oulr22cmdestination = config['destination']['oulr22cm']
    startDir = config['archive']['startDir']
    mmwsource = config['source']['mmw']
    mmwdestination = config['destination']['mmw']

    def find_sjson_latest_folder():
        # getting the names of all archive
        archivelist = os.listdir(f'{startDir}/Alinity_MW/Archive')
        trimmed_archive_list = []
        # for file in archivelist:
        #     trimmed_archive_list.append(file[0:16])
        trimmed_archive_list = sorted(archivelist)
        # trimmed_archive_list[-1]
        # sorted and send only the latest folder
        global directoryNameAndFile
        directoryNameAndFile = f'{startDir}/Alinity_MW/Archive/{trimmed_archive_list[-1]}/sMW/s2_trnsf/sJson'
        print(directoryNameAndFile)
        return list_json_files()



    def list_json_files():
        # START : Multiple File Loop
        # Jsonfiles_FolderPath = fd.askdirectory()  # Select folder path with all json files with user input
        Jsonfiles_FolderPath = directoryNameAndFile
        ResultsList = list()
        for file in os.listdir(Jsonfiles_FolderPath):  # Loop through Json files for data and files names
            FilePath = str(os.path.join(Jsonfiles_FolderPath, str(file)))
            File = open(FilePath, "r")
            if file.endswith(".json"):
                ResultsList.append({"results": json.loads(File.read()), "filename": str(file)})  # Store files data

        '''
        JsonData = json.dumps(ResultsList)      # Convert whole data in List to json format
        JsonData = json.dumps(ResultsList[0])   # Convert 1st data in List to json format
        print(JsonData["results"])              # Access results of 1st Data
        print(JsonData["filename"])             # Access filename of 1st Data
        '''
        # END : Multiple File Loop
        dataToSend = json.dumps(ResultsList)
        return dataToSend


    def copy_smw():
        shutil.copy(smw_uat_source, smw_uat_destination)
        smwloc = config['copiedfiles']['sMWmasterlistUAT']
        smwmasterlist_csv_file = fr"{smwloc}"
        smwmasterlist_read = pd.read_csv(smwmasterlist_csv_file)
        smwoutput = smwmasterlist_read.to_json(indent=1, orient='records')
        print("Smw Masterlist UAT copied successfully.")
        return smwoutput

    def copy_smw_prd():
        shutil.copy(smw_prd_source, smw_prd_destination)
        smwloc = config['copiedfiles']['sMWmasterlistPRD']
        smwmasterlist_csv_file = fr"{smwloc}"
        smwmasterlist_read = pd.read_csv(smwmasterlist_csv_file)
        smwoutput = smwmasterlist_read.to_json(indent=1, orient='records')
        print("Smw Masterlist PRD copied successfully.")
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


    def copy_m_masterlist():
        shutil.copy(mmwsource, mmwdestination)
        mmwloc = config['copiedfiles']['mmw']
        mmw_csv_file = fr"{mmwloc}"
        mmw_read = pd.read_csv(mmw_csv_file, sep=',', header=None)
        mmw_read.columns = ["sampleID", "ctTarget", "ctControl", "result", "ratioTarget", "ratioControl", "completeTime", "operator",
                            "operatorSend", "comment", "flagDetail", "testType", "machineNo", "msgTimeStamp", "txtFileName", "txtCreateTime",
                            "wptRecvTime", "msgID", "kitID", "sampleType", "sampleRole", "modSerialNo", "rackPosn", "deckPosn",
                            "statusChange", "status", "priority", "resultStatus", "negCtrLotNo", "posCtrLotNo", "kitALotNo", "kitBLotNo", "reagentALotNo",
                            "reagentBLotNo", "calibratorLotNo", "lysisLotNo", "diluentLotNo", "vBarrierLotNo", "serialAPU", "locationAPU", "mJsonFileName"]
        mmwoutput = mmw_read.to_json(indent=1, orient='records')
        print("mmw masterlist copied successfully.")
        return mmwoutput



    app = Flask(__name__)
    CORS(app)

    @app.route('/', methods=['GET'])

    def home_page():
        data_set = {'Page': 'Home', 'Message': 'Successfully loaded home page', 'Timestamp': time.time()}
        json_dump = json.dumps(data_set)

        return json_dump

    @app.route('/smwResults', methods=['POST'])

    def smwmasterlist_results():
        return copy_smw()

    @app.route('/smwResultsPRD', methods=['POST'])
    def smwmasterlist_results_prd():
        return copy_smw_prd()

    @app.route('/omlo33Results', methods=['POST'])
    def omlo33_results():
        return copy_omlo33()


    @app.route('/orl42Results', methods=['POST'])
    def orl42_results():
        return copy_orl42()


    @app.route('/oulr22cmResults', methods=['POST'])
    def oulr22cm_results():
        return copy_oulr22cm()


    @app.route('/mmwResults', methods=['POST'])
    def m_masterlist_results():
        return copy_m_masterlist()

    @app.route('/listLatestSJSON', methods=['POST'])
    def list_latest_sjson():
        return find_sjson_latest_folder()


    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=7777)


except Exception as error:
    print("Error Msg: ", error)