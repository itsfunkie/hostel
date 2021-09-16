from werkzeug.wrappers import response
import hostelapp
from hostelapp.mymodel import Hostel,db
from flask import json, make_response, request,url_for
from flask_httpauth import HTTPBasicAuth

#import the blueprint's instance
from . import apiobj

auth = HTTPBasicAuth()

@apiobj.route('/list/')
def listall():
    hostels = []
    data = Hostel.query.all()
    for x in data:
        a = {}
        a['hostel'] = x.hostel_name
        a['type'] = x.hostel_type
        a['desc'] = x.hostel_desc
        hostels.append(a)
    return json.dumps(data)

@apiobj.route('/list/<int:hostel_id>/')
def listone(hostel_id):
    data = Hostel.query.filter(Hostel.hostel_id == hostel_id).first()
    data2send = {'hostel':data.hostel_name,'type':data.hostel_typ}
    rsp = make_response(json.dumps(data2send),200)
    rsp.headers['Content-Type'] = 'application/json'
    return rsp

@apiobj.route('/addnew/', methods = ['POST'])
def addnew():
    if request.is_json:
        hostel_deets = request.get_json()
        hostelname = hostel_deets ['hostelname']
        desc = hostel_deets['description']
        hosteltype = hostel_deets['type']
        host = Hostel(hostel_name = hostelname,hostel_desc=desc, hostel_type = hosteltype)
        db.session.add(host)
        db.session.commit
        ret = {'status':1, 'msg': 'Hostel added'}
        return json.jsonify(ret)
    else:
        ret = {'status': 0, 'msg': 'Try Again'}
        return json.jsonify(ret)

@apiobj.route('/deletehostel/<int:hostel_id>', methods = ['POST'])
def deletehostel(hostel_id):
    return "Hostel Deleted!.."


@apiobj.route('/updatehostel/<int:hostel_id>', methods = ['DELETE'])
def updatehostel():
    return "Hostel updated!.."
