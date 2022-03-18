def GenerateConfig(context):

    resources = [{
        'name': context.properties['infra_id'] + '-Owner',
        'type': 'iam.v1.serviceAccount',
        'properties': {
            'accountId': context.properties['infra_id'] + '-Owner',
            'displayName': context.properties['infra_id'] + '-Owner'
        }
    }, {
        'name': context.properties['infra_id'] + '-Viewer',
        'type': 'iam.v1.serviceAccount',
        'properties': {
            'accountId': context.properties['infra_id'] + '-Viewer',
            'displayName': context.properties['infra_id'] + '-Viewer'
        }
    }]

    return {'resources': resources}