import os
import subprocess

# Define ANSI escape codes for colors
END = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"

# Add the previous functions here

def print_error(message):
    print(f"{RED}[ERROR]{END} {message}")

def print_success(message):
    print(f"{GREEN}[SUCCESS]{END} {message}")

def print_warning(message):
    print(f"{YELLOW}[WARNING]{END} {message}")

def print_info(message):
    print(f"{CYAN}[INFO]{END} {message}")

# 1 : Create Tools Directories
def create_tools_directory():
    current_directory = os.getcwd()
    tools_directory = os.path.join(current_directory, 'VPS', 'tools')

    # Check if the 'VPS/tools' directory exists, and create it if not
    if not os.path.exists(tools_directory):
        os.makedirs(tools_directory)

    return tools_directory

# 2 : Create Wordlists Directories
#def create_wordlists_directory():
    current_directory = os.getcwd()
    wordlists_directory = os.path.join(current_directory, 'VPS', 'wordlists')

    # Check if the 'VPS/wordlists' directory exists, and create it if not
    if not os.path.exists(wordlists_directory):
        os.makedirs(wordlists_directory)

    return wordlists_directory

# 3 : Create Nuclei Templates Directories
def create_Nuclei_Templates_directory():
    current_directory = os.getcwd()
    templates_directory = os.path.join(current_directory, 'VPS', 'Templates')

    # Check if the 'VPS/Templates' directory exists, and create it if not
    if not os.path.exists(templates_directory):
        os.makedirs(templates_directory)

    return templates_directory

# 4 : Install requirements
def install_requirements():
    print("Installing system requirements...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt", "install", "git"])
    subprocess.run(["sudo", "apt", "install", "python3"])
    subprocess.run(["sudo", "apt", "install", "curl" ,"-y"])
    subprocess.run(["sudo", "apt", "install", "unzip" ,"-y"])
    subprocess.run([ "sudo" ,"apt-get",  "install",  "ruby-full" , "rubygems"])

# 5 : Install Go
def install_go():
    print(f"{YELLOW}[SUBDOMAINS ENUMERATION]{RED}Golang installation in progress ...{YELLOW}")

    # Change the current working directory to where the Go archive will be downloaded
    current_directory = os.getcwd()
    download_directory = os.path.join(current_directory)
    os.chdir(download_directory)

    # Download and extract Go
    download_cmd = [
        "wget",
        "https://go.dev/dl/go1.21.0.linux-amd64.tar.gz"
    ]

    extract_cmd = [
        "tar",
        "-zxvf",
        "go1.21.0.linux-amd64.tar.gz",
        "-C",
        "/usr/local/"
    ]

    try:
        subprocess.run(download_cmd, check=True)
        subprocess.run(extract_cmd, check=True)

        # Set Go environment variables
        os.environ["GOROOT"] = "/usr/local/go"
        os.environ["GOPATH"] = os.path.expanduser("~/.go")
        os.environ["PATH"] = f"{os.environ['PATH']}:{os.environ['GOROOT']}/bin:{os.environ['GOPATH']}/bin"

        # Configure alternatives for the 'go' command
        update_cmd_1 = [
            "update-alternatives",
            "--install",
            "/usr/bin/go",
            "go",
            f"{os.environ['GOROOT']}/bin/go",
            "0"
        ]

        update_cmd_2 = [
            "update-alternatives",
            "--set",
            "go",
            f"{os.environ['GOROOT']}/bin/go"
        ]

        subprocess.run(update_cmd_1, check=True)
        subprocess.run(update_cmd_2, check=True)

        print(f"{GREEN}[SUBDOMAINS ENUMERATION]{GREEN}Golang installation is done !{GREEN}\n")
    except subprocess.CalledProcessError as e:
        print(f"Error while installing Go: {e}")


def install_metabigor():
    try:
        # Install metabigor
        subprocess.run(["go", "install", "github.com/j3ssie/metabigor@latest"])

        # Get the user's home directory
        home_directory = os.path.expanduser("~")

        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")

        # Now you are in the ~/root/go/bin directory
        print(f"Current directory: {go_bin_directory}")
        
        # Copiez le binaire résultant dans /usr/local/bin
        metabigor_binary = os.path.join(go_bin_directory,"metabigor")
        subprocess.run(["sudo", "cp", metabigor_binary, "/usr/local/bin"])

        print("Metabigor has been installed.")
    except Exception as e:
        print(f"An error occurred while installing Metabigor : {str(e)}")
    

def install_SecretFinder(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing SecretFinder now...{CYAN}")       
        # Navigate to the tools directory
        tools_dir = tools_directory()
        os.chdir(tools_dir)
        # Clone SecretFinder repository
        os.system('git clone https://github.com/m4ll0k/SecretFinder.git > /dev/null 2>&1')        
        # Navigate to SecretFinder directory
        secretfinder_directory = os.path.join(tools_dir, 'SecretFinder')
        os.chdir(secretfinder_directory)
        # Install Python requirements
        os.system('pip3 install -r requirements.txt > /dev/null 2>&1')
        os.system('pip3 install jsbeautifier > /dev/null 2>&1')
        os.system('pip3 install lxml > /dev/null 2>&1')
        os.chdir(tools_dir)
        
        print_success(f"{GREEN}[SUCCESS]SecretFinder has been installed.")
    except Exception as e:
        print_error(f"{RED}An error occurred while installing SecretFinder: {str(e)}")

def install_amass():
    try :
        # Install Amass using Go
        print(f"{CYAN}[INFO] Installing amass...{CYAN}")
        subprocess.run(["go", "install", "-v", "github.com/owasp-amass/amass/v4/...@master"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")

        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")

        # Copiez le binaire résultant dans /usr/local/bin
        amass_binary = os.path.join(go_bin_directory,"amass")
        subprocess.run(["sudo", "cp", amass_binary, "/usr/local/bin"])

        print(f"{GREEN}[SUCCESS]amass has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] amass installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_assetfinder():
    try:
        print(f"{CYAN}[INFO] Installing assetfinder...{CYAN}")
        subprocess.run(["go", "install", "github.com/tomnomnom/assetfinder@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")

        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")

        # Copiez le binaire résultant dans /usr/local/bin
        assetfinder_binary = os.path.join(go_bin_directory,"assetfinder")
        subprocess.run(["sudo", "cp", assetfinder_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS]assetfinder has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] assetfinder installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_subfinder():
    try:
        # Install subfinder using go
        print(f"{CYAN}[INFO] Installing subfinder...{CYAN}")
        subprocess.run(["go", "install", "-v", "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")

        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")

        # Copiez le binaire résultant dans /usr/local/bin
        subfinder_binary = os.path.join(go_bin_directory,"subfinder")
        subprocess.run(["sudo", "cp", subfinder_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS]subfinder has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] subfinder installation failed. Please check the Go installation and build process : {str(e)}{RED}")
  
def install_shuffledns():
    try :
        print(f"{CYAN}[INFO] Installing shuffledns...{CYAN}")
        subprocess.run(["go", "install", "-v", "github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest"])
        
        # Get the user's home directory
        home_directory = os.path.expanduser("~")

        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")

        # Copiez le binaire résultant dans /usr/local/bin
        shuffledns_binary = os.path.join(go_bin_directory,"shuffledns")
        subprocess.run(["sudo", "cp", shuffledns_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] shuffledns has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] shuffledns installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_github_subdomains():
    try:
        print(f"{CYAN}[INFO] Installing github_subdomains...{CYAN}")
        subprocess.run(["go", "install", "github.com/gwen001/github-subdomains@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")

        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")

        # Copiez le binaire résultant dans /usr/local/bin
        github_subdomains_binary = os.path.join(go_bin_directory,"github-subdomains")
        subprocess.run(["sudo", "cp", github_subdomains_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] github-subdomains has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] github-subdomains installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_ffuf():
    try:
        print(f"{CYAN}[INFO]{END} Installing ffuf...")
        subprocess.run(["go", "install", "github.com/ffuf/ffuf@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        ffuf_binary = os.path.join(go_bin_directory,"ffuf")
        subprocess.run(["sudo", "cp", ffuf_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] ffuf has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] ffuf installation failed. Please check the Go installation and build process : {str(e)}{RED}")    

def install_BBoT(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing BBoT now...{CYAN}")
        # Clone BBoT repository (replace with the actual BBoT repository URL)
        os.system('git clone https://github.com/blacklanternsecurity/bbot.git > /dev/null 2>&1')
        # Perform the installation steps for BBoT
        print_success(f"{GREEN}[SUCCESS] BBoT has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR] An error occurred while installing BBoT: {str(e)}{RED}")

def install_haktrails():
    try:
        print(f"{CYAN}[INFO] Installing haktrails now...{CYAN}")
        subprocess.run(["go", "install", "-v", "github.com/hakluke/haktrails@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")

        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")

        # Copiez le binaire résultant dans /usr/local/bin
        haktrails_binary = os.path.join(go_bin_directory,"haktrails")
        subprocess.run(["sudo", "cp", haktrails_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] haktrails has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] haktrails installation failed. Please check the Go installation and build process : {str(e)}{RED}") 

def install_httpx():
    try:
        print(f"{CYAN}[INFO] Installing HTTPX now...{CYAN}")
        subprocess.run(["go", "install", "github.com/projectdiscovery/httpx/cmd/httpx@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        httpx_binary = os.path.join(go_bin_directory,"httpx")
        subprocess.run(["sudo", "cp", httpx_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] HTTPX has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] HTTPX installation failed. Please check the Go installation and build process : {str(e)}{RED}") 

def install_naabu():
    try:
        print(f"{CYAN}[INFO] Installing naabu now...{CYAN}")
        subprocess.run(["go", "install", "-v", "github.com/projectdiscovery/naabu/v2/cmd/naabu@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")

        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")

        # Copiez le binaire résultant dans /usr/local/bin
        naabu_binary = os.path.join(go_bin_directory,"naabu")
        subprocess.run(["sudo", "cp", naabu_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] naabu has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] naabu installation failed. Please check the Go installation and build process : {str(e)}{RED}")


def install_brutespray(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing brutespray now...{CYAN}")
        # Clone SecretFinder repository
        os.system('git clone https://github.com/x90skysn3k/brutespray.git > /dev/null 2>&1')
        # Install Python requirements
        os.system('pip install -r requirements.txt > /dev/null 2>&1')
        print_success(f"{GREEN}[SUCCESS]brutespray has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing brutespray: {str(e)}{RED}")

def install_gau():
    try:
        print(f"{CYAN}[INFO]gau is not installed. Installing gau now...{CYAN}")
        subprocess.run(["go", "install", "github.com/lc/gau/v2/cmd/gau@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")

        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")

        # Copiez le binaire résultant dans /usr/local/bin
        gau_binary = os.path.join(go_bin_directory,"gau")
        subprocess.run(["sudo", "cp", gau_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] gau has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] gau installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_katana():
    try:
        print(f"{CYAN}[INFO] Installing Katana now...{CYAN}")
        subprocess.run(["go", "install", "github.com/projectdiscovery/katana/cmd/katana@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        Katana_binary = os.path.join(go_bin_directory,"Katana")
        subprocess.run(["sudo", "cp", Katana_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] Katana has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] Katana installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_gitleaks(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing gitleaks now...{CYAN}")
        # Clone gitleaks repository
        os.system('git clone https://github.com/zricethezav/gitleaks.git > /dev/null 2>&1')        
        # Install  
        os.system('make build')
        print_success(f"{GREEN}[SUCCESS]gitleaks has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing gitleaks: {str(e)}{RED}")

def install_trufflehog(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing trufflehog now...{CYAN}")
        # Clone trufflehog repository
        os.system('git clone https://github.com/trufflesecurity/trufflehog.git > /dev/null 2>&1')       
        # Navigate to trufflehog directory
        tools_dir = tools_directory
        trufflehog_directory = os.path.join(tools_dir, 'trufflehog')
        os.chdir(trufflehog_directory)
        # Install  
        os.system('go install')
        print_success(f"{GREEN}[SUCCESS]trufflehog has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing trufflehog: {str(e)}{RED}")

def install_dirsearch(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing dirsearch now...{CYAN}")
        # Clone dirsearch repository
        os.system('git clone https://github.com/maurosoria/dirsearch.git > /dev/null 2>&1')     
        # Install  
        os.system('chmod +x dirsearch/dirsearch.py')
        print_success(f"{GREEN}[SUCCESS] dirsearch has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing dirsearch: {str(e)}{RED}")

def install_gobuster():
    try:
        print(f"{CYAN}[INFO] Gobuster is not installed. Installing Gobuster now...{CYAN}")
        subprocess.run(["go", "install", "github.com/OJ/gobuster/v3@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        Gobuster_binary = os.path.join(go_bin_directory,"gobuster")
        subprocess.run(["sudo", "cp", Gobuster_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] Gobuster has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] Gobuster installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_nuclei():
    try:
        print(f"{CYAN}[INFO] Nuclei is not installed. Installing Nuclei now...{CYAN}")
        subprocess.run(["go", "install", "github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        nuclei_binary = os.path.join(go_bin_directory,"nuclei")
        subprocess.run(["sudo", "cp", nuclei_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] nuclei has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] nuclei installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_gf():
    try:
        print(f"{CYAN}[INFO] Installing GF now...{CYAN}")
        subprocess.run(["go", "install", "github.com/tomnomnom/gf@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        GF_binary = os.path.join(go_bin_directory,"gf")
        subprocess.run(["sudo", "cp", GF_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] GF has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] GF installation failed. Please check the Go installation and build process : {str(e)}{RED}")


def install_asnmap():
    try:
        print(f"{CYAN}[INFO] Installing Asnmap now...{CYAN}")
        subprocess.run(["go", "install", "github.com/projectdiscovery/asnmap/cmd/asnmap@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        asnmap_binary = os.path.join(go_bin_directory,"asnmap")
        subprocess.run(["sudo", "cp", asnmap_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] asnmap has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] asnmap installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_jsleak():
    try:
        print(f"{CYAN}[INFO]Jsleak is not installed. Installing Jsleak now...{CYAN}")
        subprocess.run(["go", "install", "github.com/channyein1337/jsleak@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        jsleak_binary = os.path.join(go_bin_directory,"jsleak")
        subprocess.run(["sudo", "cp", jsleak_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] jsleak has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] jsleak installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_mapcidr():
    try:
        print(f"{CYAN}[INFO] Installing Mapcidr now...{CYAN}")
        subprocess.run(["go", "install", "github.com/projectdiscovery/mapcidr/cmd/mapcidr@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        mapcidr_binary = os.path.join(go_bin_directory,"mapcidr")
        subprocess.run(["sudo", "cp", mapcidr_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] mapcidr has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] mapcidr installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_dnsx():
    try:
        print(f"{CYAN}[INFO] Dnsx is not installed. Installing Dnsx now...{CYAN}")
        subprocess.run(["go", "install", "github.com/projectdiscovery/dnsx/cmd/dnsx@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        dnsx_binary = os.path.join(go_bin_directory,"dnsx")
        subprocess.run(["sudo", "cp", dnsx_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] dnsx has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] dnsx installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_gospider():
    try:
        print(f"{CYAN}[INFO]Gospider is not installed. Installing Gospider now...{CYAN}")
        subprocess.run(["go", "install", "github.com/jaeles-project/gospider@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        gospider_binary = os.path.join(go_bin_directory,"gospider")
        subprocess.run(["sudo", "cp", gospider_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] gospider has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] gospider installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_crlfuzz():
    try:
        print(f"{CYAN}[INFO] CRLFuzz is not installed. Installing CRLFuzz now...{CYAN}")
        subprocess.run(["go", "install", "github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        crlfuzz_binary = os.path.join(go_bin_directory,"crlfuzz")
        subprocess.run(["sudo", "cp", crlfuzz_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] crlfuzz has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] crlfuzz installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_uncover():
    try:
        print(f"{CYAN}[INFO] Installing Uncover now...{CYAN}")
        subprocess.run(["go", "install", "github.com/projectdiscovery/uncover/cmd/uncover@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        uncover_binary = os.path.join(go_bin_directory,"uncover")
        subprocess.run(["sudo", "cp", uncover_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] Uncover has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] Uncover installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_dalfox():
    try:
        print(f"{CYAN}[INFO] Installing Dalfox now...{CYAN}")
        subprocess.run(["go", "install", "github.com/hahwul/dalfox/v2@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        dalfox_binary = os.path.join(go_bin_directory,"dalfox")
        subprocess.run(["sudo", "cp", dalfox_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] Dalfox has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] Dalfox installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_getjs():
    try:
        print(f"{CYAN}[INFO] Installing getJS now...{CYAN}")
        subprocess.run(["go", "install", "github.com/003random/getJS@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        getJS_binary = os.path.join(go_bin_directory,"getJS")
        subprocess.run(["sudo", "cp", getJS_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] getJS has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] getJS installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_socialhunter():
    try:
        print(f"{CYAN}[INFO] Installing SocialHunter now...{CYAN}")
        subprocess.run(["go", "install", "github.com/utkusen/socialhunter@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")
        # Copiez le binaire résultant dans /usr/local/bin
        socialhunter_binary = os.path.join(go_bin_directory,"socialhunter")
        subprocess.run(["sudo", "cp", socialhunter_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] socialhunter has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] socialhunter installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_paramspider(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing ParamSpider now...{CYAN}")
        # Clone ParamSpider repository
        os.system('git clone https://github.com/devanshbatham/ParamSpider.git > /dev/null 2>&1')      
        # Install Python requirements
        os.system('pip3 install -r requirements.txt > /dev/null 2>&1')
        print_success(f"{GREEN}[SUCCESS]ParamSpider has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing ParamSpider: {str(e)}{RED}")

def install_nosqlmap(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing NoSQLMap now...{CYAN}")
        # Clone NoSQLMap repository
        os.system('git clone https://github.com/codingo/NoSQLMap.git > /dev/null 2>&1')        
        # Install Python requirements
        os.system('pip3 install -r requirements.txt > /dev/null 2>&1')
        print_success(f"{GREEN}[SUCCESS]NoSQLMap has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing NoSQLMap: {str(e)}{RED}")

def install_jwt_tool(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing jwt_tool now...{CYAN}")
        # Clone jwt_tool repository
        os.system('git clone https://github.com/ticarpi/jwt_tool.git > /dev/null 2>&1')        
        # Install Python requirements
        os.system('python3 -m pip install termcolor cprint pycryptodomex requests > /dev/null 2>&1')
        os.system('chmod +x jwt_tool.py')
        print_success(f"{GREEN}[SUCCESS]jwt_tool has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing jwt_tool: {str(e)}{RED}")

def install_arjun(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing Arjun now...{CYAN}")
        # Clone Arjun repository
        os.system('git clone https://github.com/s0md3v/Arjun.git > /dev/null 2>&1')        
        # Install Python requirements
        os.system('python3 setup.py install > /dev/null 2>&1')
        print_success(f"{GREEN}[SUCCESS] Arjun has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing Arjun: {str(e)}{RED}")

def install_http_request_smuggling(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing http-request-smuggling now...{CYAN}")
        # Clone http-request-smuggling repository
        os.system('git clone https://github.com/anshumanpattnaik/http-request-smuggling.git > /dev/null 2>&1')       
        # Install Python requirements
        os.system('pip3 install -r requirements.txt > /dev/null 2>&1')
        print_success(f"{GREEN}[SUCCESS] http-request-smuggling has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing http-request-smuggling: {str(e)}{RED}")

def install_commix(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing commix now...{CYAN}")
        # Clone commix repository
        os.system('git clone https://github.com/commixproject/commix.git > /dev/null 2>&1')        
        print_success(f"{GREEN}[SUCCESS] commix has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing commix: {str(e)}{RED}")

def install_graphqlmap(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing GraphQLmap now...{CYAN}")
        # Clone GraphQLmap repository
        os.system('git clone https://github.com/swisskyrepo/GraphQLmap.git > /dev/null 2>&1')        
        # Install Python requirements
        os.system('python3 setup.py install > /dev/null 2>&1')
        print_success(f"{GREEN}[SUCCESS] GraphQLmap has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing GraphQLmap: {str(e)}{RED}")

def install_whatweb(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing WhatWeb now...{CYAN}")
        # Clone WhatWeb repository
        os.system('git clone https://github.com/urbanadventurer/WhatWeb.git > /dev/null 2>&1')       
        # Install Python requirements
        os.system('gem install bundler > /dev/null 2>&1')
        os.system('bundle update  > /dev/null 2>&1')
        os.system('bundle install  > /dev/null 2>&1')
        print_success(f"{GREEN}[SUCCESS] WhatWeb has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing WhatWeb: {str(e)}{RED}")

def install_golinkfinder(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing GoLinkFinder now...{CYAN}")
        #Clone GoLinkFinder repository
        subprocess.run(['git clone https://github.com/0xsha/GoLinkFinder.git  > /dev/null 2>&1'])     
        print(f"{GREEN}[SUCCESS] GoLinkFinder has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] GoLinkFinder installation failed. Please check the Go installation and build process : {str(e)}{RED}")


def install_osmedeus():
    try:
        print(f"{CYAN}[INFO] Installing osmedeus now...{CYAN}")
        subprocess.run(["go", "install", "-v", "github.com/j3ssie/osmedeus@latest"])
        # Get the user's home directory
        home_directory = os.path.expanduser("~")

        # Define the path to the ~/root/go/bin directory
        go_bin_directory = os.path.join(home_directory, "go", "bin")

        # Copiez le binaire résultant dans /usr/local/bin
        osmedeus_binary = os.path.join(go_bin_directory,"osmedeus")
        subprocess.run(["sudo", "cp", osmedeus_binary, "/usr/local/bin"])
        print(f"{GREEN}[SUCCESS] osmedeus has been installed.{GREEN}")
    except Exception as e:
        print(f"{RED}[ERROR] osmedeus installation failed. Please check the Go installation and build process : {str(e)}{RED}")

def install_xnlinkfinder(tools_directory):  
    try:
        print(f"{CYAN}[INFO] Installing xnLinkFinder now...{CYAN}")
        # Clone xnLinkFinder repository
        os.system('git clone https://github.com/xnl-h4ck3r/xnLinkFinder.git > /dev/null 2>&1')       
        # Install Setup Installation
        os.system('python3 setup.py install > /dev/null 2>&1')
        print_success(f"{GREEN}[SUCCESS] xnLinkFinder has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing xnLinkFinder: {str(e)}{RED}")

def install_dontgo403(tools_directory):
    try:
        print(f"{CYAN}[INFO] Installing dontgo403 now...{CYAN}")
        # Clone dontgo403 repository
        os.system('git clone https://github.com/devploit/dontgo403.git > /dev/null 2>&1')        
        # Install Setup Installation
        os.system('go get > /dev/null 2>&1')
        os.system('go build > /dev/null 2>&1')
        print_success(f"{GREEN}[SUCCESS] dontgo403 has been installed.{GREEN}")
    except Exception as e:
        print_error(f"{RED}[ERROR]An error occurred while installing dontgo403: {str(e)}{RED}")
# 7 : Download Nuclei templates
def install_nuclei_templates(templates_directory):
    user_choice = input("Do you want to download and install Nuclei templates? (yes/no): ").lower()
    
    if user_choice == "yes":
        print(f"{CYAN}[INFO] Downloading Nuclei templates now...{CYAN}")
        # Navigate to the templates directory
        os.chdir(templates_directory)
        # Clone Nuclei templates repository
        os.system('git clone https://github.com/projectdiscovery/nuclei-templates.git > /dev/null 2>&1')
        print(f"{GREEN}[SUCCESS] Nuclei templates download complete.{GREEN}")
    else:
        print(f"{YELLOW} Skipping Nuclei templates download.{YELLOW}")
# 6 : Install tools

def install_tools():
    tools = [
        "metabigor", "SecretFinder", "amass", "assetfinder", "subfinder",
        "shuffledns", "github_subdomains", "ffuf", "bbot", "haktrails",
        "httpx", "eyewitness", "naabu", "brutespray", "gau", "katana",
        "gitleaks", "trufflehog", "dirsearch", "gobuster", "nuclei", "gf",
        "asnmap", "jsleak", "mapcider", "dnsx", "gospider", "wpscan",
        "crlfuzz", "uncover", "dalfox", "getjs", "socialhunter", "paramspider",
        "nosqlmap", "jwt_tool", "arjun", "graphqlmap", "whatweb",
        "golinkfinder", "xnlinkfinder", "dontgo403", "nuclei_template"
    ]
    tools_directory = create_tools_directory

    for tool in tools:
        user_choice = input(f"Do you want to install {tool}? (yes/no): ").lower()
        if user_choice == "yes":
            if tool == "metabigor":
                install_metabigor()
            elif tool == "SecretFinder":
                install_SecretFinder(tools_directory)
            elif tool == "amass" :
                install_amass()
            elif tool == "assetfinder":
                install_assetfinder()
            elif tool == "subfinder":
                install_subfinder()
            elif tool == "shuffledns":
                install_shuffledns()
            elif tool == "github_subdomains":
                install_github_subdomains()
            elif tool == "ffuf":
                install_ffuf()
            elif tool == "bbot":
                install_BBoT(tools_directory)
            elif tool == "haktrails":
                install_haktrails()
            elif tool == "httpx":
                install_httpx()
            elif tool == "naabu":
                install_naabu()
            elif tool == "brutespray":
                install_brutespray(tools_directory)
            elif tool == "gau":
                install_gau()
            elif tool == "katana":
                install_katana()
            elif tool == "gitleaks":
                install_gitleaks(tools_directory)
            elif tool == "trufflehog":
                install_trufflehog(tools_directory)
            elif tool == "dirsearch":
                install_dirsearch(tools_directory)
            elif tool == "gobuster":
                install_gobuster()
            elif tool == "nuclei":
                install_nuclei()
            elif tool == "gf":
                install_gf()
            elif tool == "asnmap":
                install_asnmap()
            elif tool == "jsleak":
                install_jsleak()
            elif tool == "mapcider":
                install_mapcidr()
            elif tool == "dnsx":
                install_dnsx()
            elif tool == "gospider":
                install_gospider()
            elif tool == "crlfuzz":
                install_crlfuzz()
            elif tool == "uncover":
                install_uncover()
            elif tool == "dalfox":
                install_dalfox()
            elif tool == "getjs":
                install_getjs()
            elif tool == "socialhunter":
                install_socialhunter()
            elif tool == "paramspider":
                install_paramspider(tools_directory)
            elif tool == "nosqlmap":
                install_nosqlmap(tools_directory)
            elif tool == "jwt_tool":
                install_jwt_tool(tools_directory)
            elif tool == "arjun":
                install_arjun(tools_directory)
            elif tool == "http_request_smuggling":
                install_http_request_smuggling(tools_directory)
            elif tool == "commix":
                install_commix(tools_directory)
            elif tool == "graphqlmap":
                install_graphqlmap(tools_directory)
            elif tool == "whatweb":
                install_whatweb(tools_directory)
            elif tool == "golinkfinder":
                install_golinkfinder(tools_directory)
            elif tool == "osmedeus":
                install_osmedeus()
            elif tool == "xnlinkfinder":
                install_xnlinkfinder(tools_directory)
            elif tool == "dontgo403":
                install_dontgo403(tools_directory)
            elif tool == "nuclei_template":
                install_nuclei_templates()
        elif user_choice == "no":
            print(f"Skipping {tool} installation.")

# Step 4: Install wordlists from github_subdomains GitHub
#def install_wordlists(wordlists_directory):
    #wordlists_directory = create_wordlists_directory
    #user_choice = input("Do you want to install wordlists from GitHub? (yes/no): ").lower()
    #if user_choice == "yes":
        #print(f"{CYAN}[INFO] Download wordlist now .... {CYAN}")
        # Navigate to the tools directory{tool}
        #os.chdir(wordlists_directory)
        #os.system('git clone url github > /dev/null 2>&1')
        #print(f"{GREEN}[SUCCESS] Wordlists  Download complete.{GREEN}")
    #else: print(f"{YELLOW} Skipping Wordlists  Download.{YELLOW}")


# 8 : Exit
def exit_script():
    print("Exiting the script...")
    exit()

# Main function
def main():
    create_tools_directory()
    install_requirements()
    install_go()
    install_tools()
    #install_wordlists()
    templates_directory = create_Nuclei_Templates_directory()
    install_nuclei_templates(templates_directory)
    exit_script()

if __name__ == "__main__":
    main()