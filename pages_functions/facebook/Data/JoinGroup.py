from pages_functions.__init__ import *

class JoinGroup:
    def __init__(self,url,cookie ) -> None:
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.url = url
        try:self.url = self.url.replace("www", "mbasic")
        except:pass

    def Start(self):
        response = self.req.get( self.url )
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
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
                      Update_cookies(self.cookie,(';'.join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items() ])).replace("cookie=", ""))
                      return f'Done joined', 1
                else: return f'Faild joine', 0
            except:   return f'Faild joine', 0
        else:         return f'Faild Find Group', 0
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
            Update_cookies(self.cookie,(';'.join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items() ])).replace("cookie=", ""))
            return f"Done joined"