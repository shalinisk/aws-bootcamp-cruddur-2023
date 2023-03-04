import os
from datetime import datetime, timedelta, timezone

# XRay SDK libraries
from aws_xray_sdk.core import xray_recorder
# from aws_xray_sdk.core import patch_all
# from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

class UserActivities:
  # def __init__(self, request):
  #       self.request = request

  def run(user_handle):
    try:
      # Start a segment
      # parent_subsegment = xray_recorder.begin_subsegment('activities_users_start')
      # parent_subsegment.put_annotation('url', self.request.url)

      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()

      # # Add metadata/annotation
      # xray_dict = {'now': now.isoformat()}
      # parent_subsegment.put_metadata('now', xray_dict, 'activities_users')
      # parent_subsegment.put_metadata('method', self.request.method, 'http')
      # parent_subsegment.put_metadata('url', self.request.url, 'http')

      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['blank_user_handle']
      else:
        now = datetime.now()
        results = [{
          'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
          'handle':  'Andrew Brown',
          'message': 'Cloud is fun!',
          'created_at': (now - timedelta(days=1)).isoformat(),
          'expires_at': (now + timedelta(days=31)).isoformat()
        }]
        model['data'] = results
      
      # X-Ray
      subsegment = xray_recorder.begin_subsegment('mock-data')
      
      dict = {
        "now": now.isoformat(),
        "results-size": len(model['data'])
      }
      subsegment.put_metadata('key', dict, 'namespace')
      xray_recorder.end_subsegment()
    finally:  
      #Close the segment
      xray_recorder.end_subsegment()
    return model