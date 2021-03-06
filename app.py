#!/usr/bin/env python

import json
import os
import math



from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])


def webhook():
    req = request.get_json(silent=True, force=True)
    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'

    return r




def makeWebhookResult(req):
     if req.get("result").get("action") == "penjumlahan":
        number=int(req.get("result").get("parameters").get("number"))
        operasi=req.get("result").get("parameters").get("OPerasi")
        number1=int(req.get("result").get("parameters").get("number1"))

        if operasi=="+":
            hasil=number+number1
        if operasi=="-":
            hasil=number-number1
        if operasi=="*":
            hasil=number*number1
        if operasi=="/":
            hasil=number/number1

        return {
            "speech": "Hasil perhitungan: "+str(hasil),
            "displayText": "Hasil perhitungan: "+str(hasil),
            #"data": {},
            #"contextOut": [],
            "source": "Hasil perhitungan: "+str(hasil)
        }

        app.intent('setup_push', (conv) => {
          conv.ask(new UpdatePermission({intent: 'tell_latest_tip'}));
        });

if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))

    print ("Starting app on port %d" %(port))

    app.run(debug=False, port=port, host='0.0.0.0')
