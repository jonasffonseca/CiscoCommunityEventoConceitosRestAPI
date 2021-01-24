import requests
import urllib3
import json

# Desabilita avisos de certificado inválido
urllib3.disable_warnings()

baseUrl = 'https://api.meraki.com/api/v1'


def getOrgID(apiKey):
    header = {
        "X-Cisco-Meraki-API-Key": apiKey
    }
    response = requests.get(
        f'{baseUrl}/organizations', headers=header, verify=False)
    orgId = json.loads(response.content)
    return orgId[0]['id']


def getNetworkID(apiKey, orgId, name):
    header = {
        "X-Cisco-Meraki-API-Key": apiKey
    }
    url = f'{baseUrl}/organizations/{orgId}/networks'
    response = requests.get(url, headers=header, verify=False)
    networkId = json.loads(response.content)
    # Função Lambda que percorre cada um dos objetos networkId e
    # retorna o valor daquele que tem o mesmo nome do parâmetro name
    filteredData = list(filter(lambda x: x['name'] == name, networkId))
    return filteredData[0]['id']


def putWifiNetworkSettings(apiKey, networkId, newBody):
    header = {
        "X-Cisco-Meraki-API-Key": apiKey
    }
    url = f'{baseUrl}/networks/{networkId}/wireless/settings'
    response = requests.put(url,
                            headers=header, data=newBody, verify=False)
    return response.content
