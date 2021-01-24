import getIds

apiKey = 'API KEY DO MERAKI'
networkName = 'NOME DA NETWORK MERAKI PARA FILTRO'

# Exemplo de Body para aprendizado
body = body = {
    "meshingEnabled": True,
    "ipv6BridgeEnabled": True,
    "locationAnalyticsEnabled": True
}

orgId = getIds.getOrgID(apiKey)

print(orgId)

networkId = getIds.getNetworkID(apiKey, orgId, networkName)
print(networkId)

changeWifi = getIds.putWifiNetworkSettings(apiKey, networkId, body)

print(changeWifi)
