import sys
import info
import json

if __name__ == "__main__":
    getting = info.get_info()
    r = json.loads(json.dumps(getting))
    print("Data: "+r[0], "\n\nLocalizacao: "+r[1])#, "\n\nTemperatura: "+r[2], "\n\nSensacao Termica: " +r[3], "\n\nHumidade: "+r[4])
