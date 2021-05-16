#!/usr/bin/env python3

import os
import requests
import datetime
import sys
import json
from simple_term_menu import TerminalMenu
from urllib3.exceptions import InsecureRequestWarning
from urllib.request import urlopen
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

log_name = 'output.log'
vault_addr = ''
vault_token = ''
vault_headers = {'X-Vault-Token' : vault_token}

api_endpoints_get = [
  '/v1/sys/audit',
  '/v1/sys/auth',
  '/v1/sys/health',
  '/v1/sys/host-info',
  '/v1/sys/internal/ui/mounts'
  ]

api_endpoints_post = [
  '/v1/sys/capabilities'
  ]

api_info_urls = [
  'https://www.vaultproject.io/api-docs/system/audit',
  'https://www.vaultproject.io/api-docs/system/auth',
  'https://www.vaultproject.io/api-docs/system/health',
  'https://www.vaultproject.io/api-docs/system/host-info',
  'https://www.vaultproject.io/api-docs/system/internal-ui-mounts',
  'https://www.vaultproject.io/api-docs/system/capabilities'
  ]

def main():
    main_menu_title = " Main Menu\n"
    main_menu_items = [
            "vault_sys_audit", 
            "vault_sys_auth", 
            "vault_sys_health",
            "vault_sys_host_info",
            "vault_sys_internal_ui_mounts",
            "sys_capabilities", 
            "quit"
            ]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_green", "fg_black")
    main_menu_exit = False

    main_menu = TerminalMenu(
            menu_entries=main_menu_items,
            title=main_menu_title,
            menu_cursor=main_menu_cursor,
            menu_cursor_style=main_menu_cursor_style,
            menu_highlight_style=main_menu_style,
            cycle_cursor=True,
            clear_screen=True,
    )

    back_menu_title = ""
    back_menu_items = ["Back to Main Menu"]
    back_menu_back = False
    back_menu = TerminalMenu(
        back_menu_items,
        title=back_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=False,
        clear_screen=False,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()
        if main_sel == 0:
            # call sys/audit
            vault_api_call_get(api_endpoints_get[0])
            api_info(api_info_urls[0])
        elif main_sel == 1:
            # call sys/auth
            vault_api_call_get(api_endpoints_get[1])
            api_info(api_info_urls[1])
        elif main_sel == 2:
            # call sys/health
            vault_api_call_get(api_endpoints_get[2])
            api_info(api_info_urls[2])
        elif main_sel == 3:
            # call sys/host-info
            vault_api_call_get(api_endpoints_get[3])
            api_info(api_info_urls[3])
        elif main_sel == 4:
            # call sys/internal/ui/mounts
            vault_api_call_get(api_endpoints_get[4])
            api_info(api_info_urls[4])
        elif main_sel == 5:
            # call sys/capabilities
            token = input('Token: ')
            paths_input = input('Paths: ')
            paths = paths_input.split()
            post_args = {"token": token, "paths": paths}
            vault_api_call_post(api_endpoints_post[0],post_args)
            api_info(api_info_urls[5])
        elif main_sel == 6:
            main_menu_exit = True
        if (main_sel >= 0) and (main_sel < 6):
            back_menu.show()

def vault_api_call_get(api_endpoint):
  try:
    response = requests.get(vault_addr+api_endpoint, headers=vault_headers, verify=False)
    response.raise_for_status()
    req = json.dumps(response.json(), indent=2, sort_keys=True)
    print(req)
    log_file(log_name,str(req))
  except requests.exceptions.HTTPError as errh:
    print(errh)
  except requests.exceptions.ConnectionError as errc:
    print(errc)
  except requests.exceptions.Timeout as errt:
    print(errt)
  except requests.exceptions.RequestException as err:
    print(err)

def vault_api_call_post(api_endpoint, post_args):
  try:
    response = requests.post(vault_addr+api_endpoint, headers=vault_headers, data=post_args, verify=False)
    response.raise_for_status()
    req = json.dumps(response.json(), indent=2, sort_keys=True)
    print(req)
    log_file(log_name,str(req))
  except requests.exceptions.HTTPError as errh:
    print(errh)
  except requests.exceptions.ConnectionError as errc:
    print(errc)
  except requests.exceptions.Timeout as errt:
    print(errt)
  except requests.exceptions.RequestException as err:
    print(err)

def log_file(log_name,req):
    now = datetime.datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
    try:
      f = open(log_name+'_'+timestamp, 'a')
      f.write(req)
      f.close
    except Exception as err:
      print(str(err))

def api_info(url):
    try:
      html = urlopen(url).read()
      soup = BeautifulSoup(html, features="html.parser")
      text = soup.find("p", {"class" : "g-type-long-body"})
      text = str(text.contents).replace(r'\n',' ').replace('<code>','').replace('</code>','').replace("'","").replace(' , ', ' ').replace(',','',1)
    except HTTPError as hp:
      print(hp)
    else:
      print(text)

if __name__ == "__main__":
    main()
