import environment as envProp
import funcs as fn
import requests

import json
# step 1
# read an API https://adsladsl.pythonanywhere.com/points
# end point 
# authrntication  -   private_key 


# api call  -  return output  almost 99 % - JSON 


response_API = requests.get(envProp.API_LINK)

if(response_API.status_code==200):
    # next steps
    pass
    df=fn.break_down_code(response_API)
    # function to get counts based on date
    df2=fn.grouping_df(df)
    fn.plot_graph(df2)
else:
    # exit()
    raise Exception("The response code is negative :"+ response_API.status_code)



# step2
# understand the pattern / hierarcy and break it down for further usage



# step3
# Business logic/ requirement
# to identify number of entires per day and identify the traffic.



