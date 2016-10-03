import sys
import os
import requests

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

print("Starting program Function Create for Request ID:" + sys.argv[1])
print("DB IP received is " + sys.argv[2])

request_id = sys.argv[1]
db_ip_ddress = sys.argv[2]

##################################################
#updating API for request parameters to DB Service
##################################################
def put_request_db(get_request_api_arg, db_ip_ddress_arg, set_status_arg)
	 #generating GET API for getting Request from DB Service
        get_request_api = 'http://' + db_ip_ddress_arg + '/request/' + request_id_arg
	resp = requests.put(get_request_api, json={'status': set_status_arg})
        if resp.status_code != 200:
		# This means something went wrong.
		print('PUT /request/{} {}'.format(set_status_arg, resp.status_code))
		return 1
	else:
		print('PUT /request/{} {}'.format(set_status_arg, resp.status_code))
		return 0

######################################################
#requesting API for request parameters from DB Service
######################################################
def get_request_db(get_request_api_arg, db_ip_ddress_arg)
	#generating GET API for getting Request from DB Service
	get_request_api = 'http://' + db_ip_ddress_arg + '/request/' + request_id_arg
	resp = requests.get(get_request_api)
	if resp.status_code != 200:
		# This means something went wrong.
		print('GET /request/ {}'.format(resp.status_code))
		#put_request_db(request_id_arg, db_ip_ddress_arg, 'CreationFailed')
	for todo_item in resp.json():
		print('{}\n{} '.format(todo_item['id'], todo_item['body']))

##########################################################
#requesting API to save tehfunction and its contents to DB
##########################################################
def post_function_create_db
	#generating API for getting Function Created
	get_request_api = 'http://' + db_ip_ddress_arg + '/function/'
	 resp = requests.post(get_request_api,json={
        'id': summary,
        'name': description,
	'content': content,
	'userid': userid,
        })
        if resp.status_code != 200:
                # This means something went wrong.
                print('GET /request/ {}'.format(resp.status_code))
                #put_request_db(request_id_arg, db_ip_ddress_arg, 'CreationFailed')
        for todo_item in resp.json():
                print('{}\n{} '.format(todo_item['id'], todo_item['body']))


print(resp)

