#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib3
import random
import time
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # No SSL certificate, so ignore https warnings


#website_url = "https://www.intopic.it/crono/varie/cronaca/?pagina="
website_url = 'https://www.lanuovasardegna.it/cagliari/cronaca?page='
http = urllib3.PoolManager()

def get_random_user_agent_header():
    
    user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                   'Mozilla/5.0 (iPad; CPU OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/83.0.4103.88 Mobile/15E148 Safari/604.1',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
                   'Mozilla/5.0 (Android 10; Mobile; LG-M255; rv:68.0) Gecko/68.0 Firefox/68.0'
                   ]
    
    user_agent = user_agents[random.randint(0, len(user_agents)-1)]
    
    hdr = {'User-Agent': user_agent,
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
           'Connection': 'keep-alive'}
    
    
    return hdr

province = {'cagliari':31 + 1, 'sassari':153 + 1, 'oristano':17 + 1, 'nuoro':121 + 1}
for provincia in ['nuoro']:
    
    
    limit_provincia = province[provincia]
    
    for i in range(27, limit_provincia):
        url = website_url + str(i)
        
        
        #file_path = "/home/marco/workspace/git/StatLearnTeam/web_pages_index/new_pages/" + str(i) + ".html"
    
        file_path = "/home/marco/workspace/git/StatLearnTeam/web_pages_index/new_pages/nuova_sardegna_" + provincia + '_' + str(i) + ".html"
    
        hdr = get_random_user_agent_header()
    
        try:
            response = http.request('GET', url, headers=hdr)
            
            content = response.data.decode('ISO-8859-1')
            
            f = open(file_path, 'w') # Saving path: files will be like 234.html
            f.write(str(content))
            f.close()
            file_size_kb = int(Path(file_path).stat().st_size / 1024)
            
            print('Downloaded %s %s.html | Size: %d Kb' % (provincia, str(i), file_size_kb))
    
            #if file_size_kb < 15:
            #    raise Exception('Size error: check if downloader is blocked.')
    
        
        
            wait_time = random.randint(9,  11) 
            time.sleep(wait_time)
            
            
        except Exception as e: # In case something happens, wait 
            i = i - 1
            print(e)
            time.sleep(60)
