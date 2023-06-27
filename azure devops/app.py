from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import matplotlib.pyplot as plt


# Organization URL
organization_url = 'http://dev.azure.com/grupoins/sec'

# personal access token
personal_access_token = '2skiwf4lt67k5oc2l7lwod7a6lldzubkrmzsngxglbdkatnfm6kq'

credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)


wit_client = connection.clients.get_work_item_tracking_client()

sprint_id = 'Sprint%2056%20(RF-517942-1-387778)'
query = "SELECT [System.Id], [System.Title], [System.State] FROM workitems WHERE [System.IterationId] = '{}'".format(sprint_id)
work_items = wit_client.query_by_wiql(query).work_items
