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
     if req.get("result").get("action") == "halo":
            hasil=req.get("result").get("resolvedQuery")
            return {
                "speech": hasil,
                "displayText": hasil,
                #"data": {},
                #"contextOut": [],
                "source": hasil
            }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))

    print ("Starting app on port %d" %(port))

    app.run(debug=False, port=port, host='0.0.0.0')
