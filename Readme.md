Bug_Bounty Deep Reconnaissance

------------------------------
------------------------------
This Roadmap For BugBounty or Penetration Testing a comprehensive overview of the reconnaissance activities conducted during the bug bounty program. The aim of the reconnaissance phase was to identify potential attack surfaces, subdomains, vulnerabilities, and possible areas of exploitation.

------------------------------
Table of Contents
``````
    Acquisitions

    ASN

    Seeds

    Shodan.io

    Cloud

    Subdomains Discovery

    Subdomain Enumeration

    Duplicate Subdomains Resolution

    Port Analysis

    Alive Subdomains

    Screenshot

    Dorking

    Subdomain Take Over
``````
The reconnaissance phase provided valuable insights into the target's attack surface, potential vulnerabilities, and areas of focus for further testing. 
The information collected through various tools and techniques will be instrumental in planning and executing subsequent phases of the bug bounty program.

-----------------------------------------
-------------------------------------------
### DeeP_RecoN:

------------------------------------------

- [ ] Find Acquisitions:

[Crunchbase](https://www.crunchbase.com/)

- [ ] ASN:

Manually:

[BGP.he.net](https://bgp.he.net)

[ARIN Whois](https://whois.arin.net/ui/query.do)

[Domain Research Suite](https://tools.whoisxmlapi.com/)

Automated:

[metabigor](https://github.com/j3ssie/metabigor): 
``````
echo 'ASN_NUMBER' | metabigor net --asn -o asn
``````
[Amass](https://github.com/owasp-amass/amass): 
``````
amass intel --asn [ASN NUMBER]
``````
- [ ] Find Seeds:

[Builtwith](https://builtwith.com/):

    Check the website with the BuiltWith extension: Go to Relationship BuiltWith

[WHOXY](https://www.whoxy.com)

[DomLink](https://github.com/vysecurity/DomLink) : 
``````
python domLink.py -D  {domain.com} -o target.out.txt
``````
- [ ] CLOUD:

[SNI-IP-Ranges](https://kaeferjaeger.gay/?dir=sni-ip-ranges)

Extract using commands...  :
``````
 cat  *.txt | grep "\.Target\.com" | awk -F'-- ' '{print $2}'| tr ' ' '\n' | tr '[' ' ' | sed 's/ //' | sed 's/\]//' 
``````
- [ ] Find Subdomains:

Client-Side Linked Discovery:

[LinkFinder](https://github.com/GerbenJavado/LinkFinder):
``````
python3 linkfinder.py -i {Path of js Domain} -d 2 -r "https?://(www\.)?example\.com" -o cli
``````
[SecretFinder](https://github.com/m4ll0k/SecretFinder):
``````
python3 SecretFinder.py -i {Path of js Domain} -o cli >> secretfinder.txt
``````
Add Regex:
``````
{
    "URLs": [
        "\\bhttps?://[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}\\b",
        "\\b(?:http|ftp)s?://\\S+\\b"
    ]
}
``````
[Burpsuite Pro](https://portswigger.net/burp/pro):

    Turn on Passive Scan

- [ ] Subdomains Enumeration:

Infrastructure Source:

[Censys](https://search.censys.io/)

[DNS Dumpster](https://dnsdumpster.com/)

[Web Archive](https://web.archive.org/)

[Shodan](https://www.shodan.io/)

[SecurityTrails](https://securitytrails.com/)

[Subdomain finder C99](http://subdomainfinder.c99.nl/)

Certificate Sources:

[CRT.sh](https://crt.sh/)

[SSLMate Certspotter](https://sslmate.com/certspotter/)

Security Sources:

[VirusTotal](https://www.virustotal.com/gui/)

Tools:

[Amass](https://github.com/owasp-amass/amass): 
``````
amass enum -passive -norecursive -noalts -d {target_domain} -o amass.txt
``````
BRUTE FORCING: 
``````
amass enum -brute -d {target_domain} -rf
``````
[Assetfinder](https://github.com/tomnomnom/assetfinder): 
``````
echo {target_domain} | assetfinder --subs-only | tee assetfinder.txt
``````
[Subfinder](https://github.com/projectdiscovery/subfinder): 
``````
subfinder -d {target_domain} -o subfinder.txt
``````
[Shuffledns](https://github.com/projectdiscovery/shuffledns): 
``````
shuffledns -d [DOMAIN] -w wordlist.txt -r resolvers.txt >> shuffledns.txt
``````
[Github-subdomains](https://github.com/gwen001/github-subdomains): 
``````
python github-subdomains.py --organization <organization_name> --token <your_github_token> >> git_subd.txt
``````
[FFUF](https://github.com/ffuf/ffuf) : 
``````
ffuf -u https://FUZZ.{target_domain} -w /usr/share/wordlists/dirb/common.txt -p 1 -o ffuf_subdom.txt
``````
[BBOT](https://github.com/blacklanternsecurity/bbot): 
``````
bbot -t {target_domain} -f subdomain-enum >> bbot.txt
``````
[Script_autom]() :
``````
[ python recon.py ]: Enumerated and Collected subdomains + unique subdomains and Resolve duplicate + Check alive or statut 200
``````
[haktrails](https://github.com/hakluke/haktrails) + [hakrawler](https://github.com/hakluke/hakrawler) : 
``````
echo {target_domain} | haktrails subdomains | hakrawler hak.txt‌
``````
- [ ] Resolve & Check Alive:

[httpx](https://github.com/projectdiscovery/httpx) : 
``````
httpx -l Input_file_sub.txt -o active_sub.txt -threads 200 -status-code -follow-redirects | tee alive_sub.txt
``````
- [ ] Screenshot:

[EyeWitness](https://github.com/RedSiege/EyeWitness) : 
``````
./EyeWitness -f alive.txt --web
``````
- [ ] Port Analysis:

[masscan](https://github.com/robertdavidgraham/masscan): 
``````
masscan -p1-65535 -iL list.txt --rate 10000 | sort -u >> results.txt
``````
[nmap](https://nmap.org/):
`````` 
nmap -p- -iL list.txt -oN results.txt
``````
[naabu](https://github.com/projectdiscovery/naabu): 
``````
naabu -list list.txt -top-ports 1000 -exclude-ports 80,443,21,22,25 -o ports.txt
``````
CHECK FOR DEFAULT CREDS:

[brutespray](https://github.com/x90skysn3k/brutespray): 
``````
python brutespray.py -h <TARGET_IP_FILE> -U <USER_LIST> -P <PASS_LIST> -s <SERVICE>
``````
- [ ] Collecting URL Endpoint:

[Burpsuite Pro]() : Automate Web Crawling {Crawl} // manually

[Gau](https://github.com/lc/gau) : 
``````
for i in $(cat alive_sub.txt); do gau $i | egrep -vE "\.(woff|woff2|ttf|toff|eot|webp|gif|tiff|bmp|wav|png|jpg|jpeg|svg|ico|css|mp4|m4v)" | httpx -silent -fc 404 | tee -a domain-archive.txt; done
``````
Find Endpoint in JS files :

[katana](https://github.com/projectdiscovery/katana) : 
``````
katana -u https://{target_domain} --js-crawl -d 5 -hl -field endpoint | anew endpoint.txt
``````
[hakrawler](https://github.com/hakluke/hakrawler) : 
``````
echo {target_domain} / cat urls.txt | hakrawler
``````
[Brute Forcing]() : 
``````
ffuf -w wordlist -u {target_domain/FUZZ}
``````
[ ] Search for {drive.google / docs.google / document}:
``````
cat alive_sub.txt | katana -silent | while read url; do cu=$(curl -s $url | grep -E'(drive.google|docs.google|spreadsheet\/d|document.\/d\/)';echo -e "==> $url" "\n"" $cu";done
``````
- [ ] Dorking:

[Google Dorking](https://www.google.com) :

Leaked credentials on Google :
``````
site:docs.Google.com/spreadsheets "company name"
``````
``````
site:groups.Google.com "company name"
``````


Find Sensitive Data in Cloud Storage :

``````
site:http://s3.amazonaws.com "{target_domain}"
``````
``````
site:http://blob.core.windows.net "{target_domain}"
``````
``````
site:http://googleapis.com "{target_domain}"
``````
``````
site:http://drive.google.com "{target_domain}"
``````
``````
 #exclued add  -www / -example .....
 #show me in the URL  inurl:api /inurl:v1 /login...
 #show me in the title  intitle:login
 #Looking for File Type  filetype:pdf /filetype:pdf / filetype:txt / filetype:php
 #search extension  ext:php /ext:aspx /....
 #look for every parameter  inurl:"&"
 #look for keyword name  inurl:"name"
``````
[Shodan Dorking]() :
``````
ssl:"target[.]com" 200 http.title:"dashboard" --unauthenticated dashboard
``````
``````
org:"{target_domain}  " x-jenkins 200 --- unauthenticated jenkins server
``````
``````
ssl:"{target_domain} " 200 proftpd port:21 --- proftpd port:21 org:"{target_domain} "
``````
``````
http.html:zabbix ---CVE-2022-24255 Main & Admin Portals : Authentication
``````
``````
Bypass org:"{target_domain} " http.title:"phpmyadmin" --- PHP My Admin
``````
``````
ssl:"{target_domain} " http.title:"BIG-IP --- F5 BIG-IP using CVE-2020-5902
``````
[Github Dorking]() :

Find endpoints and subdomains

Make custom wordlists for each target based on technologies discovered

    After searching, check "Languages for scripting languages"
    Check for recently submitted repos
    Identify users that work at the organization but are not listed under the Org's main repo (look for them on Linkedin to confirm)

Search Queries :

``````
filename:config.json
``````
``````
filename:secrets
``````
``````
filename:.env
``````
``````
filename:docker-compose.yml
``````
``````
filename:aws_keys
``````
``````
filename:.pem
``````
``````
filename:.gitconfig
``````
``````
filename:database.yml
``````
``````
filename:oauth
``````
``````
filename:slack_token
``````
``````
filename:prod.exs
``````

GitHub Dorking Tools:

[gitleaks](https://github.com/gitleaks/gitleaks) : 
``````
finding secrets and sensitive files in Git repositories
``````
[trufflehog](https://github.com/trufflesecurity/trufflehog) : 
``````
searches for sensitive data in code and commits
``````
[gitrob](https://github.com/michenriksen/gitrob) : 
``````
scan GitHub repositories for sensitive files and information
``````
[shhgit](https://github.com/eth0izzle/shhgit) : 
``````
identifying secrets and sensitive files across GitHub
``````
- [ ] Find Source / Backups Files:

subdomain.target.com :
``````
subdomain.target.com/subdomain.zip - target.zip - admin.zip - backup.zip
``````
``````
subdomain.target.com/subdomain/subdomain.zip - target.zip - admin.zip - backup.zip
``````
``````
subdomain.target.com/target/subdomain.zip - target.zip - admin.zip - backup.zip
``````
``````
subdomain.target.com/admin/subdomain.zip - target.zip - admin.zip - backup.zip
``````

[dirsearch](https://github.com/maurosoria/dirsearch) :
``````
dirsearch -u https://{target_domain} -e php,html,js,css,txt,log,old,inc,backup,bak,swp,zip,tar.gz,tar,sql -w /usr/share/wordlists/dirb/common.txt -x 403,404 -t 50 -r -o results.txt
``````
[gobuster](https://github.com/OJ/gobuster):
``````
gobuster dir -u https://{target_domain} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .php,.html,.js,.css,.txt,.log,.old,.inc,.backup,.bak,.swp,.zip,.tar.gz,.tar,.sql -t 50 -r -o results.txt
``````
[fuzzuli](https://github.com/musana/fuzzuli):
``````
fuzzuli -f alive_sub.txt -w 32 -ex .rar,.zip,.tar.gz,.7z,backup,log,txt,old -p
``````
- [ ] Subdomain Take Over:

[can-i-take-over-xyz](https://github.com/EdOverflow/can-i-take-over-xyz) : 
``````
    1/Go to the repository and access the list of vulnerable domains.
    2/ Browse the list to find potential takeover candidates.
    3/ Manually assess the domains to see if they are indeed vulnerable and if they can be taken over.
``````

[SubOver](https://github.com/Ice3man543/SubOver) : 
``````
python3 subover.py -l subdomains.txt
``````
[nuclei](https://github.com/projectdiscovery/nuclei) : 
``````
nuclei -t takeovers -l subdomains.txt
``````
-------------------------------------
-------------------------------------


#### Note :
``````
    Remember, this roadmap is meant to be used responsibly and legally, with proper authorization. 
    Dive into the world of deep reconnaissance and strengthen your bug bounty and penetration testing capabilities with this comprehensive guide. 
 
``````

[My Github ](https://github.com/TNRooT)
                
[My Youtube Channel](https://youtube.com/@The_Ethical_TN)

Author: [RooT0x2TN]