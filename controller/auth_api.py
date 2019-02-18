from flask import Response,request,session,g

from services import Login
from controller import api_blueprint as api

@api.route('/auth/login', methods=['POST'])
def login():
    requested_data = request.get_json()
    session.pop('email',None)
    if(Login.IsUserMatched(requested_data)):
        session['email']=requested_data["email"]
        return Response('',201,mimetype='application/json')
    return Response('',401,mimetype="application/json")
