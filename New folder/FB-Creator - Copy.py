import hashlib, threading , sqlite3 , random , string , requests , json , gzip
from faker import Faker

conn = sqlite3.connect('P:\API\GUI\pages_functions\info.db',check_same_thread=False)
cursor = conn.cursor()
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def create_mail_tm_account():
    chrs = 'abcdefghijklmnopqrstuvwxyz'
    fake = Faker()
    username  = ''.join(random.choices(chrs, k=random.randrange(6,7)))
    chrs = ''.join((chrs, '0123456789'))
    password = ''.join(random.choices(chrs, k=random.randrange(7,9))) 
    birthday = fake.date_of_birth(minimum_age=10, maximum_age=24)
    random_item = cursor.execute("SELECT data FROM name WHERE type='female' ORDER BY RANDOM() LIMIT 1").fetchone()
    name = random_item[0].split(' ')
    first_name = name[0]
    last_name = name[1]
    return f"Fb1e+{username}@yandex.com", password, first_name, last_name, birthday
def register_facebook_account(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    req = {'api_key': api_key,
           'attempt_login': True,
           'birthday': birthday.strftime('%Y-%m-%d'),
           'client_country_code': 'EN',
           'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
           'fb_api_req_friendly_name': 'registerAccount',
           'firstname': first_name,
           'format': 'json',
           'gender': gender,
           'lastname': last_name,
           'email': email,
           'locale': 'en_US',
           'method': 'user.register',
           'password': password,
           'reg_instance': generate_random_string(32),
           'return_multiple_errors': True}
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-graph.facebook.com/app/users'
    reg = _call(api_url, req)
    id=reg['new_user_id']
    token=reg['session_info']['access_token']
    print(f'''[+] Email : {email}
[+] ID : {id}
[+] Token : {token}
[+] PassWord : {password}
[+] Name : {first_name} {last_name}
[+] BirthDay : {birthday}
[+] Gender : {gender}
===================================''')
    
    input_data = {
    "method": "post",
    "pretty": False,
    "format": "json",
    "server_timestamps": True,
    "locale": "en_US",
    "purpose": "fetch",
    "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.reg.confirmation.async",
    "fb_api_caller_class": "graphservice",
    "client_doc_id": "11994080423068421059028841356",
    "variables": {
        "params": {
        "params": "{\"params\":\"{\\\"client_input_params\\\":{\\\"confirmed_cp_and_code\\\":{},\\\"code\\\":\\\"30002\\\",\\\"fb_ig_device_id\\\":[],\\\"device_id\\\":\\\"34755123-f240-45ac-afba-6bf04bb07711\\\",\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\",\\\"lara_override\\\":\\\"\\\"}},\\\"server_params\\\":{\\\"event_request_id\\\":\\\"34efb418-bebe-43d2-8f0d-e83a129638b3\\\",\\\"is_from_logged_out\\\":0,\\\"text_input_id\\\":20421463600046,\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\"34755123-f240-45ac-afba-6bf04bb07711\\\",\\\"waterfall_id\\\":\\\"a5bc0874-0c50-49b8-8db3-ebe415cca97d\\\",\\\"wa_timer_id\\\":\\\"wa_retriever\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":2.0421463600096E13,\\\"flow_info\\\":{\\\"flow_name\\\":\\\"new_to_family_fb_default\\\",\\\"flow_type\\\":\\\"ntf\\\"},\\\"is_platform_login\\\":0,\\\"sms_retriever_started_prior_step\\\":0,\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"reg_info\\\":{\\\"contactpoint\\\":\\\"fb1e+g0wgd2r@yandex.com\\\",\\\"contactpoint_type\\\":\\\"email\\\",\\\"first_name\\\":null,\\\"last_name\\\":null,\\\"full_name\\\":null,\\\"ar_contactpoint\\\":null,\\\"is_using_unified_cp\\\":null,\\\"unified_cp_screen_variant\\\":null,\\\"is_cp_auto_confirmed\\\":null,\\\"is_cp_auto_confirmable\\\":null,\\\"confirmation_code\\\":null,\\\"birthday\\\":null,\\\"did_use_age\\\":null,\\\"gender\\\":null,\\\"use_custom_gender\\\":null,\\\"custom_gender\\\":null,\\\"encrypted_password\\\":null,\\\"username\\\":null,\\\"username_prefill\\\":null,\\\"fb_conf_source\\\":null,\\\"device_id\\\":\\\"34755123-f240-45ac-afba-6bf04bb07711\\\",\\\"ig4a_qe_device_id\\\":null,\\\"ig_nta_test_group\\\":null,\\\"family_device_id\\\":\\\"34755123-f240-45ac-afba-6bf04bb07711\\\",\\\"nta_eligibility_reason\\\":null,\\\"youth_consent_decision_time\\\":null,\\\"username_screen_experience\\\":null,\\\"user_id\\\":null,\\\"safetynet_token\\\":null,\\\"safetynet_response\\\":null,\\\"machine_id\\\":null,\\\"profile_photo\\\":null,\\\"profile_photo_id\\\":null,\\\"profile_photo_upload_id\\\":null,\\\"avatar\\\":null,\\\"email_oauth_token_no_contact_perm\\\":null,\\\"email_oauth_token\\\":null,\\\"email_oauth_tokens\\\":null,\\\"should_skip_two_step_conf\\\":null,\\\"openid_tokens_for_testing\\\":null,\\\"encrypted_msisdn\\\":null,\\\"encrypted_msisdn_for_safetynet\\\":null,\\\"cached_headers_safetynet_info\\\":null,\\\"should_skip_headers_safetynet\\\":null,\\\"headers_last_infra_flow_id\\\":null,\\\"headers_last_infra_flow_id_safetynet\\\":null,\\\"headers_flow_id\\\":null,\\\"was_headers_prefill_available\\\":null,\\\"sso_enabled\\\":null,\\\"existing_accounts\\\":null,\\\"used_ig_birthday\\\":null,\\\"sync_info\\\":null,\\\"create_new_to_app_account\\\":null,\\\"skip_session_info\\\":null,\\\"ck_error\\\":null,\\\"ck_id\\\":null,\\\"ck_nonce\\\":null,\\\"should_save_password\\\":null,\\\"horizon_synced_username\\\":null,\\\"fb_access_token\\\":null,\\\"horizon_synced_profile_pic\\\":null,\\\"is_identity_synced\\\":null,\\\"is_msplit_reg\\\":null,\\\"user_id_of_msplit_creator\\\":null,\\\"dma_data_combination_consent_given\\\":null,\\\"xapp_accounts\\\":null,\\\"horizon_synced\\\":null,\\\"is_cp_auto_confirmed_from_sync\\\":null,\\\"horizon_synced_profile_pic_from\\\":null,\\\"xapp_account_sync_from_sync\\\":null,\\\"num_consented_unread\\\":null,\\\"consent_setting_state\\\":null,\\\"fb_access_token_from_sync\\\":null,\\\"xapp_login_from_sync\\\":null,\\\"last_consented_unread\\\":null}}}}"
        }
    }
    }

    # مدخلات المستخدم الجديدة
    new_code = input("code: ")

    # تحديث قيمة code في السلسلة النصية
    client_input_params = {
        "client_input_params": {
            "confirmed_cp_and_code": {},
            "code": new_code,
            "fb_ig_device_id": [],
            "device_id": "34755123-f240-45ac-afba-6bf04bb07711",
            "lois_settings": {
                "lois_token": "",
                "lara_override": ""
            }
        }
    }

    server_params = {
        "server_params": {
            "event_request_id": "34efb418-bebe-43d2-8f0d-e83a129638b3",
            "is_from_logged_out": 0,
            "text_input_id": 20421463600046,
            "layered_homepage_experiment_group": None,
            "device_id": "34755123-f240-45ac-afba-6bf04bb07711",
            "waterfall_id": "a5bc0874-0c50-49b8-8db3-ebe415cca97d",
            "wa_timer_id": "wa_retriever",
            "INTERNAL__latency_qpl_instance_id": 2.0421463600096E13,
            "flow_info": {
                "flow_name": "new_to_family_fb_default",
                "flow_type": "ntf"
            },
            "is_platform_login": 0,
            "sms_retriever_started_prior_step": 0,
            "INTERNAL__latency_qpl_marker_id": 36707139,
            "reg_info": {
                "contactpoint": email,
                "contactpoint_type": "email",
                "first_name": None,
                "last_name": None,
                "full_name": None,
                "ar_contactpoint": None,
                "is_using_unified_cp": None,
                "unified_cp_screen_variant": None,
                "is_cp_auto_confirmed": None,
                "is_cp_auto_confirmable": None,
                "confirmation_code": None,
                "birthday": None,
                "did_use_age": None,
                "gender": None,
                "use_custom_gender": None,
                "custom_gender": None,
                "encrypted_password": None,
                "username": None,
                "username_prefill": None,
                "fb_conf_source": None,
                "device_id": "34755123-f240-45ac-afba-6bf04bb07711",
                "ig4a_qe_device_id": None,
                "ig_nta_test_group": None,
                "family_device_id": "34755123-f240-45ac-afba-6bf04bb07711",
                "nta_eligibility_reason": None,
                "youth_consent_decision_time": None,
                "username_screen_experience": None,
                "user_id": None,
                "safetynet_token": None,
                "safetynet_response": None,
                "machine_id": None,
                "profile_photo": None,
                "profile_photo_id": None,
                "profile_photo_upload_id": None,
                "avatar": None,
                "email_oauth_token_no_contact_perm": None,
                "email_oauth_token": None,
                "email_oauth_tokens": None,
                "should_skip_two_step_conf": None,
                "openid_tokens_for_testing": None,
                "encrypted_msisdn": None,
                "encrypted_msisdn_for_safetynet": None,
                "cached_headers_safetynet_info": None,
                "should_skip_headers_safetynet": None,
                "headers_last_infra_flow_id": None,
                "headers_last_infra_flow_id_safetynet": None,
                "headers_flow_id": None,
                "was_headers_prefill_available": None,
                "sso_enabled": None,
                "existing_accounts": None,
                "used_ig_birthday": None,
                "sync_info": None,
                "create_new_to_app_account": None,
                "skip_session_info": None,
                "ck_error": None,
                "ck_id": None,
                "ck_nonce": None,
                "should_save_password": None,
                "horizon_synced_username": None,
                "fb_access_token": None,
                "horizon_synced_profile_pic": None,
                "is_identity_synced": None,
                "is_msplit_reg": None,
                "user_id_of_msplit_creator": None,
                "dma_data_combination_consent_given": None,
                "xapp_accounts": None,
                "horizon_synced": None,
                "is_cp_auto_confirmed_from_sync": None,
                "horizon_synced_profile_pic_from": None,
                "xapp_account_sync_from_sync": None,
                "num_consented_unread": None,
                "consent_setting_state": None,
                "fb_access_token_from_sync": None,
                "xapp_login_from_sync": None,
                "last_consented_unread": None
            }
        }
    }

    merged_params = {**client_input_params, **server_params}
    params_str = json.dumps({"params": merged_params}).replace('"', '\\"')

    input_data["variables"]["params"]["params"] = params_str

    prams=json.dumps(input_data, indent=2)
    response = requests.post('https://graph.facebook.com/graphql', data=prams, headers=headers)
    input(response)
def _call(url, params, post=True):
    headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; SM-N975F Build/PI) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/en_US;FBBV/480086274;FBCR/CoolTEL Aps;FBMF/samsung;FBBD/samsung;FBDV/SM-N975F;FBSV/9;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;FBRV/0;]'}
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()
for i in range(int(input('[+] How Many Accounts : '))):
 email, password, first_name, last_name, birthday = create_mail_tm_account()
 if email and password and first_name and last_name and birthday:
  register_facebook_account(email, password, first_name, last_name, birthday)
