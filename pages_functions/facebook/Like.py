from pages_functions.__init__ import *

from ui.Facebook.Like_ui import Ui_Form
from pages_functions.Public.Info import Info
from pages_functions.Facebook.Data.Action import Like as like
from pages_functions.Facebook.Data.get_count import *
from pages_functions.Public.Select import Select

class Like(QWidget):
    def __init__(self):
        super(Like, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.URL = config['server']['URL']
        self.API_KEY  = config['server']['API_KEY']
        self.TIMEOUT = 10
        self.time = 1
        self.succes = 0
        self.failed = 0
        self.order = 0
        self.is_running = False
        self.lock = Lock()

        self.Info = Info()
        layout = QVBoxLayout(self.ui.widget_Info); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.Info)
        header_labels = ["#", "ID", "Data","Name","Action","Message"]
        self.Info.ui.table.setHorizontalHeaderLabels(header_labels)
        self.ui.Start.clicked.connect(lambda : Thread(target=self.Start).start())
        self.ui.Select_Account.clicked.connect(self.Select)
        self.ui.pushButton_like.clicked.connect(lambda: (config.set('server', 'like', self.ui.lineEdit_like.text()), config.write(open('pages_functions\settings.ini', 'w')),self.ui.label_like.setText(config['server']['like']))) ; self.ui.label_like.setText(config['server']['like'])
        self.ui.pushButton_love.clicked.connect(lambda: (config.set('server', 'love', self.ui.lineEdit_love.text()), config.write(open('pages_functions\settings.ini', 'w')),self.ui.label_love.setText(config['server']['love']))) ; self.ui.label_love.setText(config['server']['love'])
        self.ui.pushButton_care.clicked.connect(lambda: (config.set('server', 'care', self.ui.lineEdit_care.text()), config.write(open('pages_functions\settings.ini', 'w')),self.ui.label_care.setText(config['server']['care']))) ; self.ui.label_care.setText(config['server']['care'])
        self.ui.pushButton_haha.clicked.connect(lambda: (config.set('server', 'haha', self.ui.lineEdit_haha.text()), config.write(open('pages_functions\settings.ini', 'w')),self.ui.label_haha.setText(config['server']['haha']))) ; self.ui.label_haha.setText(config['server']['haha'])
        self.ui.pushButton_wow.clicked.connect(lambda: (config.set('server', 'wow', self.ui.lineEdit_wow.text()), config.write(open('pages_functions\settings.ini', 'w')),self.ui.label_wow.setText(config['server']['wow']))) ; self.ui.label_wow.setText(config['server']['wow'])
        self.ui.pushButton_sad.clicked.connect(lambda: (config.set('server', 'sad', self.ui.lineEdit_sad.text()), config.write(open('pages_functions\settings.ini', 'w')),self.ui.label_sad.setText(config['server']['sad']))) ; self.ui.label_sad.setText(config['server']['sad'])
        self.ui.pushButton_ll.clicked.connect(lambda: (config.set('server', 'll', self.ui.lineEdit_ll.text()), config.write(open('pages_functions\settings.ini', 'w')),self.ui.label_ll.setText(config['server']['ll']))) ; self.ui.label_ll.setText(config['server']['ll'])
        self.ui.pushButton_lc.clicked.connect(lambda: (config.set('server', 'lc', self.ui.lineEdit_lc.text()), config.write(open('pages_functions\settings.ini', 'w')),self.ui.label_lc.setText(config['server']['lc']))) ; self.ui.label_lc.setText(config['server']['lc'])
        self.ui.pushButton_llc.clicked.connect(lambda: (config.set('server', 'llc', self.ui.lineEdit_llc.text()), config.write(open('pages_functions\settings.ini', 'w')),self.ui.label_llc.setText(config['server']['llc']))) ; self.ui.label_llc.setText(config['server']['llc'])

        for i in range(self.ui.stackedWidget.count()):
            self.ui.stackedWidget.widget(i).setVisible(False)

        self.ui.like_check.stateChanged.connect(lambda state: self.toggle_page(state, 0))
        self.ui.love_chek.stateChanged.connect(lambda state: self.toggle_page(state, 1))
        self.ui.care_chek.stateChanged.connect(lambda state: self.toggle_page(state, 3))
        self.ui.haha_chek.stateChanged.connect(lambda state: self.toggle_page(state, 4))
        self.ui.wow_chek.stateChanged.connect(lambda state: self.toggle_page(state, 5))
        self.ui.sad_chek.stateChanged.connect(lambda state: self.toggle_page(state, 6))
        self.ui.ll_check.stateChanged.connect(lambda state: self.toggle_page(state, 7))
        self.ui.lc_check.stateChanged.connect(lambda state: self.toggle_page(state, 8))
        self.ui.llc_chek.stateChanged.connect(lambda state: self.toggle_page(state, 9))
        

        self.checked_state = [False,False,False,False,False,False,False,False,False,False]
           
    def toggle_page(self, state, index):
        if state == 2:
            self.checked_state[index] = True
            self.ui.stackedWidget.setCurrentIndex(index)
            self.ui.stackedWidget.widget(index).setVisible(True)
        elif self.checked_state[index]:
            self.checked_state[index] = False
            self.ui.stackedWidget.widget(index).setVisible(False)
            self.ui.stackedWidget.setCurrentIndex(2)
        
    def Select(self):
        table_dialog = Select(self)
        table_dialog.exec()
    def Update_info(self,info):
        self.ui.Number_Account.setText(str(len(info)))
        self.data = queue.Queue(); [self.data.put(i) for i in info]

    def get_pending_order(self,SERVICEs_ID):
        params = {
            "key": self.API_KEY,
            "type": SERVICEs_ID,
            "action": "getOrder",
        }
        return json.loads(requests.get(self.URL, params=params, timeout=self.TIMEOUT).text)
    def set_start_count(self,order_id, start_count):
        params = {
            "key": self.API_KEY,
            "action": "setStartcount",
            "id": order_id,
            "start_count": start_count
        }
        return json.loads(requests.get(self.URL, params=params, timeout=self.TIMEOUT, verify=False).text)
    def set_remains(self,order_id, remains):
        params = {
            "key": self.API_KEY,
            "action": "setRemains",
            "id": order_id,
            "remains": remains
        }
        return json.loads(requests.get(self.URL, params=params, timeout=self.TIMEOUT, verify=False).text)
    def set_completed(self,order_id):
        params = {
            "key": self.API_KEY,
            "action": "setCompleted",
            "id": order_id
        }
        return json.loads(requests.get(self.URL, params=params, timeout=self.TIMEOUT, verify=False).text)
    def set_Fail(self,order_id):
        params = {
            "key": self.API_KEY,
            "action": "setFail",
            "id": order_id
        }
        return json.loads(requests.get(self.URL, params=params, timeout=self.TIMEOUT, verify=False).text)
    def Order(self,name,type,num):
        try:
            pending = self.get_pending_order(num)
            if pending["status"] == "fail": sleep(10) ; return
            if pending["status"] == "success":
                self.succes = 0 ; self.failed = 0 ; self.Info.Update(s=0,f=0,o=self.order)
                id = pending['id']
                link = pending['link']
                link = re.sub(r'/reel/', '/', link) or re.sub(r'/r/', '/', link)
                quantity = int(pending['quantity'])
                result = get_likes(link).Start()
                listt = []
                if result[0] == 'No match found' :
                    self.Info.Add_order(0,id,'None',name,f'Error {result[1]}')
                else:
                    try:
                        self.set_start_count(int(id),int(result[1]))
                        def perfom():
                            while not self.data.empty():
                                if self.succes >= quantity : break
                                else:
                                    try:
                                        cookie = self.data.get()
                                        listt.append(cookie)
                                        result = like(link,random.choice(type),cookie[5]).Start()
                                        self.Info.Add_order(result[1],id,cookie[1],name,f'{result[0]} {link}')
                                        if result[1] == 1: self.succes += 1
                                        else: self.failed += 1
                                        self.Info.Update(s=self.succes,f=self.failed,o=self.order) ;  sleep(self.time)
                                    except Exception as e:
                                        try: self.Info.Add_order(0,id,cookie[1],name,f'{e}')
                                        except : self.Info.Add_order(0,id,'None',name,"No Account") 
                                        self.failed += 1
                                        self.Info.Update(s=self.succes,f=self.failed,o=self.order) ;  sleep(self.time)
                        with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
                            futures = [executor.submit(perfom) for _ in range(15)]
                            concurrent.futures.wait(futures)
                    except Exception as e : input(e)
            self.order += 1
            self.Info.Add_order(1,id,'Compelet',name,f'Total : {quantity} Succes : {self.succes} Failed : {self.failed} Link : {link}',"ok") ; self.Info.Update(s=self.succes,f=self.failed,o=self.order) 
            if self.succes >= quantity  : self.set_completed(id)
            else : self.set_remains(id,quantity-self.succes)
            for i in listt:
                self.data.put(i)
        except Exception as e :print(f'{num}\n {e}')
    def Start(self):
        if self.ui.Number_Account.text() == '0': QMessage(text = 'No Account Selected').mainloop() ; self.ui.Start.setChecked(False)
        else:
            if self.is_running == False : self.ui.Start.setText("Stop") ; self.is_running = True ; self.Info.Update(s=0,f=0,o=0)
            elif self.is_running : self.ui.Start.setText("Start") ; self.ui.Start.setChecked(False) ; self.is_running = False
            while  self.is_running :
                    if self.ui.like_check.isChecked() and self.is_running :
                        self.Order('Like',['Like'],int(self.ui.label_like.text()))
                    if self.ui.love_chek.isChecked() and self.is_running :
                        self.Order('Love',['Love'],int(self.ui.label_love.text()))
                    if self.ui.care_chek.isChecked() and self.is_running :
                        self.Order('Care',['Care'],int(self.ui.label_care.text()))
                    if self.ui.haha_chek.isChecked() and self.is_running :
                        self.Order('Haha',['Haha'],int(self.ui.label_haha.text()))
                    if self.ui.wow_chek.isChecked() and self.is_running :
                        self.Order('Wow',['Wow'],int(self.ui.label_wow.text()))
                    if self.ui.sad_chek.isChecked() and self.is_running :
                        self.Order('Sad',['Sad'],int(self.ui.label_sad.text()))
                    if self.ui.ll_check.isChecked() and self.is_running :
                        self.Order('Like - Love',['Like','Love'],int(self.ui.label_ll.text()))
                    if self.ui.lc_check.isChecked() and self.is_running :
                        self.Order('Love - care',['Love','care'],int(self.ui.label_lc.text()))
                    if self.ui.llc_chek.isChecked() and self.is_running :
                        self.Order('Like - Love - Care',['Like','Love','Care'],int(self.ui.label_llc.text()))
                    

                        