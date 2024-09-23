
#To collect required information as per command
def get_detail(inpData):
    
    tempC=inpData["current"]["temp_c"]
    tempF=inpData["current"]["temp_f"]
    country=inpData["location"]["country"]
    state=inpData["location"]["region"]
    condition=inpData["current"]["condition"]["text"]

    
    if tempF > 90:
        bg="gold"
    elif tempF < 50:
        bg="white"
    else:
        bg="SystemButtonFace"    
    
    forecast_data=inpData["forecast"]
    forecast_date=[]
    forecast_max_temp=[]
    forecast_min_temp=[]
    for i in range(0,5):
        forecast_date.append(forecast_data["forecastday"][i]["date"][5:])
        forecast_max_temp.append(forecast_data["forecastday"][i]["day"]["maxtemp_f"])
        forecast_min_temp.append(forecast_data["forecastday"][i]["day"]["mintemp_f"])
    
    
    return tempC,tempF,country,state,condition,bg,forecast_date,forecast_max_temp,forecast_min_temp
    