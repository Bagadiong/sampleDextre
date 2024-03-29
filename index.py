"""
Lambda events entry point
"""

import _uxy_core
from _uxy_core import core
from _uxy_core.utility.common import fbtoken_verifier


def lambda_handler(event, context):
  try:
    if( event['method'] == 'GET' ):
      return fbtoken_verifier.verify(event['queryParams'], \
        _uxy_core.appconfig['fb:verifyToken'])

    if( event['method'] == 'POST' ):
      return core.handler(event['body'])

    return {
      'status' : 405,
      'body' : 'Method not supported'
    }
  except Exception as e:
    print(str(e))
  return {
    'status' : 500,
    'body' : 'Uxy app error'
  }

