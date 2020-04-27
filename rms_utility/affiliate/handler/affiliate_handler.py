from flask import Flask, jsonify, request
import json


app = Flask(__name__)


@app.route('/')
def index() -> str:
    return json.dumps({'List all API V.0': "list all apis and inputs outputs for each here"})

@app.route('/createAffiliate', methods=['POST','GET'])
def create_affiliate() -> str:
    # initiate database session
        # we should not care what database just create session abtract away
    # extract users commands from request and pass to domain service(model)
    #status code resposne
    #return response error message if something goes wrong and code 200,404...etc
    
    # Get paramaters from request
    req_data = request.get_json()
    userid = req_data['user_id']
    affiliate_name = req_data['affiliate_name']
    affiliate_id = req_data['affiliate_id']
    
    return json.dumps({'affiliate': "Affiliate {}:{} was created".format(affiliate_name,affiliate_id)})

@app.route('/getAffiliate')
def get_affiliate() -> str:
    return json.dumps({'affiliate': "Affiliate data"})

@app.route('/getAffiliates')
def get_affiliates() -> str:
    return json.dumps({'affiliate': "Affiliates datas"})

@app.route('/updateAffiliate')
def update_affiliate() -> str:
    return json.dumps({'affiliate': "Affiliate data was updated"})

@app.route('/deleteAffiliate')
def delete_affiliate() -> str:
    return json.dumps({'affiliate': "Affiliate was deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')