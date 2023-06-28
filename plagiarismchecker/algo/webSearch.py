from plagiarismchecker.algo import ConsineSim
from googleapiclient.discovery import build
searchEngine_API = 'AIzaSyCYnJJY9sfBp7n1AD2MPLWqp-EHsoNRNf0'
searchEngine_Id = 'e7907aab111c04688'

def searchWeb(text, output, c):
    text = text
    try:
        res = build("customsearch", 'v1',developerKey=searchEngine_API).cse()
        result = res.list(q=text, cx=searchEngine_Id).execute()
        searchInfo = result['searchInformation']
        if(int(searchInfo['totalResults']) > 0):
            Max_Sim = 0
            Max_Sim_Link = ''
            Num_Items = len(result['items']) 
            if Num_Items >= 5:
                Num_Items = 5
            for i in range(0, Num_Items):
                item = result['items'][i]
                Item_content = item['snippet']
                Sim_Value = ConsineSim.cosineSim(text, Item_content)
                if Sim_Value > Max_Sim:
                    Max_Sim = Sim_Value
                    Max_Sim_Link = item['link']
                if item['link'] in output:
                    Max_Sim_Link = item['link']
                    break
            if Max_Sim_Link in output:
                output[Max_Sim_Link] = output[Max_Sim_Link] + 1
                c[Max_Sim_Link] = ((c[Max_Sim_Link] *(output[Max_Sim_Link]-1) + Max_Sim)/(output[Max_Sim_Link]))
            else:
                output[Max_Sim_Link] = 1
                c[Max_Sim_Link] = Max_Sim
    except Exception as e:
        return output, c, 1
    return output, c, 0
