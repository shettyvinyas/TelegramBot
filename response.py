import re
import requests
import json
import datetime
import  enum
# import numpy as np

defaultline= "To Fetch Information Regarding  Vaccination :\n\nPlease Send Your District Name As DISTRICT_DISTRICTNAME \n  EX:-DISTRICT_Bangalorerural\n \n**************** OR ******************\n\nPlease Send Your Pin Code As 'PIN_PINCODE' \n  EX:-PIN_576102 \n\nCurrently, District-Based Search Is Supported Only For State Of Karnataka.\n \n To Fetch District List Send Any Number\n \n Please Share Your Feedback At:vinyas1947@gmail.Com \n"

class District(enum.Enum):
        bagalkot=270
        bangalorerural=276
        bangaloreurban=265
        bbmp=294
        belgaum=264
        bellary=274
        bidar=272
        chamarajanagar=271
        chikamagalur=273
        chikkaballapur=291
        chitradurga=268
        dakshinakannada=269
        davanagere=275
        dharwad=278
        gadag=280
        gulbarga=267
        hassan=289
        haveri=279
        kodagu=283
        kolar=277
        koppal=282
        mandya=290
        mysore=266
        raichur=284
        ramanagara=292
        shimoga=287
        tumkur=288
        udupi=286
        uttarkannada=281
        vijayapura = 293
        yadgir=285

regex="[a-zA-Z0-9]"
PIN_regex="^[Pp][Ii][Nn]_[0-9]"
District_regex="^[Dd][Ii][Ss][Tt][Rr][Ii][Cc][Tt]_[A-Za-z]"
digit="^[0-9]"


def Checkbypin(message:object)->object:
        strmessage=str(message)
        strlist=strmessage.strip().split('_');
        d1 = datetime.datetime.now()
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+strlist[1]+"&date="+d1.strftime("%d-%m-%Y")+""
        r = requests.get(url = URL)
        data = r.json()
        arr=data["centers"]
        name=""
        queue = []

        for x in arr:
           d3=x['sessions']
           d4=d3[0];
           print(d4['session_id'])
           name="Name : "+x['name']+"\n"+"Address : "+x['address']+"\n"+"Fee : "+x['fee_type']+"\n"+"Vaccine : "+d4['vaccine']+"\n"+"Available Dose 1 : "+str(d4['available_capacity_dose1'])+"\n"+"Available Dose 2 : "+str(d4['available_capacity_dose2'])+"\n"
           queue.append(name)

        # print()


        return name


def CheckbyDistrict(message: object) -> object:
    stra = str(message)
    print(stra);
    print(stra.strip().split('_'))
    strlist = stra.strip().split('_');
    print(strlist[1])
    d1 = datetime.datetime.now()
    district_id =str(District[strlist[1]].value)
    print(district_id)
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+district_id+"&date=" + d1.strftime("%d-%m-%Y") + ""
    r = requests.get(url=URL)
    r = requests.get(url=URL)
    data = r.json()
    print(data);
    arr = data["sessions"]
    name = ""
    queue = []

    for x in arr:
     if(x['available_capacity_dose1'] >0 and x['available_capacity_dose2']>0 ):
        name = "Name : " + x['name'] + "\n" + "Address : " + x['address'] + "\n" + "Fee : " + x[
            'fee_type'] + "\n" + "Vaccine : " + x['vaccine'] + "\n" + "Available Dose 1 : " + str(
            x['available_capacity_dose1']) + "\n" + "Available Dose 2 : " + str(x['available_capacity_dose2']) + "\n"+"Age Limit :"+  str(x['min_age_limit'])+"\n"
        queue.append(name)

    Nosolts = "No Vaccination Slot is Available in " + strlist[1].capitalize() + " Please Check After Some Time"
    if(len(queue)==0):
        queue.append(Nosolts)
    return queue

def Getlist():
    str="List of Districts"
    dist= list(map(lambda c: c.name, District))
    string_list = [each_string.upper() for each_string in dist]
    string_list.insert(0,str)
    stringlist="LIST OF DISTRICT\n\nBAGALKOT\nBANGALORERURAL\nBANGALOREURBAN\nBBMP\nBELGAUM\nBELLARY\nBIDAR\nCHAMARAJANAGAR\nCHIKAMAGALUR\nCHIKKABALLAPUR\nCHITRADURGA\nDAKSHINAKANNADA\nDAVANAGERE\nDHARWAD\nGADAG\nGULBARGA\nHASSAN\nHAVERI\nKODAGU\nKOLAR\nKOPPAL\nMANDYA\nMYSORE\nRAICHUR\nRAMANAGARA\nSHIMOGA\nTUMKUR\nUDUPI\nUTTARKANNADA\nVIJAYAPURA\nYADGIR"
    print(string_list)
    return [stringlist]

def Response(input_message: object) -> object:
    message = input_message.lower()
    print(message)
    if re.match(PIN_regex,message):
        return Checkbypin(message)
    elif re.match(District_regex, message):
        return CheckbyDistrict(message)
    elif re.match(digit,message):
        return Getlist()
    else:
        return [defaultline];