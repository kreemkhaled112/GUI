from pages_functions.__init__ import *
class Name:
    def __init__(self,url) :
        self.req = requests.Session()
        self.req.headers.update(Header_www())
        self.url = url
    def Start(self):
        try:  
            response = self.req.get( self.url )
            name = re.search(r'<title>(.*?)</title>', response.text).group(1)
            return name
        except :
            open("html.html" , "w" , encoding="utf-8").write(response.text)
            return ""
class Get_Name:
    def __init__(self, cookie) :
        self.req = requests.Session()
        self.req.headers.update(Header())
        self.cookie = cookie
        cookie = cookie_format(cookie)
        self.req.cookies.update(cookie)
    def Get(self):
        try:
            response = self.req.get( 'https://mbasic.facebook.com/profile.php?')
            name = re.search(r'<title>(.*?)</title>', response.text).group(1)
            cookie_string = (';'.join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items() ])).replace("cookie=", "").strip()
            if name == "" :
                return "CheckPoint" , cookie_string
            return name , cookie_string
        except :
            return ""
class Get_i_user:
    def __init__(self , cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update(Header())
        self.cookie = cookie
        cookie = cookie_format(cookie)
        self.req.cookies.update(cookie)
    def Get(self):
        try:
            response = self.req.get( 'https://www.facebook.com/profile.php?' )
            id_index_start = response.text.find('"id":"', response.text.find('{"profile":{"id":"')) + len('"id":"')
            id_index_end = response.text.find('"', id_index_start)
            profile_id = response.text[id_index_start:id_index_end]
            cookie = f"{self.cookie};i_user={profile_id};"
            return "success" , cookie , Get_Name(cookie).Get()
        except : return "" 
class Allow():
    def __init__(self,soup,cookie):
        try:
            headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1',
            'origin': 'https://mbasic.facebook.com',
            'priority': 'u=0, i',
            'referer': 'https://mbasic.facebook.com/privacy/consent_framework/prompt/?consent_flow_name=user_cookie_choice&consent_entry_source=pft_user_cookie_choice&consent_extra_params%5Bpft_surface%5D=facebook_mbasic&consent_extra_params%5Bpft_gk%5D=epd_cookies_baseline_4_mbasic&consent_extra_params%5Bpft_gk_pass%5D=true&consent_extra_params%5Bpft_vc%5D=%7B%22type%22%3A%22FBViewerContext%22%2C%22is_omni%22%3A0%2C%22viewer_id%22%3A61561081676305%2C%22app_id%22%3A0%7D&consent_surface=facebook_mbasic&paipv=0&eav=Afa9UcV_7UeJyg3stDSskA6osYlBHDNsu116yduteJqpIsNFzjyoYaPB4v_RPsXFTm4&_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.57", "Google Chrome";v="126.0.6478.57"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            }
            href = soup.select_one('form [action^="/privacy/consent_framework/server_callback/?"]')['action']
            fb_dtsg = soup.find('input', {'name': 'fb_dtsg'}).get("value")
            jazoest = soup.find('input', {'name': 'jazoest'}).get("value")
            data = [
                ('fb_dtsg', fb_dtsg),
                ('jazoest', jazoest),
                ('fb_trackers_on_other_companies', 'false'),
                ('other_company_trackers_on_foa', 'false'),
                ('card_one_learnt_more', ''),
                ('card_two_learnt_more', ''),
                ('card_three_learnt_more', ''),
                ('card_four_learnt_more', ''),
                ('fb_trackers_on_other_companies', 'false'),
                ('other_company_trackers_on_foa', 'false'),
                ('primary_consent_button', 'Allow all or selected cookies'),
            ]

            response = requests.post(f'https://mbasic.facebook.com/{href}',cookies=cookie, headers=headers,data=data)
            open("html.html" , "w" , encoding="utf-8").write(response.text)
            webbrowser.open('html.html')
            return BeautifulSoup(response.content,'html.parser')
        except Exception as e :print(e)
class Edit_Photo:
    def __init__(self, photo, cookie) :
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))
        self.url = "https://mbasic.facebook.com/profile_picture/"
        self.photo = photo
    def Start(self):
        try:
            if not self.photo :
                'No Photo' , 0
            req = BeautifulSoup(self.req.get(self.url).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'  : 'Save'}
            fil = {'pic' : open(self.photo, 'rb')}
            sleep(1)
            response = self.req.post(raq['action'],data=dat,files=fil,headers=Header_www())
            pos = BeautifulSoup(response.content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Your account is restricted at this time' or cek == 'You are Temporarily Blocked' or cek == 'Error' : return "Failed Change Profile Photo" , 0
            else:
                return "Successfully Change Profile Photo" , 1
        except Exception as e: return "Failed Change Profile Photo1" , 0
class Edit_Cover:
    def __init__(self, photo, cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))
        self.url = 'https://mbasic.facebook.com/photos/upload/?cover_photo'
        self.photo = photo
    def Start(self):
        try:
            if not self.photo :
                'No Photo' , 0
            req = BeautifulSoup(self.req.get(self.url).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'                  : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'                  : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri'               : re.search('name="return_uri" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri_error'         : re.search('name="return_uri_error" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ref'                      : re.search('name="ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'csid'                     : re.search('name="csid" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ctype'                    : re.search('name="ctype" type="hidden" value="(.*?)"',str(raq)).group(1),
                'profile_edit_logging_ref' : re.search('name="profile_edit_logging_ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'                   : 'Upload'}
            fil = {'file1' : open(self.photo, 'rb')}
            sleep(1)
            pos = BeautifulSoup(self.req.post('https://mbasic.facebook.com'+raq['action'],data=dat,files=fil).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Your account is restricted at this time' or cek == 'You are Temporarily Blocked' or cek == 'Error' : return "Failed Change Cover Photo" , 2 
            else: 
                return "Successfully Change Cover Photo" , 1
        except Exception as e: print(e);return "Failed Change Cover Photo" , 0 
class Edit_bio:
    def __init__(self, bio ,cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))
        self.url = "https://mbasic.facebook.com/profile/basic/intro/bio/"
        self.bio = bio
    def Start(self):
        try:
            if not self.bio :
                'No Bio' , 0
            req = BeautifulSoup(self.req.get(self.url).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'         : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'         : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'bio'             : self.bio,
                'publish_to_feed' : False,
                'submit'          : 'Save'}
            sleep(2)
            pos = BeautifulSoup(self.req.post('https://mbasic.facebook.com'+raq['action'],data=dat).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Your account is restricted at this time' or cek == 'You are Temporarily Blocked' or cek == 'Error' : return "Failed Change Bio" , 0
            else: 
                return "Successfully Change Bio" , 1
        except Exception as e: return "Failed Change Bio" , 0
class Edit_City:
    def __init__(self, city ,cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))
        self.url = 'https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city'   
        self.city = city
    def Start(self):
        try:
            if not self.city :
                'No City' , 0
            req = BeautifulSoup(self.req.get(self.url).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'edit'       : 'current_city',
                'type'       : 'basic',
                'current_city[]' : self.city,
                'save'       : 'submit'}
            sleep(2)
            pos = BeautifulSoup(self.req.post('https://mbasic.facebook.com'+raq['action'],data=dat).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Your account is restricted at this time' or cek == 'You are Temporarily Blocked' or cek == 'Error' : return 'Failed Change City' , 0
            else: 
                return f'Successfully Change City To {self.city}' , 1 
        except Exception as e: return 'Failed Change City' , 0
class Edit_Hometown:
    def __init__(self, hometown ,cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))
        self.url = 'https://mbasic.facebook.com/editprofile.php?type=basic&edit=hometown'        
        self.hometown = hometown
    def Start(self):
        try:
            if not self.hometown :
                'No Hometown' , 0
            req = BeautifulSoup(self.req.get(self.url).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'edit'       : "hometown",
                'type'       : 'basic',
                'hometown[]' : self.hometown,
                'save'       : 'submit'}
            sleep(2)
            pos = BeautifulSoup(self.req.post('https://mbasic.facebook.com'+raq['action'],data=dat).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Your account is restricted at this time' or cek == 'You are Temporarily Blocked' or cek == 'Error' : return 'Failed Change Hometown' , 0
            else: 
                return f'Successfully Change Hometown To {self.hometown}' , 1
        except Exception as e: return 'Failed Change Hometown' , 0
class Work:
    def __init__(self,work,cookie):
        self.req = requests.Session()
        self.cookie = cookie_format(cookie)
        self.req.cookies.update(self.cookie)
        try:self.id = re.search(r'c_user=(\d+)', cookie).group(1)
        except:pass
        self.work = work
    def Start(self):
        try:
            if not self.work :
                'No Work' , 0
            req = BeautifulSoup(self.req.get(f'https://www.facebook.com/profile.php?id={self.id}&sk=about_work_and_education',allow_redirects=True).content,'html.parser')
            haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
            rev = re.search('{"rev":(.*?)}',str(req)).group(1)
            hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
            dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
            jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
            spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
            token = re.search('"sectionToken":(.*?),',str(req)).group(1)
            var = {"collectionToken":token,"input":{"description":"","employer_id":"","employer_name":self.work,"end_date":{},"is_current":True,"location_id":"","mutation_surface":"PROFILE","position_id":"","position_name":"","privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"},"start_date":{},"actor_id":self.id,"client_mutation_id":"2"},"scale":1,"sectionToken":token,"useDefaultActor":False}
            data = {'av': self.id,'__aaid': '0','__user': self.id,'__a': '1','__req': '1d','__hs': haste,'dpr': '1','__ccg': 'EXCELLENT','__rev': rev,'__s': 'vp3naj:ofqa5d:6ovf0j','__hsi': hsi,'__comet_req': '15','fb_dtsg': dtsg,'jazoest': jazoest,'lsd': lsd, '__spin_r': spinr,'__spin_b': 'trunk','__spin_t': spint,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'ProfileCometWorkExperienceSaveMutation','variables': json.dumps(var),'server_timestamps': 'true','doc_id': '7741834642519580'}
            headers = {'accept': '*/*','accept-language': 'en,en-US;q=0.9,ar;q=0.8,ar-EG;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.facebook.com','priority': 'u=1, i','referer': f'https://www.facebook.com/profile.php?id={self.id}&sk=about_work_and_education','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"','sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"10.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36','x-asbd-id': '129477','x-fb-friendly-name': 'ProfileCometWorkExperienceSaveMutation','x-fb-lsd': lsd}
            pos = self.req.post('https://www.facebook.com/api/graphql/',data=data,headers=headers,cookies=self.cookie,allow_redirects=True).json()
            return f'Successfully Add Work {self.work}' , 1
        except Exception as e:
            return e , 0
class School:
    def __init__(self,school,cookie):
        self.req = requests.Session()
        self.cookie = cookie_format(cookie)
        self.req.cookies.update(self.cookie)
        try:self.id = re.search(r'c_user=(\d+)', cookie).group(1)
        except:pass
        self.school = school
    def Start(self):
        try:
            if not self.school :
                'No Sckool' , 0
            req = BeautifulSoup(self.req.get(f'https://www.facebook.com/profile.php?id={self.id}&sk=about_work_and_education',allow_redirects=True).content,'html.parser')
            haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
            rev = re.search('{"rev":(.*?)}',str(req)).group(1)
            hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
            dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
            jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
            spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
            token = re.search('"sectionToken":(.*?),',str(req)).group(1)
            var =  {"collectionToken":token,"input":{"description":"","end":{},"has_graduated":True,"mutation_surface":"PROFILE","privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"},"school_id":"","school_name":self.school,"school_type":"hs","start":{},"actor_id":self.id,"client_mutation_id":"1"},"scale":1,"sectionToken":token,"useDefaultActor":False}
            data = {'av': self.id,'__aaid': '0','__user': self.id,'__a': '1','__req': '13','__hs': haste,'dpr': '1','__ccg': 'EXCELLENT','__rev': rev,'__s': '5w9uqd:ofqa5d:rf0pru','__hsi': hsi,'__comet_req': '15','fb_dtsg': dtsg,'jazoest': jazoest,'lsd': lsd,'__spin_r': spinr,'__spin_b': 'trunk','__spin_t': spint,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'ProfileCometEducationExperienceSaveMutation','variables': json.dumps(var),'server_timestamps': 'true','doc_id': '26212740801705794'}
            headers = {'accept': '*/*','accept-language': 'en,en-US;q=0.9,ar;q=0.8,ar-EG;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.facebook.com','priority': 'u=1, i','referer': f'https://www.facebook.com/profile.php?id={self.id}&sk=about_work_and_education','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"','sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"10.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36','x-asbd-id': '129477','x-fb-friendly-name': 'ProfileCometEducationExperienceSaveMutation','x-fb-lsd': lsd}
            pos = self.req.post('https://www.facebook.com/api/graphql/',data=data,headers=headers,cookies=self.cookie,allow_redirects=True).json()
            return f'Successfully Add School {self.school}' , 1
        except Exception as e:
            return e , 0
class lock_profile:
    def __init__(self,cookie):
        self.req = requests.Session()
        self.cookie = cookie_format(cookie)
        self.req.cookies.update(self.cookie)
        try:self.id = re.search(r'c_user=(\d+)', cookie).group(1)
        except:pass
    def Start(self):
        try:
            stat = True
            req = BeautifulSoup(self.req.get(f'https://www.facebook.com/{self.id}',allow_redirects=True).content,'html.parser')
            haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
            rev = re.search('{"rev":(.*?)}',str(req)).group(1)
            hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
            dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
            jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
            spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
            var = {"enable":stat}
            data = {'av':self.id,'__user':self.id,'__a':'1','__hs':haste,'dpr':'1.5','__ccg':'EXCELLENT','__rev':rev,'__hsi':hsi,'__comet_req':'15','fb_dtsg': dtsg,'jazoest': jazoest,'lsd': lsd,'__spin_b':'trunk','__spin_r':spinr,'__spin_t':spint,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'WemPrivateSharingMutation','variables':json.dumps(var),'server_timestamps':'true','doc_id':'5507005232662559'}
            headpos = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,image/jpeg,image/jpg,image/png,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Origin':'https://www.facebook.com','Referer':'https://www.facebook.com/','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','X-Fb-Friendly-Name':'WemPrivateSharingMutation','X-Fb-Lsd':lsd}
            pos = self.req.post('https://www.facebook.com/api/graphql/',data=data,headers=headpos,cookies=self.cookie,allow_redirects=True).json()
            if str(pos['data']['toggle_wem_private_sharing_control_enabled']) == 'None': return 'Locked Profile Not Available!' , 0
            elif str(pos['data']['toggle_wem_private_sharing_control_enabled']['private_sharing_enabled']) == 'True': return 'Successfully Activating the Locked Profile' , 1
            elif str(pos['data']['toggle_wem_private_sharing_control_enabled']['private_sharing_enabled']) == 'False': return 'Successfully Deactivated the Locked Profile' , 1
            else: return pos ,  0
        except Exception as e:
            return e , 0

class Change_Password:
    def __init__(self, password , new_password , cookie):
        self.req = requests.Session()
        self.req.headers.update(Header())
        self.cookie = cookie
        cookie = cookie_format(cookie)
        self.req.cookies.update(cookie)
        self.url = 'https://mbasic.facebook.com/settings/security_login'
        self.password = password
        self.new_password = new_password
    def Start(self):
        # try:
            req = BeautifulSoup(self.req.get(self.url).content,'html.parser') ; sleep(1)
            href = req.select_one('a[href^="/settings/security/password/?"]').get('href')
            req = BeautifulSoup(self.req.get('https://mbasic.facebook.com'+ href).content,'html.parser') ; sleep(1)
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'password_change_session_identifier': raq.find('input', {'name': 'password_change_session_identifier'}).get("value"),
                'password_old': self.password,
                'password_new': self.new_password,
                'password_confirm': self.new_password,
                'save': 'Save changes',
                }
            self.req.headers.update({'referer': href})
            pos = BeautifulSoup(self.req.post('https://mbasic.facebook.com'+raq['action'],data=dat).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Your account is restricted at this time' or cek == 'You are Temporarily Blocked' or cek == 'Error' : return 'Failed Change Password' , 0
            else:
                self.req.headers.update({'referer': raq['action']})
                pos = pos.find('form',{'method':'post'})
                dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(pos)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(pos)).group(1),
                'session_invalidation_options': 'review_sessions',
                'submit_action': 'Continue',
                }
                pos = BeautifulSoup(self.req.post('https://mbasic.facebook.com'+pos['action'],data=dat).content,'html.parser')
                href = pos.select_one('a[href^="/settings/security_login/sessions/log_out_all"]').get('href')
                req = BeautifulSoup(self.req.get('https://mbasic.facebook.com'+ href).content,'html.parser') ; sleep(1)
                open("html.html" , "w" , encoding="utf-8").write(req.prettify())
                webbrowser.open('html.html')
                input("......")
                return f'Successfully Change Password To {self.new_password}' , 1
        # except Exception as e: print(e) ; return 'Failed Change Password' , 0
