const { json } = require('express');
const { STATUS_CODES } = require('http');
const https = require('https');
age = 45;
d_id = 286;
let date_ob = new Date();
let date = date_ob.getDate();
let month = date_ob.getMonth() + 1;
let year = date_ob.getFullYear();
let request_date=date+"-"+month+"-"+year;
var DATA = {
    Date: '',
    Name: '',
    vaccine: '',
    available_capacity_dose1: 0,
    available_capacity_dose2: 0
}
https.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=' + d_id + '&date='+request_date+'', (resp) => {
    let data = '';

    resp.on('data', (chunk) => {
        data += chunk;
    });

    resp.on('end', () => {
        var length = JSON.parse(data).centers.length;
        var info = JSON.parse(data);
        for (var i = 0; i < length; i++) {
            var dat = info.centers[i];
            if (dat.sessions[0].min_age_limit == age) {
                // if (dat.sessions[0].available_capacity_dose1 > 0 || dat.sessions[0].available_capacity_dose2 > 0) {
//                   console.log(Date:request_date)
//                    console.log(dat.name);
//                    console.log(dat.sessions[0].vaccine)
//                    console.log(dat.sessions[0].available_capacity_dose1);
//                    console.log(dat.sessions[0].available_capacity_dose2);
                     DATA.date=request_date;
                     DATA.Name=dat.name;
                     DATA.vaccine=dat.sessions[0].vaccine;
                     DATA.available_capacity_dose1=dat.sessions[0].available_capacity_dose1;
                     DATA.available_capacity_dose2=dat.sessions[0].available_capacity_dose2;
                     console.log(DATA)
                // }
            }
        }
    });

}).on("error", (err) => {
    console.log("Error: " + err.message);
});
