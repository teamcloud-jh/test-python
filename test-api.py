import v20

#
# Create the API context based on the provided arguments
#
api = v20.Context(
    hostname='api-fxpractice.oanda.com',
    token='43b546aff89ed477d1c2841a0193b263-23e07b9e94639df4e20d217b02ddaa97'
)

#
# Submit the request to create the Market Order
#
response = api.order.market(
    accountID='101-011-14995955-001', # remove dash
    instrument='SPX500_USD',
    units=1
)

#
# Process the response
#
# print("Response: {} ({})".format(response.status, response.reason))
print(f'Response: {format(response.status)} ({format(response.reason)})')
