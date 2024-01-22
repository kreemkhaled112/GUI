from pages_functions.__init__ import *

class JoinGroup:
    def __init__(self, id, cookie ) -> None:

        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.Get_Group(id)

    def Get_Group(self,id):
        response = self.req.get( f'https://mbasic.facebook.com/groups/{id}' )
        sleep(1)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            try:
                link = soup.select_one('form[action^="/a/group/join"]')["action"]
                
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
                    
                    self.Answer(link)     
                elif response.status_code == 200 :
                    print(Colorate.Diagonal(Colors.green_to_cyan, f'[ Done joined ] : [ {id} ]', 1))
                else:
                    print(Colorate.Diagonal(Colors.red_to_blue, f'[ Faild joine ] : [ {id} ]', 1))
            except:
                print(Colorate.Diagonal(Colors.red_to_blue, f'[ Faild joine ] : [ {id} ]', 1))
        else:
            print(Colorate.Diagonal(Colors.red_to_blue, f'[ Faild Find Group ] : [ {id} ]', 1))
    def Answer(self,link):      
        data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'questionnaire_answers[]': [ ],
                }
        for new_answer in self.answers : 
            data['questionnaire_answers[]'].append(new_answer)
        
        response = self.req.post(
            f'https://mbasic.facebook.com/{link}',
            data=data,
        )
        if response.status_code == 200 and "Edit Answers" in response.text :
            print("Done Answer")