import os

def passive_reconnaissance(target_domain):
    # Subfinder
    print("{+}[Subdomain Enumeration] Starting Subfinder ...") 
    subfinder_cmd = f'subfinder -d {target_domain} -o subfinder.txt'
    os.system(subfinder_cmd)

    # Amass
    print("{+}[Subdomain Enumeration] Starting Amass ...") 
    amass_cmd = f'amass enum -passive -norecursive -d {target_domain} -o amass.txt'
    os.system(amass_cmd)

    # Assetfinder
    print("{+}[Subdomain Enumeration] Starting Assetfinder ...")  
    assetfinder_cmd = f'echo {target_domain} | assetfinder --subs-only | tee assetfinder.txt'
    os.system(assetfinder_cmd)

    # FFuF
    print("{+}[Subdomain Enumeration] Starting FUZZ ...") 
    wordlist_path = input("Enter the path to the wordlist (e.g., /usr/share/wordlist/common.txt) ").strip()
    ffuf_cmd = f'ffuf -u https://FUZZ.{target_domain} -w {wordlist_path} -p 1 -o ffuf_subdom.txt'
    os.system(ffuf_cmd)

    # BBoT
    print("{+}[Subdomain Enumeration] Starting BBoT ...") 
    bbot_cmd = f'bbot -t {target_domain} -f subdomain-enum >> bbot.txt'
    print(' You find it on ./bbot/scans')
    os.system(bbot_cmd)

    #Hacktrails
    print("{+}[Subdomain Enumeration] Starting Hacktrails && Hakrawler ...") 
    haktrails_cmd = f'echo {target_domain} | haktrails subdomains | hakrawler  > haktrails.txt'
    os.system(haktrails_cmd)

    # Github_subdomains
    print("{+}[Subdomain Enumeration] Starting Github_Subdomain ...") 
    organization_name = input("Enter the organization name: ")
    githubsubdomains_cmd = f'python github-subdomains.py --organization {organization_name} --token ghp_lkyJGU3jv1xmwk4SDXavrLDJ4dl2pSJMzj4X >> git_subd.txt'
    os.system(githubsubdomains_cmd)
    
    # Manually_Searching
    print("{+}[Manual_Phase] Infrastructure Source && Certificate Sources && Security Sources ...")
    manual_search_file_path = input("Enter the path to the manual search file (or press Enter to skip): ").strip()

    # Check if a manual search file is specified
    if manual_search_file_path:
        # Add the contents of the manual search file to the subdomain.txt
        with open(manual_search_file_path, 'r') as manual_file:
            manual_data = manual_file.read()
            with open('manual_subdomain.txt', 'a') as subdomain_file:
                subdomain_file.write(manual_data)

    # Combine and deduplicate results
    print("{+}[Combine and Deduplicate Subdomains] Starting  ...") 
    combine_cmd = 'cat subfinder.txt amass.txt assetfinder.txt ffuf_subdom.txt git_subd.txt bbot.txt haktrails.txt manual_subdomain.txt | sort -u | anew subdomain.txt'
    os.system(combine_cmd)
   
    #Resolve Subdomains and check alive or statut 200
    print("{+}[Resolve Subdomains and check alive] Starting  ...") 
    httpx_cmd = f'httpx -l subdomain.txt -o active_subdomain.txt -threads 200 -status-code -follow-redirects'
    print("{+} Alive Subdomains active_subdomain.txt...")
    os.system(httpx_cmd)
    
    # Remove the specified files
    files_to_remove = ['subfinder.txt', 'amass.txt', 'assetfinder.txt', 'ffuf_subdom.txt', 'git_subd.txt', 'bbot.txt','haktrails.txt','manual_subdomain.txt']
    for file in files_to_remove:
        try:
            os.remove(file)
            print(f'Removed: {file}')
        except FileNotFoundError:
            print(f'File not found: {file}')

if __name__ == "__main__":
    print("To execute the Program (e.g., python Recon_Subdomain.py ")
    target_domain = input("Enter the target domain : ")
    passive_reconnaissance(target_domain)
