from pages_functions.__init__ import *

class Follow:
    def __init__(self, url ,cookie):
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))
    
        try:self.url = url.replace("www", "mbasic")
        except:pass

    def Start(self):
        try:
            soup = BeautifulSoup(self.req.get(self.url).content, 'html.parser')
            try:
                try: 
                    self.href = soup.select_one('a[href^="/a/subscribe.php?"]').get('href')
                    sleep(1)
                    return self.Follow_Profile()
                except:
                    self.href = soup.select_one('a[href^="/a/subscriptions/remove?"]').get('href')
                    return "Already followed" , 2
            except:
                return "Faild Follow" , 2
        except Exception as e:
            return e , 0

    def Follow_Profile(self):
        self.req.headers.update({'referer': self.url})

        response = self.req.get( f'https://mbasic.facebook.com/{self.href}' )
        if response.status_code == 200 :
            self.id = (re.search(r'id=(\d+)', self.url) or re.search(r'/([^/]+)$', self.url) or re.search(r'facebook.com/([^/]+)', self.url) or "").group(1)
            return (f'Done Follow : {self.id}') , 1
        
class Follow_www:
    def __init__(self, url ,cookie):
        self.req = requests.Session()
        self.headers = Header_www()
        self.cookie = cookie_format(cookie)
        self.url = url

    def Start(self):
        try:
            soup = BeautifulSoup(self.req.get(self.url,headers=self.headers,cookies=self.cookie).content, 'html.parser')
            statu = re.search(r'"ProfileActionFollowingStatus",\s*"title":\{"text":"(.*?)"\}', str(soup)).group(1)
            if statu == 'Following':
                return  "Already followed" , 2
            haste_session = re.search('"haste_session":"(.*?)",', str(soup)).group(1)
            rev = re.search('{"rev":(.*?)}', str(soup)).group(1)
            hsi = re.search('"hsi":"(.*?)",', str(soup)).group(1)
            fb_dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', str(soup)).group(1)
            jazoest = re.search('&jazoest=(.*?)",', str(soup)).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"', str(soup)).group(1)
            spinr = re.search('"__spin_r":(.*?),', str(soup)).group(1)
            spint = re.search('"__spin_t":(.*?),', str(soup)).group(1)
            c_user_value = self.cookie["c_user"]
            userID = next((m.group(1) for script in soup.find_all('script') if script.string and (m := re.search(r'"userID":"(\d+)"', script.string)) and m.group(1) != "100013698670173"), None)
            data = {'av': c_user_value,'__aaid': '0','__user': c_user_value,'__a': '1','__req': 'r','__hs': haste_session,'dpr': '1','__ccg': 'EXCELLENT','__rev': rev,'__s': 'rbr0s4:av99i5:ig0mol','__hsi': hsi,'__comet_req': '15','fb_dtsg': fb_dtsg,'jazoest': jazoest,'lsd': lsd,'__spin_r': spinr,'__spin_b': 'trunk','__spin_t': spint,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'CometUserFollowMutation','variables': f'{{"input":{{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1715096581887,975750,250100865708545,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":{userID},"tracking":null,"actor_id":{c_user_value},"client_mutation_id":"1"}}, "scale":1}}','server_timestamps': 'true','doc_id': '7393793397375006',}
            self.headers['referer'] = self.url ; self.headers['x-fb-friendly-name'] = 'CometUserFollowMutation' ; self.headers['x-fb-lsd'] = lsd
            response = self.req.post('https://www.facebook.com/api/graphql/',headers=self.headers,cookies=self.cookie,data=data)
            self.id = (re.search(r'id=(\d+)', self.url) or re.search(r'/([^/]+)$', self.url) or re.search(r'facebook.com/([^/]+)', self.url) or "").group(1)
            return (f'Done Follow : {self.id}') , 1            
        except: return "Faild Follow" , 0
class Un_Follow:
    def __init__(self, url ,cookie):
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))

        try:self.url = url.replace("www", "mbasic")
        except:pass

    def Start(self):
        try:
            soup = BeautifulSoup(self.req.get(self.url).content, 'html.parser')
            try : 
                try:
                    self.href = soup.select_one('a[href^="/a/subscriptions/remove?"]').get('href')
                    return self.Un_Follow_Profile()
                except : 
                    self.href = soup.select_one('a[href^="/a/subscribe.php?"]').get('href')
                    return "Don't Follow Before" , 2
            except: 
                open("html.html" , "w" , encoding="utf-8").write(soup.prettify())
                return "Faild" , 0
        except Exception as e:
            return e , 0

    def Un_Follow_Profile(self):
        self.req.headers.update({'referer': self.url})

        response = self.req.get( f'https://mbasic.facebook.com/{self.href}' )
        if response.status_code == 200 : 
            self.id = (re.search(r'id=(\d+)', self.url) or re.search(r'/([^/]+)$', self.url) or re.search(r'facebook.com/([^/]+)', self.url) or "").group(1)
            return (f'Done Un Follow : {self.id}') , 1
class Like:
    def __init__(self, url ,type ,cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))

        self.type = type
        try:self.url = url.replace("www", "mbasic")
        except:pass
        self.Type_reaction()
    def Type_reaction (self):
        if self.type == "Like" :
            self.reaction_id = '1635855486666999'
            self.reaction_type = "1"
        elif self.type == "Love" :
            self.reaction_id = '1678524932434102'
            self.reaction_type = "2"
        elif self.type == "Care" :
            self.reaction_id = '613557422527858'
            self.reaction_type = "16"
        elif self.type == "Haha" :
            self.reaction_id = '115940658764963'
            self.reaction_type = "4"
        elif self.type == "Wow" :
            self.reaction_id = '478547315650144'
            self.reaction_type = '3'
        elif self.type == "Sad" :
            self.reaction_id = '908563459236466'
            self.reaction_type = "7"
        else:pass

    def Start(self):
        try:
            soup = BeautifulSoup(self.req.get(self.url).content, 'html.parser')
            self.href = soup.select_one('a[href^="/reactions/picker/?"]').get('href')
            sleep(1)
            return self.Get_reactions()
        except Exception as e:
            return e , 0

    def Get_reactions(self):
        self.req.headers.update({'referer': self.url})

        response = self.req.get( f'https://mbasic.facebook.com/{self.href}' )
        self.referer = response.url
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            try:
                for a in soup.find_all('a', href=True):
                    parsed_url = urlparse(a['href'])
                    query_params = parse_qs(parsed_url.query)

                    if 'reaction_type' in query_params and query_params['reaction_type'][0] == "0":
                        return (f"Already {self.type} befor :") , 2
                    elif 'reaction_id' in query_params and query_params['reaction_id'][0] == self.reaction_id:
                        href = a['href']
                        sleep(1)
                        return self.Like_post(href)
            except:
                return "Faild Get_reactions 1" , 0
        else:
            return "Faild Get_reactions" , 0

    def Like_post(self,href):
        self.req.headers.update({'referer': self.url})

        response = self.req.get( f'https://mbasic.facebook.com/{href}' )
        if response.status_code == 200 :
            return f"Done {self.type} :" , 1
class Like_Page:
    def __init__(self, url ,cookie):
        self.req = requests.Session()
        self.headers = Header_www()
        self.cookie = cookie_format(cookie)
        self.url = url
        try:self.id = re.search(r'c_user=(\d+)', cookie).group(1)
        except:pass
    def Start(self):
        try:
            req = BeautifulSoup(self.req.get(self.url,headers=self.headers,cookies=self.cookie,allow_redirects=True).content, 'html.parser')
            page_id = re.search('"delegate_page":{"id":"(.*?)"}',str(req)).group(1)
            haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
            rev = re.search('{"rev":(.*?)}',str(req)).group(1)
            hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
            dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
            jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
            spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
            data = {'av': self.id,'__aaid': '0','__user': self.id,'__a': '1','__req': 'm','__hs': haste,'dpr': '1','__ccg': 'EXCELLENT','__rev': rev,'__s': 'a7eibq:ofqa5d:ywyrw3','__hsi': hsi,'__comet_req': '15','fb_dtsg': dtsg,'jazoest': jazoest,'lsd': lsd,'__spin_r': spinr,'__spin_b': 'trunk','__spin_t': spint,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'CometProfilePlusLikeMutation','variables': f'{{"input":{{"is_tracking_encrypted":false,"page_id":{page_id},"source":null,"tracking":null,"actor_id":{self.id},"client_mutation_id":"1"}},"scale":1}}','server_timestamps': 'true','doc_id': '6716077648448761'}
            headers = {'accept': '*/*','accept-language': 'en,en-US;q=0.9,ar;q=0.8,ar-EG;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.facebook.com','priority': 'u=1, i','referer': self.url,'sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"','sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"10.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36','x-asbd-id': '129477','x-fb-friendly-name': 'CometProfilePlusLikeMutation','x-fb-lsd': lsd}
            pos = self.req.post('https://www.facebook.com/api/graphql/',data=data,headers=headers,cookies=self.cookie,allow_redirects=True).json()
            if str(pos['data']['page_like']['page']['profile_plus_for_delegate_page']['profile_action']['title']['text']) == 'Liked' or 'أعجبك': return 'Successfully Liked ' , 1
            else : return pos, 1
        except Exception as e:
            return e , 0
class JoinGroup:
    def __init__(self,url,cookie ) -> None:
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))
        try:self.url = url.replace("www", "mbasic")
        except:pass

    def Start(self):
        try:
            soup = BeautifulSoup(self.req.get(self.url).content, 'html.parser')
            try:
                link = soup.select_one('form[action^="/a/group/join"]')["action"]
                sleep(1)
                response = self.req.get( f'https://mbasic.facebook.com/{link}' )  
                if response.status_code == 200 and "custom_questions" in response.text :
                    print("Answer The Questions To Join ")
                    soup = BeautifulSoup(response.content, 'html.parser')
                    self.fb_dtsg = soup.find('input', {'name': 'fb_dtsg'}).get("value")
                    self.jazoest = soup.find('input', {'name': 'jazoest'}).get("value")
                    link = soup.select_one('form[action^="/groups/membership_criteria_answer/save/?"]')["action"]
                    self.answers = []
                    Questions = soup.find_all('span', {'dir': 'rtl'})
                    for Q in Questions:
                        Answer = input(f"{Q.text.strip()} :")
                        self.answers.append(Answer)
                    
                    return self.Answer(link)     
                elif response.status_code == 200 :
                      return f'Done joined', 1
                else: return f'Faild joine', 0
            except:   return f'Faild joine', 0
        except Exception as e:
            return e , 0
    def Answer(self,link):      
        data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'questionnaire_answers[]': [ ],
                }
        for new_answer in self.answers : 
            data['questionnaire_answers[]'].append(new_answer)
        
        response = self.req.post( f'https://mbasic.facebook.com/{link}', data=data )
        if response.status_code == 200 and "Edit Answers" in response.text :
            return f"Done joined"
class Share:
    def __init__(self, url ,message ,cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))
        self.message = message
        try:self.url = url.replace("www", "mbasic")
        except:pass
    def Start(self):
        try:
            soup = BeautifulSoup(self.req.get(self.url).content, 'html.parser')
            self.href = soup.select_one('a[href^="/composer/mbasic/?"]').get('href')
            return self.Get_data() 
        except Exception as e:
            return e , 0
        
    def Get_data(self):
        response = self.req.get( f'https://mbasic.facebook.com/{self.href}' )
        sleep(1)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            self.target = soup.find('input', {'name': 'target'}).get("value")
            self.csid = soup.find('input', {'name': 'csid'}).get("value")
            self.sid = soup.find('input', {'name': 'sid'}).get("value")
            self.shared_from_post_id = soup.find('input', {'name': 'shared_from_post_id'}).get("value")
            self.fb_dtsg = soup.find('input', {'name': 'fb_dtsg'}).get("value")
            self.jazoest = soup.find('input', {'name': 'jazoest'}).get("value")
            link = soup.select_one('form[action^="/composer/mbasic/?"]')["action"]
            return self.Share_post(link)
            
    def Share_post(self,link):
        data = {
                "fb_dtsg" :{self.fb_dtsg},
                "jazoest" :{self.jazoest},
                "target" :{self.target},
                "csid" :{self.csid},
                "c_src": "share",
                "referrer" : "permalink",
                "ctype" : "advanced",
                "cver" : "amber_share",
                "waterfall_source" : "advanced_composer_timeline",
                "privacyx" : "300645083384735",
                "appid" : "0",
                "sid" : {self.sid},
                "m" : "self",
                "xc_message": {self.message},
                "view_post" : "Share",
                "shared_from_post_id":{self.shared_from_post_id},
                }
        response = self.req.post( f'https://mbasic.facebook.com/{link}', data=data)
        if response.status_code == 200 : 
            return f"Done Share : " , 1
        else: return "Faild Share" , 0
class Comment:
    def __init__(self, url ,message ,cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))
        self.message = message
        try:self.url = url.replace("www", "mbasic")
        except:pass
    def Start(self):
        if not self.message :
            return
        try:
            soup = BeautifulSoup(self.req.get(self.url).content, 'html.parser')
            href = soup.select_one('a[href^="/mbasic/comment/advanced/?"]')['href']
            soup = BeautifulSoup(self.req.get(f'https://mbasic.facebook.com/{href}').content, 'html.parser')
            raq = soup.find('form',{'method':'post'})
            self.fb_dtsg = re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
            self.jazoest =  re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
            data = {'fb_dtsg': (None, self.fb_dtsg),'jazoest': (None, self.jazoest),'comment_text': (None, self.message),'photo': ('', '', 'application/octet-stream'),'post': (None, 'Comment')}
            response = self.req.post(raq['action'],data=data,headers=Header_www())  
            if response.status_code == 200:
                return "Done Comment" , 1  
        except Exception as e :
            return e , 0
        
class Comment_Like:
    def __init__(self, url ,message ,cookie) -> None:
        self.req = requests.Session()
        self.message = message
        self.headers = Header()
        self.req.headers.update(self.headers)
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.url = url
        try:self.url = self.url.replace("www", "mbasic")
        except:pass
    def Start(self):
        response = self.req.get(self.url)
        sleep(1)
        try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                self.href  = soup.select_one('a[href^="/comment/replies/"]')['href']
                response = requests.get(f'https://mbasic.facebook.com{self.url}', cookies=self.cookie,headers=self.headers, timeout=30)
                soup = BeautifulSoup(response.text, "html5lib")
                if response.status_code == 200:
                    fb_dtsg = soup.find('input', {'name': 'fb_dtsg'}).get("value")
                    jazoest = soup.find('input', {'name': 'jazoest'}).get("value")
                    url2 = soup.select_one('form[action^="/a/comment.php?"]')['action']
                return self.Get_data()
            else: return "Faild Get_post" , 0
        except:
            open("html.html" , "w" , encoding="utf-8").write(response.text)
            return "failed Comment" , 0
        
    def Get_data(self):
        self.headers['origin'] = 'https://mbasic.facebook.com'
        self.headers['referer'] = self.href
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            # 'comment_text': comments[comments_index],
            }
        if response.status_code == 200: 
            response = requests.post(f'https://mbasic.facebook.com{self.url2}', cookies=self.cookies, data=data,headers=self.headers, timeout=30)
        if response.status_code == 200:
            return "Done Comment" , 1
class AddFriend:
    def __init__(self, url, cookie ) :
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))
        try:self.url = url.replace("www", "mbasic")
        except:pass
    def Start(self):
        try:
            soup = BeautifulSoup(self.req.get(self.url).content, 'html.parser')
            href = soup.select_one('a[href^="/a/friends/profile/add/"]')["href"]
            sleep(1)
            response = self.req.get( f'https://mbasic.facebook.com/{href}' )  
            if response.status_code == 200 : 
                self.id = (re.search(r'id=(\d+)', self.url) or re.search(r'/([^/]+)$', self.url) or re.search(r'facebook.com/([^/]+)', self.url) or "").group(1) 
                return f'Done Friend   :  {self.id} ' , 1
        except Exception as e:
            return e , 0
class Accept:
    def __init__(self, cookie ) -> None:
        self.req = requests.Session()
        self.req.headers.update( Header())
        self.req.cookies.update(cookie_format(cookie))

    def Start(self):
        url = f'https://mbasic.facebook.com/friends/center/requests/'
        sleep(1)
        try:
                soup = BeautifulSoup(self.req.get(url).content, 'html.parser')
                href = soup.select_one('a[href^="/a/notifications.php?confirm"]')["href"]
                response = self.req.get( f'https://mbasic.facebook.com/{href}' )
                if response.status_code == 200 :
                    return f'Done Accept Friend', 1
        except Exception as e:
            return e , 0
class View:
    def __init__(self,url,cookie ) -> None:
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        self.cookie = cookie
        self.url = url
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)

    def Start(self):
        response = self.req.get( self.url )
        sleep(1)
        if response.status_code == 200:
            try:
                open("html.html" , "w" , encoding="utf-8").write(response.text)
                webbrowser.open('html.html')
            except: return f'Faild Accept Account', 0
        else: return f'Faild Find Friend', 0