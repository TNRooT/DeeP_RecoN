import os
import subprocess

#Define Colors
END = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"

#Function Message
def print_error(message):
    print(f"{RED}[ERROR]{END} {message}")
def print_success(message):
    print(f"{GREEN}[SUCCESS]{END} {message}")
def print_warning(message):
    print(f"{YELLOW}[WARNING]{END} {message}")
def print_info(message):
    print(f"{CYAN}[INFO]{END} {message}")

#Create Directory
def create_directory():
    tools_dir="/root/AllInOne/tools"
    file_dir = os.path.join(tools_dir,"file")
    WL_dir ="/root/AllInOne/Wordlist"
    templates_dir = "/root/AllInOne/templates"
    NT = os.path.join(templates_dir,"nuclei_templates")
    CTN = os.path.join(templates_dir,"community_nuclei_templates")
    os.makedirs(tools_dir, exist_ok=True)
    os.makedirs(file_dir, exist_ok=True)
    os.makedirs(WL_dir, exist_ok=True)
    os.makedirs(templates_dir, exist_ok=True)
    os.makedirs(NT, exist_ok=True)
    os.makedirs(CTN, exist_ok=True)

#def check_tool(tool_name):
    #result = subprocess.run(["whereis", tool_name], capture_output=True, text=True)
    #if result.returncode == 0 and result.stdout.strip():
        #return True
    #else:
        #return False

#Install Requirements 
def install_requirements():
    print_info(f"{CYAN}Update in progress...{END} ")
    subprocess.run(["sudo","apt-get" , "update"])
    print_info(f"{CYAN}Git installation in progress ...{END} ")
    subprocess.run(["sudo","apt-get" , "install", "git"])
    print_success(f"{GREEN}Git installation is done !{END}")
    print_info(f"{CYAN}Python3 installation in progress ...{END} ")
    subprocess.run(["sudo","apt-get" , "install", "python3"])
    print_success(f"{GREEN}Python3 installation is done !{END}")
    print_info(f"{CYAN}PIP3 installation in progress ...{END}")
    subprocess.run(["sudo", "apt-get", "install", "python3-pip"])
    print_success(f"{GREEN}pip installation is done !{END}")
    print_info(f"{CYAN}Upgrade pip in progress ...{END}")
    subprocess.run(["pip", "install", "--upgrade", "pip"])
    print_success(f"{GREEN}Upgrade pip is done !{END}")
    print_info(f"{CYAN}Curl installation in progress ...{END} ")
    subprocess.run(["sudo","apt-get" , "install", "curl", "-y"])
    print_success(f"{GREEN}Curl installation is done !{END}")
    print_info(f"{CYAN}Unzip installation in progress ...{END} ")
    subprocess.run(["sudo","apt-get" , "install", "unzip", "-y"])
    print_success(f"{GREEN}Unzip installation is done !{END}")

    # Install GO:
    print_info(f"{CYAN}Golang installation in progress ...{END} ")
    os.chdir("/root/AllInOne/tools/file")
    subprocess.run(["wget", "https://go.dev/dl/go1.22.1.linux-amd64.tar.gz"])
    subprocess.run(["tar", "-zxvf", "go1.22.1.linux-amd64.tar.gz", "-C", "/usr/local/"])
    subprocess.run(["rm", "-rf", "go1.22.1.linux-amd64.tar.gz"])

        # Settings environment variables
    os.environ["GOROOT"] = "/usr/local/go"
    os.environ["GOPATH"] = "/root/go"
    os.environ["PATH"] = f"{os.environ['GOPATH']}/bin:{os.environ['GOROOT']}/bin:{os.environ['PATH']}"

    subprocess.run(["update-alternatives", "--install", "/usr/bin/go", "go", "/usr/local/go/bin/go", "0"])
    subprocess.run(["update-alternatives", "--set", "go", "/usr/local/go/bin/go"])

    print_success(f"{GREEN}Golang installation is done !{END}")

def ASN():
    try : 
        print_info(f"{CYAN}metabigor installation in progress ...{END} ")        
        os.chdir("/root/AllInOne/tools/file")
        subprocess.run(["git", "clone", "https://github.com/j3ssie/metabigor.git"])
        os.chdir("/root/AllInOne/tools/file/metabigor")
        subprocess.run(["go", "install"])
        print_success(f"{GREEN}metabigor installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}metabigor installation failed. Please check the Go installation and build process : {str(e)}{END}")

    try :
        print_info(f"{CYAN}asnmap installation in progress ...{END} ") 
        subprocess.run(["go", "install", "github.com/projectdiscovery/asnmap/cmd/asnmap@latest"])
        print_success(f"{GREEN}asnmap installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} asnmap installation failed. An unexpected error occurred : {str(e)} {END}")

def SUBDOMAINS_ENUMERATION ():
    try : 
        print_info(f"{CYAN}Altdns installation in progress ...{END} ")
        subprocess.run(["pip3", "install", "py-altdns==1.0.2"])
        print_success(f"{GREEN}Altdns installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}Altdns installation failed. An unexpected error occurred: {str(e)}{END}")
    
    try :
        print_info(f"{CYAN}amass installation in progress ...{END} ") 
        subprocess.run(["go", "install", "-v", "github.com/owasp-amass/amass/v4/...@master"])
        print_success(f"{GREEN}amass installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} amass installation failed. An unexpected error occurred : {str(e)} {END}")

    try:
        print_info(f"{CYAN} Linkfinder installation in progress ...{END}")
        os.chdir("/root/AllInOne/tools/file") 
        subprocess.run(["git", "clone", "https://github.com/GerbenJavado/LinkFinder.git"]) 
        os.chdir("/root/AllInOne/tools/file/LinkFinder")
        subprocess.run(["python", "setup.py", "install"])      
        print_success(f"{GREEN}LinkFinder installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} LinkFinder installation failed. An unexpected error occurred : {str(e)} {END}")
    
    try:
        print_info(f"{CYAN} secretfinder installation in progress ...{END}")
        os.chdir("/root/AllInOne/tools/file") 
        subprocess.run(["git", "clone", "https://github.com/m4ll0k/SecretFinder.git"]) 
        os.chdir("/root/AllInOne/tools/file/SecretFinder")
        subprocess.run(["pip", "install", "-r", "requirements.txt"])      
        print_success(f"{GREEN}secretfinder installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} secretfinder installation failed. An unexpected error occurred : {str(e)} {END}")
    
    try :
        print_info(f"{CYAN}assetfinder installation in progress ...{END} ") 
        subprocess.run(["go", "get", "-u", "github.com/tomnomnom/assetfinder"])
        print_success(f"{GREEN}assetfinder installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} assetfinder installation failed. An unexpected error occurred : {str(e)} {END}")

    try :
        print_info(f"{CYAN}subfinder installation in progress ...{END} ") 
        subprocess.run(["go", "install", "-v", "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"])
        print_success(f"{GREEN}subfinder installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} subfinder installation failed. An unexpected error occurred : {str(e)} {END}")
               
    try :
        print_info(f"{CYAN}shuffledns installation in progress ...{END} ") 
        subprocess.run(["go", "install", "-v", "github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest"])
        print_success(f"{GREEN}shuffledns installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} shuffledns installation failed. An unexpected error occurred : {str(e)} {END}")
              
    try :
        print_info(f"{CYAN}github-subdomains installation in progress ...{END} ") 
        subprocess.run(["go", "install", "github.com/gwen001/github-subdomains@latest"])
        print_success(f"{GREEN}github-subdomains installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} github-subdomains installation failed. An unexpected error occurred : {str(e)} {END}")

    try :
        print_info(f"{CYAN}ffuf installation in progress ...{END} ") 
        subprocess.run(["go", "install", "github.com/ffuf/ffuf/v2@latest"])
        print_success(f"{GREEN}ffuf installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}ffuf installation failed. An unexpected error occurred : {str(e)} {END}")
              
    try :
        print_info(f"{CYAN}bbot installation in progress ...{END} ") 
        subprocess.run(["pip", "install", "bbot"])
        print_success(f"{GREEN}bbot installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}bbot installation failed. An unexpected error occurred : {str(e)} {END}")
                  
    try :
        print_info(f"{CYAN}haktrails installation in progress ...{END} ") 
        subprocess.run(["go", "install", "-v", "github.com/hakluke/haktrails@latest"])
        print_success(f"{GREEN}haktrails installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}haktrails installation failed. An unexpected error occurred : {str(e)} {END}")
             
    try :
        print_info(f"{CYAN}hakrawler installation in progress ...{END} ") 
        subprocess.run(["go", "install", "github.com/hakluke/hakrawler@latest"])
        print_success(f"{GREEN}hakrawler installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}hakrawler installation failed. An unexpected error occurred : {str(e)} {END}")

def Resolve_Check_Alive():           
    try :
        print_info(f"{CYAN}httpx installation in progress ...{END} ") 
        subprocess.run(["go", "install", "-v", "github.com/projectdiscovery/httpx/cmd/httpx@latest"])
        print_success(f"{GREEN}httpx installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}httpx installation failed. An unexpected error occurred : {str(e)} {END}")
           


    # Add /root/go/bin to the PATH
    #try:
        subprocess.run(["export", f"PATH=$PATH:/root/go/bin"])
        print_warning(f"{YELLOW}Updated PATH: {os.environ['PATH']}{END}")
    #except Exception as e:
        print_error(f"{RED}Failed to update PATH environment variable: {str(e)}{END}")

def Screenshot():
    try:
        print_info(f"{CYAN} EyeWitness installation in progress ...{END}")
        os.chdir("/root/AllInOne/tools/file") 
        subprocess.run(["git", "clone", "https://github.com/RedSiege/EyeWitness.git"]) 
        os.chdir("/root/AllInOne/tools/file/EyeWitness/Python/setup")
        subprocess.run(["bash", "setup.sh"])      
        print_success(f"{GREEN}EyeWitness installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} EyeWitness installation failed. An unexpected error occurred : {str(e)} {END}")
    
def Port_Analysis():
    try :
        print_info(f"{CYAN}nmap installation in progress ...{END} ")
        subprocess.run(["apt", "install", "build-essential", "libssl-dev"])
        os.chdir("/root/AllInOne/tools/file")
        subprocess.run(["wget", "https://nmap.org/dist/nmap-7.94.tar.bz2"]) 
        subprocess.run(["tar", "-xvjf", "nmap-7.94.tar.bz2"])
        os.chdir("/root/AllInOne/tools/file/nmap-7.94")
        subprocess.run("./configure", "&&", "make", "&&", "sudo", "make", "install", shell=True, check=True)
        print_success(f"{GREEN}nmap installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} nmap installation failed. An unexpected error occurred : {str(e)} {END}")
   
    try :
        print_info(f"{CYAN}naabu installation in progress ...{END} ") 
        subprocess.run(["go", "install", "-v", "github.com/projectdiscovery/naabu/v2/cmd/naabu@latest"])
        print_success(f"{GREEN}naabu installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} naabu installation failed. An unexpected error occurred : {str(e)} {END}")

def CHECK_FOR_DEFAULT_CREDS():
    try : 
        print_info(f"{CYAN}brutespray installation in progress ...{END} ")        
        os.chdir("/root/AllInOne/tools/file")
        subprocess.run(["git", "clone", "https://github.com/x90skysn3k/brutespray.git"])
        os.chdir("/root/AllInOne/tools/file/brutespray")
        subprocess.run(["go", "build", "-o", "brutespray", "main.go"])
        print_success(f"{GREEN}brutespray installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}brutespray installation failed. Please check the Go installation and build process : {str(e)}{END}")

def Collecting_URL_Endpoint():
    try :
        print_info(f"{CYAN}gau installation in progress ...{END} ") 
        subprocess.run(["go", "install", "github.com/lc/gau/v2/cmd/gau@latest"])
        print_success(f"{GREEN}gau installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} gau installation failed. An unexpected error occurred : {str(e)} {END}")

    try :
        print_info(f"{CYAN}katana installation in progress ...{END} ") 
        subprocess.run(["go", "install", "github.com/projectdiscovery/katana/cmd/katana@latest"])
        print_success(f"{GREEN}katana installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} katana installation failed. An unexpected error occurred : {str(e)} {END}")

def GitHub_Dorking_Tools():
    try:
        print_info(f"{CYAN} gitleaks installation in progress ...{END}")
        os.chdir("/root/AllInOne/tools/file") 
        subprocess.run(["git", "clone", "https://github.com/gitleaks/gitleaks.git"]) 
        os.chdir("/root/AllInOne/tools/file/gitleaks")
        subprocess.run(["make", "build"])      
        print_success(f"{GREEN}gitleaks installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} gitleaks installation failed. An unexpected error occurred : {str(e)} {END}")
        
    try:
        print_info(f"{CYAN} trufflehog installation in progress ...{END}")
        os.chdir("/root/AllInOne/tools/file") 
        subprocess.run(["git", "clone", "https://github.com/trufflesecurity/trufflehog.git"]) 
        os.chdir("/root/AllInOne/tools/file/trufflehog")
        subprocess.run(["go ", "install"])      
        print_success(f"{GREEN}trufflehog installation is done !{END}")
    except Exception as e:
        print_error(f"{RED} trufflehog installation failed. An unexpected error occurred : {str(e)} {END}")
        
    try :
        print_info(f"{CYAN}gitrob installation in progress ...{END} ") 
        subprocess.run(["go", "get", "github.com/michenriksen/gitrob"])
        print_success(f"{GREEN}gitrob installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}gitrob installation failed. An unexpected error occurred : {str(e)} {END}")
            
def  Find_Source_Backups_Files():

    try :
        print_info(f"{CYAN}dirsearch installation in progress ...{END} ") 
        subprocess.run(["pip", "install", "dirsearch"])
        print_success(f"{GREEN}dirsearch installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}dirsearch installation failed. An unexpected error occurred : {str(e)} {END}")
             
    try :
        print_info(f"{CYAN}gobuster installation in progress ...{END} ") 
        subprocess.run(["go", "install", "github.com/OJ/gobuster/v3@latest"])
        print_success(f"{GREEN}gobuster installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}gobuster installation failed. An unexpected error occurred : {str(e)} {END}")

    try :
        print_info(f"{CYAN}fuzzuli installation in progress ...{END} ") 
        subprocess.run(["go", "install", "-v", "github.com/musana/fuzzuli@latest"])
        print_success(f"{GREEN}fuzzuli installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}fuzzuli installation failed. An unexpected error occurred : {str(e)} {END}")

def Subdomain_Take_Over():
    try :
        print_info(f"{CYAN}SubOver installation in progress ...{END} ") 
        subprocess.run(["go", "get", "github.com/Ice3man543/SubOver"])
        print_success(f"{GREEN}SubOver installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}SubOver installation failed. An unexpected error occurred : {str(e)} {END}")

    try :
        print_info(f"{CYAN}nuclei installation in progress ...{END} ") 
        subprocess.run(["go", "install", "-v", "github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest"])
        print_success(f"{GREEN}nuclei installation is done !{END}")
    except Exception as e:
        print_error(f"{RED}nuclei installation failed. An unexpected error occurred : {str(e)} {END}")

def Download_Wordlist():
    user_choice = input("Do you want to download Wordlists? (yes/no): ").lower()
    
    if user_choice == "yes":
        print_info(f"{CYAN} Downloading Wordlists now...{END}")
        # Navigate to the Wordlists directory
        os.chdir("/root/AllInOne/Wordlist")
        # Clone Wordlists repository
        subprocess.run(["git", "clone", "https://github.com/TNRooT/DeeP_RecoN/tree/ce41a3dd332a8d0f6194425ce0755b7ab20fa1be/wordlists/IIS_Microsoft_Framework"])
        subprocess.run(["git", "clone", "https://github.com/TNRooT/DeeP_RecoN/tree/ce41a3dd332a8d0f6194425ce0755b7ab20fa1be/wordlists/JAVA"])
        subprocess.run(["git", "clone", "https://github.com/TNRooT/DeeP_RecoN/tree/ce41a3dd332a8d0f6194425ce0755b7ab20fa1be/wordlists/PHP_CGI"])
        subprocess.run(["git", "clone", "https://github.com/TNRooT/DeeP_RecoN/tree/ce41a3dd332a8d0f6194425ce0755b7ab20fa1be/wordlists/General_API"])
        print_success(f"{GREEN} Wordlists download complete.{END}")
    else:
        print_warning(f"{YELLOW} Skipping Wordlists download.{END}")    


def Download_Nuclei_Template():
    user_choice = input(f"{CYAN}Do you want to download Nuclei Templates? (yes/no): {END}").lower()
    if user_choice == "yes":
        print_info(f"{CYAN}[INFO] Downloading Nuclei Templates now...{CYAN}")
        # Navigate to the nuclei-templates directory
        os.chdir("/root/AllInOne/templates/nuclei_templates")
        # Clone nuclei-templates repository
        os.system('git clone https://github.com/projectdiscovery/nuclei-templates.git > /dev/null 2>&1')
        print_success(f"{GREEN}[SUCCESS] Nuclei Templates download complete.{GREEN}")
    else:
        print_warning(f"{YELLOW} Skipping Nuclei Templates download.{YELLOW}")

def Download_Nuclei_Community_Template():
    user_choice = input(f"{CYAN}Do you want to download Nuclei Community Templates? (yes/no): {END}").lower()
    if user_choice == "yes":
        os.chdir("/root/AllInOne/templates/community_nuclei_templates")
        destination_path = "/root/AllInOne/templates/community_nuclei_templates"
        url ="https://raw.githubusercontent.com/TNRooT/DeeP_RecoN/main/URL.txt"
        subprocess.run(["wget", url])
        url_file = "/root/AllInOne/templates/community_nuclei_templates/url.txt"
        with open(url_file, 'r') as file:
            urls = file.readlines()
        for u in urls:
            u = url.strip()
            repo_name = url.split('/')[-1]
            repo_destination = os.path.join(destination_path, repo_name)
            clone = f"git clone {url} {repo_destination}"
            os.system(clone)
        print_success(f"{GREEN} Nuclei Community Templates download complete{END}")
    else:
        print_warning(f"{YELLOW}Skipping Nuclei Community Templates download.{END}")

#EXIT PROGRAMME
def exist_program():
    print_warning(f"{YELLOW}Exiting The Program ...{END} ")
    exit()
#Main Function
def main():
    create_directory()
    install_requirements()
    ASN()
    SUBDOMAINS_ENUMERATION ()
    Resolve_Check_Alive()
    Screenshot()
    Port_Analysis()
    CHECK_FOR_DEFAULT_CREDS()
    Collecting_URL_Endpoint()
    Find_Source_Backups_Files()
    Subdomain_Take_Over()
    Download_Wordlist()
    Download_Nuclei_Template()
    Download_Nuclei_Community_Template()
    exist_program()
if __name__ == "__main__":
    main()
